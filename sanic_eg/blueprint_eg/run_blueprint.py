from sanic import Sanic
from sanic_eg.blueprint_eg.my_blueprint import bp

app = Sanic(__name__)
app.blueprint(bp)

app.run(host='127.0.0.1', port=8888, debug=True)