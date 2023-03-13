"""
Resultados, vistas
"""
from flask import Blueprint, render_template

resultados = Blueprint("resultados", __name__, template_folder="templates")


@resultados.route("/resultado/registrado/<string:folio>", methods=["GET", "POST"])
def registrado(folio):
    """Solicitud registrada"""

    # Entregar
    return render_template("resultados/registrado.jinja2", folio=folio)


@resultados.route("/resultado/fallido/<string:message>", methods=["GET", "POST"])
def fallido(message):
    """Solicitud fallida"""

    # Entregar
    return render_template("resultados/fallido.jinja2", message=message)
