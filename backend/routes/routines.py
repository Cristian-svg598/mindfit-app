from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import date
from models import Routine
from db import db
from services.gemini_service import generar_rutina
import json

routines_bp = Blueprint("routines", __name__)

@routines_bp.route("/generate", methods=["POST"])
@jwt_required()
def generate_routine():
    data = request.json
    estado = data["estado"]
    objetivo = data["objetivo"]
    user_id = get_jwt_identity()

    rutina_json = generar_rutina(estado, objetivo)
    rutina = json.loads(rutina_json)

    nueva = Routine(
        user_id=user_id,
        date=date.today(),
        content=rutina
    )
    db.session.add(nueva)
    db.session.commit()

    return jsonify({"message": "Rutina generada", "rutina": rutina})
