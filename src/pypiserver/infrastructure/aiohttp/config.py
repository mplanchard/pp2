"""Configuration options for aiohttp."""

import typing as t


class AioHttpConfig:
    """Configuration values for AIOHTTP."""

    def __init__(
        self,
        backlog: int = 128,
        host: str = "0.0.0.0",
        port: int = 5000,
        shutdown_timeout: int = 60,
    ) -> None:
        """Create the config object."""
        self._backlog = backlog
        self._host = host
        self._port = port
        self._shutdown_timeout = shutdown_timeout

    @classmethod
    def new(cls) -> "AioHttpConfig":
        """Construct a new instance of this class.

        Right now this is a bit sparse, but the intention here is to
        have this automatically parse the environment as needed.
        """
        return cls()

    def to_dict(self) -> t.Dict[str, t.Any]:
        """Cast the object to a dictionary."""
        keys = ("backlog", "host", "port", "shutdown_timeout")
        return dict(map(lambda k: (k, getattr(self, f"_{k}")), keys,))
