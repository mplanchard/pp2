"""Unit tests for pkg domain models."""

import pytest

from pypiserver.domain.pkg import SupportedFormat


class TestSupportedFormat:
    """It provides methods for validating file format."""

    @pytest.mark.parametrize(
        "fmt, filename, matches",
        (
            (SupportedFormat.SDIST, "foo.tar.gz", True),
            (SupportedFormat.SDIST, ".tar.gz", False),
            (SupportedFormat.SDIST, "abc-def.tar.gz", True),
            (SupportedFormat.WHEEL, "foo.whl", True),
            (SupportedFormat.WHEEL, "bar.baz.whl", True),
            (SupportedFormat.WHEEL, "bar.baz.whl", True),
        ),
    )
    def test_matches(
        self, fmt: SupportedFormat, filename: str, matches: bool
    ) -> None:
        """It matches appropriate filenames and does not match others."""
        assert fmt.matches(filename) is matches
