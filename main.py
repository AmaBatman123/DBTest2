import sqlite3

with sqlite3.connect('person.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employee (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    DepartmentID INTEGER,
    FOREIGN KEY(DepartmentID) REFERENCES Department(ID)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Departments(
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName TEXT
    )''')

    cursor.execute('''INSERT INTO Departments(DepartmentID, DepartmentName) 
    VALUES (101, "HR"), (102, "IT"), (103, "Sales")
    ''')

    cursor.execute('''INSERT INTO Employee(FirstName, LastName, DepartmentID)
    VALUES ("Замиров", "Камиль", 1), ("Аманов", "Рустам", 1),
     ("Вашин", "Антон", 2), ("Пургов", "Марат", 2),
      ("Алиев", "Денис", 3), ("Мамытова", "Арина", 3), ("Астарков", "Марат", 3)
      ''')

