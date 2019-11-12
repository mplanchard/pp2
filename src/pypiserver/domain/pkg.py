"""Package-related Domain models."""


import re
import typing as t
from enum import Enum
from functools import partial

from baseutils.iter import first
from baseutils.option import exists


class _SupportedFormat(t.NamedTuple):
    """A supported file format."""

    regex: t.Pattern

    def matches(self, filename: str) -> bool:
        """Return whether the filename matches this format."""
        return exists(self.regex.match(filename))


class SupportedFormat(Enum):
    """Supported package formats and their extensions."""

    SDIST = _SupportedFormat(re.compile(r"^.+\.tar\.gz$"))
    WHEEL = _SupportedFormat(re.compile(r"^.+\.whl"))

    @classmethod
    def of(cls, filename: str) -> t.Optional["SupportedFormat"]:
        """Return the format of the given filename, or None.

        >>> assert SupportedFormat.of("foo.whl") is SupportedFormat.WHEEL
        """
        return first(filter(lambda i: i.matches(filename), cls))

    def matches(self, filename: str) -> bool:
        """Return whether the format matches the given filename.

        >>> assert SupportedFormat.SDIST.matches("foo.sdist") is True
        """
        # pylint: disable=no-member
        return t.cast(bool, self.value.matches(filename))
        # pylint: enable=no-member


class PackageBinary(t.NamedTuple):
    """A binary package file."""

    data: bytes


# class PackageFileName:


# class IndexPackage:
#     """An indexed package."""

# def __init__(self, filename: str)
