from flask import Flask,render_template,request
import requests
from datetime import *
import smtplib

#Date
posts= requests.get("https://api.npoint.io/8f1546bcc5573e676fc4").json()
now= datetime.now()
day= now.day
year = now.year
month = now.month
today = f"{day},{month},{year}"
author = "Tony"

#Email
MY_EMAIL = "email@email.com"
PASSWORD = "dwada"


#Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_post = posts, date= today, author= author)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"],data["email"],data["phone"],data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent= False)
    
def send_email(name,email,phone,message):
    email_message = f"Subject: New Message\n\nName: {name},\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = MY_EMAIL, password = PASSWORD)
            connection.sendmail(s
                from_addr= MY_EMAIL,
                to_addrs= MY_EMAIL,
                msg = email_message
            )



@app.route('/post')
def post():
    return render_template("post.html", post= posts,date= today, author= author)



if __name__ == "__main__":
    app.run(debug = True)
