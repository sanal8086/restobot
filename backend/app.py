from flask import Flask
from flask_cors import CORS
import os
from firebase_client import init_firebase

def create_app():
    app = Flask(__name__)
    
    # Initialize Firebase
    init_firebase()

    # Register blueprints
    from routes.auth import auth_bp
    from routes.admin import admin_bp
    from routes.menu import menu_bp
    from routes.tables import tables_bp
    from routes.analytics import analytics_bp
    from routes.chat import chat_bp
    from routes.superadmin import superadmin_bp
    from routes.wishlist import wishlist_bp
    from routes.guests import guests_bp

    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(admin_bp, url_prefix='/api')
    app.register_blueprint(menu_bp, url_prefix='/api')
    app.register_blueprint(tables_bp, url_prefix='/api')
    app.register_blueprint(analytics_bp, url_prefix='/api')
    app.register_blueprint(chat_bp, url_prefix='/api')
    app.register_blueprint(superadmin_bp, url_prefix='/api')
    app.register_blueprint(wishlist_bp, url_prefix='/api')
    app.register_blueprint(guests_bp, url_prefix='/api')

    # CORS: allow Vercel frontend
    # FRONTEND_URL env var on Render should be your Vercel URL e.g. https://restobot-zeta.vercel.app
    # We support multiple origins by splitting on comma if needed
    frontend_url = os.environ.get('FRONTEND_URL', '')
    if frontend_url:
        allowed_origins = [o.strip() for o in frontend_url.split(',')]
    else:
        allowed_origins = '*'  # local dev fallback

    # NOTE: supports_credentials=True + origins='*' is INVALID CORS and causes browser blocks.
    # Since we use JWT in Authorization headers (not cookies), credentials=False is correct.
    CORS(app,
         resources={r"/*": {"origins": allowed_origins}},
         supports_credentials=False,
         allow_headers=["Content-Type", "Authorization"],
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"])

    return app
