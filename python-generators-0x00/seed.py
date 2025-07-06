import mysql.connector
import csv
import os
from mysql.connector import errorcode

def connect_db():
    """Connect to the MySQL server (not to a specific database)."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Change if your MySQL user is different
            password='',  # Change if your MySQL password is set
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    """Create the ALX_prodev database if it does not exist."""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS ALX_prodev DEFAULT CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';"
        )
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

def connect_to_prodev():
    """Connect to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Change if your MySQL user is different
            password='',  # Change if your MySQL password is set
            database='ALX_prodev'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    """Create the user_data table if it does not exist."""
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL,
                INDEX(user_id)
            );
            """
        )
        connection.commit()
        print("Table user_data created successfully")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Failed creating table: {err}")

def insert_data(connection, csv_file):
    """Insert data from CSV into user_data table if not already present."""
    try:
        cursor = connection.cursor()
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cursor.execute(
                    """
                    INSERT IGNORE INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (row['user_id'], row['name'], row['email'], row['age'])
                )
        connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Error inserting data: {e}") 