from __future__ import annotations

import pytest


def test_probpipe_and_benchmark_imports() -> None:
    import probpipe

    import probpipe_benchmark

    assert probpipe is not None
    assert probpipe_benchmark.__version__


def test_validation_comparison_surface_is_importable() -> None:
    from probpipe.validation import Reference, score_posterior

    assert Reference.__name__ == "Reference"
    assert callable(score_posterior)


def test_version_falls_back_to_sentinel(monkeypatch: pytest.MonkeyPatch) -> None:
    import importlib
    import importlib.metadata as _md

    import probpipe_benchmark

    def _raise(_name: str) -> str:
        raise _md.PackageNotFoundError

    # Force the PackageNotFoundError branch (as in a source tree with no install)
    # and re-execute the module body so __version__ takes the fallback path.
    monkeypatch.setattr(_md, "version", _raise)
    try:
        importlib.reload(probpipe_benchmark)
        assert probpipe_benchmark.__version__ == "0.0.0+unknown"
    finally:
        monkeypatch.undo()
        importlib.reload(probpipe_benchmark)
