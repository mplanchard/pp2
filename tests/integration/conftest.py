"""Integration test fixtures."""

import typing as t

from asyncio import AbstractEventLoop

import pytest
from aiohttp import web
from aiohttp.test_utils import TestClient

from pypiserver.main import create_app


@pytest.fixture()
def client(
    loop: AbstractEventLoop,
    aiohttp_client: t.Callable[[web.Application], t.Awaitable[TestClient]],
) -> TestClient:
    """Return a client configured to use the app."""
    return loop.run_until_complete(aiohttp_client(create_app()))
