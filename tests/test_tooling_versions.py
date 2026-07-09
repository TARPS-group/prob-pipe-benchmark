"""Guard the no-lockfile version pins against silent drift.

This repo has no uv.lock, so the tool versions live in more than one place: the
ruff pin in the ``dev`` extra must match the ``rev`` in .pre-commit-config.yaml
(the version CI resolves from), and the pyright pin in the ``dev`` extra must
match the version CI installs in the typecheck job. These tests make those the
enforced single sources of truth instead of a documented hope.
"""

from __future__ import annotations

import re
import tomllib
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_PYPROJECT = _ROOT / "pyproject.toml"
_PRECOMMIT = _ROOT / ".pre-commit-config.yaml"
_CI = _ROOT / ".github" / "workflows" / "ci.yml"


def _dev_pin(package: str) -> str:
    """Return the ``==`` version pinned for ``package`` in the ``dev`` extra."""
    dev = tomllib.loads(_PYPROJECT.read_text())["project"]["optional-dependencies"]["dev"]
    for entry in dev:
        name = re.split(r"[\[=]", entry, maxsplit=1)[0]
        if name == package:
            match = re.search(r"==\s*([0-9][0-9A-Za-z.\-]*)", entry)
            assert match, f"{package} is not pinned with == in the dev extra: {entry!r}"
            return match.group(1)
    raise AssertionError(f"no {package} entry in [project.optional-dependencies].dev")


def test_ruff_pin_matches_precommit_rev() -> None:
    match = re.search(
        r"astral-sh/ruff-pre-commit.*?\brev:\s*[\"']?v?([0-9][0-9.]+)",
        _PRECOMMIT.read_text(),
        re.DOTALL,
    )
    assert match, "could not find the ruff-pre-commit rev in .pre-commit-config.yaml"
    assert _dev_pin("ruff") == match.group(1)


def test_pyright_pin_matches_ci() -> None:
    match = re.search(r"pyright\[nodejs\]==([0-9][0-9.]+)", _CI.read_text())
    assert match, "could not find the pyright pin in .github/workflows/ci.yml"
    assert _dev_pin("pyright") == match.group(1)
