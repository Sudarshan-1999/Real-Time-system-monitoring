from flask import Flask
from api.routes import setup_routes

app = Flask(__name__)

setup_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
