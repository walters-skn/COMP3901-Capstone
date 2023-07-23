USE diabot;

INSERT INTO users (email, upassword, is_admin) VALUES ('admin@admin.com', 'admin', 1);


INSERT INTO patients (first_name, last_name, address1, address2) VALUES ('Pamella', 'Jones', 'Richardware', NULL);
INSERT INTO patients (first_name, last_name, address1, address2) VALUES ('Patrick', 'Allen', 'David Ave', NULL);
INSERT INTO patients (first_name, last_name, address1, address2) VALUES ('Mitchell', 'Montana', 'Doherty DR', 'Cider Walk Ave');

INSERT INTO medications (patient_id, medication_name, commencement_date, termination_date, frequency, quantity) VALUES (1, 'insulin isophane', '18-07-23', '26-07-23', 'once daily', 500);
INSERT INTO medications (patient_id, medication_name, commencement_date, termination_date, frequency, quantity) VALUES (2, 'metaformin', '23-08-23', '12-08-23', 'twice daily', 1000);

INSERT INTO clinics (cname, ctype, caddress, parish) VALUES ('Angels Health Care AMDG', 'Private', 'Shop 16 Angles Plaza Ang1 Spanish Town St. Catherine', 'St. Catherine');
INSERT INTO clinics (cname, ctype, caddress, parish) VALUES ('Amadeo Medical Group', 'Private', '11A Young St, Spanish Town St. Catherine', 'St. Catherine');
INSERT INTO clinics (cname, ctype, caddress, parish) VALUES ('St Jago Park Health Center (SERHA)', 'Public', ' Burke Road, Spanish Town St. Catherine', 'St. Catherine');
INSERT INTO clinics (cname, ctype, caddress, parish) VALUES ('Andrews Memorial Seventh-Day Adventist Hospital', 'Private', '27 Hope Rd, Kingston', 'Kingston');
INSERT INTO clinics (cname, ctype, caddress, parish) VALUES ('Medical Associates', 'Private', '18, 10 Tangerine Pl, Kingston', 'Kingston');
INSERT INTO clinics (cname, ctype, caddress, parish) VALUES ('Kingston Public Hospital (K.P.H.)', 'Public', 'North St, Kingston', 'Kingston');
INSERT INTO clinics (cname, ctype, caddress, parish) VALUES ('Trinity Mall Medical Centre', 'Private', '3 Barnett St, Montego Bay', 'St. James');
INSERT INTO clinics (cname, ctype, caddress, parish) VALUES ('Sekhmet Medical Center', 'Private', 'Shop 14, Bogue City Center, Bogue Rd, Montego Bay', 'St. James');
INSERT INTO clinics (cname, ctype, caddress, parish) VALUES ('Cornwall Regional Hospital', 'Public', 'Montego Bay, St James', 'St. James');

INSERT INTO reminders(patient_id, clinic_id, medication_id, appt_date, appt_time, remind_type, remind_desc)VALUES(1, 1, NULL, '21-07-23', NULL, 'appointment', 'patient has appointment at 6am');
INSERT INTO reminders(patient_id, clinic_id, medication_id, appt_date, appt_time, remind_type, remind_desc)VALUES(2, 3, 2, NULL, NULL, 'medication', 'patient has meds to take at 2pm');


INSERT INTO contacts (patient_id, phone) VALUES (1, '1876-233-8765');
INSERT INTO contacts (patient_id, phone) VALUES (2, '1876-675-0089');
INSERT INTO contacts (patient_id, phone) VALUES (3, '1876-142-8523');

INSERT INTO meals (patient_id, meal_type, meal_cont, nutri_lvl) VALUES (2, 'breakfast', '2 slice wheat bread with eggs', 2);
INSERT INTO meals (patient_id, meal_type, meal_cont, nutri_lvl) VALUES (2, 'dinner', '3 spoon rice with baked chicken and broccoli', 3);

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


