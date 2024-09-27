from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mysql
import bcrypt

app = Flask(__name__)

databaseHost = 'your_database_host'
databaseUser = 'your_database_user'
databasePassword = 'Dhruv471__01'

def get_db_connection():
    mycon = mysql.connect(
        host=databaseHost,
        user=databaseUser,
        password=databasePassword,
        database='sairag'
    )
    return mycon

@app.route('/')
def travel():
    return render_template('travel.html')

@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html')

@app.route('/registration.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        if not password:
            return "Password is required", 400

        hashed_password = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())

        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO user_details (first_name, last_name, phone, email, username, password) VALUES (%s, %s, %s, %s, %s, %s)',
                (first_name, last_name, phone, email, username, hashed_password)
            )
            connection.commit()
            return "Form Submitted Successfully!"
        except mysql.Error as err:
            print(f"Error: {err}")
            return redirect(url_for('register'))
        finally:
            cursor.close()
            connection.close()

    return "Registration successful!"

if __name__ == '__main__':
    app.run(debug=True)