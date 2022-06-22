from flask import render_template, jsonify
from flaskr import app
from flask import request
from flaskr.server.DeviceAdministration import DeviceAdministration
import time
from flaskr.server.bo.RulesBO import RulesBO


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Test', methods=["GET"])
# hier ist die get_Status Methode
# former Test()
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

    odata['d']['results'].append(last_status.get_percentage())

    return jsonify(odata)


@app.route('/Jalousien', methods=["POST"])
def set_jal():
    """
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    data = request.form["value"]
    data = int(data)
    #time.sleep(4)
    k = adm.set_status_to_percentage_by_id(1, data)
    if type(k) == tuple:
        test = str(k)
        return "0"
    else:
        adm.set_status_to_percentage_by_id(1, data)
        jal = adm.get_last_status()
        return ' ', 200



@app.route('/JalousienStatusPerHour', methods=["GET"])
def get_jal_stats_per_hour_for_weekday():
    """
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()
    weekday = request.form["weekday"]
    von = request.form["von"]
    bis = request.form["bis"]
    data = adm.get_median_jal_for_timespan(von, bis, weekday)

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

@app.route('/StatusPerDay', methods=["GET"])
def status_per_day():
    """
    Return a simple odata container with date time information
    :return:
    """
    """
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    day = request.form["day"]
    stats = adm.get_jal_mean_per_day(day)
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

@app.route('/StatusPerWeek', methods=["GET"])
def status_for_week():
    """
    Return a simple odata container with date time information
    :return:
    """
    """
    Return a simple odata container with date time information
    :return:
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
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    data = request.form["value"]
    data = int(data)
    time.sleep(4)
    adm.set_temperature(data)
    temp = adm.get_temperature()
    print('temp: ', temp)
    x = "Hi"
    return x


@app.route('/GetTemp', methods=["GET"])
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


@app.route('/GetStandardJalousienMonday', methods=["GET"])
def get_entries_jal_monday():
    """
    Return a simple odata container with date time information
    :return:
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': [
                
            ]
        }
    }

    entries = adm.get_all_jal_standard_entries_monday()
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
    Return a simple odata container with date time information
    :return:
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_jal_standard_entries_tuesday()
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
    Return a simple odata container with date time information
    :return:
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_jal_standard_entries_wednesday()
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
    Return a simple odata container with date time information
    :return:
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_jal_standard_entries_thursday()
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
    Return a simple odata container with date time information
    :return:
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_jal_standard_entries_friday()
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
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(4)

    k = adm.set_jal_standard_entry_monday(start, end, value)
    if type(k) == tuple:
        test = str(k)
        return "0"
    else:
        return ' ', 200


@app.route('/SetJalousienStandardTuesday', methods=["POST"])
def set_jal_standard_tuesday():
    """
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(4)
    adm.set_jal_standard_entry_tuesday(start, end, value)
    return ' '


@app.route('/SetJalousienStandardWednesday', methods=["POST"])
def set_jal_standard_wednesday():
    """
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(4)
    adm.set_jal_standard_entry_wednesday(start, end, value)
    return ' '


@app.route('/SetJalousienStandardThursday', methods=["POST"])
def set_jal_standard_thursday():
    """
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(4)
    adm.set_jal_standard_entry_thursday(start, end, value)
    return ' '


@app.route('/SetJalousienStandardFriday', methods=["POST"])
def set_jal_standard_friday():
    """
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(4)
    adm.set_jal_standard_entry_friday(start, end, value)
    return ' '

@app.route('/DeleteStandardJalousienMonday', methods=["DELETE"])
def delete_entry_jal_monday():
    """
    Return a simple odata container with date time information
    :return:
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
    Return a simple odata container with date time information
    :return:
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
    Return a simple odata container with date time information
    :return:
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
    Return a simple odata container with date time information
    :return:
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
    Return a simple odata container with date time information
    :return:
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
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    min = request.form["min"]
    max = request.form["max"]
    time.sleep(4)
    adm.set_jal_rule(min, max, start, end)
    return ' '

@app.route('/GetJalRule', methods=["GET"])
def get_jal_rules():
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
    rules = adm.get_all_jal_rules()
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
    Return a simple odata container with date time information
    :return:
    """
    adm = DeviceAdministration()
    id_entry = request.form["id_entry"]
    id_entry = int(id_entry)
    adm.delete_jal_rules_byId(id_entry)
    return ' '


@app.route('/SetMinTemp', methods=["POST"])
def set_min_temp():
    """
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()
    data = request.form["value"]
    temp = adm.set_temp_rule_min(data)
    print('temp: ', temp)
    return data


@app.route('/GetMinTemp', methods=["GET"])
# hier ist die get_Status Methode
def get_min_temp():
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

    temp = adm.get_min_temp()
    odata['d']['results'].append({
        'min_temperature': temp
    })

    return jsonify(odata)


@app.route('/SetMaxTemp', methods=["POST"])
def set_max_temp():
    """
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()
    data = request.form["value"]
    temp = adm.set_temp_rule_max(data)
    print('temp: ', temp)
    return data


@app.route('/GetStandardThermostatMonday', methods=["GET"])
def get_entries_temp_monday():
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

    entries = adm.get_all_temp_standard_entries_monday()
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
    Return a simple odata container with date time information
    :return:
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_temp_standard_entries_tuesday()
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
    Return a simple odata container with date time information
    :return:
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_temp_standard_entries_wednesday()
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
    Return a simple odata container with date time information
    :return:
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_temp_standard_entries_thursday()
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
    Return a simple odata container with date time information
    :return:
    """
    adm = DeviceAdministration()

    odata = {
        'd': {
            'results': []
        }
    }

    entries = adm.get_all_temp_standard_entries_friday()
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
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(4)
    adm.set_temp_standard_entry_monday(start, end, value)
    return ' '


@app.route('/SetThermostatStandardTuesday', methods=["POST"])
def set_temp_standard_tuesday():
    """
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(4)
    adm.set_temp_standard_entry_tuesday(start, end, value)
    return ' '


@app.route('/SetThermostatStandardWednesday', methods=["POST"])
def set_temp_standard_wednesday():
    """
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(4)
    adm.set_temp_standard_entry_wednesday(start, end, value)
    return ' '


@app.route('/SetThermostatStandardThursday', methods=["POST"])
def set_temp_standard_thursday():
    """
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(4)
    adm.set_temp_standard_entry_thursday(start, end, value)
    return ' '


@app.route('/SetThermostatStandardFriday', methods=["POST"])
def set_temp_standard_friday():
    """
    Return a simple odata container with date time information
    :return:
    """

    adm = DeviceAdministration()

    start = request.form["start"]
    end = request.form["end"]
    value = request.form["value"]
    value = int(value)
    time.sleep(4)
    adm.set_temp_standard_entry_friday(start, end, value)
    return ' '


