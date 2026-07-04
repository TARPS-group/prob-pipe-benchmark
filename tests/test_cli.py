from __future__ import annotations

import subprocess
import sys

import pytest

OPTIONAL_HEAVY_MODULES = {
    "bayesflow",
    "bridgestan",
    "cmdstanpy",
    "inference_gym",
    "nutpie",
    "posteriordb",
    "pymc",
    "sbibm",
    "torch",
}


def test_cli_help_exits_cleanly(capsys: pytest.CaptureFixture[str]) -> None:
    from probpipe_benchmark.cli import main

    with pytest.raises(SystemExit) as exc_info:
        main(["--help"])

    assert exc_info.value.code == 0
    assert "usage:" in capsys.readouterr().out


def test_cli_version_exits_cleanly(capsys: pytest.CaptureFixture[str]) -> None:
    from probpipe_benchmark.cli import main

    with pytest.raises(SystemExit) as exc_info:
        main(["--version"])

    assert exc_info.value.code == 0
    assert "probpipe-benchmark" in capsys.readouterr().out


def test_cli_import_does_not_load_optional_heavy_dependencies() -> None:
    script = f"""
import sys

heavy_modules = {sorted(OPTIONAL_HEAVY_MODULES)!r}
before = set(sys.modules)

from probpipe_benchmark import cli

loaded = sorted(
    name.split(".", 1)[0]
    for name in sys.modules
    if name not in before and name.split(".", 1)[0] in heavy_modules
)
if loaded:
    raise SystemExit("loaded optional heavy modules: " + ", ".join(loaded))
if not callable(cli.main):
    raise SystemExit("probpipe_benchmark.cli.main is not callable")
"""
    result = subprocess.run(
        [sys.executable, "-c", script],
        capture_output=True,
        check=False,
        text=True,
    )

    assert result.returncode == 0, result.stderr
