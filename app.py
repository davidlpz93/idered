from flask import Flask, redirect, url_for, render_template, session, flash
from forms import LoginForm
from functools import wraps
from werkzeug.security import generate_password_hash, \
     check_password_hash
from models import db, User

# Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret'
app.config['DEBUG'] = True

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/idered'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Decoradores
def login_required(f):
    # Decoration: check login in session
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            session.clear()
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# end decorations

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login", methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Validate email and password
        email = form.email.data
        my_user = User.query.filter_by(email=email).first()
        if my_user and check_password_hash(
                my_user.password,
                form.password.data):
            # Login de usuario
            session['user'] = my_user.id
            if my_user.rol == 1:
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('dashboard'))
        else:
            flash('Su email o su contraseña no es válida', 'danger')
    return render_template('layouts/web/login.html', form=form)

@app.route("/admin")
@login_required
def admin():
    return render_template('layouts/web/admin/create_user.html')

@app.route("/dashboard")
@login_required
def dashboard():
    return 'Dashboard'
    
    

if __name__ == "__main__":
    app.run()