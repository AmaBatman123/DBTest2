import sqlite3

with sqlite3.connect('person.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employee (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    DepartmentID INTEGER,
    DepartmentName TEXT
    )''')

