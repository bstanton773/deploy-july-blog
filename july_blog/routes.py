from  july_blog import app, db, Message, mail
from flask import render_template, request, redirect, url_for

# Import for Forms
from july_blog.forms import UserInfoForm, BlogPostForm, LoginForm

# Import for Models
from july_blog.models import User, Post, check_password_hash

# Import for Flask Login - login_required, login_user, current_user, logout_user
from flask_login import login_required, login_user, current_user, logout_user

# Home route
@app.route('/')
def home():
    customer_name = "Brian"
    order_number = 1
    item_dict = {1:"Ice Cream", 2:"Bread", 3:"Lemons", 4:"Cereal"}
    return render_template("home.html", customer_name=customer_name, order_number=order_number, item_dict = item_dict)

# Register route
@app.route('/register', methods=['GET','POST'])
def register():
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        # Get Information from POST request
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n",username, password, email)
        # Create an instance of User
        user = User(username, email, password)
        # Open and insert into database
        db.session.add(user)
        # Save info to database
        db.session.commit()

        # Flask Email Sender
        msg = Message(f'Thanks for signing up, {username}!', recipients=[email])
        msg.body = ('Congrats on signing up! Looking forward to your posts!')
        msg.html = ('<h1>Welcome to the July Blog!</h1>' '<p>This will be fun! </p>')

        mail.send(msg)
    return render_template("register.html", form=form)

# Create Post route
@app.route('/createposts', methods=['GET', 'POST'])
@login_required
def createposts():
    form = BlogPostForm()
    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        print("\n", title, content)
    return render_template('createposts.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == email).first()
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))