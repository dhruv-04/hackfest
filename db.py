import mysql.connector as Mysql

# Establishing the connection
mycon = Mysql.connect(
    host='localhost',
    user='root',
    password='Dhruv471__01'
)

if mycon.is_connected():
    print("Connection to Database successful!")
else:
    print("Connection to database unsuccessful!")

cursor = mycon.cursor()

# Dropping the database if it exists and creating a new one
cursor.execute('DROP DATABASE IF EXISTS sairag;')
cursor.execute('CREATE DATABASE sairag;')

# Selecting the newly created database
cursor.execute('USE sairag;')

# Creating the user_details table
cursor.execute('''
    CREATE TABLE user_details (
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        phone VARCHAR(10) NOT NULL,
        email VARCHAR(255) NOT NULL,
        username VARCHAR(255) PRIMARY KEY,
        password VARCHAR(255) NOT NULL
    );
''')

print("Table user_details created successfully!")

cursor.execute('''
    CREATE TABLE travel_plans (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        content TEXT NOT NULL           
    );
''')

print("Table travel_plans created successfully!")

# Closing the cursor and connection
cursor.close()
mycon.close()