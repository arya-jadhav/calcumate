from flask import Flask, render_template, request, redirect
import smtplib
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# source virtual/Scripts/activate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'
# initialize the database
db = SQLAlchemy(app)

#Create db model
class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    # Create a function to return a string when something is added

    def __repr__(self):
        return '<Name %r>' % self.id

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

@app.route('/friends', methods=['post','get'])
def friends():
    title = "Acquaintances"
    if request.method == "POST":
        friend_name = request.form['name'] #name is the name of the input box
        new_friend = Friends(name=friend_name)

        # Push to db
        try:
            db.session.add(new_friend)
            db.session.commit()
            return redirect('/friends')
        except:
            return "There was an error adding your friend"
    else:
        friends = Friends.query.order_by(Friends.date_created)
        return render_template("friends.html", title=title, friends=friends)

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    friend_to_update = Friends.query.get_or_404(id)
    if request.method == "POST":
        friend_to_update.name = request.form['name']
        try:
            db.session.commit()
            return redirect('/friends')
        except:
            return "There was a problem updating that friend"
    else:
        return render_template('/update.html', friend_to_update=friend_to_update)

@app.route('/delete/<int:id>')
def delete(id):
    friend_to_delete = Friends.query.get_or_404(id)

    try:
        db.session.delete(friend_to_delete)
        db.session.commit()
        return redirect('/friends')
    except:
        return"There was a problem deleting that friend"
