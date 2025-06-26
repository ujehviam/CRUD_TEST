import sqlite3

conn = sqlite3.connect("Project1.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS CRUD_TEST (
    ID INT PRIMARY KEY NOT NULL, 
    FIRSTNAME TEXT NOT NULL, 
    MIDDLENAME TEXT NOT NULL, 
    LASTNAME TEXT NOT NULL, 
    DOB TEXT NOT NULL, 
    CURRENT_CITY TEXT NOT NULL
    )
    ''')
conn.commit()

print("you have successfully created a new table")