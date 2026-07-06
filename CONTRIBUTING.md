# Contributing

This repository follows the ProbPipe development conventions where applicable,
with a narrower initial scope: it is the benchmark harness repository, not the
core ProbPipe package.

## Local workflow

- Use `dev/...` branch names for development branches.
- Keep PR descriptions focused on the final state of the change.
- Format with Ruff: `ruff format .`.
- Lint with Ruff: `ruff check .`.
- Keep `probpipe_benchmark` imports lightweight.
- Do not commit benchmark outputs, caches, downloaded datasets, or large
  reference artifacts.

## Dependency policy

The initial scaffold depends on the `probpipe-core` distribution, which provides
the `probpipe` import package. This keeps the first infrastructure PR focused.

Future benchmark dependencies should be added deliberately with the functionality
that needs them. A dependency may belong in the base install if it supports core
benchmark operation, or in an extra if it is tied to a specific suite, method
family, plotting stack, or offline workflow.

## Tests

Future heavy tests should use these markers:

- `optional`: requires optional benchmark dependencies.
- `offline`: requires heavy local data, compiled models, or offline artifacts.
- `slow`: too slow for the default CI path.

The default test command should remain:

```bash
pytest -m "not optional and not offline and not slow"
```
