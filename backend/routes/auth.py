from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models import User
from db import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()  
    if not data:
        return {"error": "No se recibió JSON"}, 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {"error": "Faltan campos email o password"}, 400

    if User.query.filter_by(email=email).first():
        return {"error": "El usuario ya existe"}, 400

    new_user = User(
        email=email,
        password=generate_password_hash(password)
    )
    db.session.add(new_user)
    db.session.commit()

    return {"message": "Usuario creado con éxito"}, 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return {"error": "No se recibió JSON"}, 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {"error": "Faltan campos email o password"}, 400

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return {"error": "Credenciales incorrectas"}, 401

    token = create_access_token(identity=user.id)
    return {"token": token}
