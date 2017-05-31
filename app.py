from flask import Flask, redirect, url_for, render_template

# Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret'
app.config['DEBUG'] = True

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login")
def login():
    return render_template('layouts/web/login.html')

if __name__ == "__main__":
    app.run()