"""
Flask App
"""
from flask import Flask

from .blueprints.avisos.views import avisos
from .blueprints.resultados.views import resultados
from .blueprints.sistemas.views import sistemas
from .blueprints.solicitudes.views import solicitudes
from .extensions import csrf


def create_app():
    """Crear app"""

    # Definir app
    app = Flask(__name__)

    # Cargar la configuración
    app.config.from_object("config.settings")

    # Registrar blueprints
    app.register_blueprint(resultados)
    app.register_blueprint(sistemas)
    app.register_blueprint(avisos)
    app.register_blueprint(solicitudes)

    # Cargar las extensiones
    extensions(app)

    # Entregar app
    return app


def extensions(app):
    """Extensiones"""

    # CSRF
    csrf.init_app(app)
