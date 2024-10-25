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

    # cursor.execute('''INSERT INTO Departments(DepartmentID, DepartmentName)
    # VALUES (101, "HR"), (102, "IT"), (103, "Sales")
    # ''')
    #
    # cursor.execute('''INSERT INTO Employee(FirstName, LastName, DepartmentID)
    # VALUES ("Замиров", "Камиль", 101), ("Аманов", "Рустам", 101),
    #  ("Вашин", "Антон", 102), ("Пургов", "Марат", 102),
    #   ("Алиев", "Денис", 103), ("Мамытова", "Арина", 103), ("Астарков", "Марат", 103)
    #   ''')

    cursor.execute('''SELECT Employee.FirstName, Employee.LastName, Departments.DepartmentName FROM Employee JOIN Departments ON Departments.DepartmentId = Employee.DepartmentID
    ''')
    for row in cursor.fetchall():
        print(row)

