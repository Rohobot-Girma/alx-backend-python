#!/usr/bin/python3
import seed

def stream_user_ages():
    """Generator that yields user ages one by one."""
    connection = seed.connect_to_prodev()
    if not connection:
        return
    
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    
    for row in cursor:
        yield row[0]  # Yield the age value
    
    cursor.close()
    connection.close()

def average_age():
    """Calculate average age using the generator without loading all data into memory."""
    total_age = 0
    count = 0
    
    for age in stream_user_ages():
        total_age += age
        count += 1
    
    if count > 0:
        average = total_age / count
        print(f"Average age of users: {average}")
    else:
        print("No users found") 