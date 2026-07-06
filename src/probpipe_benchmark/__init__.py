"""Benchmark harness package for ProbPipe inference method evaluation."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError as _PackageNotFoundError
from importlib.metadata import version as _version

# Version is read from the installed ``probpipe-benchmark`` distribution.
try:
    __version__ = _version("probpipe-benchmark")
except _PackageNotFoundError:  # pragma: no cover - source tree with no install
    __version__ = "0.0.0+unknown"

__all__ = ["__version__"]
