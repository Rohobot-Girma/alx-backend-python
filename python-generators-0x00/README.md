# Python Generators Project

This project introduces advanced usage of Python generators to efficiently handle large datasets, process data in batches, and simulate real-world scenarios involving live updates and memory-efficient computations. The tasks focus on leveraging Python's `yield` keyword to implement generators that provide iterative access to data, promoting optimal resource utilization, and improving performance in data-driven applications.

## Learning Objectives

By completing this project, you will:

- **Master Python Generators**: Learn to create and utilize generators for iterative data processing, enabling memory-efficient operations.
- **Handle Large Datasets**: Implement batch processing and lazy loading to work with extensive datasets without overloading memory.
- **Simulate Real-world Scenarios**: Develop solutions to simulate live data updates and apply them to streaming contexts.
- **Optimize Performance**: Use generators to calculate aggregate functions like averages on large datasets, minimizing memory consumption.
- **Apply SQL Knowledge**: Use SQL queries to fetch data dynamically, integrating Python with databases for robust data management.

## Requirements

- Proficiency in Python 3.x
- Understanding of `yield` and Python's generator functions
- Familiarity with SQL and database operations (MySQL and SQLite)
- Basic knowledge of database schema design and data seeding
- Ability to use Git and GitHub for version control and submission

## Setup Instructions

### Prerequisites

1. Install MySQL server and MySQL Connector for Python:
   ```bash
   pip install mysql-connector-python
   ```

2. Ensure MySQL server is running on your system

3. Update database credentials in `seed.py` if needed:
   - Default: `user='root'`, `password=''`
   - Modify these values according to your MySQL setup

### Database Setup

1. Run the database setup script:
   ```bash
   python3 0-main.py
   ```

   This will:
   - Connect to MySQL server
   - Create the `ALX_prodev` database
   - Create the `user_data` table with required fields
   - Populate the table with sample data from `user_data.csv`

## Project Structure

```
python-generators-0x00/
├── seed.py                    # Database connection and seeding functions
├── user_data.csv             # Sample user data
├── 0-main.py                 # Database setup test script
├── 0-stream_users.py         # Task 1: Stream users one by one
├── 1-main.py                 # Test script for streaming users
├── 1-batch_processing.py     # Task 2: Batch processing
├── 2-main.py                 # Test script for batch processing
├── 2-lazy_paginate.py        # Task 3: Lazy pagination
├── 3-main.py                 # Test script for lazy pagination
├── 4-stream_ages.py          # Task 4: Memory-efficient aggregation
├── 4-main.py                 # Test script for average age calculation
└── README.md                 # This file
```

## Tasks Overview

### Task 0: Database Setup (`seed.py`)

**Objective**: Set up MySQL database with user data table and populate it with sample data.

**Functions**:
- `connect_db()`: Connects to MySQL server
- `create_database(connection)`: Creates `ALX_prodev` database
- `connect_to_prodev()`: Connects to `ALX_prodev` database
- `create_table(connection)`: Creates `user_data` table
- `insert_data(connection, data)`: Inserts data from CSV file

**Database Schema**:
```sql
CREATE TABLE user_data (
    user_id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age DECIMAL NOT NULL,
    INDEX(user_id)
);
```

### Task 1: Stream Users (`0-stream_users.py`)

**Objective**: Create a generator that streams rows from SQL database one by one.

**Function**: `stream_users()`
- Uses `yield` keyword
- Returns each row as a dictionary
- Maximum 1 loop allowed

**Usage**:
```bash
python3 1-main.py
```

**Expected Output**:
```
{'user_id': '00234e50-34eb-4ce2-94ec-26e3fa749796', 'name': 'Dan Altenwerth Jr.', 'email': 'Molly59@gmail.com', 'age': 67}
{'user_id': '006bfede-724d-4cdd-a2a6-59700f40d0da', 'name': 'Glenda Wisozk', 'email': 'Miriam21@gmail.com', 'age': 119}
...
```

### Task 2: Batch Processing (`1-batch_processing.py`)

**Objective**: Create generators to fetch and process data in batches.

**Functions**:
- `stream_users_in_batches(batch_size)`: Yields batches of users
- `batch_processing(batch_size)`: Filters users over age 25

**Constraints**:
- Maximum 3 loops total
- Must use `yield` generator

**Usage**:
```bash
python3 2-main.py | head -n 5
```

**Expected Output**:
```
{'user_id': '00234e50-34eb-4ce2-94ec-26e3fa749796', 'name': 'Dan Altenwerth Jr.', 'email': 'Molly59@gmail.com', 'age': 67}
{'user_id': '006bfede-724d-4cdd-a2a6-59700f40d0da', 'name': 'Glenda Wisozk', 'email': 'Miriam21@gmail.com', 'age': 119}
...
```

### Task 3: Lazy Pagination (`2-lazy_paginate.py`)

**Objective**: Simulate fetching paginated data using generators to lazily load each page.

**Functions**:
- `paginate_users(page_size, offset)`: Fetches specific page
- `lazy_paginate(page_size)`: Yields pages lazily

**Constraints**:
- Maximum 1 loop
- Must use `yield` generator

**Usage**:
```bash
python3 3-main.py | head -n 7
```

**Expected Output**:
```
{'user_id': '00234e50-34eb-4ce2-94ec-26e3fa749796', 'name': 'Dan Altenwerth Jr.', 'email': 'Molly59@gmail.com', 'age': 67}
{'user_id': '006bfede-724d-4cdd-a2a6-59700f40d0da', 'name': 'Glenda Wisozk', 'email': 'Miriam21@gmail.com', 'age': 119}
...
```

### Task 4: Memory-Efficient Aggregation (`4-stream_ages.py`)

**Objective**: Use generators to compute memory-efficient aggregate functions.

**Functions**:
- `stream_user_ages()`: Yields user ages one by one
- `average_age()`: Calculates average age without loading all data

**Constraints**:
- Maximum 2 loops
- Cannot use SQL AVERAGE function

**Usage**:
```bash
python3 4-main.py
```

**Expected Output**:
```
Average age of users: 71.2
```

## Key Features

### Memory Efficiency
- Generators process data one item at a time
- No need to load entire datasets into memory
- Ideal for large datasets that don't fit in RAM

### Performance Optimization
- Lazy evaluation: data is processed only when needed
- Batch processing for efficient database operations
- Streaming approach for real-time data processing

### Database Integration
- Direct SQL queries for data fetching
- Connection management and error handling
- Support for both MySQL and SQLite

## Testing

Each task includes a corresponding test script (`*-main.py`) that demonstrates the functionality and provides expected output examples. Run these scripts to verify your implementation:

```bash
# Test database setup
python3 0-main.py

# Test streaming users
python3 1-main.py

# Test batch processing
python3 2-main.py

# Test lazy pagination
python3 3-main.py

# Test average age calculation
python3 4-main.py
```

## Error Handling

The implementation includes proper error handling for:
- Database connection failures
- SQL query errors
- File I/O operations
- Broken pipe errors (for command-line piping)

## Best Practices Demonstrated

1. **Resource Management**: Proper connection and cursor cleanup
2. **Memory Efficiency**: Generators for large dataset processing
3. **Error Handling**: Graceful handling of database and I/O errors
4. **Code Organization**: Clear separation of concerns
5. **Documentation**: Comprehensive docstrings and comments

## Contributing

This project is part of the ALX Backend Python curriculum. Follow the established coding standards and ensure all tests pass before submitting. 