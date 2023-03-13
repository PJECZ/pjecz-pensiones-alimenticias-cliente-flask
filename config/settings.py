"""
Configuración de la aplicación
"""
import os


# API
API_BASE_URL = os.environ.get("API_BASE_URL", "http://172.30.37.233:7086/v3")
API_TIMEOUT = int(os.environ.get("API_TIMEOUT", 12))

# Salt para convertir/reconverir el id en hash
SALT = os.environ.get("SALT", "Esta es una muy mala cadena aleatoria")

# Secret key para CSRF
SECRET_KEY = os.environ.get("SECRET_KEY", "Esta es una muy mala cadena aleatoria")

# reCAPTCHA configuration
RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")
