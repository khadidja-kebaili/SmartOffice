from flask import render_template, jsonify
from flaskr import app
from flask import request
from flaskr.server.DeviceAdministration import DeviceAdministration
import time
from flaskr.server.bo.RulesBO import RulesBO



@app.route('/')
def index():
    '''
    main-HTML Seite, die gerendert werden soll
    :return: index.html
    '''
    return render_template("index.html")


@app.route('/Test', methods=["GET"])
# hier ist die get_Status Methode
# former Test()
def Status():
    """
    Generieriung einer JSON-Datei anhand Liste aller Jalousienstatus
    :return: JSON-Datei mit Datum und Jalousienstand (0-100)
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    names = adm.get_all_jal_status()

    for elem in names:
        odata['d']['results'].append({
            'date': elem.get_date(),
            'percentage': elem.get_percentage()
        })

    return jsonify(odata)


@app.route('/LastStatusJalousien', methods=["GET"])
# hier ist die get_Status Methode
def LastStatusJalousien():
    """
    Generieriung einer JSON-Datei anhand des letzten Jalousienstatus
    :return: JSON-Datei mit letztem Jalousienstatus
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    last_status = adm.get_last_jal_status()

    odata['d']['results'].append(last_status.get_percentage())

    return jsonify(odata)


@app.route('/Jalousien', methods=["POST"])
def set_jal():
    """
    Lädt Werte aus dem Frontend und steuert mit dem Wert eine Jalousie
    :return: Dict()
    """

    adm = DeviceAdministration()

    data = request.form["value"]
    data = int(data)
    time.sleep(1)
    k = adm.set_status_to_percentage_by_id(1, data)
    if type(k) == dict:
        return k
    else:
        return {"type": 1}



@app.route('/JalousienStatusPerHour', methods=["GET"])
def get_jal_stats_per_hour_for_weekday():
    """
    Generieriung einer JSON-Datei anhand Liste mit Werten für das Reporting
    :return: JSON-Datei mit 4 Werten.
    """

    adm = DeviceAdministration()
    weekday = request.form["weekday"]
    von = request.form["von"]
    bis = request.form["bis"]
    data = adm.get_ist_value_jal_for_timespan(von, bis, weekday)

    odata = {
        'd': {
            'results': []
        }
    }
    for elem in data:
        odata['d']['results'].append({
            'median_value': elem,
        })

    return jsonify(odata)

@app.route('/JalIstStatusPerDay', methods=["GET"])
def status_per_day():
    adm = DeviceAdministration()
    day = request.args.get('day')
    print(day)
    stats = adm.get_ist_values_jal(day)
    print('Jal: ', stats)

    odata = {
        'd': {
            'results': []
        }
    }

    count = 0

    for elem in stats:
        odata['d']['results'].append({
            'tageszeitjalist': count,
            'valuejalist': elem
        })
        count = count + 1

    return odata

@app.route('/TempIstStatusPerDay', methods=["GET"])
def temp_ist_status_per_day():
    """
    Return a simple odata container with date time information
    """

    adm = DeviceAdministration()

    day = request.args.get('day')
    print(day)
    stats = adm.get_median_ist_values_temp(day)
    print('Temp: ', stats)

    odata = {
        'd': {
            'results': []
        }
    }

    count = 0

    for elem in stats:
        odata['d']['results'].append({
            'tageszeittempist': count,
            'valuetempist': elem
        })
        count = count + 1

    return odata

@app.route('/JalSollStatusPerDay', methods=["GET"])
def jal_soll_status_per_day():
    """
    Return a simple odata container with date time information
    """


    adm = DeviceAdministration()

    day = request.args.get('day')
    print(day)
    stats = adm.get_median_soll_values_jal(day)
    print('Jal: ', stats)

    odata = {
        'd': {
            'results': []
        }
    }

    count = 0

    for elem in stats:
        odata['d']['results'].append({
            'tageszeitjalsoll': count,
            'valuejalsoll': elem
        })
        count = count + 1

    return odata

@app.route('/TempSollStatusPerDay', methods=["GET"])
def temp_soll_status_per_day():
    """
    Return a simple odata container with date time information
    """

    adm = DeviceAdministration()

    day = request.args.get('day')
    stats = adm.get_median_soll_values_temp(day)

    odata = {
        'd': {
            'results': []
        }
    }

    count = 0

    for elem in stats:
        odata['d']['results'].append({
            'tageszeittempsoll': count,
            'valuetempsoll': elem
        })
        count = count + 1

    return odata

