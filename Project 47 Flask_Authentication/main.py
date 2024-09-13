from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html",logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET','POST'])
def register():
    if request.form:
        new_user = User(
            email=request.form.get("email"),
            password=generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8),
            name=request.form.get('name')
        )
        if db.session.execute(db.select(User).where(User.email == new_user.email)).scalar():
            flash('You are already a user, please login instead.')  
            return render_template("register.html")
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('secrets'))
    return render_template("register.html",logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        User_to_login = db.session.execute(db.select(User).where(User.email == request.form.get('email'))).scalar()
        if User_to_login:
            if check_password_hash(User_to_login.password, request.form.get('password')):
                login_user(User_to_login)
                return redirect(url_for('secrets'))
            else:
                flash(message='Wrong Password')
        else:
            flash(message='Write the correct mail_id and try again.')   

    return render_template("login.html",logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html",name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")

if __name__ == "__main__":
    app.run(debug=True)
