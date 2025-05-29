# app.py
from flask import Flask
from routes.caixa_routes import caixa_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app = Flask(__name__)
app.register_blueprint(caixa_bp)

if __name__ == "__main__":
    app.run(debug=True)
