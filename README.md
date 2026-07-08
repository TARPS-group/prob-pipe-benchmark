# probpipe-benchmark

Heavy posterior-recovery benchmark harness for ProbPipe inference methods.

This repository is separate from `prob-pipe` by design. The lightweight
posterior-vs-reference validation utilities live in `probpipe.validation`; this
package will host heavier target/reference/method runners, optional benchmark
suite integrations, offline jobs, plotting, and leaderboards.

## Current status

This repository is scaffold-only. It does not yet include benchmark targets,
method adapters, scorecard runners, plotting, or external benchmark-suite
integrations.

## Development setup

Clone the two repositories as siblings:

```bash
git clone https://github.com/TARPS-group/prob-pipe.git
git clone https://github.com/TARPS-group/prob-pipe-benchmark.git
cd prob-pipe-benchmark
```

Create an environment and install both packages:

```bash
uv venv --python 3.12
source .venv/bin/activate
uv pip install -e ../prob-pipe
uv pip install -e ".[dev]"
```

The benchmark package depends on the `probpipe-core` distribution. User code
still imports `probpipe`; `probpipe-core` is the minimal distribution that
provides that import package. Until `probpipe-core` is published, the sibling
`uv pip install -e ../prob-pipe` provides `probpipe-core` locally, so the
subsequent `.[dev]` install finds it already satisfied and does not look for it
on PyPI. The `dev` extra installs the same tooling CI uses and pins Ruff and
Pyright to the exact CI versions (their check output must match); the test and
pre-commit tools float.

Run scaffold checks:

```bash
probpipe-benchmark --help
probpipe-benchmark --version
python -c "import probpipe; import probpipe_benchmark"
python -c "from probpipe.validation import Reference, score_posterior"
pytest -m "not optional and not offline and not slow"
ruff check .
ruff format --check .
pyright
```

## Dependency policy

The scaffold starts with a minimal dependency surface so package setup, CI, and
import behavior can be reviewed independently.

This benchmark repository may eventually need heavier default dependencies than
the core ProbPipe package because its purpose is to compare many methods across
many external packages. Future PRs should decide dependency placement
deliberately: base install for core benchmark operation, extras for specific
suites, method families, plotting stacks, or offline workflows.
