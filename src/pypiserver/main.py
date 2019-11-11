"""Pypiserver Entrypoint."""

import asyncio
import typing as t

import uvloop
from aiohttp import web
from baseutils.iter import for_each

from pypiserver.infrastructure.aiohttp.config import AioHttpConfig


class ViewDefinition(t.NamedTuple):
    """A simple specification for a view."""

    route: str
    view: t.Type[web.View]


class RootView(web.View):
    """A view for the root of the application."""

    async def get(self) -> web.Response:
        """Return an empty response."""
        return web.Response(status=204)


def get_views() -> t.Iterable[ViewDefinition]:
    """Return the endpoints and views for the application.

    The endpoints here are not prefaced with the global prefix (v3).
    """
    return (ViewDefinition("/", RootView),)


def create_app() -> web.Application:
    """Create the application."""
    app = web.Application()
    views = map(lambda v: ViewDefinition(f"{v.route}", v.view), get_views())
    for_each(lambda view: app.router.add_view(*view), views)
    return app


def main() -> None:
    """Primary application entrypoint."""
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    web.run_app(create_app(), **AioHttpConfig.new().to_dict())


if __name__ == "__main__":
    main()
