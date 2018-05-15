import tempfile
import platform
from os import path
from datetime import datetime
from shutil import copy
from webruntime import launch
from aiohttp import web

# work around buggy _clean_nw_dirs()
from webruntime._nw import NWRuntime
NWRuntime._clean_nw_dirs = lambda x: x

filename = "nwjs-v0.30.3-win-ia32.zip"
if platform.system() == "Darwin":
    filename = "nwjs-v0.30.3-osx-x64.zip"
copy(path.join(path.dirname(path.__file__), filename), tempfile.gettempdir())


async def handle(request):
    return web.Response(text="""<html>
<head><title>date</title></head>
<body>
{}</p>
<a href="/">get time</a">
</body>
</html>
""".format(datetime.today().isoformat()), content_type="text/html")

app = web.Application()
app.router.add_get('/', handle)

launch('http://localhost:9999', 'nw-app or firefox-app')
web.run_app(app, port=9999)
