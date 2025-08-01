#!/usr/bin/python3
import seed

def stream_users():
    """Generator that yields each row from user_data table as a dictionary."""
    connection = seed.connect_to_prodev()
    if not connection:
        return
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    
    for row in cursor:
        yield row
    
    cursor.close()
    connection.close() 