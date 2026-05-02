"""
Entry point da aplicação Flask — configura e registra os blueprints.
"""
import sys
import os

# Garante que os pacotes internos (models/, controllers/) sejam encontrados
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask
from controllers.prediction_controller import prediction_bp

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "fiap-tech-challenge-fase1"

app.register_blueprint(prediction_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
