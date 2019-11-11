"""Tests for the Root resource."""

from aiohttp.test_utils import TestClient


class TestRoot:
    """Test the Root resource."""

    async def test_endpoint_exists(self, client: TestClient) -> None:
        """Ensure the expected endpoint exists."""
        resp = await client.get("/")
        assert resp.status == 204
