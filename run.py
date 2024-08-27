from app import create_app
import os

# Establece el entorno
env_name = os.getenv('FLASK_ENV', 'development')

# Crea la aplicación Flask usando la configuración adecuada
app = create_app(env_name)

if __name__ == '__main__':
    app.run(debug=True)
