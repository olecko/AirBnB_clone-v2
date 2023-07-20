#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thursday 20 July 21:35:54 2023
@author: Paul Emumena Michael
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Start a basic Flask web application"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