@app.route('/JalCombinedPerDay', methods=["GET"])
def jalstatuscombined_per_day():
    """
    Return a simple odata container with date time information
    """
    adm = DeviceAdministration()

    day = request.args.get('day')
    statsist = adm.get_ist_values_jal(day)
    statssoll = adm.get_median_soll_values_jal(day)
    
    odata = {
        'd': {
            'results': []
        }
    }
    count = 0
    for elem1, elem2 in zip(statsist, statssoll):
        odata['d']['results'].append({
            'tageszeitjal': count,
            'valuejalist': elem1,
            'valuejalsoll': elem2
        })
        count = count + 1

    return odata

@app.route('/TempCombinedPerDay', methods=["GET"])
def tempstatuscombined_per_day():
    """
    Return a simple odata container with date time information
    """
    adm = DeviceAdministration()

    day = request.args.get('day')
    statsist = adm.get_median_ist_values_temp(day)
    statssoll = adm.get_median_soll_values_temp(day)
    
    odata = {
        'd': {
            'results': []
        }
    }
    count = 0
    for elem1, elem2 in zip(statsist, statssoll):
        odata['d']['results'].append({
            'tageszeittemp': count,
            'valuetempist': elem1,
            'valuetempsoll': elem2
        })
        count = count + 1

    return odata
    
@app.route('/StatusPerWeek', methods=["GET"])
def status_for_week():
    """
    Return a simple odata container with date time information
    """

    adm = DeviceAdministration()

    week = request.form["week"]
    stats = adm.get_jal_median_per_week(week)
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



@app.route('/SetTemp', methods=["POST"])
def set_temp():
    """
    Setzten der Temperatur mithilfe von Werten aus dem Frontend.
    :return: dict()
    """

    adm = DeviceAdministration()

    data = request.form["value"]
    data = float(data)
    data = data * 10
    time.sleep(4)
    k = adm.set_temperature(data)
    temp = adm.get_temp_from_device()
    print('temp: ', temp)
    if type(k) == dict:
        return k
    else:
        return {'type': '2'}


@app.route('/GetTemp', methods=["GET"])
def get_temp():
    """
    Generierung einer JSON-Datei mit der jetztigen Temperatur.
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    temp = adm.get_temp_from_device()
    temp = int(temp)
    temp = temp / 10
    odata['d']['results'].append({
        'temperature': temp
    })

    return jsonify(odata)

@app.route('/GetSollTemp', methods=["GET"])
def get_soll_temp():
    """
    Generierung einer JSON-Datei mit der Soll-Temperatur.
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    temp = adm.get_soll_temp()
    temp = int(temp)
    temp = temp / 10
    odata['d']['results'].append({
        'temperature': temp
    })

    return jsonify(odata)


@app.route('/GetStandardJalousienMonday', methods=["GET"])
def get_entries_jal_monday():
    """
    Generierung einer JSON-Datei mit einem Jalousien-Wochenplaneintrag am Montag
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': [
                
            ]
        }
    }

    entries = adm.get_all_jal_standard_entries_monday()
    entries.sort(key=lambda x: x._start_time, reverse=False)
    for elem in entries:
        odata['d']['results'].append({
            'id': elem.get_id(),
            'startzeit': elem.get_start_time(),
            'endzeit': elem.get_end_time(),
            'wert': elem.get_value()
        })

    return jsonify(odata)


@app.route('/GetStandardJalousienTuesday', methods=["GET"])
def get_entries_jal_tuesday():
    """
    Generierung einer JSON-Datei mit einem Jalousien-Wochenplaneintrag am Dienstag.
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_jal_standard_entries_tuesday()
    entries.sort(key=lambda x: x._start_time, reverse=False)
    for elem in entries:
        odata['d']['results'].append({
            'id': elem.get_id(),
            'startzeit': elem.get_start_time(),
            'endzeit': elem.get_end_time(),
            'wert': elem.get_value()
        })

    return jsonify(odata)


