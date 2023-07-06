from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'diabot1'

cnx = mysql.connector.connect(user='root', password='mysql-25', host='localhost', database=DB_NAME)
cursor = cnx.cursor()


TABLES = {}
TABLES['users'] = (
    "CREATE TABLE `users` ("
    "  `user_id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
    "  `password` VARCHAR(255) NOT NULL,"
    "  `email` VARCHAR(255) NOT NULL,"
    "  `is_admin` INT"
    ") ENGINE=InnoDB"
)
TABLES['patients'] = (
    "CREATE TABLE `patients` ("
    "  `patient_id` INT PRIMARY KEY,"
    "  `address1` varchar(255),"
    "  `address2` varchar(255),"
    "  `first_name` varchar(255) NOT NULL,"
    "  `last_name` varchar(255) NOT NULL,"
    ") ENGINE=InnoDB"
)

TABLES['medications'] = (
    "CREATE TABLE `medications` ("
    "  `medication_id`  INT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
    "  `med_name` varchar(255) NOT NULL,"
    "  `qty` INT NOT NULL,"
    "  `patient_id` INT,"
    "  FOREIGN KEY(patient_id) REFERENCES `patients`(patient_id)"
    ") ENGINE=InnoDB")

TABLES['reminders'] = (
    "CREATE TABLE `reminders` ("
    "  `rem_id `INT PRIMARY KEY NOT NULL AUTO_INCREMENT,,"
    "  `app_date` date NOT NULL,"
    "  `patient_id` INT NOT NULL,"
    "  `remind_type` varchar(255) NOT NULL,"
    " `remind_desc` varchar(255) NOT NULL,"
    "  FOREIGN KEY(patient_id) REFERENCES `patients`(patient_id)"
    ") ENGINE=InnoDB")

TABLES['symptoms'] = (
    "CREATE TABLE `symptoms` ("
    "  `symptom_id` int PRIMARY key NOT NULL AUTO_INCREMENT,"
    "  `gender` varchar(6) NOT NULL,"
    "  `weight` float NOT NULL,"
    "  `height` float NOT NULL,"
    "  `age` int NOT NULL,"
    "  `waist_circumference` float NOT NULL,"
    "  `is_physically_active` INT NOT NULL,"
    "  `fruit_veggie_intake` int NOT NULL,"
    "  `has_high_bp_medication` INT NOT NULL,"
    "  `has_hyperglycemia_history` INT NOT NULL,"
    "  `has_family_history` INT NOT NULL,"
    ") ENGINE=InnoDB")

# TABLES['risks'] = (
#     "CREATE TABLE `risks` ("
#     "  `risk_id` int(11) NOT NULL AUTO_INCREMENT,"
#     "  `patient_id` int(11) NOT NULL,"
#     "  `risk_score` int(11) NOT NULL,"
#     "  `risk_category` varchar(10) NOT NULL,"
#     "  `chance_of_developing_diabetes` float NOT NULL,"
#     "  `screening_recommendation` varchar(100) NOT NULL,"
#     "  PRIMARY KEY (`risk_id`),"
#     "  KEY `patient_id` (`patient_id`),"
#     "  CONSTRAINT `risks_ibfk_1` FOREIGN KEY (`patient_id`) "
#     "     REFERENCES `symptoms` (`symptom_id`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")

TABLES['clinics'] = (
    "CREATE TABLE `clinics` ("
    "  `clinic_id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,"
    "  `patient_id INT`,"
    "  `name` varchar(50),"
    "  `type` varchar(10),"
    "  `address` varchar(100),"
    "  FOREIGN KEY(patient_id) REFERENCES `patients`(patient_id)"
    ") ENGINE=InnoDB")

TABLES['meals'] = (
    "CREATE TABLE `meals` ("
    "  `meal_id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,"
    "  `patient_id` int,"
    "  `meal_type` varchar(120),"
    "  `meal_cont` varchar(200) NOT NULL,"
    "  `nutri_lvl` DOUBLE NOT NULL,"
    " FOREIGN KEY(patient_id) REFERENCES `patients`(patient_id)"
    ") ENGINE=InnoDB")

TABLES['diabetes_questions'] = (
    "CREATE TABLE 'diabetes_questions'("
    "   `db_id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL," 
	"   `questions` VARCHAR(255) NOT NULL"
    
    ") ENGINE=InnoDB")


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