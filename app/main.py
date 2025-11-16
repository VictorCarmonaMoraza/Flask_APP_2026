import os

from flask import Flask
from app.config.settings import Settings
from presentation.controllers.hello_controller import hello_bp
from presentation.controllers.index_controller import index_bp




# Si luego tienes más blueprints, los registrarás aquí:
# from presentation.controllers.user_controller import user_bp

def create_app():
    """Crea y configura la aplicación Flask (punto de entrada principal)."""

    # 📁 Definir rutas de templates y static manualmente
    base_dir = os.path.dirname(__file__)  # Ruta de /app/
    template_dir = os.path.join(base_dir, '../presentation/templates')
    static_dir = os.path.join(base_dir, '../presentation/static')

    app = Flask(__name__,
                template_folder=template_dir,
                static_folder=static_dir)

    # 1️⃣ Cargar configuración
    settings = Settings()
    app.config.from_object(settings)

    # 2️⃣ Registrar controladores (rutas HTTP)
    app.register_blueprint(hello_bp)
    app.register_blueprint(index_bp)

    # 3️⃣ Inicializar extensiones (si las usas más adelante)
    # from infrastructure.db.database import db
    # db.init_app(app)

    # 4️⃣ (Opcional) CORS si trabajas con Angular u otro frontend
    # from flask_cors import CORS
    # CORS(app)

    # 5️⃣ Endpoint raíz opcional (salud del sistema)
    @app.route('/health', methods=['GET'])
    def health():
        return {'status': 'ok', 'service': 'Flask Hexagonal API'}

    return app
