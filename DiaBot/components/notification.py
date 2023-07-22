from flask import Blueprint, request, jsonify
import mysql.connector
from db.connect import db_config

# Download the helper library from https://www.twilio.com/docs/python/install
import os
# !pip install twilio
from twilio.rest import Clientdentials


notification_bp = Blueprint('notification')

@notification_bp.route('/notification', methods=['POST'])
def add_notification():
    # Medication Table
    medication_name = request.json.get('medicationName')
    # quantity_mg = request.json.get('')
    commence_date = request.json.get('comDate')
    terminate_date = request.json.get('termDate')
    # patient_id = request.json.get('patientId')
    frequency = request.json.get('frequency')

    # Reminder Table
    # patient_id = request.json.get('patientId')
    # clinic_id = request.json.get('clinicId')
    medication_id = request.json.get('medicationId')
    appt_location = request.json.get('location')


def send_sms():
    try:
        # Read more at http://twil.io/secure
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        body="Hello from Twilio",
        from_="+15407012621",
        to="+18765664460"
        )
        print(message.sid)
    except Exception as e:
        return jsonify({'error': str(e)}), 400