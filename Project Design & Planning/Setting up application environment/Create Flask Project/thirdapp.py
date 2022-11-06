# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 09:28:31 2022

@author: Kutty❤Mani😍
"""

from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/admin')
def hello_admin():
    return "hello admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "hello %s guest" %guest

@app.route('/user/<name>')
def hello_user(name):
    if (name=='admin'):
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest",guest=name))
app.run(debug=True)    