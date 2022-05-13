from flask import render_template, request
from signup.models import User
from signup import app, db

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        user = request.form['name']
        print(user)
        #Add validation here. don't think this work but for the sake of proof if concept...
        if user is None:
            return render_template('index.html', message="Must fill field")
        if db.session.query(User).filter(User.username == user).count() ==0:
            data = User(username=user)
            db.session.add(data)
            db.session.commit()
            return render_template('success.html')
        return render_template('index.html', message="Account already exists!")
    
