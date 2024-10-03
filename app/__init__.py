from flask import Flask
from http import HTTPStatus
from config import config  # Importa las configuraciones desde config.py
from .extensions import db, migrate  # Importa las extensiones (SQLAlchemy, Migrate)
from .routes import user_bp, form_bp  # Importa el blueprint de rutas principales

def create_app(env_name='development'):
    
    
    
    app = Flask(__name__)
    
    # Cargar la configuración según el entorno
    app.config.from_object(config[env_name])
    
    # Inicializar extensiones (Base de datos y migraciones)
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Registrar las rutas
    app.register_blueprint(user_bp)
    app.register_blueprint(form_bp, url_prefix='/formulario')
    
    return app
