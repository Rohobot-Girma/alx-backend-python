#!/usr/bin/python3
import seed

def stream_users_in_batches(batch_size):
    """Generator that yields batches of users from the database."""
    connection = seed.connect_to_prodev()
    if not connection:
        return
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    
    batch = []
    for row in cursor:
        batch.append(row)
        if len(batch) >= batch_size:
            yield batch
            batch = []
    
    # Yield any remaining rows
    if batch:
        yield batch
    
    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """Process each batch to filter users over age 25 and print them."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user) 