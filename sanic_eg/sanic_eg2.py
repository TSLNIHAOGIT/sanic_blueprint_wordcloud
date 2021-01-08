from sanic import Sanic
from sanic.response import json

app = Sanic("App Name")

@app.route("/")
async def myExample(request):
    return json({"hello": "world"})

if __name__ == "__main__":
    ##默认8000端口，被CLodopPrint32占用了
    app.run(host="0.0.0.0", port=8800)