"""HTTP Interfaces."""

import typing as t

from pypiserver.application.persistence.store import Store


class View:
    """Define a common parent for views."""

    def get_store(self) -> Store:
        """Retrieve the store for the application."""


V = t.TypeVar("V", bound=View)


def view_factory(
    get_store: t.Callable[[], Store], view: t.Type[V]
) -> t.Type[V]:
    """Hydrate the view as needed."""
    return type(view.__name__, (view,), {"get_store": get_store})
