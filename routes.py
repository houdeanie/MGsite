from flask import render_template, request, redirect, url_for, abort
from server import app
from datetime import datetime
from src.print import print_hello
from src.plug import discover_device, get_device_info, get_device_power
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
@app.route('/section_A_1', methods=["GET", "POST"])
def home():
    #print_hello()
    #discover_device()
    #get_device_info()
    # if request.method == 'POST':
    
    get_device_info()
    get_device_power()
    return render_template('home.html')


'''
FAKE1
'''
@app.route('/section_A', methods=["GET", "POST"])
def  section1():
    #print_hello()
    #discover_device()
    #get_device_info()
    # if request.method == 'POST':
    #    
    return render_template('home.1.html')

'''
Fake2
'''
@app.route('/section_B', methods=["GET", "POST"])
def section2():
    #print_hello()
    #discover_device()
    #get_device_info()
    # if request.method == 'POST':
    #    
    return render_template('home.2.html')