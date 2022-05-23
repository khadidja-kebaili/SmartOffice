from flask import render_template, jsonify
import time
from datetime import datetime
from . import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/DashboardAnalytics', methods=["GET"])
def DashboardAnalytics():
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
            "name": names[i],
            "datetime": datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),

        })
        i += 1

    return jsonify(odata)
