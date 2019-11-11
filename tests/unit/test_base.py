"""Test the most fundamental of things."""

import pypiserver


def test_version() -> None:
    """We have a __version__ attribute on the package root."""
    assert pypiserver.__version__


def test_version_info() -> None:
    """We have a __version_info__ attribute on the package root."""
    assert pypiserver.__version_info__
