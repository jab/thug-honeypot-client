#!/usr/bin/env python

import os
from flask import Flask, render_template, url_for, request, redirect
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required
from pymongo import MongoClient
from thug_api import ThugClient

app = Flask(__name__)
thug = ThugClient()()
client = MongoClient("mongodb://localhost:27017/thug")
db = client.thug

# Config
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/<result>', methods=['GET', 'POST'])
def index():
    error = None
    form = URLForm()

    return render_template('search.html', form=form, page_title='Thug client', error=error, result=result)

@app.route('/search', methods=['GET', 'POST'])
def search():

    search = {'url': request.form['search']
    # add more search fields here
    }

    # add thug code here to run_remote on the url search
    # thug.run_remote(url)

    _result = db.urls.find(search)
    result = [result for result in _result]

    return redirect(url_for('index', result=result))



class URLForm(Form):
    search = TextField('Enter a URL to scan')
    spoof_referrer = TextField('spoof referrer')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
