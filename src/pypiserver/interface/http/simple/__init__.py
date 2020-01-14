"""Simple interface."""

from textwrap import dedent

import jinja2
from aiohttp import web
from aiostream import stream
from baseutils.aio.iter import collect

from pypiserver.domain.model import PythonPackage
from pypiserver.interface.http import View


class SimpleIndex(web.View, View):
    """The root of the simple index."""

    _TEMPLATE = jinja2.Template(
        dedent(
            r"""\
            <html>
                <head>
                    <title>Simple Index</title>
                </head>
                <body>
                    <h1>Simple Index</h1>
                    {% for pkg in packages %}
                        <a href="{{pkg.normalized_name}}/">
                            {{pkg.normalized_name}}
                        </a><br>
                    {% endfor %}
                </body>
            </html>
            """
        )
    )

    async def get(self) -> web.Response:
        """Return an index of packages."""
        packages = await collect(self.get_store().all(PythonPackage))
        response = await self._TEMPLATE.render_async(
            packages=sorted(packages, key=lambda pkg: pkg.sorted_name,)
        )
        return web.Response(text=response)
