"""Benchmark harness package for ProbPipe inference method evaluation."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

_DISTRIBUTION_NAME = "probpipe-benchmark"


def _package_version() -> str:
    try:
        return version(_DISTRIBUTION_NAME)
    except PackageNotFoundError:
        return "0.1.0"


__version__ = _package_version()

__all__ = ["__version__"]
