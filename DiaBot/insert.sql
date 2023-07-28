USE diabot;

INSERT INTO users (email, upassword, is_admin) VALUES ('admin@admin.com', 'admin', 1);


INSERT INTO patients (first_name, last_name, address1, address2) VALUES ('Pamella', 'Jones', 'Richardware', NULL);
INSERT INTO patients (first_name, last_name, address1, address2) VALUES ('Patrick', 'Allen', 'David Ave', NULL);
INSERT INTO patients (first_name, last_name, address1, address2) VALUES ('Mitchell', 'Montana', 'Doherty DR', 'Cider Walk Ave');
INSERT INTO patients (first_name, last_name, address1, address2) VALUES ('Katherine', 'Daley', 'David Clement', NULL);
INSERT INTO patients (first_name, last_name, address1, address2) VALUES ('George', 'Rose', NULL, 'Maze Ave');
INSERT INTO patients (first_name, last_name, address1, address2) VALUES ('Ezra', 'Kerr', 'Port View', NULL);

INSERT INTO medications (patient_id, medication_name, commencement_date, termination_date, frequency, quantity) VALUES (1, 'insulin isophane', '18-07-23', '26-07-23', 'once daily', 500);
INSERT INTO medications (patient_id, medication_name, commencement_date, termination_date, frequency, quantity) VALUES (2, 'metaformin', '23-08-23', '12-08-23', 'twice daily', 1000);

INSERT INTO symptoms (patient_id, gender, weight, height, age, waist_circumference, is_physically_active, fruit_veggie_intake, has_high_bp_medication, has_hyperglycemia_history, has_family_history) VALUES (1, 'female', 54, 1.5, 23, 32, true, 1, false, false, true);
INSERT INTO symptoms (patient_id, gender, weight, height, age, waist_circumference, is_physically_active, fruit_veggie_intake, has_high_bp_medication, has_hyperglycemia_history, has_family_history) VALUES (2, 'male', 64, 2.3, 30, 36, false, 0, true, true, true);
INSERT INTO symptoms (patient_id, gender, weight, height, age, waist_circumference, is_physically_active, fruit_veggie_intake, has_high_bp_medication, has_hyperglycemia_history, has_family_history) VALUES (3, 'female', 58, 1.7, 26, 34, true, 2, false, true, false);
INSERT INTO symptoms (patient_id, gender, weight, height, age, waist_circumference, is_physically_active, fruit_veggie_intake, has_high_bp_medication, has_hyperglycemia_history, has_family_history) VALUES (4, 'female', 76, 2.0, 40, 40, false, 1, false, true, true);
INSERT INTO symptoms (patient_id, gender, weight, height, age, waist_circumference, is_physically_active, fruit_veggie_intake, has_high_bp_medication, has_hyperglycemia_history, has_family_history) VALUES (5, 'male', 48, 1.4, 21, 24, false, 0, false, false, false);
INSERT INTO symptoms (patient_id, gender, weight, height, age, waist_circumference, is_physically_active, fruit_veggie_intake, has_high_bp_medication, has_hyperglycemia_history, has_family_history) VALUES (6, 'male', 56, 1.7, 27, 33, true, 2, true, true, false);

INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (3, 'Angels Health Care AMDG', 'Private', 'Shop 16 Angles Plaza Ang1 Spanish Town St. Catherine', 'St. Catherine');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (4, 'Amadeo Medical Group', 'Private', '11A Young St, Spanish Town St. Catherine', 'St. Catherine');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'St Jago Park Health Center (SERHA)', 'Public', ' Burke Road, Spanish Town St. Catherine', 'St. Catherine');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Andrews Memorial Seventh-Day Adventist Hospital', 'Private', '27 Hope Rd, Kingston', 'Kingston');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Medical Associates', 'Private', '18, 10 Tangerine Pl, Kingston', 'Kingston');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Kingston Public Hospital (K.P.H.)', 'Public', 'North St, Kingston', 'Kingston');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (5, 'Trinity Mall Medical Centre', 'Private', '3 Barnett St, Montego Bay', 'St. James');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Sekhmet Medical Center', 'Private', 'Shop 14, Bogue City Center, Bogue Rd, Montego Bay', 'St. James');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Cornwall Regional Hospital', 'Public', 'Montego Bay, St James', 'St. James');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (6, 'Annotto Bay Hospital', 'Public', 'Annotto Bay', 'St Mary');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Port Maria Hospital', 'Public', 'Trinity, Port Maria, West Indies', 'St. Mary');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'St. Ann’s Bay Hospital', 'Public', 'Seville Road, St. Ann’s Bay', 'St. Ann');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'May Pen Hospital', 'Public', 'Muirhead Avenue, May Pen, South Central Clarendon', 'Clarendon');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Lionel Town Hospital', 'Public', 'Vere', 'Clarendon');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Chapleton Community Hospital', 'Public', 'Chapleton P.O.,', 'Clarendon');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Hargreaves Memorial Hospital', 'Private', '32 Hargreaves Ave. Mandeville', 'Manchester');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Mandeville Hospital', 'Public', '32 Hargreaves Ave., Mandeville', 'Manchester');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Percy Junior Hospital', 'Public', 'Spaldings, Christiana', 'Manchester');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Black River Hospital', 'Public', ' 45 Main St. Black River', 'St. Elizabeth');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Montego Bay Hospital & Urology Centre', 'Private', '1 Mount Salem Main Rd', 'St. James');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Falmouth Hospital', 'Public', 'Rodney St. Falmouth, West Indies', 'Trelawny');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Savanna-la-mar Hospital', 'Public', 'Barracks Rd., Savanna-lar-mar', 'Westmoreland');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Royale Medical Hospital and Clinic', 'Private', '10 Lewis St., Savanna-lar-mar', 'Westmoreland');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Noel Holmes Hospital', 'Public', 'Fort Charolette Drive, Lucea', 'Hanover');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Port Antonio Hospital', 'Public', 'Naylor’s Hill, Port Antonio', 'Portland');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Princess Magaret Hospital', 'Public', 'Lyssons Road, Morant Bay', 'St. Thomas');
INSERT INTO clinics (patient_id, cname, ctype, caddress, parish) VALUES (NULL, 'Andrews Memorial Seventh-Day Adventist Hospital', 'Public', '22 Deanery Rd, Kingston', 'St. Andrew');

