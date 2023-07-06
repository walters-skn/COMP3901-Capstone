USE diabot;

INSERT INTO patients( address1, address2, first_name, last_name )VALUES('Richardware','NULL','Pamella', 'Jones');
INSERT INTO patients( address1, address2, first_name, last_name )VALUES('David Ave','NULL', 'Patrick', 'Allen');
INSERT INTO patients( address1, address2, first_name, last_name )VALUES('Doherty DR', 'Cider Walk Ave', 'Mitchell', 'Montana');

INSERT INTO clinics( name, type, address )VALUES('kingston public hospital', 'public', '6 Mona Rd');
INSERT INTO clinics( name, type, address )VALUES('UWI hospital', 'public', 'Mona Rd');
INSERT INTO clinics( name, type, address )VALUES('Sir Bustamante hospital', 'public', 'Musgrave Rd');

INSERT INTO contacts(patient_id, phone)VALUES(1,'1876-233-8765');
INSERT INTO contacts(patient_id, phone)VALUES(2, '1876-675-0089');
INSERT INTO contacts(patient_id, phone)VALUES(3, '1876-142-8523');

INSERT INTO meals(patient_id, meal_type, meal_cont, nutri_lvl)VALUES(1, 'breakfast', '2 slice wheat bread with eggs', '2');
INSERT INTO meals(patient_id, meal_type, meal_cont, nutri_lvl)VALUES(2, 'dinner', '3 spoon rice with baked chicken and broccoli', '3');

INSERT INTO medications(med_name, qty, patient_id)VALUES('insulin isophane', 500mg, 1);
INSERT INTO medications(med_name, qty, patient_id)VALUES('metaformin', 1000mg, 2);

INSERT INTO reminders(app_date, patient_id, remind_type, remind_desc)VALUES('21-07-23', 1, 'appointment', 'patient has appointment at Sir Bustamante Hospital');
INSERT INTO reminders(app_date, patient_id, remind_type, remind_desc)VALUES('07-07-23', 2, 'medication', 'patient has meds to take at 2pm');

INSERT INTO diabetes_questions(questions)
VALUES
	('What is your gender?'),
	('What is your height?'),
	('What is your weight?'),
    ('What is your age?'),
	('What is your waist circumference?'),
	('Are you physically active?'),
	('Do you prefer fruits or vegetables?'),
	('Are you taking any form of medication for high blood pressure?'),
	('When last did you check your glucose level and what was the reading?'),
	('Do you have any family member who may have diabetes?');
      


-- Inspect dummy data
SELECT * FROM patients;
SELECT * FROM clinics;
SELECT * FROM contacts;
SELECT * FROM meals;
SELECT * FROM medications;
SELECT * FROM reminders;
SELECT * FROM diabetes_questions;




INSERT INTO diabetes_questions(questions)
VALUES
	('What is your gender?'),
	('What is your height?'),
	('What is your weight?'),
    ('What is your age?'),
	('What is your waist circumference?'),
	('Are you physically active?'),
	('Do you prefer fruits or vegetables?'),
	('Are you taking any form of medication for high blood pressure?'),
	('When last did you check your glucose level and what was the reading?'),
	('Do you have any family member who may have diabetes?');
      


-- Inspect dummy data
SELECT * FROM patients;
SELECT * FROM clinics;
SELECT * FROM contacts;
SELECT * FROM meals;
SELECT * FROM medications;
SELECT * FROM reminders;
SELECT * FROM diabetes_questions;




