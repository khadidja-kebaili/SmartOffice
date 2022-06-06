from flask import request
from flaskr import app
from flask import render_template, jsonify, Flask, request
from flask_restx import Resource, Api, fields, marshal
from flask_cors import CORS
import time
from datetime import datetime
from server.DeviceAdministration import DeviceAdministration
from server.bo.Jalousien import JalousienBO
import json


app = Flask(__name__, template_folder='templates')

CORS(app, resources=r'/devicemanagement/*')

api = Api(app, version='1.0', title='Device API',
          description='Eine rudimentäre Demo-API für eine einfache Gerätesteuerung.')

bo = api.model('Businessobject', {
    'id': fields.Integer(attribute='_id', description='Der Unique Identifier eines Business Object'),
})

jalousie = api.inherit('Jalousie', bo, {
    'device_id': fields.String(attribute='_device_id', description='Device_ID der Jalousie'),
    'local_key': fields.String(attribute='_local_key', description='Local_Key der Jalousie'),
    'ip_address': fields.String(attribute='_ip_address', description='IP-Addresse der Jalousie')
})

thermostat = api.inherit('Thermostat', bo, {
    'ain': fields.String(attribute='_ain', description='Geräte-ID für AVM Geräte'),
})

status = api.inherit('Jalousienstatus', bo, {
    'percentage': fields.Integer(attribute='_percentage', description='Höhe des Jalousienstands in Prozent'),
    'status': fields.String(attribute='_status', description='Status der Jalousie'),
    'jalousieid': fields.Integer(attribute='_jalousieid', description='ID der Jalousie')
})


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


@app.route('/jalousie', methods=["GET"])
def Jal():
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
    names = adm.get_all_jalousies()
    while i < len(names):
        odata['d']['results'].append({
            "id": i,
            "name": str(names[i])
        })
        i += 1

    return (odata)


@app.route('/Jal', methods=["POST"])
def post():


@app.route('/Jalousien', methods=["POST"])
def TestJalousien():
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

    data = request.form["value"]
    print(data)

    adm.set_status_to_percentage_by_id(data)
    return int(data)


if __name__ == "__main__":
    app.run(debug=True)
    data = request.form["value"]
    print(data)
    return data
