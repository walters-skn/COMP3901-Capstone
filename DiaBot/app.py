from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

# @app.route('/', methods=['GET'])
# def home():
#     return "Hello World"

@app.route('/predict', methods=['POST'])
def predict(patient_id=None):
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
    bmi = weight / (height * height)
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