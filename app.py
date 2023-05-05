from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask (__name__)

app.secret_key = "secret key"

mail = Mail(app)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.getenv("email_username")
app.config["MAIL_PASSWORD"] = os.getenv("email_password")
mail.init_app(app)


db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="ruths_childminding"
)

cursor = db.cursor()

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":

        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        subject = request.form.get('subject')

        sql = "INSERT INTO contact_form(Name, Email_Address, Contact_Number, Subject) VALUES (%s, %s, %s, %s)"
        val = (name, email, number, subject)

        cursor.execute(sql, val)
        db.commit()

        msg = Message(sender='ruths.childminding1@gmail.com', recipients=['ruths.childminding1@gmail.com'])
        msg.body = """From: %s, <%s>, <%s>, <%s>""" % (name, email, number, subject)
        mail.send(msg)

        flash('Your message has been sent successfully.')
        return redirect(url_for("home")+"#contact")

    return render_template("index.html")

@app.route("/sign-up/", methods=["GET", "POST"])
def signUp():
    if request.method == "POST":

        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        number = request.form.get('number')
        password = request.form.get('password')

        sql = "INSERT INTO account_details(First_Name, Last_Name, Email_Address, Contact_Number, Password) VALUES (%s, %s, %s, %s, %s)"
        val = (firstname, lastname, email, number, password)

        sql1 = "INSERT INTO login_details(Email_Address, Password) VALUES (%s, %s)"
        val1 = (email, password)

        cursor.execute(sql, val)
        
        cursor.execute(sql1, val1)
        db.commit()

        flash('Account created successfully')
        return render_template("signup.html")

    return render_template("signup.html")

@app.route("/login/", methods=["GET", "POST"])
def logIn():
    if request.method == "POST":

        email = request.form.get('email')
        password = request.form.get('password')

        sql = "INSERT INTO account_details(First_Name, Last_Name, Email_Address, Contact_Number, Password) VALUES (%s, %s, %s, %s, %s)"
        val = ( email, password)

        cursor.execute(sql, val)
        db.commit()

    return render_template("login.html")


@app.route("/useful-links/")
def usefulLinks():

    return render_template("useful_links.html")


@app.route("/Q&A/")
def qanda():

    return render_template("qanda.html")


@app.route("/EYFS/")
def eyfs():

    return render_template("eyfs.html")


app.run(debug=True)


