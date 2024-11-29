"""
Este modulo almacena las configuraciones principales de la aplicación Flask
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """ Configuración base """
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """ Configuración para el entorno de desarrollo """
    DEBUG = True

class ProductionConfig(Config):
    """ Configuración para el entorno de desarrollo """
    DEBUG = False