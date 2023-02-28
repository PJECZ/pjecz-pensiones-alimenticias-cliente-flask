"""
Solicitudes, vistas
"""
from flask import abort, Blueprint, render_template, redirect, request, url_for
import requests

from config.settings import API_BASE_URL, API_TIMEOUT
from lib.safe_string import safe_clave, safe_email, safe_string
from lib.hashids import cifrar_id, descifrar_id

from .forms import IngresarForm

solicitudes = Blueprint("solicitudes", __name__, template_folder="templates")


@solicitudes.route("/solicitud", methods=["GET", "POST"])
def ingresar():
    """Ingresar datos personales"""

    form = IngresarForm()

    if form.validate_on_submit():

        # Preparar el cuerpo a enviar a la API
        request_body = {
            "autoridad_clave": safe_string(form.juzgado.data),
            "cit_cliente_curp": safe_string(form.curp.data),
            "cit_cliente_email": safe_email(form.email.data),
            "cit_cliente_nombres": safe_string(form.nombres.data, save_enie=True),
            "cit_cliente_apellido_primero": safe_string(form.apellido_primero.data, save_enie=True),
            "cit_cliente_apellido_segundo": safe_string(form.apellido_segundo.data, save_enie=True),
            "cit_cliente_telefono": safe_string(form.telefono.data),
            "domicilio_calle": safe_string(form.calle.data),
            "domicilio_numero": safe_string(form.numero.data),
            "domicilio_colonia": safe_string(form.colonia.data),
            "domicilio_cp": int(safe_string(form.codigo.data)),
            "compania_telefonica": safe_string(form.compania.data),
            "numero_expediente": safe_string(form.expediente.data),
        }
        print(request_body)
        #Tomar el archivo
        archivo = request.files["ine"]

        # Enviar al API los datos para registrar solicitud 
        try:
            respuesta = requests.post(
                f"{API_BASE_URL}/ppa_solicitudes/solicitar",
                json=request_body,
                timeout=API_TIMEOUT,
            )
            respuesta.raise_for_status()
        except requests.exceptions.ConnectionError as error:
            abort(500, "No se pudo conectar con la API Pension Alimenticia. " + str(error))
        except requests.exceptions.Timeout as error:
            abort(500, "Tiempo de espera agotado al conectar con la API Pension Alimenticia. " + str(error))
        except requests.exceptions.HTTPError as error:
            abort(500, "Error HTTP porque la API de Pension Alimenticia arrojó un problema: " + str(error))
        except requests.exceptions.RequestException as error:
            abort(500, "Error desconocido con la API Pension Alimenticia. " + str(error))
        datos = respuesta.json()

        # Verificar que haya tenido exito
        if not "success" in datos:
            abort(400, "No se logro la comunicacion con la API.")
        if datos["success"]==False:
            return redirect(url_for("resultados.fallido", message=datos['message'] ))    

        # documento INE
        archivoINE = request.files["ine"]

        try:
            respuesta = requests.post(
                f"{API_BASE_URL}/ppa_solicitudes/subir/identificacion_oficial?id_hasheado={datos['id_hasheado']}",
                files={ "archivo" : archivoINE.stream.read() },
                timeout=API_TIMEOUT,
            )
            respuesta.raise_for_status()
        except requests.exceptions.ConnectionError as error:
            abort(500, "No se pudo conectar con la API Pago de Pension Alimenticia. " + str(error))
        except requests.exceptions.Timeout as error:
            abort(500, "Tiempo de espera agotado al conectar con la API Pago de Pension Alimenticia. " + str(error))
        except requests.exceptions.HTTPError as error:
            abort(500, "Error HTTP porque la API de Pago de Pension Alimenticia arrojó un problema: " + str(error))
        except requests.exceptions.RequestException as error:
            abort(500, "Error desconocido con la API Pago de Pension Alimenticia. " + str(error))
        datosINE = respuesta.json()

        # Verificar que haya tenido exito
        if not "success" in datosINE:
            abort(400, "No se logro la comunicacion con la API.")
        if datos["success"]==False:
            return redirect(url_for("resultados.fallido", message=datosINE['message'] ))


        # documento Comprobante de domicilio
        archivoComprobante = request.files["comprobante"]

        try:
            respuesta = requests.post(
                f"{API_BASE_URL}/ppa_solicitudes/subir/comprobante_domicilio?id_hasheado={datos['id_hasheado']}",
                files={ "archivo" : archivoComprobante.stream.read() },
                timeout=API_TIMEOUT,
            )
            respuesta.raise_for_status()
        except requests.exceptions.ConnectionError as error:
            abort(500, "No se pudo conectar con la API Pago de Pension Alimenticia. " + str(error))
        except requests.exceptions.Timeout as error:
            abort(500, "Tiempo de espera agotado al conectar con la API Pago de Pension Alimenticia. " + str(error))
        except requests.exceptions.HTTPError as error:
            abort(500, "Error HTTP porque la API de Pago de Pension Alimenticia arrojó un problema: " + str(error))
        except requests.exceptions.RequestException as error:
            abort(500, "Error desconocido con la API Pago de Pension Alimenticia. " + str(error))
        datosComprobante = respuesta.json()

        # Verificar que haya tenido exito
        if not "success" in datosComprobante:
            abort(400, "No se logro la comunicacion con la API.")
        if datos["success"]==False:
            return redirect(url_for("resultados.fallido", message=datosComprobante['message'] ))


        # documento Autorizacion
        archivoAutorizacion = request.files["autorizacion"]

        try:
            respuesta = requests.post(
                f"{API_BASE_URL}/ppa_solicitudes/subir/autorizacion?id_hasheado={datos['id_hasheado']}",
                files={ "archivo" : archivoAutorizacion.stream.read() },
                timeout=API_TIMEOUT,
            )
            respuesta.raise_for_status()
        except requests.exceptions.ConnectionError as error:
            abort(500, "No se pudo conectar con la API Pago de Pension Alimenticia. " + str(error))
        except requests.exceptions.Timeout as error:
            abort(500, "Tiempo de espera agotado al conectar con la API Pago de Pension Alimenticia. " + str(error))
        except requests.exceptions.HTTPError as error:
            abort(500, "Error HTTP porque la API de Pago de Pension Alimenticia arrojó un problema: " + str(error))
        except requests.exceptions.RequestException as error:
            abort(500, "Error desconocido con la API Pago de Pension Alimenticia. " + str(error))
        datosAutorizacion = respuesta.json()

        # Verificar que haya tenido exito
        if not "success" in datosAutorizacion:
            abort(400, "No se logro la comunicacion con la API.")
        if datos["success"]==False:
            return redirect(url_for("resultados.fallido", message=datosAutorizacion['message'] ))


        # Redireccionar a la página de resultados
        return redirect(url_for("resultados.registrado" , folio= "F-" + str(descifrar_id(datos['id_hasheado'])).zfill(5) )  )
        
    
    return render_template(
        "solicitudes/solicitud.jinja2",
        form=form,
        api_base_url = API_BASE_URL ,
    )
