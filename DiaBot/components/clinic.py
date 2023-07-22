from flask import Blueprint, request, jsonify
import mysql.connector
from db.connect import db_config

clinic_bp = Blueprint('clinic', __name__)


@clinic_bp.route('/clinic', methods=['GET'])
# @jwt_required()
def get_clinic_recommendations():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    clinic_data = []
    
    try:
        cursor.execute("SELECT name, type, address, parish FROM clinics")

        for name, type, address, parish in cursor:
            clinic = {}
            clinic['name'] = name
            clinic['type'] = type
            clinic['address'] = address
            clinic['parish'] = parish
            clinic_data.append(clinic)

        return jsonify({'clinics': clinic_data}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

