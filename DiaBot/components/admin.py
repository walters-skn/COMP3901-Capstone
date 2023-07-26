from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

import mysql.connector
from db.connect import db_config

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/patients', methods=['GET'])
@jwt_required()
def get_patient():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    patient_data = []
    
    try:
        cursor.execute("SELECT patient_id, first_name, last_name FROM patients")

        for patient_id, first_name, last_name in cursor:
            patients = {}
            patients['patient_id'] = patient_id
            patients['first_name'] = first_name
            patients['last_name'] = last_name
            patients_data.append(patients)

        return jsonify({'patients': patients_data}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

