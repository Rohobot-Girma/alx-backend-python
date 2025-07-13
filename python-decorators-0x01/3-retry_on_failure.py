import sqlite3
import functools
import time


def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('user.db')
        try:
            return func(conn, args, kwargs)
        finally:
            conn.close()
    return wrapper


def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempts in range(1, retries + 1):
                try:
                    print(f'attempting {attempts}')
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    print(f'error-{e}, retrying in {delay}s')
                    time.sleep(delay)
            print('all retries failed')
            raise last_error
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


# attempt to fetch users with automatic retry on failure
users = fetch_users_with_retry()
print(users)
