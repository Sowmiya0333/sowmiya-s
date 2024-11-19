from flask import Flask, render_template, request, redirect, flash, url_for
import pymysql
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# MySQL database connection setup
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='portfolio',
    port=3306  
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process form data
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Insert the data into the MySQL database
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO contacts (name, email, subject, message) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (name, email, subject, message))
            conn.commit()
            flash("Thank you for contacting Me! Have a great dayyy", "success")
        except Exception as e:
            conn.rollback()
            flash("An error occurred. Please try again.", "danger")
            print(f"Error: {e}")
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
