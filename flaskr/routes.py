from flask import render_template, jsonify
from flask_restx import Resource, Api, fields
import time
from datetime import datetime
from flaskr import app



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Test', methods=["GET"])
def Test():
    """
    Return a simple odata container with date time information
    :return:
    """
    odata = {
        'd': {
            'results': []
        }
    }
    i = 0
    names = 'abcdefghijklmnopqrxtu'
    while i < 20:
        odata['d']['results'].append({
            "id": i,
            "name": names[i]
        })
        i += 1

    return jsonify(odata)
