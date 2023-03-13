# pjecz-pensiones-cliente-flask
Front-end para el registro de solicitud de tarjetas de debito para pensiones alimenticias hecho con Flask.

## Configurar

Crear archivo `.env` con

    # Citas cliente API:
    API_BASE_URL=http://localhost:7086/v3
    API_TIMEOUT=12

    # Base URL
    BASE_URL=http://localhost:5000

    # Flask
    FLASK_APP=pension-alimenticia-cliente-flask.app
    FLASK_DEBUG=1

    # Salt sirve para cifrar el ID con HashID
    SALT=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    # Secret key sirve para CSRF
    SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    # reCAPTCHA configuration
    RECAPTCHA_PUBLIC_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    RECAPTCHA_PRIVATE_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Crear archivo `.bashrc` que arranque el entorno virtual y cargue las variables

    if [ -f ~/.bashrc ]
    then
        . ~/.bashrc
    fi

    if command -v figlet &> /dev/null
    then
        figlet Pensiones Alimeticias cliente Flask
    else
        echo "== Pensiones Alimenticias cliente Flask"
    fi
    echo

    if [ -f .env ]
    then
        echo "-- Variables de entorno"
        export $(grep -v '^#' .env | xargs)
        echo "   API_BASE_URL: ${API_BASE_URL}"
        echo "   API_TIMEOUT: ${API_TIMEOUT}"
        echo "   BASE_URL: ${BASE_URL}"
        echo "   FLASK_APP: ${FLASK_APP}"
        echo "   FLASK_DEBUG: ${FLASK_DEBUG}"
        echo "   RECAPTCHA_PUBLIC_KEY: ${RECAPTCHA_PUBLIC_KEY}"
        echo "   RECAPTCHA_PRIVATE_KEY: ${RECAPTCHA_PRIVATE_KEY}"
        echo "   SALT: ${SALT}"
        echo "   SECRET_KEY: ${SECRET_KEY}"
        echo
    fi

    if [ -d .venv ]
    then
        echo "-- Python Virtual Environment"
        source .venv/bin/activate
        echo "   $(python3 --version)"
        export PYTHONPATH=$(pwd)
        echo "   PYTHONPATH: ${PYTHONPATH}"
        echo
        echo "-- Ejecutar Flask"
        alias arrancar="flask run --host=0.0.0.0 --port=5000"
        echo "   arrancar"
        echo
    fi

    if [ -f app.yaml ]
    then
        echo "-- Subir a Google Cloud"
        echo "   poetry export -f requirements.txt --output requirements.txt --without-hashes"
        echo "   gcloud app deploy"
        echo
    fi

## Instalar

Crear entorno virtual con Python 3.10

    python3.10 -m venv .venv

Activar entorno virtual

    source .venv/bin/activate

Actualizar pip de ser necesario

    pip install --upgrade pip

Instalar Poetry para manejar dependencias

    pip install poetry

Instalar dependencias

    poetry install

## Arrancar

Ejecutar Flask con el alias arrancar

    . .bashrc
    arrancar


