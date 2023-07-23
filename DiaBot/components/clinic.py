from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

import mysql.connector
from db.connect import db_config

clinic_bp = Blueprint('clinic', __name__)


@clinic_bp.route('/clinic', methods=['GET'])
@jwt_required()
def get_clinic_recommendations():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    clinic_data = []
    
    try:
        cursor.execute("SELECT cname, ctype, caddress, parish FROM clinics")

        for cname, ctype, caddress, parish in cursor:
            clinic = {}
            clinic['name'] = cname
            clinic['type'] = ctype
            clinic['address'] = caddress
            clinic['parish'] = parish
            clinic_data.append(clinic)

        return jsonify({'clinics': clinic_data}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

