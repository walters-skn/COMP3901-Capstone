-- DROP DATABASE diabot;
create database diabot;
USE diabot;

CREATE TABLE `users`(
    user_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    password VARCHAR(225) NOT NULL,
    email VARCHAR(225),
    is_admin INT
);
CREATE TABLE `patients`(
    patient_id INT PRIMARY KEY,
    address1 VARCHAR(255),
    address2 VARCHAR(255),
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL
);
CREATE TABLE `clinics`(
    clinic_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    patient_id INT,
    name VARCHAR(50),
    type VARCHAR(10),
    address VARCHAR(80),
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
);
CREATE TABLE `contacts` (
    patient_id int not null,
    phone VARCHAR(25),
    PRIMARY KEY(patient_id, phone),
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
);
CREATE TABLE `meals` (
    meal_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    patient_id INT,
    meal_type VARCHAR(120),
    meal_cont VARCHAR(200),
    nutri_lvl DOUBLE NOT NULL,
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
);
CREATE TABLE `medications` (
    medication_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    med_name varchar(255) NOT NULL,
    qty INT NOT NULL,
    patient_id INT,
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
);
CREATE TABLE `reminders` (
    rem_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    app_date date NOT NULL,
    patient_id INT NOT NULL,
    remind_type varchar(255) NOT NULL,
    remind_desc varchar(255) NOT NULL,
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
);
CREATE TABLE `symptoms` (
    symptom_id int PRIMARY key NOT NULL AUTO_INCREMENT,
    gender varchar(6) NOT NULL,
    weight float NOT NULL,
    height float NOT NULL,
    age int NOT NULL,
    waist_circumference float NOT NULL,
    is_physically_active int NOT NULL,
    fruit_veggie_intake int NOT NULL,
    has_high_bp_medication int NOT NULL,
    has_hyperglycemia_history int NOT NULL,
    has_family_history int NOT NULL
);

CREATE TABLE diabetes_questions(
	db_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
	questions VARCHAR(255) NOT NULL
);



INSERT INTO diabetes_questions(questions)
VALUES('What is your gender?'),
	  ('What is your height?'),
	  ('What is your weight?'),
     	 ('What is your age?'),
  ('What is your waist circumference?'),
 ('Are you physically active?'),
 ('Do you prefer fruits or vegetables?'),
 ('Are you taking any form of medication for high blood pressure?'),
 ('When last did you check your glucose level and what was the reading?'),
 ('Do you have any family member who may have diabetes?');
      
