"""
Avisos, vistas
"""
from flask import Blueprint, render_template

avisos = Blueprint("avisos", __name__, template_folder="templates")


@avisos.route("/aviso", methods=["GET", "POST"])
def aviso_de_privacidad():
    """Mostrar aviso de privacidad"""

    # Entregar
    return render_template("avisos/aviso.jinja2")
