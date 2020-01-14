"""A store is some persistence layer, e.g. the filesystem."""

import typing as t


T_Model = t.TypeVar("T_Model")


class Store:
    """A Store encapsulates retrieval and storage of persistent data."""

    async def all(self, model: t.Type[T_Model]) -> t.AsyncIterator[T_Model]:
        """Iterate over all available instances of the provided model."""
        raise NotImplementedError
        # the yield is needed for the type checker to realize this is an
        # async iterator.
        yield  # pylint: disable=unreachable
