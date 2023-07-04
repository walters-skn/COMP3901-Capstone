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
    med_id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    med_name CHAR(200) NOT NULL,
    qty INT NOT NULL,
    patient_id int NOT NULL,
    PRIMARY KEY(med_id),
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id) ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE `reminders` (
    app_id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    app_date date NOT NULL,
    patient_id varchar(50) NOT NULL,
    remind_type varchar(255) NOT NULL,
    remind_desc varchar(255) NOT NULL,
    PRIMARY KEY(app_id),
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id) ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE `symptoms` (
    symptom_id int PRIMARY key NOT NULL AUTO_INCREMENT,
    gender varchar(6) NOT NULL,
    weight float NOT NULL,
    height float NOT NULL,
    age int(11) NOT NULL,
    waist_circumference float NOT NULL,
    is_physically_active tinyint(1) NOT NULL,
    fruit_veggie_intake int(11) NOT NULL,
    has_high_bp_medication tinyint(1) NOT NULL,
    has_hyperglycemia_history tinyint(1) NOT NULL,
    has_family_history tinyint(1) NOT NULL,
    PRIMARY KEY(symptom_id)
);