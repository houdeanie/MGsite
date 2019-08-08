from flask import render_template, request, redirect, url_for, abort
from server import app
from datetime import datetime
from src.print import print_hello

'''
Dedicated page for "page not found"
'''
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404

'''
HOME
'''
@app.route('/home', methods=["GET", "POST"])
def home():
    print_hello()
    return render_template('home.html', input="Hello world")