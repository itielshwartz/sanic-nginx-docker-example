import os

from sanic import Sanic
from sanic.response import json

from app.utils.helper import hello_world

SANIC_PREFIX = "SANIC_"

app = Sanic()


@app.route("/hello-world")
async def test(request):
    return json(hello_world())


app.static('/static', './static')  # while in docker files from static will be served by ngnix
if __name__ == "__main__":
    for k, v in os.environ.items():
        if k.startswith(SANIC_PREFIX):
            _, config_key = k.split(SANIC_PREFIX, 1)
            app.config[config_key] = v
    app.run(host="0.0.0.0", port=8000, debug=True)
