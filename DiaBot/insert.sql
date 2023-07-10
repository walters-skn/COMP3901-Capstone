USE diabot;

INSERT INTO users (email, password, is_admin) VALUES ('admin@admin.com', 'admin', 1);
INSERT INTO users (email, password) VALUES ('user1@example.com', 'user1');
INSERT INTO users (email, password) VALUES ('user2@example.com', 'user2');

INSERT INTO patients (user_id, address1, address2, first_name, last_name) VALUES (2, 'Richardware', NULL,'Pamella', 'Jones');
INSERT INTO patients (user_id, address1, address2, first_name, last_name) VALUES (3, 'David Ave', NULL, 'Patrick', 'Allen');
INSERT INTO patients (user_id, address1, address2, first_name, last_name) VALUES (NULL, 'Doherty DR', 'Cider Walk Ave', 'Mitchell', 'Montana');

INSERT INTO clinics (patient_id, name, type, address) VALUES (3, 'kingston public hospital', 'public', '6 Mona Rd');
INSERT INTO clinics (patient_id, name, type, address) VALUES (3, 'UWI hospital', 'public', 'Mona Rd');
INSERT INTO clinics (patient_id, name, type, address) VALUES (2, 'Sir Bustamante hospital', 'public', 'Musgrave Rd');

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
INSERT INTO diabetes_questions (question) VALUES ('What is your height?');
INSERT INTO diabetes_questions (question) VALUES ('What is your weight?');
INSERT INTO diabetes_questions (question) VALUES ('What is your age?');
INSERT INTO diabetes_questions (question) VALUES ('What is your waist circumference?');
INSERT INTO diabetes_questions (question) VALUES ('Are you physically active?');
INSERT INTO diabetes_questions (question) VALUES ('Do you prefer fruits or vegetables?');
INSERT INTO diabetes_questions (question) VALUES ('Are you taking any form of medication for high blood pressure?');
INSERT INTO diabetes_questions (question) VALUES ('When last did you check your glucose level and what was the reading?');
INSERT INTO diabetes_questions (question) VALUES ('Do you have any family member who may have diabetes?');
      


-- Inspect dummy data
SELECT * FROM patients;
SELECT * FROM clinics;
SELECT * FROM contacts;
SELECT * FROM meals;
SELECT * FROM medications;
SELECT * FROM reminders;
SELECT * FROM diabetes_questions;


