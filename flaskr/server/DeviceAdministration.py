from flaskr.server.bo.Jalousien import JalousienBO
from flaskr.server.database.JalousienMapper import JalousienMapper
from flaskr.server.bo.Thermostat import ThermostatBO
from flaskr.server.database.ThermostatMapper import ThermostatMapper
from flaskr.server.bo.JalosuienStatusBO import JalousienStatusBO
from flaskr.server.database.JalousienStatusMapper import JalousienStatusMapper
from flaskr.server.bo.WochenplanJalBO import WeeklyPlanJalBO
from flaskr.server.database.WochenplanJalMapper import WeeklyPlanJalMapper
from flaskr.server.bo.WochenplanThermoBO import WeeklyPlanTempBO
from flaskr.server.database.WochenplanTempMapper import WeeklyPlanTempMapper
from flaskr.server.bo.weekdays_jal.MondayBO import Monday
from flaskr.server.bo.weekdays_jal.TuesdayBO import Tuesday
from flaskr.server.bo.weekdays_jal.WednesdayBO import Wednesday
from flaskr.server.bo.weekdays_jal.ThursdayBO import Thursday
from flaskr.server.bo.weekdays_jal.FridayBO import Friday
from flaskr.server.database.weekday_mapper.MondayMapper import MondayMapper
from flaskr.server.database.weekday_mapper.TuesdayMapper import TuesdayMapper
from flaskr.server.database.weekday_mapper.WednesdayMapper import WednesdayMapper
from flaskr.server.database.weekday_mapper.ThursdayMapper import ThursdayMapper
from flaskr.server.database.weekday_mapper.FridayMapper import FridayMapper
from flaskr.server.bo.RulesBO import RulesBO
from flaskr.server.database.RulesMapper import RulesMapper
from flaskr.server.AuthGen import get_sid
from flaskr.server.bo.ThermostatStatusBO import ThermostatStatusBO
from flaskr.server.database.ThermostatStatusMapper import ThermostatStatusMapper
import time
import http.client
from datetime import datetime, timedelta
import datetime
import statistics


