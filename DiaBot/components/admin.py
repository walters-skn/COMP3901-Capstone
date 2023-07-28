from components.connect import db_config
from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import mysql.connector

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_patient():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    profiles = []
    
    try:
        user_id = get_jwt_identity()
        identity_data = {'user_id': user_id}

        if identity_data.get('is_admin', False):
            return jsonify({'error': 'Unauthorized access'}), 401

        else:
            cursor.execute("""
            SELECT
                p.patient_id AS 'Patient ID', 
                p.first_name AS 'First Name', 
                p.last_name AS 'Last Name', 
                s.phone AS 'Patient Contact Number', 
                m.nutri_lvl AS 'Nutritional Level', 
                md.medication_name AS 'Medication Name', 
                md.commencement_date AS 'Commencement Date', 
                md.termination_date AS 'Termination Date',
                c.cname AS 'Clinic Name', 
                r.appt_date AS 'Appointment Date', 
                r.remind_type AS 'Reminider Type'
            FROM patients p
            LEFT JOIN contacts s ON s.patient_id = p.patient_id
            LEFT JOIN meals m ON m.patient_id = s.patient_id
            LEFT JOIN medications md ON md.patient_id = m.patient_id
            LEFT JOIN clinics c ON c.patient_id = md.patient_id
            LEFT JOIN reminders r ON r.patient_id = c.patient_id
            """)

            for patient_id, first_name, last_name, phone, nutri_lvl, medication_name, commencement_date, termination_date, cname, appt_date, remind_type in cursor:
                profile = {}
                profile['patient_id']        = patient_id
                profile['first_name']        = first_name
                profile['last_name']         = last_name
                profile['phone']             = phone
                profile['nutri_lvl']         = nutri_lvl
                profile['medication_name']   = medication_name
                profile['commencement_date'] = commencement_date
                profile['termination_date']  = termination_date 
                profile['cname']             = cname 
                profile['appt_date']         = appt_date  
                profile['remind_type']       = remind_type

                profiles.append(profile)

            return jsonify({'profiles': profiles}), 200
            
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