@app.route('/GetStandardJalousienWednesday', methods=["GET"])
def get_entries_jal_wednesday():
    """
    Generierung einer JSON-Datei mit einem Jalousien-Wochenplaneintrag am Mittwoch.
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_jal_standard_entries_wednesday()
    entries.sort(key=lambda x: x._start_time, reverse=False)
    for elem in entries:
        odata['d']['results'].append({
            'id': elem.get_id(),
            'startzeit': elem.get_start_time(),
            'endzeit': elem.get_end_time(),
            'wert': elem.get_value()
        })

    return jsonify(odata)


@app.route('/GetStandardJalousienThursday', methods=["GET"])
def get_entries_jal_thursday():
    """
    Generierung einer JSON-Datei mit einem Jalousien-Wochenplaneintrag am Donnerstag.
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_jal_standard_entries_thursday()
    entries.sort(key=lambda x: x._start_time, reverse=False)
    for elem in entries:
        odata['d']['results'].append({
            'id': elem.get_id(),
            'startzeit': elem.get_start_time(),
            'endzeit': elem.get_end_time(),
            'wert': elem.get_value()
        })

    return jsonify(odata)


@app.route('/GetStandardJalousienFriday', methods=["GET"])
def get_entries_jal_friday():
    """
    Generierung einer JSON-Datei mit einem Jalousien-Wochenplaneintrag am Freitag.
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_jal_standard_entries_friday()
    entries.sort(key=lambda x: x._start_time, reverse=False)
    for elem in entries:
        odata['d']['results'].append({
            'id': elem.get_id(),
            'startzeit': elem.get_start_time(),
            'endzeit': elem.get_end_time(),
            'wert': elem.get_value()
        })

    return jsonify(odata)


@app.route('/SetJalousienStandardMonday', methods=["POST"])
def set_jal_standard_monday():
    """
    Setzen eines Jalousien-Wochenplaneintrag am Montag
    """
    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(1)

    k = adm.set_jal_standard_entry_monday(start, end, value)
    if type(k) == dict:
        return k
    else:
        return {'type': '2'}


@app.route('/SetJalousienStandardTuesday', methods=["POST"])
def set_jal_standard_tuesday():
    """
    Setzen eines Jalousien-Wochenplaneintrag am Dienstag.
    """
    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(1)
    k = adm.set_jal_standard_entry_tuesday(start, end, value)
    if type(k) == dict:
        return k
    else:
        return {'type': '2'}


@app.route('/SetJalousienStandardWednesday', methods=["POST"])
def set_jal_standard_wednesday():
    """
    Setzen eines Jalousien-Wochenplaneintrag am Mittwoch
    """
    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(1)
    k = adm.set_jal_standard_entry_wednesday(start, end, value)
    if type(k) == dict:
        return k
    else:
        return {'type': '2'}


@app.route('/SetJalousienStandardThursday', methods=["POST"])
def set_jal_standard_thursday():
    """
    Setzen eines Jalousien-Wochenplaneintrag am Donnerstag
    """
    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(1)
    k = adm.set_jal_standard_entry_thursday(start, end, value)
    if type(k) == dict:
        return k
    else:
        return {'type': '2'}


@app.route('/SetJalousienStandardFriday', methods=["POST"])
def set_jal_standard_friday():
    """
    Setzen eines Jalousien-Wochenplaneintrag am Freitag.
    """
    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(1)
    k = adm.set_jal_standard_entry_friday(start, end, value)
    if type(k) == dict:
        return k
    else:
        return {'type': '2'}

@app.route('/DeleteStandardJalousienMonday', methods=["DELETE"])
def delete_entry_jal_monday():
    """
    Löschen eines Jalousien-Wochenplaneintrag am Montag
    """
    adm = DeviceAdministration()
    id_entry = request.form["id_entry"]
    id_entry = int(id_entry)
    liste = adm.get_all_standard_weekly_jal_entries_by_weekday(1)
    for elem in liste:
        if elem.get_monday_id() == id_entry:
            adm.delete_entry_in_standard_weeklyplan_jal(elem)
    monday = adm.get_all_jal_standard_entries_monday()
    for elem in monday:
        if elem.get_id() == id_entry:
            adm.delete_standard_entry_monday(elem)

    return ' '

@app.route('/DeleteStandardJalousienTuesday', methods=["DELETE"])
def delete_entry_jal_tuesday():
    """
    Löschen eines Jalousien-Wochenplaneintrag am Dienstag
    """
    adm = DeviceAdministration()
    id_entry = request.form["id_entry"]
    id_entry = int(id_entry)
    liste = adm.get_all_standard_weekly_jal_entries_by_weekday(2)
    for elem in liste:
        if elem.get_tuesday_id() == id_entry:
            adm.delete_entry_in_standard_weeklyplan_jal(elem)
    tuesday = adm.get_all_jal_standard_entries_tuesday()
    for elem in tuesday:
        if elem.get_id() == id_entry:
            adm.delete_standard_entry_tuesday(elem)

    return ' '

@app.route('/DeleteStandardJalousienWednesday', methods=["DELETE"])
def delete_entry_jal_wednesday():
    """
    Löschen eines Jalousien-Wochenplaneintrag am Mttwoch
    """
    adm = DeviceAdministration()
    id_entry = request.form["id_entry"]
    id_entry = int(id_entry)
    liste = adm.get_all_standard_weekly_jal_entries_by_weekday(3)
    for elem in liste:
        if elem.get_wednesday_id() == id_entry:
            adm.delete_entry_in_standard_weeklyplan_jal(elem)
    wednesday = adm.get_all_jal_standard_entries_wednesday()
    for elem in wednesday:
        if elem.get_id() == id_entry:
            adm.delete_standard_entry_wednesday(elem)

    return ' '

@app.route('/DeleteStandardJalousienThursday', methods=["DELETE"])
def delete_entry_jal_thursday():
    """
    Löschen eines Jalousien-Wochenplaneintrag am Donnerstag
    """
    adm = DeviceAdministration()
    id_entry = request.form["id_entry"]
    id_entry = int(id_entry)
    liste = adm.get_all_standard_weekly_jal_entries_by_weekday(4)
    for elem in liste:
        if elem.get_thursday_id() == id_entry:
            adm.delete_entry_in_standard_weeklyplan_jal(elem)
    thursday = adm.get_all_jal_standard_entries_thursday()
    for elem in thursday:
        if elem.get_id() == id_entry:
            adm.delete_standard_entry_thursday(elem)

    return ' '

@app.route('/DeleteStandardJalousienFriday', methods=["DELETE"])
def delete_entry_jal_friday():
    """
    Löschen eines Jalousien-Wochenplaneintrag am Freitag
    """
    adm = DeviceAdministration()
    id_entry = request.form["id_entry"]
    id_entry = int(id_entry)
    liste = adm.get_all_standard_weekly_jal_entries_by_weekday(5)
    for elem in liste:
        if elem.get_friday_id() == id_entry:
            adm.delete_entry_in_standard_weeklyplan_jal(elem)
    friday = adm.get_all_jal_standard_entries_friday()
    for elem in friday:
        if elem.get_id() == id_entry:
            adm.delete_standard_entry_friday(elem)

    return ' '

@app.route('/SetJalRule', methods=["POST"])
def set_jal_rule():
    """
    Setzen einer Jalousien-Regel
    """
    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    min = request.form["min"]
    max = request.form["max"]
    time.sleep(1)
    k = adm.set_jal_rule(min, max, start, end)
    if type(k) == dict:
        return k
    else:
        return {'type': '1'}

@app.route('/GetJalRule', methods=["GET"])
def get_jal_rules():
    """
    Laden einer Jalousien-Regel und Generierung zu einer JSON-Datei
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }
    rules = adm.get_all_jal_rules()
    rules.sort(key=lambda x: x._start, reverse=False)
    for elem in rules:
        odata['d']['results'].append({
            'id': elem.get_id(),
            'startzeit': elem.get_start_time(),
            'endzeit': elem.get_end_time(),
            'min': elem.get_min(),
            'max': elem.get_max(),
            'removeNew': "true"
        })

    return jsonify(odata)