INSERT INTO reminders(patient_id, clinic_id, medication_id, appt_date, appt_time, remind_type, remind_desc)VALUES(1, 1, 1, NULL, NULL, 'medication', 'patient has medication to take at 6am');
INSERT INTO reminders(patient_id, clinic_id, medication_id, appt_date, appt_time, remind_type, remind_desc)VALUES(2, 3, 2, NULL, NULL, 'medication', 'patient has medication to take at 2pm');
INSERT INTO reminders(patient_id, clinic_id, medication_id, appt_date, appt_time, remind_type, remind_desc)VALUES(3, 1, NULL, 23-08-08, 10:00:00, 'appointment', 'patient has appointment at 10am');
INSERT INTO reminders(patient_id, clinic_id, medication_id, appt_date, appt_time, remind_type, remind_desc)VALUES(4, 2, NULL, 23-08-12, 12:00:00, 'appointment', 'patient has appointment at 12pm');
INSERT INTO reminders(patient_id, clinic_id, medication_id, appt_date, appt_time, remind_type, remind_desc)VALUES(5, 7, NULL, 23-08-15, 08:00:00, 'appointment', 'patient has appointment at 8am');
INSERT INTO reminders(patient_id, clinic_id, medication_id, appt_date, appt_time, remind_type, remind_desc)VALUES(6, 10, NULL, 23-09-08, 07:00:00, 'appointment', 'patient has appointment to take at 7am');


INSERT INTO contacts (patient_id, phone) VALUES (1, '1876-233-8765');
INSERT INTO contacts (patient_id, phone) VALUES (2, '1876-675-0089');
INSERT INTO contacts (patient_id, phone) VALUES (3, '1876-142-8523');
INSERT INTO contacts (patient_id, phone) VALUES (4, '1876-456-9898');
INSERT INTO contacts (patient_id, phone) VALUES (5, '1876-342-8543');
INSERT INTO contacts (patient_id, phone) VALUES (6, '1876-874-2318');

INSERT INTO recommendations (risk_category, risk_meals) VALUES ('Low to moderate risk', 'Scrambled eggs with spinach and tomatoes.');
INSERT INTO recommendations (risk_category, risk_meals) VALUES ('Low to moderate risk', 'Whole-grain toast.');
INSERT INTO recommendations (risk_category, risk_meals) VALUES ('Low to moderate risk', 'A side of fresh fruit like berries or a small apple');
INSERT INTO recommendations (risk_category, risk_meals) VALUES ('High risk', 'Grilled salmon seasoned with herbs and lemon.');
INSERT INTO recommendations (risk_category, risk_meals) VALUES ('High risk', 'Steamed broccoli and cauliflower');
INSERT INTO recommendations (risk_category, risk_meals) VALUES ('Very high risk', 'Cherry tomatoes, cucumbers and radishes.');
INSERT INTO recommendations (risk_category, risk_meals) VALUES ('Very high risk', 'Grilled chicken with a generous portion of mixed salad greens.');



INSERT INTO meals (patient_id, meal_type, meal_cont, nutri_lvl, meal_date, meal_time) VALUES (2, 'breakfast', '2 slice wheat bread with eggs', 2, '2023-07-25', '07:30:00');
INSERT INTO meals (patient_id, meal_type, meal_cont, nutri_lvl, meal_date, meal_time) VALUES (1, 'dinner', '3 spoon rice with baked chicken and broccoli', 3,  '2023-07-26', '06:00:00');

INSERT INTO diabetes_questions (question) VALUES ('What is your gender (male/female)?');
INSERT INTO diabetes_questions (question) VALUES ('What is your height (meters)?');
INSERT INTO diabetes_questions (question) VALUES ('What is your weight (kg)?');
INSERT INTO diabetes_questions (question) VALUES ('What is your age?');
INSERT INTO diabetes_questions (question) VALUES ('What is your waist circumference (cm)?');
INSERT INTO diabetes_questions (question) VALUES ('Are you physically active?');
INSERT INTO diabetes_questions (question) VALUES ('How many times per day do you eat fruits or vegetables?');
INSERT INTO diabetes_questions (question) VALUES ('Are you taking any form of medication for high blood pressure?');
INSERT INTO diabetes_questions (question) VALUES ('Is your glucose level above 130mg/dL?');
INSERT INTO diabetes_questions (question) VALUES ('Is there a history of diabetes in your family?');

