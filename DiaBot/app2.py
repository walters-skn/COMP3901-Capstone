from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import mysql.connector

import mysql.connector


app = Flask(__name__)
app.config.from_object(__name__)
app.config["JWT_SECRET_KEY"] = "comp3901-secret-key"
jwt = JWTManager(app)

CORS(app, resources={r'/*': {'origins': '*'}})

db_config = {
    "user": "root",
    "password": "mysql-25",
    "host": "localhost",
    "database": "diabot"
}



@app.route('/', methods=['GET'])
def home():
    return "Hello World"


@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        if user:
            access_token = create_access_token(identity=user[0])
            return jsonify(access_token=access_token)
        else:
            return jsonify({"error": "Invalid username or password"}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        # check if email already exists
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user:
            return jsonify({"error": "Email already exists"}), 400
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
        cnx.commit()
        return jsonify({"message": "Patient successfully registered"}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/predict', methods=['GET', 'POST'])
def send_questions_to_client():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM diabetes_questions WHERE is_answered = 0 LIMIT 1")
    question_data = []
    
    if request.method == 'GET':
        try:
            for db_id, questions, is_answered in cursor:
                if is_answered == 1:
                    continue
                question = {}
                question['db_id'] = db_id
                question['question'] = questions
                question['is_answered'] = is_answered
                question_data.append(question)

                cursor.execute("UPDATE diabetes_questions SET is_answered = 1 WHERE db_id = %s", (db_id,))
                cnx.commit()
            cursor.close()
            return jsonify(question_data)
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    # query the is_answered column in the database to see if the question has been answered
    # if it has been answered, predict if the patient has diabetes
    # if it has not been answered, return the question to the client
    if request.method == 'POST':
        try:
            db_id = request.json.get('db_id')
            answer = request.json.get('answer')
            cursor.execute("UPDATE diabetes_questions SET is_answered = 1 WHERE db_id = %s", (db_id,))
            cnx.commit()
            cursor.close()
            return jsonify({'message': 'Answer successfully saved'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400



def predict(patient_id=None):
    patient_id = request.json.get('patient_id')
    gender = request.json.get('gender')
    weight = float(request.json.get('weight'))
    height = float(request.json.get('height'))
    age = int(request.json.get('age'))
    waist_circumference = float(request.json.get('waist_circumference'))
    is_physically_active = request.json.get('is_physically_active')
    fruit_veggie_intake = request.json.get('fruit_veggie_intake')
    has_high_bp_medication = request.json.get('has_high_bp_medication')
    has_hyperglycemia_history = request.json.get('has_hyperglycemia_history')
    has_family_history = request.json.get('has_family_history')
    
    risk_score = calculate_risk_score(gender, weight, height, age, waist_circumference, is_physically_active,
                                      fruit_veggie_intake, has_high_bp_medication, has_hyperglycemia_history,
                                      has_family_history)
    
    risk_category = determine_risk_category(risk_score)
    chance_of_developing_diabetes = determine_chance_of_diabetes(risk_score)
    screening_recommendation = determine_screening_recommendation(risk_category)

    # store the request data as a patient symptoms in the patients table
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    cursor.execute("""
        INSERT INTO patients 
            (patient_id, gender, weight, height, age, waist_circumference, is_physically_active, fruit_veggie_intake, has_high_bp_medication, has_hyperglycemia_history, has_family_history) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (patient_id, gender, weight, height, age, waist_circumference, is_physically_active, fruit_veggie_intake, has_high_bp_medication, has_hyperglycemia_history, has_family_history))
    cnx.commit()
    cursor.close()
    
    return jsonify({
        'total_risk_score': risk_score,
        'risk_category': risk_category,
        'chance_of_developing_diabetes': chance_of_developing_diabetes,
        'screening_recommendation': screening_recommendation
    })

def calculate_risk_score(gender, weight, height, age, waist_circumference, is_physically_active,
                         fruit_veggie_intake, has_high_bp_medication, has_hyperglycemia_history,
                         has_family_history):
    risk_score = 0
    
    # Age
    if age >= 45:
        risk_score += 3
    
    # BMI
    bmi = weight / (height * height) # weight in kg, height in m
    if bmi >= 25:
        risk_score += 3
    
    # Waist Circumference
    if gender == 'male':
        if waist_circumference >= 94:
            risk_score += 4
    else:
        if waist_circumference >= 80:
            risk_score += 4
    
    # Physical Activity
    if is_physically_active:
        risk_score -= 1
    
    # Fruit & Veggie Intake
    if fruit_veggie_intake <= 2:
        risk_score += 1
    
    # High Blood Pressure Medication
    if has_high_bp_medication:
        risk_score += 2
    
    # Hyperglycemia History
    if has_hyperglycemia_history:
        risk_score += 5
    
    # Family History
    if has_family_history:
        risk_score += 3
    
    return risk_score

def determine_risk_category(risk_score):
    if risk_score <= 14 and risk_score >= 0:
        return 'Low to moderate risk'
    elif risk_score <= 20 and risk_score >= 15:
        return 'High risk'
    else:
        return 'Very high risk'

def determine_chance_of_diabetes(risk_score):
    if risk_score <= 14 and risk_score >= 0:
        return '1-17%'
    elif risk_score <= 20 and risk_score >= 15:
        return '33%'
    else:
        return '50%'

def determine_screening_recommendation(risk_category):
    if risk_category == 'Low to moderate risk':
        return 'Recommend screening every 3-5 years with Health Professional.'
    elif risk_category == 'High risk':
        return 'Recommend screening every 1-2 years with Health Professional.'
    else:
        return 'Recommend annual screening with Health Professional.'



    

if __name__ == "__main__":
    app.run(debug=True)