@app.route('/DeleteJalRule', methods=["DELETE"])
def delete_jal_rules():
    """
    Löschen einer Jalousien-Regel.
    """
    adm = DeviceAdministration()
    id_entry = request.form["id_entry"]
    id_entry = int(id_entry)
    adm.delete_jal_rules_byId(id_entry)
    return ' '


@app.route('/SetMinTemp', methods=["POST"])
def set_min_temp():
    '''
    Setzen einer Mindesttemperatur
    '''
    adm = DeviceAdministration()
    data = request.form["value"]
    data = float(data)
    data = data * 10
    temp = adm.set_temp_rule_min(data)
    print('temp: ', temp)
    return ' '


@app.route('/GetMinTemp', methods=["GET"])
# hier ist die get_Status Methode
def get_min_temp():
    """
    Laden einer Mindesttemperatur und Generierung zu einer JSON-Datei
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    temp = adm.get_min_temp()
    temp = int(temp)
    temp = temp / 10
    odata['d']['results'].append({
        'min_temperature': temp
    })

    return jsonify(odata)


@app.route('/SetMaxTemp', methods=["POST"])
def set_max_temp():
    '''
    Setzen einer Maximaltemperatur
    '''
    adm = DeviceAdministration()
    data = request.form["value"]
    data = float(data)
    data = data * 10
    temp = adm.set_temp_rule_max(data)
    print('temp: ', temp)
    return ' '

@app.route('/GetMaxTemp', methods=["GET"])
# hier ist die get_Status Methode
def get_max_temp():
    """
    Laden einer Maximaltemperatur und Generierung zu einer JSON-Datei
    """
    adm = DeviceAdministration()
    odata = {
        'd': {
            'results': []
        }
    }

    temp = adm.get_max_temp()
    temp = int(temp)
    temp = temp / 10
    odata['d']['results'].append({
        'max_temperature': temp
    })

    return jsonify(odata)


@app.route('/GetStandardThermostatMonday', methods=["GET"])
def get_entries_temp_monday():
    """
    Generierung einer JSON-Datei mit einem Thermostat-Wochenplaneintrag am Montag
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_temp_standard_entries_monday()
    entries.sort(key=lambda x: x._start_time, reverse=False)
    for elem in entries:
        odata['d']['results'].append({
            'id': elem.get_id(),
            'startzeit': elem.get_start_time(),
            'endzeit': elem.get_end_time(),
            'wert': elem.get_value()
        })

    return jsonify(odata)


