USE diabot;
INSERT INTO patients( address1, address2, first_name, last_name )VALUES('Richardware',NULL,'Pamella', 'Jones');
INSERT INTO patients( address1, address2, first_name, last_name )VALUES('David Ave',NULL, 'Patrick', 'Allen');
INSERT INTO patients( address1, address2, first_name, last_name )VALUES('Doherty DR', 'Cider Walk Ave', 'Mitchell', 'Montana');

INSERT INTO clinics( name, type, address )VALUES('Angels Health Care AMDG', 'Private', 'shop 16 Angles Plaza Ang1 Spanish Town St. Catherine');
INSERT INTO clinics( name, type, address )VALUES('Amadeo Medical Group', 'Private', '11A Young St, Spanish Town St. Catherine');
INSERT INTO clinics( name, type, address )VALUES('St Jago Park Health Center (SERHA)', 'Public', ' Burke Road, Spanish Town St. Catherine');
INSERT INTO clinics( name, type, address )VALUES('Andrews Memorial Seventh-Day Adventist Hospital', 'Private', '27 Hope Rd, Kingston');
INSERT INTO clinics( name, type, address )VALUES('Medical Associates', 'Private', '18, 10 Tangerine Pl, Kingston');
INSERT INTO clinics( name, type, address )VALUES('Kingston Public Hospital (K.P.H.)', 'Private', '3 Barnett St, Montego Bay');
INSERT INTO clinics( name, type, address )VALUES('Sekhmet Medical Center', 'Private', 'Shop 14, Bogue City Center, Bogue Rd, Montego Bay');
INSERT INTO clinics( name, type, address )VALUES('Cornwall Regional Hospital', 'Public', 'Montego Bay, St James');


INSERT INTO contacts(patient_id, phone)VALUES(1,'1876-233-8765');
INSERT INTO contacts(patient_id, phone)VALUES(2,'1876-675-0089');
INSERT INTO contacts(patient_id, phone)VALUES(3,'1876-142-8523');

INSERT INTO contacts (patient_id, phone) VALUES ( 2,'1876-233-8765');
INSERT INTO contacts (patient_id, phone) VALUES ( 2, '1876-675-0089');
INSERT INTO contacts (patient_id, phone) VALUES ( 3, '1876-142-8523');

INSERT INTO meals (patient_id, meal_type, meal_cont, nutri_lvl) VALUES (2, 'breakfast', '2 slice wheat bread with eggs', 2);
INSERT INTO meals (patient_id, meal_type, meal_cont, nutri_lvl) VALUES (2, 'dinner', '3 spoon rice with baked chicken and broccoli', 3);

INSERT INTO medications (patient_id, med_name, qty) VALUES (NULL, 'insulin isophane', 500);
INSERT INTO medications (patient_id, med_name, qty) VALUES (3, 'metaformin', 1000);

INSERT INTO reminders (patient_id, app_date, remind_type, remind_desc) VALUES (3, '21-07-23', 'appointment', 'patient has appointment at Sir Bustamante Hospital');
INSERT INTO reminders (patient_id, app_date, remind_type, remind_desc) VALUES (2, '07-07-23', 'medication', 'patient has meds to take at 2pm');

INSERT INTO diabetes_questions (question) VALUES ('What is your gender?');
INSERT INTO diabetes_questions (question) VALUES ('What is your height(meters)?');
INSERT INTO diabetes_questions (question) VALUES ('What is your weight(kg)?');
INSERT INTO diabetes_questions (question) VALUES ('What is your age?');
INSERT INTO diabetes_questions (question) VALUES ('What is your waist circumference(cm)?');
INSERT INTO diabetes_questions (question) VALUES ('Are you physically active?');
INSERT INTO diabetes_questions (question) VALUES ('How many times per day do you eat fruits or vegetables?');
INSERT INTO diabetes_questions (question) VALUES ('Are you taking any form of medication for high blood pressure?');
INSERT INTO diabetes_questions (question) VALUES ('Is your glucose level above 130mg/dL?');
INSERT INTO diabetes_questions (question) VALUES ('Is there a history of diabetes in your family?');
      


-- Inspect dummy data
SELECT * FROM patients;
SELECT * FROM clinics;
SELECT * FROM contacts;
SELECT * FROM meals;
SELECT * FROM medications;
SELECT * FROM reminders;
SELECT * FROM diabetes_questions;


