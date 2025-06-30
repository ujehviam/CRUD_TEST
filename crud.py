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

UserData = {
    1:["Emmanuel", "Ujeh", "Mayaki", "17/10/1994", "Lagos"], 
    2:["Glory", "Oiza", "Mayaki", "03/09/1997", "Lagos"],
    3:["Osarumwense", "Peace", "Osayuwa", "10/02/1997", "Banin"]
}

UserData_list = [] #creat an empty list to store the unpacked dictionary key and values.

for i,j in UserData.items(): #iterate over the dictionary 
    unpack_UserData = (i, *j) #unpack the dictionry into a tuple with the asterick sign
    print(unpack_UserData) 
    UserData_list.append(unpack_UserData) #put the tupple inside the empty list

    cursor.executemany("INSERT OR REPLACE INTO CRUD_TEST(ID, FIRSTNAME, MIDDLENAME, LASTNAME, DOB, CURRENT_CITY) VALUES(?,?,?,?,?,?)", UserData_list)
    conn.commit()


print("you have successfully created a new table")