@app.route('/GetStandardThermostatTuesday', methods=["GET"])
def get_entries_temp_tuesday():
    """
    Generierung einer JSON-Datei mit einem Thermostat-Wochenplaneintrag am Dienstag
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_temp_standard_entries_tuesday()
    entries.sort(key=lambda x: x._start_time, reverse=False)
    for elem in entries:
        odata['d']['results'].append({
            'id': elem.get_id(),
            'startzeit': elem.get_start_time(),
            'endzeit': elem.get_end_time(),
            'wert': elem.get_value()
        })

    return jsonify(odata)


@app.route('/GetStandardThermostatWednesday', methods=["GET"])
def get_entries_temp_wednesday():
    """
    Generierung einer JSON-Datei mit einem Thermostat-Wochenplaneintrag am Mittwoch
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_temp_standard_entries_wednesday()
    entries.sort(key=lambda x: x._start_time, reverse=False)
    for elem in entries:
        odata['d']['results'].append({
            'id': elem.get_id(),
            'startzeit': elem.get_start_time(),
            'endzeit': elem.get_end_time(),
            'wert': elem.get_value()
        })

    return jsonify(odata)


@app.route('/GetStandardThermostatThursday', methods=["GET"])
def get_entries_temp_thursday():
    """
    Generierung einer JSON-Datei mit einem Thermostat-Wochenplaneintrag am Donnerstag
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_temp_standard_entries_thursday()
    entries.sort(key=lambda x: x._start_time, reverse=False)
    for elem in entries:
        odata['d']['results'].append({
            'id': elem.get_id(),
            'startzeit': elem.get_start_time(),
            'endzeit': elem.get_end_time(),
            'wert': elem.get_value()
        })

    return jsonify(odata)


@app.route('/GetStandardThermostatFriday', methods=["GET"])
def get_entries_temp_friday():
    """
    Generierung einer JSON-Datei mit einem Thermostat-Wochenplaneintrag am Freitag
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_temp_standard_entries_friday()
    entries.sort(key=lambda x: x._start_time, reverse=False)
    for elem in entries:
        odata['d']['results'].append({
            'id': elem.get_id(),
            'startzeit': elem.get_start_time(),
            'endzeit': elem.get_end_time(),
            'wert': elem.get_value()
        })

    return jsonify(odata)


@app.route('/SetThermostatStandardMonday', methods=["POST"])
def set_temp_standard_monday():
    """
    Setzen eines Thermostat-Wochenplaneintrag am Montag.
    """
    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(1)
    k = adm.set_temp_standard_entry_monday(start, end, value)
    if type(k) == dict:
        return k
    else:
        return {'type': '2'}
    


@app.route('/SetThermostatStandardTuesday', methods=["POST"])
def set_temp_standard_tuesday():
    """
    Setzen eines Thermostat-Wochenplaneintrag am Dienstag.
    """
    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(1)
    k = adm.set_temp_standard_entry_tuesday(start, end, value)
    if type(k) == dict:
        return k
    else:
        return {'type': '2'}

@app.route('/SetThermostatStandardWednesday', methods=["POST"])
def set_temp_standard_wednesday():
    """
    Setzen eines Thermostat-Wochenplaneintrag am Mittwoch.
    """

    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(1)
    k = adm.set_temp_standard_entry_wednesday(start, end, value)
    if type(k) == dict:
        return k
    else:
        return {'type': '2'}


