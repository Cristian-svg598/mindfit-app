from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from db import db
from routes.auth import auth_bp
from routes.routines import routines_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mindfit.db"
app.config["JWT_SECRET_KEY"] = "supersecretkey"

CORS(app)
JWTManager(app)
db.init_app(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(routines_bp, url_prefix="/routines")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=3001)
