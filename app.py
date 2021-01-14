from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = "Calcumate"
    return render_template("index.html")

@app.route('/why')
def about():
    words = ['cause', 'we', 'can']
    title = "Why?"
    return render_template("about.html", title = title, words=words)

@app.route('/cute-image')
def cute():
    title = "So cute"
    return render_template("cute.html", title=title)
