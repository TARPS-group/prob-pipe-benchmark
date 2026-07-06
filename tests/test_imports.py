from __future__ import annotations


def test_probpipe_and_benchmark_imports() -> None:
    import probpipe

    import probpipe_benchmark

    assert probpipe is not None
    assert probpipe_benchmark.__version__


def test_validation_comparison_surface_is_importable() -> None:
    from probpipe.validation import Reference, score_posterior

    assert Reference.__name__ == "Reference"
    assert callable(score_posterior)
