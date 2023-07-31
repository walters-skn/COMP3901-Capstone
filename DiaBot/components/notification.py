
from components.connect import db_config
from dotenv import load_dotenv
from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from twilio.rest import Client
import mysql.connector
import os
# Download the helper library from https://www.twilio.com/docs/python/install

notification_bp = Blueprint('notification', __name__)

@notification_bp.route('/medication', methods=['POST'])
@jwt_required()
def add_medication():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    try:
        # Medication Table
        medication_name = request.json.get('medicationName')
        commence_date = request.json.get('comDate')
        terminate_date = request.json.get('termDate')
        frequency = request.json.get('frequency')
        quantity_mg = request.json.get('quantityMeds')

        # get the patient_id from the user_id
        email = get_jwt_identity()
        cursor.execute("SELECT * FROM users WHERE email = %s LIMIT 1", (email,))
        user_id = cursor.fetchone()
        if user_id is not None:
            user_id = user_id[0]

            cursor.execute("SELECT * FROM patients WHERE user_id = %s LIMIT 1", (user_id,))
            patient_row = cursor.fetchone()
            if patient_row is not None:
                patient_id = patient_row[0]

                # insert into medication table
                cursor.execute("""
                    INSERT INTO medications (patient_id, medication_name, commencement_date, termination_date, frequency, quantity)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (patient_id, medication_name, commence_date, terminate_date, frequency, quantity_mg))
                cnx.commit()

                return jsonify({'message': 'Medication added successfully!'}), 201
            else:
                return jsonify({'error': 'Patient not found'}), 400
        else:
            return jsonify({'error': 'User not found'}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    # close the connection
    cursor.close()
    cnx.close()


@notification_bp.route('/appointment', methods=['POST'])
@jwt_required()
def add_appointment():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    try:
        # Reminder Table
        location = request.json.get('location')
        appt_date = request.json.get('appointmentDate')
        appt_time = request.json.get('appointmentTime')
        remind_type = request.json.get('selectedReminder')
        remind_desc = request.json.get('reminderDesc')

        # get the patient_id from the user_id
        email = get_jwt_identity()
        cursor.execute("SELECT * FROM users WHERE email = %s LIMIT 1", (email,))
        user_id = cursor.fetchone()
        if user_id is not None:
            user_id = user_id[0]

            cursor.execute("SELECT * FROM patients WHERE user_id = %s LIMIT 1", (user_id,))
            patient_row = cursor.fetchone()
            if patient_row is not None:
                patient_id = patient_row[0]

                # use the clinicName to get the clinic_id from the clinics table
                cursor.execute("SELECT * FROM clinics WHERE caddress LIKE %s LIMIT 1", (location,))
                clinic_row = cursor.fetchone()
                if clinic_row is not None:
                    clinic_id = clinic_row[0]

                    # insert into reminders table
                    cursor.execute("""
                        INSERT INTO reminders (patient_id, clinic_id, medication_id, appt_date, appt_time, remind_type, remind_desc)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (patient_id, clinic_id, medication_id, appt_date, appt_time, remind_type, remind_desc))
                    cnx.commit()



                    # SENDING REMINDER WITH TWILIO
                    # get the patient's phone number
                    cursor.execute("""
                        SELECT phone FROM contacts c
                            INNER JOIN reminders r ON c.patient_id = r.patient_id
                        WHERE r.patient_id = %s LIMIT 1
                    """, (patient_id,))

                    customer_phone_number = cursor.fetchone()
                    if customer_phone_number is not None:
                        customer_phone_number = customer_phone_number[0]
                    else:
                        return jsonify({'error': 'Patient not found'}), 400

                    # send_appointment_reminder(customer_phone_number, appt_date, appt_time)



                    return jsonify({'message': 'Appointment added successfully!'}), 201
                else:
                    return jsonify({'error': 'Clinic not found'}), 400
            else:
                return jsonify({'error': 'Patient not found'}), 400
        else:
            return jsonify({'error': 'User not found'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 400
        



def send_appointment_reminder(customer_phone_number, appt_date, appt_time):
    # Load environment variables from the .env.local file in the parent directory
    env_file_path = os.path.join(os.path.dirname(__file__), '..', '.env.local')
    load_dotenv(env_file_path)

    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_number = os.getenv('TWILIO_NUMBER')
    
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=customer_phone_number,
        from_=twilio_number,
        body=f"Hi, this is a reminder for your appointment at [{appt_date} & {appt_time}]."
    )
    
    return message