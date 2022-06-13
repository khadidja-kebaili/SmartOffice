from flask import render_template, jsonify
from flaskr import app
from flask import request
from flaskr.server.DeviceAdministration import DeviceAdministration
import time


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Test', methods=["GET"])
#hier ist die get_Status Methode
#former Test()
def Status():
    """
    Return a simple odata container with date time information
    :return:
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }
    i = 0
    names = adm.get_all_status()

    for elem in names:
        odata['d']['results'].append({
            'date': elem.get_date(),
            'percentage': elem.get_percentage()
        })

    return jsonify(odata)

@app.route('/LastStatusJalousien', methods=["GET"])
#hier ist die get_Status Methode
def LastStatusJalousien():
    """
    Return a simple odata container with date time information
    :return:
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    last_status = adm.get_last_status()

    odata['d']['results'].append({
        'date': last_status.get_date(),
        'percentage': last_status.get_percentage()
    })

    return jsonify(odata)


@app.route('/Jalousien', methods=["POST"])
def set_jal():
    """
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    data = request.form["value"]
    time.sleep(4)
    adm.set_status_to_percentage_by_id(1, data)
    jal = adm.get_last_status()
    print('Jal: ', jal)
    return data

@app.route('/Status', methods=["GET"])
def Status_by_Timeperiode():
    """
    Return a simple odata container with date time information
    :return:
    """
    """
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    stats = adm.get_all_stats_by_timeperiod(start, end)
    print('Jal: ', stats)

    odata = {
        'd': {
            'results': []
        }
    }

    for elem in stats:
        odata['d']['results'].append({
            'date': elem.get_date(),
            'percentage': elem.get_percentage()
        })

    return odata

@app.route('/Jalousien', methods=["POST"])
def set_temp():
    """
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    data = request.form["value"]
    time.sleep(4)
    adm.set_temperature(data)
    temp = adm.get_temperature()
    print('temp: ', temp)
    return data

@app.route('/LastStatusJalousien', methods=["GET"])
#hier ist die get_Status Methode
def get_temp():
    """
    Return a simple odata container with date time information
    :return:
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    temp = adm.get_temperature()
    odata['d']['results'].append({
        'temperature': temp
    })

    return jsonify(odata)
