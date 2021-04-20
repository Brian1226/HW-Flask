from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages

# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
@app.route('/', methods = ['GET', 'POST'])
def home():
    form=MessageForm()
    if form.validate_on_submit():
        # check if user exists in database
        # if not, create user and add to database
        user = User.query.filter_by(author = form.author.data).first()

        if user is None:
            create_user = User(author = form.author.data)
            db.session.add(create_user)
            db.session.commit()
        
        # create row in Message table with user (created/found) add to the database
        




    # output all messages
    # create a list of dictionaries with the following structure
    # [{'author':'carlos', 'message':'Yo! Where you at?!'},
    #  {'author':'Jerry', 'message':'Home. You?'}]

    posts = [
    {
        'author' : 'Carlos',
        'message' : 'Yo! Where you at?!'
    },
    {
        'author' : 'Jerry',
        'message' : 'Home. You?'
    }
]
return render_template('home.html', posts=posts, form=form)