class DeviceAdministration(object):
    """Realisierung eines exemplarischen Bankkontos.

    Ein Konto besitzt einen Inhaber sowie eine Reihe von Buchungen (vgl. Klasse Transaction),
    mit deren Hilfe auch der Kontostand berechnet werden kann.
    """

    def __init__(self):
        pass

    """
    Jalousie-spezifische Methoden
    """

    def add_device(self, device_id, ip_address, local_key):
        j = JalousienBO()
        j.set_device_id(device_id)
        j.set_ip_address(ip_address)
        j.set_local_key(local_key)
        j.set_device()
        with JalousienMapper() as mapper:
            return mapper.insert(j)

    def get_jalousie_by_device_id(self, device_id):
        """Alle Benutzer mit Namen name auslesen."""
        with JalousienMapper() as mapper:
            return mapper.find_by_device_id(device_id)

    def get_jalousie_by_id(self, id):
        pass
        """Alle Benutzer mit Namen name auslesen."""
        with JalousienMapper() as mapper:
            return mapper.find_by_id(id)

    def get_jalousie_by_ip_address(self, ip_address):
        """Alle Benutzer mit gegebener E-Mail-Adresse auslesen."""
        with JalousienMapper() as mapper:
            return mapper.find_by_ip_address(ip_address)

    def get_jalousie_by_local_key(self, local_key):
        """Den Benutzer mit der gegebenen Google ID auslesen."""
        with JalousienMapper() as mapper:
            return mapper.find_by_key(local_key)

    def get_all_jalousies(self):
        """Alle Benutzer auslesen."""
        with JalousienMapper() as mapper:
            return mapper.find_all()

    def save_jalousie(self, jalousie):
        """Den gegebenen Benutzer speichern."""
        with JalousienMapper() as mapper:
            mapper.update(jalousie)

    def delete_jalousie(self, jalousie):
        """Den gegebenen Benutzer aus unserem System löschen."""
        with JalousienMapper() as mapper:
            mapper.delete(jalousie)

    '''    def open_all_jalousies(self):
            jalousies = []
            status = []
            with JalousienMapper() as mapper:
                jalousies.append(mapper.find_all())
            for elem in jalousies:
                for x in elem:
                    x.set_device()
                    dev = x.get_device()
                    dev.set_value(1, 'open')
                    status.append(dev.status())
            return status

        def close_all_jalousies(self):
            jalousies = []
            status = JalousienStatusBO()
            jalousies.append(self.get_all_jalousies())
            for elem in jalousies:
                for x in elem:
                        x.set_device()
                        dev = x.get_device()
                        dev.set_value(1, 'close')
                        time.sleep(10)
                        status.set_status(str(dev.status()))
                        status.set_device(id)
            return status'''

    '''    def open_jalousie_by_id(self, id):
            jalousies = []
            status = JalousienStatusBO()
            jalousies.append(self.get_all_jalousies())
            dev_stat = None
            for elem in jalousies:
                for x in elem:
                    if x.get_id() == id:
                        x.set_device()
                        dev = x.get_device()
                        dev.set_value(1, 'open')
                        time.sleep(10)
                        status.set_status(str(dev.status()))
                        status.set_device(id)
                        date = datetime.now()
                        status.set_date(date)
                        dev_stat = dev.status()
            new_list = []
            for key in dev_stat:
                for elem in dev_stat[key].values():
                    new_list.append(elem)
            status.set_percentage(new_list[1])
            return status
    
        def close_jalousie_by_id(self, id):
            jalousies = []
            status = JalousienStatusBO()
            jalousies.append(self.get_all_jalousies())
            dev_stat = None
            for elem in jalousies:
                for x in elem:
                    if x.get_id() == id:
                        x.set_device()
                        dev = x.get_device()
                        dev.set_value(1, 'close')
                        time.sleep(10)
                        status.set_status(str(dev.status()))
                        status.set_device(id)
                        date = datetime.now()
                        status.set_date(date)
                        dev_stat = dev.status()
            new_list = []
            for key in dev_stat:
                for elem in dev_stat[key].values():
                    new_list.append(elem)
            status.set_percentage(new_list[1])
            return status'''

    def set_status_to_percentage_by_id(self, id, perc):
        date = datetime.datetime.now()
        date = date.strftime('%Y-%m-%d %H:%M:%S')
        trigger = False
        rules = self.get_all_jal_rules()
        for elem in rules:
            if elem.get_min() is None and elem.get_max() is None:
                if self.in_between_times(date, elem.get_start_time(), elem.get_end_time()):
                    message = 'Die No_Access Zeit ist eingetroffen'
                    print(message)
                    return message
            elif int(perc) > elem.get_max() or int(perc) < elem.get_min():
                message = 'Das geht so nicht!', perc, 'Mindesttemp:', elem.get_min(
                ), 'Maxtemp:', elem.get_max()
                print(message)
                return message
            else:
                trigger = True
        if trigger:
            jalousies = []
            status = JalousienStatusBO()
            status.set_percentage(perc)
            perc = status.get_percentage()
            status.set_date(date)
            jalousies.append(self.get_all_jalousies())
            for elem in jalousies:
                for x in elem:
                    if x.get_id() == id:
                        x.set_device()
                        dev = x.get_device()
                        dev.set_value(2, perc)
                        status.set_status(str(dev.status()))
                        status.set_device(id)
            with JalousienStatusMapper() as mapper:
                return mapper.insert(status)

    def get_status_of_jalousie_by_id(self, id):
        with JalousienStatusMapper() as mapper:
            return mapper.find_by_key(id)

    def delete_status_by_id(self, id):
        status = self.get_status_of_jalousie_by_id(id)
        with JalousienStatusMapper() as mapper:
            mapper.delete(status)

    def get_last_status(self):
        status = self.get_all_jal_status()
        return status[-1]

    def get_all_jal_status(self):
        with JalousienStatusMapper() as mapper:
            return mapper.find_all()

    # def get_jal_median_of_hours_for_day(self, day, hour):
    #     all_jal_stats = self.get_all_jal_status()
    #     stats_for_weekday = []
    #     hourly_rate = []
    #     for elem in all_jal_stats:
    #         vergleich = elem.get_date().strftime('%Y-%m-%d')
    #         if vergleich == day:
    #             stats_for_weekday.append(elem)
    #     for elem in stats_for_weekday:
    #         if elem.get_date().hour == hour:
    #             hourly_rate.append(elem.get_percentage())
    #     if len(hourly_rate) > 1:
    #         return statistics.median(hourly_rate)
    #     elif len(hourly_rate) == 1:
    #         return hourly_rate[0]
    #     else:
    #         return 0

    def get_last_entry_of_hour_for_day(self, day, hour):
        all_jal_stats = self.get_all_jal_status()
        stats_for_weekday = []
        hourly_rate = []
        for elem in all_jal_stats:
            vergleich = elem.get_date().strftime('%Y-%m-%d')
            if vergleich == day:
                stats_for_weekday.append(elem)
        for elem in stats_for_weekday:
            if elem.get_date().hour == hour:
                hourly_rate.append(elem.get_percentage())
        if len(hourly_rate) >= 1:
            return hourly_rate[-1]
        else:
            return 0

    def get_jal_mean_per_day(self, day):
        result = []
        i = 6
        while i <= 20:
            x = self.get_last_entry_of_hour_for_day(day, i)
            result.append(x)
            i += 1
        return statistics.mean(result)

    def get_jal_median_per_week(self, week):
        liste = self.get_all_jal_status()
        stats_for_week = []
        weekly_stats = []
        for elem in liste:
            if elem.get_date().isocalendar()[1] == week:
                stats_for_week.append(elem)
        for elem in stats_for_week:
            elem_week = elem.get_date().isocalendar()[1]
            day = elem.get_date().strftime('%Y-%m-%d')
            if elem_week == week:
                x = self.get_jal_mean_per_day(day)
                weekly_stats.append(x)
        if len(weekly_stats) > 1:
            return statistics.median(weekly_stats)
        elif len(weekly_stats) == 1:
            return weekly_stats[0]
        else:
            return 0

    def get_median_jal_for_timespan(self, von, bis, day):
        values = []
        delta = bis - von
        week = datetime.datetime.strptime(day, '%Y-%m-%d').isocalendar()[1]
        for elem in range(von, bis + 1):
            x = self.get_last_entry_of_hour_for_day(day, elem)
            values.append(x)
        return values

    def get_median_values_jal(self, day):
        values = []
        k = self.get_median_jal_for_timespan(7, 10, day)
        k = k[-1]
        values.append(k)
        m = self.get_median_jal_for_timespan(10, 13, day)
        m = m[-1]
        values.append(m)
        n = self.get_median_jal_for_timespan(13, 16, day)
        n = n[-1]
        values.append(n)
        l = self.get_median_jal_for_timespan(16, 19, day)
        l = l[-1]
        values.append(l)
        return values

    def in_between_times(self, searched_time, start, end):
        searched_time = datetime.datetime.strptime(searched_time, '%H:%M:%S')
        searched_time = searched_time.strftime('%H%M%S')
        searched_time = float(searched_time)
        start = datetime.datetime.strptime(start, '%H:%M:%S')
        start = start.strftime('%H%M%S')
        start = float(start)
        end = datetime.datetime.strptime(end, '%H:%M:%S')
        end = end.strftime('%H%M%S')
        end = float(end)
        if start <= searched_time <= end:
            return True
        else:
            return False

    def get_all_stats_by_timeperiod(self, start, end):
        enddate = datetime.now().fromisoformat(str(end))
        startdate = datetime.now().fromisoformat(str(start))
        stats = self.get_all_jal_status()
        interval = []
        for elem in stats:
            if self.in_between_times(elem.get_date(), startdate, enddate):
                print(elem.get_date())
                interval.append(elem)
            else:
                pass
        return interval

    def get_status_of_thermostat_by_id(self, id):
        with ThermostatStatusMapper() as mapper:
            return mapper.find_by_key(id)

    def delete_thermostat_status_by_id(self, id):
        status = self.get_status_of_jalousie_by_id(id)
        with ThermostatStatusMapper() as mapper:
            mapper.delete(status)

    def get_last_thermostat_status(self):
        status = self.get_all_thermostat_status()
        return status[-1]

    def get_all_thermostat_status(self):
        with ThermostatStatusMapper() as mapper:
            return mapper.find_all()

    """
    Thermostat-spezifische Methoden
    """

    def generate_sid(self, box_url, user_name, password):
        sid = get_sid(box_url, user_name, password)
        return sid

    '''    def add_thermostat(self, ain, box_url, user_name, password):
        """Einen Kunden anlegen."""
        thermostat = ThermostatBO()
        thermostat.set_ain(ain)
        with ThermostatMapper() as mapper:
            return mapper.insert(thermostat)'''

    def get_thermostat_by_ain(self, ain):
        """Alle Kunden mit übergebenem Nachnamen auslesen."""
        with ThermostatMapper() as mapper:
            return mapper.find_by_ain(ain)

    def get_thermostat_by_id(self, id):
        """Alle Kunden mit übergebenem Nachnamen auslesen."""
        with ThermostatMapper() as mapper:
            return mapper.find_by_key(id)

    '''    def get_all_thermostats(self):
        with ThermostatMapper() as mapper:
            return mapper.find_all()

    def save_thermostat(self, thermostat):
        """Den gegebenen Kunden speichern."""
        with ThermostatMapper() as mapper:
            mapper.update(thermostat)'''

    def set_temperature(self, temp, device_id=None):
        date = datetime.datetime.now()
        date_for_stat = date.strftime('%Y-%m-%d %H:%M:%S')
        date = date.strftime('%H:%M:%S')
        trigger = False
        rules = self.get_all_temp_rules()
        for elem in rules:
            if elem.get_min() is None and elem.get_max() is None:
                if self.in_between_times(date, elem.get_start_time(), elem.get_end_time()):
                    message = 'Die No_Access Zeit ist eingetroffen'
                    return message
            elif temp > elem.get_max() or temp < elem.get_min():
                message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(
                ), 'Maxtemp:', elem.get_max()
                return message
            else:
                trigger = True
        if trigger:
            conn = http.client.HTTPSConnection(
                "gmhn0evflkdlpmbw.myfritz.net", 8254)
            payload = ''
            headers = {}
            sid = self.generate_sid(
                'https://192.168.2.254:8254/', 'admin', 'QUANTO_Solutions')
            conn.request("GET",
                         "/webservices/homeautoswitch.lua?sid={}&ain=139790057201&switchcmd=sethkrtsoll&param={}".format(
                             sid, temp),
                         payload, headers)
            res = conn.getresponse()
            data = res.read()
            data = data.decode("utf-8")
            status = ThermostatStatusBO()
            status.set_temp(temp)
            status.set_date(date_for_stat)
            status.set_device(device_id)
            with ThermostatStatusMapper() as mapper:
                return mapper.insert(status)

    def get_comfort_temperature(self):
        conn = http.client.HTTPSConnection("192.168.2.254", 8254)
        payload = ''
        headers = {}
        sid = self.generate_sid(
            'https://192.168.2.254:8254/', 'admin', 'QUANTO_Solutions')
        conn.request("GET",
                     "/webservices/homeautoswitch.lua?ain=139790057201&switchcmd=gethkrkomfort&sid={}".format(
                         sid),
                     payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        print(data)
        return data

    def get_temp_from_device(self):
        conn = http.client.HTTPSConnection("192.168.2.254", 8254)
        payload = ''
        sid = self.generate_sid(
            'https://192.168.2.254:8254/', 'admin', 'QUANTO_Solutions')
        headers = {
            'Content-Type': 'application/json'
        }
        conn.request("GET",
                     "/webservices/homeautoswitch.lua?sid={}&ain=139790057201&switchcmd=gettemperature".format(sid),
                     payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        return data

    def set_min_temp_of_device(self, temp):
        conn = http.client.HTTPSConnection("192.168.2.254", 8254)
        payload = ''
        sid = self.generate_sid(
            'https://192.168.2.254:8254/', 'admin', 'QUANTO_Solutions')
        headers = {
            'Content-Type': 'application/json'
        }
        conn.request("GET",
                     "/webservices/homeautoswitch.lua?sid={}&ain=139790057201&switchcmd=sethkrtsoll&param={}".format(
                         sid, temp),
                     payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        return data

    ####################################################################################
    '''Für Statistik Soll , Ist (Durchschnitt der Stunden nehmen)'''

    # dateofLastChange -> Lösche alle Einträge, die nicht von heute sind.
    # Lösche alle Einträge bei denen es Überlappung gibt
    # Er macht einen Check und wenn die neue Zeit sich mit einem anderen Timeintervall überlappt, wird der alte gelöscht.

    def set_jal_standard_entry_monday(self, start, end, perc):
        trigger = False
        rules = self.get_all_jal_rules()
        if len(rules) == 0:
            trigger = True
        for elem in rules:
            if elem.get_min() is not None and elem.get_max() is not None and self.overlapping(start, end,
                                                                                              elem.get_start_time(),
                                                                                              elem.get_end_time()) is True:
                if perc > elem.get_max() or perc < elem.get_min():
                    message = 'Das geht so nicht!', perc, 'Mindesttemp:', elem.get_min(
                    ), 'Maxtemp:', elem.get_max()
                    print(message)
                    return message
                else:
                    trigger = True
            else:
                trigger = True
        if trigger:
            monday = Monday()
            monday.set_type('J')
            monday.set_start_time(start)
            monday.set_end_time(end)
            monday.set_value(perc)
            liste = self.get_all_standard_weekly_jal_entries_by_weekday(1)
            entries = self.get_all_jal_standard_entries_monday()
            for elem in entries:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    for y in liste:
                        if y.get_monday_id() == elem.get_id():
                            self.delete_entry_in_standard_weeklyplan_jal(y)
                            self.delete_standard_entry_monday(elem)
                            print(elem, 'wurde gelöscht.')
            with MondayMapper() as mapper:
                mapper.insert(monday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_jal_standard_entry_monday()
            standard_entry.set_monday_id(last_entry.get_id())
            standard_entry.set_weekday(1)
            with WeeklyPlanJalMapper() as mapper:
                return mapper.insert(standard_entry)

    def get_all_jal_standard_entries_monday(self):
        with MondayMapper() as mapper:
            return mapper.find_all_jal_entries()

    def get_latest_jal_standard_entry_monday(self):
        with MondayMapper() as mapper:
            return mapper.find_latest_jal_entry()

    def set_jal_standard_entry_tuesday(self, start, end, perc):
        trigger = False
        rules = self.get_all_jal_rules()
        if len(rules) == 0:
            trigger = True
        for elem in rules:
            if elem.get_min() is None and elem.get_max() is None:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    message = 'Die No_Access Zeit ist eingetroffen'
                    return message
            elif elem.get_min() is not None and elem.get_max() is not None and perc > elem.get_max() or perc < elem.get_min():
                message = 'Das geht so nicht!', perc, 'Mindesttemp:', elem.get_min(
                ), 'Maxtemp:', elem.get_max()
                return message
            else:
                trigger = True
        if trigger:
            tuesday = Tuesday()
            tuesday.set_type('J')
            tuesday.set_start_time(start)
            tuesday.set_end_time(end)
            tuesday.set_value(perc)
            liste = self.get_all_standard_weekly_jal_entries_by_weekday(2)
            entries = self.get_all_jal_standard_entries_tuesday()
            for elem in entries:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    for y in liste:
                        if y.get_tuesday_id() == elem.get_id():
                            self.delete_entry_in_standard_weeklyplan_jal(y)
                            self.delete_standard_entry_tuesday(elem)
                            print(elem, 'wurde gelöscht.')
            with TuesdayMapper() as mapper:
                mapper.insert(tuesday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_jal_standard_entry_tuesday()
            standard_entry.set_tuesday_id(last_entry.get_id())
            standard_entry.set_weekday(2)
            with WeeklyPlanJalMapper() as mapper:
                return mapper.insert(standard_entry)

    def get_all_jal_standard_entries_tuesday(self):
        with TuesdayMapper() as mapper:
            return mapper.find_all_jal_entries()

    def get_latest_jal_standard_entry_tuesday(self):
        with TuesdayMapper() as mapper:
            return mapper.find_latest_jal_entry()

    def set_jal_standard_entry_wednesday(self, start, end, perc):
        trigger = False
        rules = self.get_all_jal_rules()
        if len(rules) == 0:
            trigger = True
        for elem in rules:
            if elem.get_min() is None and elem.get_max() is None:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    message = 'Die No_Access Zeit ist eingetroffen'
                    return message
            elif elem.get_min() is not None and elem.get_max() is not None and perc > elem.get_max() or perc < elem.get_min():
                message = 'Das geht so nicht!', perc, 'Mindesttemp:', elem.get_min(
                ), 'Maxtemp:', elem.get_max()
                return message
            else:
                trigger = True
        if trigger:
            wednesday = Wednesday()
            wednesday.set_type('J')
            wednesday.set_start_time(start)
            wednesday.set_end_time(end)
            wednesday.set_value(perc)
            liste = self.get_all_standard_weekly_jal_entries_by_weekday(3)
            entries = self.get_all_jal_standard_entries_wednesday()
            for elem in entries:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    for y in liste:
                        if y.get_wednesday_id() == elem.get_id():
                            self.delete_entry_in_standard_weeklyplan_jal(y)
                            self.delete_standard_entry_wednesday(elem)
                            print(elem, 'wurde gelöscht.')
            with WednesdayMapper() as mapper:
                mapper.insert(wednesday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_jal_standard_entry_wednesday()
            standard_entry.set_wednesday_id(last_entry.get_id())
            standard_entry.set_weekday(3)
            with WeeklyPlanJalMapper() as mapper:
                return mapper.insert(standard_entry)

    def get_all_jal_standard_entries_wednesday(self):
        with WednesdayMapper() as mapper:
            return mapper.find_all_jal_entries()

    def get_latest_jal_standard_entry_wednesday(self):
        with WednesdayMapper() as mapper:
            return mapper.find_latest_jal_entry()

    def set_jal_standard_entry_thursday(self, start, end, perc):
        trigger = False
        rules = self.get_all_jal_rules()
        if len(rules) == 0:
            trigger = True
        for elem in rules:
            if elem.get_min() is None and elem.get_max() is None:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    message = 'Die No_Access Zeit ist eingetroffen'
                    return message
            elif elem.get_min() is not None and elem.get_max() is not None and perc > elem.get_max() or perc < elem.get_min():
                message = 'Das geht so nicht!', perc, 'Mindesttemp:', elem.get_min(
                ), 'Maxtemp:', elem.get_max()
                return message
            else:
                trigger = True
        if trigger:
            thursday = Thursday()
            thursday.set_type('J')
            thursday.set_start_time(start)
            thursday.set_end_time(end)
            thursday.set_value(perc)
            liste = self.get_all_standard_weekly_jal_entries_by_weekday(4)
            entries = self.get_all_jal_standard_entries_thursday()
            for elem in entries:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    for y in liste:
                        if y.get_thursday_id() == elem.get_id():
                            self.delete_entry_in_standard_weeklyplan_jal(y)
                            self.delete_standard_entry_thursday(elem)
                            print(elem, 'wurde gelöscht.')
            with ThursdayMapper() as mapper:
                mapper.insert(thursday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_jal_standard_entry_thursday()
            standard_entry.set_thursday_id(last_entry.get_id())
            standard_entry.set_weekday(4)
            with WeeklyPlanJalMapper() as mapper:
                return mapper.insert(standard_entry)

    def get_all_jal_standard_entries_thursday(self):
        with ThursdayMapper() as mapper:
            return mapper.find_all_jal_entries()

    def get_latest_jal_standard_entry_thursday(self):
        with ThursdayMapper() as mapper:
            return mapper.find_latest_jal_entry()

    def set_jal_standard_entry_friday(self, start, end, perc):
        trigger = False
        rules = self.get_all_jal_rules()
        if len(rules) == 0:
            trigger = True
        for elem in rules:
            if elem.get_min() is None and elem.get_max() is None:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    message = 'Die No_Access Zeit ist eingetroffen'
                    return message
            elif elem.get_min() is not None and elem.get_max() is not None and perc > elem.get_max() or perc < elem.get_min():
                message = 'Das geht so nicht!', perc, 'Mindesttemp:', elem.get_min(
                ), 'Maxtemp:', elem.get_max()
                return message
            else:
                trigger = True
        if trigger:
            friday = Friday()
            friday.set_type('J')
            friday.set_start_time(start)
            friday.set_end_time(end)
            friday.set_value(perc)
            liste = self.get_all_standard_weekly_jal_entries_by_weekday(5)
            entries = self.get_all_jal_standard_entries_friday()
            for elem in entries:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    for y in liste:
                        if y.get_friday_id() == elem.get_id():
                            self.delete_entry_in_standard_weeklyplan_jal(y)
                            self.delete_standard_entry_friday(elem)
                    print(elem, 'wurde gelöscht.')
            with FridayMapper() as mapper:
                mapper.insert(friday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_jal_standard_entry_friday()
            standard_entry.set_friday_id(last_entry.get_id())
            standard_entry.set_weekday(5)
            with WeeklyPlanJalMapper() as mapper:
                return mapper.insert(standard_entry)

    def get_all_jal_standard_entries_friday(self):
        with FridayMapper() as mapper:
            return mapper.find_all_jal_entries()

    def get_latest_jal_standard_entry_friday(self):
        with FridayMapper() as mapper:
            return mapper.find_latest_jal_entry()

    def set_temp_standard_entry_monday(self, start, end, temp):
        trigger = False
        rules = self.get_all_temp_rules()
        if len(rules) == 0:
            trigger = True
        for elem in rules:
            if elem.get_min() is None and elem.get_max() is None:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    message = 'Die No_Access Zeit ist eingetroffen'
                    return message
            elif elem.get_min() is not None and elem.get_max() is not None and temp > elem.get_max() or temp < elem.get_min():
                message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(
                ), 'Maxtemp:', elem.get_max()
                return message
            else:
                trigger = True
        if trigger:
            monday = Monday()
            monday.set_type('T')
            monday.set_start_time(start)
            monday.set_end_time(end)
            monday.set_value(temp)
            liste = self.get_all_standard_weekly_temp_entries_by_weekday(1)
            entries = self.get_all_temp_standard_entries_monday()
            for elem in entries:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    for y in liste:
                        if y.get_monday_id() == elem.get_id():
                            self.delete_entry_in_standard_weeklyplan_temp(y)
                            self.delete_standard_entry_monday(elem)
                            print(elem, 'wurde gelöscht.')
            with MondayMapper() as mapper:
                mapper.insert(monday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_temp_standard_entry_monday()
            standard_entry.set_monday_id(last_entry.get_id())
            standard_entry.set_weekday(1)
            with WeeklyPlanTempMapper() as mapper:
                return mapper.insert(standard_entry)

    def get_all_temp_standard_entries_monday(self):
        with MondayMapper() as mapper:
            return mapper.find_all_temp_entries()

    def get_latest_temp_standard_entry_monday(self):
        with MondayMapper() as mapper:
            return mapper.find_latest_temp_entry()

    def delete_standard_entry_monday(self, entry):
        with MondayMapper() as mapper:
            return mapper.delete(entry)

    def delete_jal_monday_by_id(self, id):
        with WeeklyPlanJalMapper() as mapper:
            return mapper.delete_byId(id)

    def set_temp_standard_entry_tuesday(self, start, end, temp):
        trigger = False
        rules = self.get_all_temp_rules()
        if len(rules) == 0:
            trigger = True
        for elem in rules:
            if elem.get_min() is None and elem.get_max() is None:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    message = 'Die No_Access Zeit ist eingetroffen'
                    return message
            elif elem.get_min() is not None and elem.get_max() is not None and temp > elem.get_max() or temp < elem.get_min():
                message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(
                ), 'Maxtemp:', elem.get_max()
                return message
            else:
                trigger = True
        if trigger:
            tuesday = Tuesday()
            tuesday.set_type('T')
            tuesday.set_start_time(start)
            tuesday.set_end_time(end)
            tuesday.set_value(temp)
            liste = self.get_all_standard_weekly_temp_entries_by_weekday(2)
            entries = self.get_all_temp_standard_entries_tuesday()
            for elem in entries:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    for y in liste:
                        if y.get_tuesday_id() == elem.get_id():
                            self.delete_entry_in_standard_weeklyplan_temp(y)
                            self.delete_standard_entry_tuesday(elem)
                    print(elem, 'wurde gelöscht.')
                    self.delete_rule(elem)
            with TuesdayMapper() as mapper:
                mapper.insert(tuesday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_temp_standard_entry_tuesday()
            standard_entry.set_tuesday_id(last_entry.get_id())
            standard_entry.set_weekday(2)
            with WeeklyPlanTempMapper() as mapper:
                return mapper.insert(standard_entry)

    def get_all_temp_standard_entries_tuesday(self):
        with TuesdayMapper() as mapper:
            return mapper.find_all_temp_entries()

    def get_latest_temp_standard_entry_tuesday(self):
        with TuesdayMapper() as mapper:
            return mapper.find_latest_temp_entry()

    def delete_standard_entry_tuesday(self, entry):
        with TuesdayMapper() as mapper:
            return mapper.delete(entry)

    def set_temp_standard_entry_wednesday(self, start, end, temp):
        trigger = False
        rules = self.get_all_temp_rules()
        if len(rules) == 0:
            trigger = True
        for elem in rules:
            if elem.get_min() is None and elem.get_max() is None:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    message = 'Die No_Access Zeit ist eingetroffen'
                    return message
            elif elem.get_min() is not None and elem.get_max() is not None and temp > elem.get_max() or temp < elem.get_min():
                message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(
                ), 'Maxtemp:', elem.get_max()
                return message
            else:
                trigger = True
        if trigger:
            wednesday = Wednesday()
            wednesday.set_type('T')
            wednesday.set_start_time(start)
            wednesday.set_end_time(end)
            wednesday.set_value(temp)
            liste = self.get_all_standard_weekly_temp_entries_by_weekday(3)
            entries = self.get_all_temp_standard_entries_wednesday()
            for elem in entries:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    for y in liste:
                        if y.get_wednesday_id() == elem.get_id():
                            self.delete_entry_in_standard_weeklyplan_temp(y)
                            self.delete_standard_entry_wednesday(elem)
                    print(elem, 'wurde gelöscht.')
                    self.delete_rule(elem)
            with WednesdayMapper() as mapper:
                mapper.insert(wednesday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_temp_standard_entry_wednesday()
            standard_entry.set_wednesday_id(last_entry.get_id())
            standard_entry.set_weekday(3)
            with WeeklyPlanTempMapper() as mapper:
                return mapper.insert(standard_entry)

    def get_all_temp_standard_entries_wednesday(self):
        with WednesdayMapper() as mapper:
            return mapper.find_all_temp_entries()

    def get_latest_temp_standard_entry_wednesday(self):
        with WednesdayMapper() as mapper:
            return mapper.find_latest_temp_entry()

    def delete_standard_entry_wednesday(self, entry):
        with WednesdayMapper() as mapper:
            return mapper.delete(entry)

    def set_temp_standard_entry_thursday(self, start, end, temp):
        trigger = False
        rules = self.get_all_temp_rules()
        if len(rules) == 0:
            trigger = True
        for elem in rules:
            if elem.get_min() is None and elem.get_max() is None:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    message = 'Die No_Access Zeit ist eingetroffen'
                    return message
            elif elem.get_min() is not None and elem.get_max() is not None and temp > elem.get_max() or temp < elem.get_min():
                message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(
                ), 'Maxtemp:', elem.get_max()
                return message
            else:
                trigger = True
        if trigger:
            thursday = Thursday()
            thursday.set_type('T')
            thursday.set_start_time(start)
            thursday.set_end_time(end)
            thursday.set_value(temp)
            liste = self.get_all_standard_weekly_temp_entries_by_weekday(4)
            entries = self.get_all_temp_standard_entries_thursday()
            for elem in entries:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    for y in liste:
                        if y.get_thursday_id() == elem.get_id():
                            self.delete_entry_in_standard_weeklyplan_temp(y)
                            self.delete_standard_entry_thursday(elem)
                    print(elem, 'wurde gelöscht.')

            with ThursdayMapper() as mapper:
                mapper.insert(thursday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_temp_standard_entry_thursday()
            standard_entry.set_thursday_id(last_entry.get_id())
            standard_entry.set_weekday(4)
            with WeeklyPlanTempMapper() as mapper:
                return mapper.insert(standard_entry)

    def get_all_temp_standard_entries_thursday(self):
        with ThursdayMapper() as mapper:
            return mapper.find_all_temp_entries()

    def get_latest_temp_standard_entry_thursday(self):
        with ThursdayMapper() as mapper:
            return mapper.find_latest_temp_entry()

    def delete_standard_entry_thursday(self, entry):
        with ThursdayMapper() as mapper:
            return mapper.delete(entry)

    def set_temp_standard_entry_friday(self, start, end, temp):
        trigger = False
        rules = self.get_all_temp_rules()
        if len(rules) == 0:
            trigger = True
        for elem in rules:
            if elem.get_min() is None and elem.get_max() is None:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    message = 'Die No_Access Zeit ist eingetroffen'
                    return message
            elif temp > elem.get_max() or temp < elem.get_min():
                message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(
                ), 'Maxtemp:', elem.get_max()
                return message
            else:
                trigger = True
        if trigger:
            friday = Friday()
            friday.set_type('T')
            friday.set_start_time(start)
            friday.set_end_time(end)
            friday.set_value(temp)
            liste = self.get_all_standard_weekly_temp_entries_by_weekday(5)
            entries = self.get_all_temp_standard_entries_friday()
            for elem in entries:
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                    for y in liste:
                        if y.get_friday_id() == elem.get_id():
                            self.delete_entry_in_standard_weeklyplan_temp(y)
                            self.delete_standard_entry_friday(elem)
                            print('wurden gelöscht.', elem, y)
            with FridayMapper() as mapper:
                mapper.insert(friday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_temp_standard_entry_friday()
            standard_entry.set_friday_id(last_entry.get_id())
            standard_entry.set_weekday(5)
            with WeeklyPlanTempMapper() as mapper:
                return mapper.insert(standard_entry)

    def get_all_temp_standard_entries_friday(self):
        with FridayMapper() as mapper:
            return mapper.find_all_temp_entries()

    def get_latest_temp_standard_entry_friday(self):
        with FridayMapper() as mapper:
            return mapper.find_latest_temp_entry()

    def delete_standard_entry_friday(self, entry):
        with FridayMapper() as mapper:
            mapper.delete(entry)

    def get_all_entries_standard_weekly_plan_jal(self):
        with WeeklyPlanJalMapper() as mapper:
            return mapper.find_all()

    def get_all_standard_weekly_jal_entries_by_weekday(self, weekday):
        with WeeklyPlanJalMapper() as mapper:
            return mapper.find_by_weekday(weekday)

    def get_all_standard_weekly_temp_entries_by_weekday(self, weekday):
        with WeeklyPlanTempMapper() as mapper:
            return mapper.find_by_weekday(weekday)

    def delete_entry_in_standard_weeklyplan_jal(self, entry):
        print(entry)
        with WeeklyPlanJalMapper() as mapper:
            mapper.delete(entry)

    def delete_entry_in_standard_weeklyplan_jal_byId(self, id):
        with WeeklyPlanJalMapper() as mapper:
            mapper.delete_byId(id)

    def delete_entry_in_standard_weeklyplan_temp(self, entry):
        with WeeklyPlanTempMapper() as mapper:
            mapper.delete(entry)

    '''Regel-Operationen'''

    def set_jal_rule(self, min, max, start, end):
        rule = RulesBO()
        rule.set_min(min)
        rule.set_max(max)
        rule.set_type('J')
        rule.set_start_time(start)
        rule.set_end_time(end)
        rules = self.get_all_jal_rules()
        for elem in rules:
            if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                print(elem, 'wurde gelöscht.')
                self.delete_rule(elem)
            else:
                print('nichts passiert', start, end,
                      elem.get_start_time(), elem.get_end_time())
        with RulesMapper() as mapper:
            return mapper.insert(rule)

    def delete_rule(self, rule):
        with RulesMapper() as mapper:
            mapper.delete(rule)

    def delete_jal_rules_byId(self, id_entry):
        with RulesMapper() as mapper:
            mapper.delete_jal_rules_byId(id_entry)

    def set_temp_rule(self, min, max, start, end):
        '''    def set_temp_rule(self, min, max, start, end):
            rule = RulesBO()
            rule.set_min(min)
            rule.set_max(max)
            rule.set_type('T')
            rule.set_start_time(start)
            rule.set_end_time(end)
            rules = self.get_all_temp_rules()
            for elem in rules:
                if elem.get_start_time() is None and elem.get_end_time() is None and min is None and elem.get_min()
                    
                    print(elem, 'wurde gelöscht.')
                    self.delete_rule(elem)
                else:
                    print('nichts passiert', start, end,
                          elem.get_start_time(), elem.get_end_time())
            with RulesMapper() as mapper:
                return mapper.insert(rule)'''

    def set_temp_rule_min(self, min):
        rule = RulesBO()
        rule.set_min(min)
        rule.set_type('T')
        rules = self.get_all_temp_rules()
        x = 0
        if len(rules) >= 1:
            for elem in rules:
                x += 1
                if elem.get_start_time() is None and elem.get_end_time() is None and elem.get_min() is not min and elem.get_max() is None:
                    print(elem, 'wurde gelöscht.')
                    self.delete_rule(elem)
                    with RulesMapper() as mapper:
                        mapper.insert(rule)
                        return min
                else:
                    print('nichts passiert')
                    if x == len(rules):
                        with RulesMapper() as mapper:
                            mapper.insert(rule)
                            return min
                    # return min
        else:
            with RulesMapper() as mapper:
                mapper.insert(rule)
                return min

    def set_temp_rule_max(self, max):
        rule = RulesBO()
        rule.set_max(max)
        rule.set_type('T')
        rules = self.get_all_temp_rules()
        x = 0
        if len(rules) >= 1:
            for elem in rules:
                x += 1
                if elem.get_start_time() is None and elem.get_end_time() is None and elem.get_max() is not max and elem.get_min() is None:
                    print(elem, 'wurde gelöscht.')
                    self.delete_rule(elem)
                    with RulesMapper() as mapper:
                        mapper.insert(rule)
                        return max
                else:
                    print('nichts passiert')
                    if x == len(rules):
                        with RulesMapper() as mapper:
                            mapper.insert(rule)
                            return max
                    # return max
        else:
            with RulesMapper() as mapper:
                mapper.insert(rule)
                return max

    def get_all_rules(self):
        with RulesMapper() as mapper:
            return mapper.find_all()

    def get_all_jal_rules(self):
        with RulesMapper() as mapper:
            return mapper.find_by_type('J')

    def get_all_temp_rules(self):
        with RulesMapper() as mapper:
            return mapper.find_by_type('T')

    def get_rule_by_id(self, id):
        with RulesMapper() as mapper:
            return mapper.find_by_key(id)

    def get_min_temp(self):
        rules = self.get_all_temp_rules()
        min_of_db = []
        if len(rules) > 0:
            for elem in rules:
                if elem.get_max() is None and elem.get_min() is not None and elem.get_start_time() is None:
                    min_of_db.append(elem.get_min())
            if len(min_of_db) >= 1:
                return min_of_db[0]
            else:
                return self.get_temp_from_device()
        else:
            return self.get_temp_from_device()

    def get_max_temp(self):
        rules = self.get_all_temp_rules()
        max_of_db = []
        if len(rules) > 0:
            for elem in rules:
                if elem.get_max() is not None and elem.get_min() is None and elem.get_start_time() is None:
                    max_of_db.append(elem.get_min())
            if len(max_of_db) >= 1:
                return max_of_db[0]
            else:
                return self.get_temp_from_device()
        else:
            return self.get_temp_from_device()

    def overlapping(self, new_start, new_end, old_start, old_end):
        new_start = datetime.datetime.strptime(new_start, '%H:%M:%S').hour
        new_start = float(new_start)
        new_end = datetime.datetime.strptime(new_end, '%H:%M:%S').hour
        new_end = float(new_end)
        old_start = datetime.datetime.strptime(old_start, '%H:%M:%S').hour
        old_start = float(old_start)
        old_end = datetime.datetime.strptime(old_end, '%H:%M:%S').hour
        old_end = float(old_end)
        if old_start < new_start < old_end or old_start < new_end < old_end:
            return True
        elif old_start == new_start and new_end == old_end:
            return True
        else:
            return False

    ##### Customized Entries ######

    '''def set_jal_customized_entry_monday(self, start, end, perc):
        monday = Monday()
        monday.set_type('J')
        monday.set_start_time(start)
        monday.set_end_time(end)
        monday.set_value(perc)
        with MondayMapper() as mapper:
            return mapper.insert(monday)

    def get_all_jal_customized_entries_monday(self):
        with MondayMapper() as mapper:
            return mapper.find_all()

    def set_jal_customized_entry_tuesday(self, start, end, perc):
        tuesday = Tuesday()
        tuesday.set_type('J')
        tuesday.set_start_time(start)
        tuesday.set_end_time(end)
        tuesday.set_value(perc)
        with TuesdayMapper() as mapper:
            return mapper.insert(tuesday)

    def get_all_jal_customized_entries_tuesday(self):
        with TuesdayMapper() as mapper:
            return mapper.find_all()

    def set_jal_customized_entry_wednesday(self, start, end, perc):
        wednesday = Wednesday()
        wednesday.set_type('J')
        wednesday.set_start_time(start)
        wednesday.set_end_time(end)
        wednesday.set_value(perc)
        with WednesdayMapper() as mapper:
            return mapper.insert(wednesday)

    def get_all_jal_customized_entries_wednesday(self):
        with WednesdayMapper() as mapper:
            return mapper.find_all()

    def set_jal_customized_entry_thursday(self, start, end, perc):
        thursday = Thursday()
        thursday.set_type('J')
        thursday.set_start_time(start)
        thursday.set_end_time(end)
        thursday.set_value(perc)
        with ThursdayMapper() as mapper:
            return mapper.insert(thursday)

    def get_all_jal_customized_entries_thursday(self):
        with ThursdayMapper() as mapper:
            return mapper.find_all()

    def set_jal_customized_entry_friday(self, start, end, perc):
        friday = Friday()
        friday.set_type('J')
        friday.set_start_time(start)
        friday.set_end_time(end)
        friday.set_value(perc)
        with FridayMapper() as mapper:
            return mapper.insert(friday)

    def get_all_jal_customized_entries_friday(self):
        with FridayMapper() as mapper:
            return mapper.find_all()

    def set_temp_customized_entry_monday(self, start, end, temp):
        monday = Monday()
        monday.set_type('T')
        monday.set_start_time(start)
        monday.set_end_time(end)
        monday.set_value(temp)
        with MondayMapper() as mapper:
            return mapper.insert(monday)

    def get_all_temp_customized_entries_monday(self):
        with MondayMapper() as mapper:
            return mapper.find_all()

    def set_temp_customized_entry_tuesday(self, start, end, temp):
        tuesday = Tuesday()
        tuesday.set_type('T')
        tuesday.set_start_time(start)
        tuesday.set_end_time(end)
        tuesday.set_value(temp)
        with TuesdayMapper() as mapper:
            return mapper.insert(tuesday)

    def get_all_temp_customized_entries_tuesday(self):
        with TuesdayMapper() as mapper:
            return mapper.find_all()

    def set_temp_customized_entry_wednesday(self, start, end, temp):
        wednesday = Wednesday()
        wednesday.set_type('T')
        wednesday.set_start_time(start)
        wednesday.set_end_time(end)
        wednesday.set_value(temp)
        with WednesdayMapper() as mapper:
            return mapper.insert(wednesday)

    def get_all_temp_customized_entries_wednesday(self):
        with WednesdayMapper() as mapper:
            return mapper.find_all()

    def set_temp_customized_entry_thursday(self, start, end, temp):
        thursday = Thursday()
        thursday.set_type('T')
        thursday.set_start_time(start)
        thursday.set_end_time(end)
        thursday.set_value(temp)
        with ThursdayMapper() as mapper:
            return mapper.insert(thursday)

    def get_all_temp_customized_entries_thursday(self):
        with ThursdayMapper() as mapper:
            return mapper.find_all()

    def set_temp_customized_entry_friday(self, start, end, temp):
        friday = Friday()
        friday.set_type('T')
        friday.set_start_time(start)
        friday.set_end_time(end)
        friday.set_value(temp)
        with FridayMapper() as mapper:
            return mapper.insert(friday)

    def get_all_temp_customized_entries_friday(self):
        with FridayMapper() as mapper:
            return mapper.find_all()'''


adm = DeviceAdministration()

print(adm.get_min_temp())