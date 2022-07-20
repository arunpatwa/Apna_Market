from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'

db=SQLAlchemy(app)#instance db



# db.session.add(item1)
# db.session.commit()
# Item.query.all()

# @app.route('/')
# def hello_world():
#     return '<h1> Hello World </h1>'


if __name__ == "__main__":
    app.run()