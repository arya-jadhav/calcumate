from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    title = "Calcumate"
    return render_template("index.html")

@app.route('/why')
def about():
    words = ['cause', 'we', 'can']
    return render_template("about.html", words=words)

@app.route('/cute-image')
def cute():
    title = "So cute"
    return render_template("cute.html", title=title)

@app.route('/talk-to-us')
def talk():
    title = "Say hi"
    return render_template("talk.html", title=title)

@app.route('/form', methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    message = request.form.get("message")
    #
    # notification = "We got your message :D"
    # server = smtplib.SMTP("smtp.gmail.com", 587)
    # server.starttls()
    # server.login("aryaj241@gmail.com", "PASSWORD") #SENSITIVE
    # server.sendmail("aryaj241@gmail.com", email, notification)

    if not (first_name and last_name and message and email):
        error_msg = "Please fill in all fields."
        return render_template("fail.html", error_msg=error_msg,       #fail is not an actual webpage, it is still a part of /form
                                first_name=first_name,
                                last_name=last_name,
                                email=email,
                                message=message)

    title = "Thank you :)"
    return render_template("form.html", title=title, first_name=first_name, last_name=last_name, email=email, message=message)
