from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

import mysql.connector
from db.connect import db_config

# Download the helper library from https://www.twilio.com/docs/python/install
import os
import datetime
from twilio.rest import Clientdentials
from twilio.rest import Client


notification_bp = Blueprint('notification')

@notification_bp.route('/notification', methods=['POST'])
@jwt_required()
def add_notification():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    try:
        # Medication Table
        # patient_id = request.json.get('patientId')
        medication_name = request.json.get('medicationName')
        commence_date = request.json.get('comDate')
        terminate_date = request.json.get('termDate')
        frequency = request.json.get('frequency')
        quantity_mg = request.json.get('quantityMeds')

        # Reminder Table
        # patient_id = request.json.get('patientId') # For both medication and reminder table
        # clinic_id = request.json.get('clinicId')
        # medication_id = #fetch from medication table
        appt_location = request.json.get('location')
        appt_date = request.json.get('appointmentDate')
        appt_time = request.json.get('appointmentTime')
        # remind_type = request.json.get('reminderType')
        # remind_desc = request.json.get('reminderDesc')

        cursor.execute("INSERT INTO medications ()")

    
    except Exception as e:
        return jsonify({'error': str(e)}), 400


def send_appointment_reminder():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twilio_number = os.environ['TWILIO_NUMBER']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hi, this is a reminder for your appointment at [Date & Time].",
        from_=twilio_number,
        to=customer_phone_number
    )

    return jsonify({'message': 'Message sent successfully'}), 200