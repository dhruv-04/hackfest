from flask import Flask, render_template, request
import mysql.connector as mysql
import bcrypt

app = Flask(__name__)

databaseHost = 'localhost'
databaseuser = 'root'
databasePassword = 'Dhruv471__01'

def get_db_connection():
    mycon = mysql.connect(
        host = databaseHost,
        user = databaseuser,
        password = databasePassword,
        database = 'sairag'
    )
    return mycon


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    phone = request.form['phone']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm-password']

    if password == confirm_password:
        hashed_password = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())

    # Print the data to the console (or store it in a database)
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Phone: {phone}")
    print(f"Email: {email}")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Confirm Password: {confirm_password}")

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO user_details (first_name, last_name, phone, email, username, password) VALUES (%s, %s, %s, %s, %s, %s)',
        (first_name, last_name, phone, email, username, hashed_password)
    )

    connection.commit()
    cursor.close()
    connection.close()   

    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)