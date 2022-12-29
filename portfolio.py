from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "webuniversal"

mysql = MySQL(app)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/courses")
def courses():
    return render_template('courses.html')

@app.route("/news")
def news():
    return render_template('news.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        details = request.form
        name = details['name']
        email = details['email']
        subject = details['subject']
        message = details['message']

        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO contact (name, email, subject, message) VALUES (%s, %s, %s, %s);''', (name, email, subject, message, ))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        details = request.form
        name = request.form['name']
        mother_name = details['mother_name']
        father_name = details['father_name']
        contact = details['contact']
        email = details['email']
        education = details['education']
        date_of_birth = details['date_of_birth']
        gender = details['gender']
        address = details['address']
        cur = mysql.connection.cursor()

        cur.execute('''INSERT INTO signup (name, mother_name, father_name, contact, email, education, date_of_birth, gender, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);''', (name, mother_name, father_name, contact, email, education, date_of_birth, gender, address))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('login'))
    return render_template('forms/signup.html')

@app.route('/login')
def login():
    return render_template('forms/login.html')

if __name__ == '__main__':
    app.run(debug=True)

