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
        cursor.execute("SELECT p.patient_id, p.first_name, p.last_name, s.phone, m.nutri_lvl, md.medication_name, md.commencement_date, md.termination_date, c.cname, r.appt_date, r.remind_type FROM patients p")

        for p.patient_id, p.first_name, p.last_name, s.phone, m.nutri_lvl, md.medication_name, md.commencement_date, md.termination_date, c.cname, r.appt_date, r.remind_type in cursor:
            patients = {}
            patients['Patient ID'] = p.patient_id
            patients['First Name'] = p.first_name
            patients['Last Name'] = p.last_name
            patients['Patient Contact Number'] = s.phone
            patients['Nutritional Level'] = m.nutri_lvl
            patients['Medication Name'] = md.medication_name
            patients['Commencement Date'] = md.commencement_date
            patients['Termination Date'] = md.termination_date 
            patients['Clinic Name'] = c.cname 
            patients['Appointment Date'] = r.appt_date  
            patients['Reminder Type'] = r.remind_type

            patients_data.append(patients)

        return jsonify({'patients': patients_data}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

