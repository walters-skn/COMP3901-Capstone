from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'diabot'

cnx = mysql.connector.connect(user='root', password='mysql-25', host='localhost', database=DB_NAME)
cursor = cnx.cursor()


TABLES = {}

TABLES['users'] = (
    "CREATE TABLE `users` ("
    "  `user_id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
    "  `email` VARCHAR(255) NOT NULL,"
    "  `password` VARCHAR(255) NOT NULL,"
    "  `is_admin` INT NOT NULL DEFAULT 0"
    ") ENGINE=InnoDB"
)

TABLES['patients'] = (
    "CREATE TABLE `patients` ("
    "  `patient_id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
    "  `user_id` INT,"
    "  `first_name` VARCHAR(255) NOT NULL,"
    "  `last_name` VARCHAR(255) NOT NULL,"
    "  `address1` VARCHAR(255),"
    "  `address2` VARCHAR(255),"
    "  FOREIGN KEY(user_id) REFERENCES `users`(user_id)"
    ") ENGINE=InnoDB"
)

TABLES['medications'] = (
    "CREATE TABLE `medications` ("
    "  `medication_id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
    "  `patient_id` INT,"
    "  `med_name` VARCHAR(255) NOT NULL,"
    "  `qty` INT NOT NULL,"
    "  FOREIGN KEY(patient_id) REFERENCES `patients`(patient_id)"
    ") ENGINE=InnoDB"
)

TABLES['reminders'] = (
    "CREATE TABLE `reminders` ("
    "  `rem_id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
    "  `patient_id` INT,"
    "  `app_date` DATE NOT NULL,"
    "  `remind_type` VARCHAR(255) NOT NULL,"
    "  `remind_desc` VARCHAR(255) NOT NULL,"
    "  FOREIGN KEY(patient_id) REFERENCES `patients`(patient_id)"
    ") ENGINE=InnoDB"
)

TABLES['symptoms'] = (
    "CREATE TABLE `symptoms` ("
    "  `symptom_id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
    "  `patient_id` INT,"
    "  `gender` VARCHAR(255),"
    "  `weight` FLOAT,"
    "  `height` FLOAT,"
    "  `age` INT,"
    "  `waist_circumference` FLOAT,"
    "  `is_physically_active` BOOLEAN,"
    "  `fruit_veggie_intake` INT,"
    "  `has_high_bp_medication` BOOLEAN,"
    "  `has_hyperglycemia_history` BOOLEAN,"
    "  `has_family_history` BOOLEAN,"
    "  FOREIGN KEY(patient_id) REFERENCES `patients`(patient_id)"
    ") ENGINE=InnoDB"
)

TABLES['clinics'] = (
    "CREATE TABLE `clinics` ("
    "  `clinic_id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
    "  `patient_id` INT,"
    "  `name` VARCHAR(255),"
    "  `type` VARCHAR(255),"
    "  `address` VARCHAR(255),"
    "  `parish` VARCHAR(255),"
    "  FOREIGN KEY(patient_id) REFERENCES `patients`(patient_id)"
    ") ENGINE=InnoDB"
)

TABLES['contacts'] = (
    "CREATE TABLE `contacts` ("
    "  `patient_id` INT,"
    "  `phone` VARCHAR(255),"
    "   PRIMARY KEY(patient_id, phone),"
    "  FOREIGN KEY(patient_id) REFERENCES `patients`(patient_id)"
    ") ENGINE=InnoDB"
)

TABLES['meals'] = (
    "CREATE TABLE `meals` ("
    "  `meal_id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
    "  `patient_id` INT,"
    "  `meal_type` VARCHAR(255),"
    "  `meal_cont` VARCHAR(255) NOT NULL,"
    "  `nutri_lvl` INT NOT NULL,"
    "  FOREIGN KEY(patient_id) REFERENCES `patients`(patient_id)"
    ") ENGINE=InnoDB"
)

TABLES['diabetes_questions'] = (
    "CREATE TABLE `diabetes_questions` ("
    "   `db_id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT," 
	"   `question` VARCHAR(255) NOT NULL,"
    "   `is_answered` INT NOT NULL DEFAULT 0"
    ") ENGINE=InnoDB"
)


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)


for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


cursor.close()
cnx.close()