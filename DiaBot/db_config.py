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
    "  `password` VARCHAR(255) NOT NULL,"
    "  `email` VARCHAR(255) NOT NULL,"
    "  `is_admin` INT"
    ") ENGINE=InnoDB"
)
TABLES['patients'] = (
    "CREATE TABLE `patients` ("
    "  `patient_id` varchar(50) NOT NULL,"
    "  `pfirst_name` varchar(50) NOT NULL,"
    "  `plast_name` varchar(50) NOT NULL,"
    "  `Plast_name` varchar(50) NOT NULL,"
    "  `uname` varchar(50) NOT NULL,"
    "  `address` varchar(50) NOT NULL,"
    "  `contact` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`patient_id`)"
    ") ENGINE=InnoDB"
)

TABLES['medications'] = (
    "CREATE TABLE `medications` ("
    "  `med_id` varchar(50) NOT NULL,"
    "  `med_name` varchar(50) NOT NULL,"
    "  `qty` varchar(50) NOT NULL,"
    "  `patient_id` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`med_id`)"
    "  KEY `patient_id` (`patient_id`),"
    "  CONSTRAINT `medications_ibfk_1` FOREIGN KEY (`patient_id`) "
    "     REFERENCES `patients` (`patient_id`) ON DELETE CASCADE ON UPDATE CASCADE"
    ") ENGINE=InnoDB")

TABLES['appointments'] = (
    "CREATE TABLE `appointments` ("
    "  `app_id` varchar(50) NOT NULL,"
    "  `app_date` date NOT NULL,"
    "  `patient_id` varchar(50) NOT NULL,"
    "  `med_id` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`app_id`)"
    "  KEY `patient_id` (`patient_id`),"
    "  CONSTRAINT `appointments_ibfk_1` FOREIGN KEY (`patient_id`) "
    "     REFERENCES `patients` (`patient_id`) ON DELETE CASCADE ON UPDATE CASCADE"
    "  KEY `med_id` (`med_id`),"
    "  CONSTRAINT `appointments_ibfk_2` FOREIGN KEY (`med_id`) "
    "     REFERENCES `medications` (`med_id`) ON DELETE CASCADE ON UPDATE CASCADE"
    ") ENGINE=InnoDB")

TABLES['symptoms'] = (
    "CREATE TABLE `symptoms` ("
    "  `symptom_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `gender` varchar(6) NOT NULL,"
    "  `weight` float NOT NULL,"
    "  `height` float NOT NULL,"
    "  `age` int(11) NOT NULL,"
    "  `waist_circumference` float NOT NULL,"
    "  `is_physically_active` tinyint(1) NOT NULL,"
    "  `fruit_veggie_intake` int(11) NOT NULL,"
    "  `has_high_bp_medication` tinyint(1) NOT NULL,"
    "  `has_hyperglycemia_history` tinyint(1) NOT NULL,"
    "  `has_family_history` tinyint(1) NOT NULL,"
    "  PRIMARY KEY (`symptom_id`)"
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

TABLES['clinic'] = (
    "CREATE TABLE `clinic` ("
    "  `clinic_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `clinic_name` varchar(50) NOT NULL,"
    "  `clinic_type` varchar(50) NULL,"
    "  `clinic_address` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`clinic_id`)"
    ") ENGINE=InnoDB")

TABLES['meal'] = (
    "CREATE TABLE `meal` ("
    "  `meal_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `patient_id` int(11) NOT NULL,"
    "  `meal_name` varchar(50) NOT NULL,"
    "  `meal_type` varchar(50) NOT NULL,"
    "  `meal_description` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`meal_id`),"
    "  KEY `patient_id` (`patient_id`),"
    "  CONSTRAINT `meal_ibfk_1` FOREIGN KEY (`patient_id`) "
    "     REFERENCES `patients` (`patient_id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['meal_content'] = (
    "CREATE TABLE `meal_content` ("
    "  `meal_content_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `meal_id` int(11) NOT NULL,"
    "  `food_name` varchar(50) NOT NULL,"
    "  `food_type` varchar(50) NOT NULL,"
    "  `food_description` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`meal_content_id`),"
    " KEY `meal_id` (`meal_id`),"
    " CONSTRAINT `meal_content_ibfk_1` FOREIGN KEY (`meal_id`) "
    "     REFERENCES `meal` (`meal_id`) ON DELETE CASCADE"
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