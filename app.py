from flask import Flask, render_template, redirect, request, session, url_for
from models import db, User
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz_master.db'
db.init_app(app)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # handle registration form
        pass
    return render_template('register.html')

@app.route('/admin')
def admin_dashboard():
    # admin homepage
    return render_template('admin_dashboard.html')

@app.route('/user')
def user_dashboard():
    # user homepage
    return render_template('user_dashboard.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