@app.route('/SetThermostatStandardThursday', methods=["POST"])
def set_temp_standard_thursday():
    """
    Setzen eines Thermostat-Wochenplaneintrag am Donnerstag.
    """
    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(1)
    k = adm.set_temp_standard_entry_thursday(start, end, value)
    if type(k) == dict:
        return k
    else:
        return {'type': '2'}


@app.route('/SetThermostatStandardFriday', methods=["POST"])
def set_temp_standard_friday():
    """
    Setzen eines Thermostat-Wochenplaneintrag am Freitag.
    """
    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(1)
    k = adm.set_temp_standard_entry_friday(start, end, value)
    if type(k) == dict:
        return k
    else:
        return {'type': '2'}


@app.route('/DeleteStandardThermoMonday', methods=["DELETE"])
def delete_entry_thermo_monday():
    """
    Löschen eines Thermostat-Wochenplaneintrag am Montag.
    """
    adm = DeviceAdministration()
    id_entry = request.form["id_entry"]
    id_entry = int(id_entry)
    liste = adm.get_all_standard_weekly_temp_entries_by_weekday(1)
    for elem in liste:
        if elem.get_monday_id() == id_entry:
            adm.delete_entry_in_standard_weeklyplan_temp(elem)
    monday = adm.get_all_temp_standard_entries_monday()
    for elem in monday:
        if elem.get_id() == id_entry:
            adm.delete_standard_entry_monday(elem)

    return ' '

@app.route('/DeleteStandardThermoTuesday', methods=["DELETE"])
def delete_entry_thermo_tuesday():
    """
    Löschen eines Thermostat-Wochenplaneintrag am Dienstag
    """
    adm = DeviceAdministration()
    id_entry = request.form["id_entry"]
    id_entry = int(id_entry)
    liste = adm.get_all_standard_weekly_temp_entries_by_weekday(2)
    for elem in liste:
        if elem.get_tuesday_id() == id_entry:
            adm.delete_entry_in_standard_weeklyplan_temp(elem)
    tuesday = adm.get_all_temp_standard_entries_tuesday()
    for elem in tuesday:
        if elem.get_id() == id_entry:
            adm.delete_standard_entry_tuesday(elem)

    return ' '

@app.route('/DeleteStandardThermoWednesday', methods=["DELETE"])
def delete_entry_thermo_wednesday():
    """
    Löschen eines Thermostat-Wochenplaneintrag am Mittwoch.
    """
    adm = DeviceAdministration()
    id_entry = request.form["id_entry"]
    id_entry = int(id_entry)
    liste = adm.get_all_standard_weekly_temp_entries_by_weekday(3)
    for elem in liste:
        if elem.get_wednesday_id() == id_entry:
            adm.delete_entry_in_standard_weeklyplan_temp(elem)
    wednesday = adm.get_all_temp_standard_entries_wednesday()
    for elem in wednesday:
        if elem.get_id() == id_entry:
            adm.delete_standard_entry_wednesday(elem)

    return ' '

@app.route('/DeleteStandardThermoThursday', methods=["DELETE"])
def delete_entry_thermo_thursday():
    """
    Löschen eines Thermostat-Wochenplaneintrag am Donnerstag.
    """
    adm = DeviceAdministration()
    id_entry = request.form["id_entry"]
    id_entry = int(id_entry)
    liste = adm.get_all_standard_weekly_temp_entries_by_weekday(4)
    for elem in liste:
        if elem.get_thursday_id() == id_entry:
            adm.delete_entry_in_standard_weeklyplan_temp(elem)
    thursday = adm.get_all_temp_standard_entries_thursday()
    for elem in thursday:
        if elem.get_id() == id_entry:
            adm.delete_standard_entry_thursday(elem)

    return ' '

@app.route('/DeleteStandardThermoFriday', methods=["DELETE"])
def delete_entry_thermo_friday():
    """
    Löschen eines Thermostat-Wochenplaneintrag am Freitag.
    """
    adm = DeviceAdministration()
    id_entry = request.form["id_entry"]
    id_entry = int(id_entry)
    liste = adm.get_all_standard_weekly_temp_entries_by_weekday(5)
    for elem in liste:
        if elem.get_friday_id() == id_entry:
            adm.delete_entry_in_standard_weeklyplan_temp(elem)
    friday = adm.get_all_temp_standard_entries_friday()
    for elem in friday:
        if elem.get_id() == id_entry:
            adm.delete_standard_entry_friday(elem)

    return ' '
