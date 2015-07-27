#!/usr/bin/env python

import os
from flask import Flask, render_template, url_for, request
from flask.ext.pymongo import PyMongo
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, validators, HiddenField
from wtforms import TextAreaField, BooleanField
from wtforms.validators import Required, EqualTo, Optional
from wtforms.validators import Length, Email

app = Flask(__name__)

# Config
app.config.from_object(os.environ['APP_SETTINGS'])

# Connect to Pymongo
# mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    # urlscan = request.form['urlscan']
    return render_template('index.html', page_title='Scythe', error=error)


if __name__ == '__main__':
    app.run()
