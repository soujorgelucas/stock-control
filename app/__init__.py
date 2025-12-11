from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configurações adicionais podem ser adicionadas aqui
    app.config['JSON_SORT_KEYS'] = False  # Mantém a ordem dos JSONs

    return app
