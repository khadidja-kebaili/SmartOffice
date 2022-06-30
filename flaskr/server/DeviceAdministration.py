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
import tinytuya


class DeviceAdministration(object):
    """
    Realisierung einer DeviceManagement-Logik für Jalousien Klasse Tuya und Thermostate Klasse Dect 301.
    """

    def __init__(self):
        pass

######## Jalousie-spezifische Methoden ########

    def add_device(self, device_id, ip_address, local_key):
        '''
        Jalousie zur Datenbank hinzufügen'
        :param device_id: 
        :param ip_address: 
        :param local_key: 
        :return: JalousieBO
        '''''
        j = JalousienBO()
        j.set_device_id(device_id)
        j.set_ip_address(ip_address)
        j.set_local_key(local_key)
        j.set_device()
        with JalousienMapper() as mapper:
            return mapper.insert(j)

    def get_jalousie_by_device_id(self, device_id):
        """
        Jalousie aus der Datenbank holen mithilfe der Device_id.
        :param device_id:
        :return: JalousieBO
        """
        with JalousienMapper() as mapper:
            return mapper.find_by_device_id(device_id)

    def get_jalousie_by_id(self, id):
        """
        Jalousie mithilfe der in der Datenbank gespeicherten ID holen
        :param id:
        :return: JalousieBO
        """
        with JalousienMapper() as mapper:
            return mapper.find_by_id(id)

    def get_jalousie_by_ip_address(self, ip_address):
        """
        Jalousie per IP-Adresse aus der Datenbank holen
        :param ip_address:
        :return: JalousieBO
        """
        with JalousienMapper() as mapper:
            return mapper.find_by_ip_address(ip_address)

    def get_jalousie_by_local_key(self, local_key):
        """
        Jalousie mithilfe des Local-Keys aus der Datenbank holen
        :param local_key:
        :return: JalousieBO
        """
        with JalousienMapper() as mapper:
            return mapper.find_by_key(local_key)

    def get_all_jalousies(self):
        """
        Alle Jalousien, die in der Datenbank gespeichert sind, auslesen."
        :return: Array (Liste) mit allen Jalousien aus der Datenbank
        """""
        with JalousienMapper() as mapper:
            return mapper.find_all()

    def save_jalousie(self, jalousie):
        """
        Eine Jalousie updaten.
        :param jalousie: JalousieBO
        """
        with JalousienMapper() as mapper:
            mapper.update(jalousie)

    def delete_jalousie(self, jalousie):
        """
        Eine Jalousie aus der Datenbank löschen.
        :param jalousie: JalousieBO
        """
        with JalousienMapper() as mapper:
            mapper.delete(jalousie)

### Jalousie Steuerungsoperationen ###

    def set_status_to_percentage_by_id(self, id, perc):
        '''
         Eine Jalousie, die in der Datenbank gespeichert ist zu einem bestimmten Prozentsatz steigern oder senken.
        Pro Steuerung wird ein Status in die Datenbank eingespeichert, für spätere Statistiken.
        :param id: id der Jalousie
        :param perc: Prozentsatz, wobei 100 ganz oben und 0 ganz unten ist
        :return: JalousienStatusBO
        '''
        date = datetime.datetime.now()
        datehour = date.strftime('%H:%M:%S')
        date2 = date.strftime('%Y-%m-%d %H:%M:%S')
        trigger = False
        rules = self.get_all_jal_rules()
        for elem in rules:
            # if elem.get_min() is None and elem.get_max() is None:
            #   if self.in_between_times(date, elem.get_start_time(), elem.get_end_time()):
            #      message = 'Die No_Access Zeit ist eingetroffen'
            #     print(message)
            #    return message
            if elem.get_min() is not None and elem.get_max() is not None and self.in_between_times(datehour, elem.get_start_time(), elem.get_end_time()) is True:
                if perc > elem.get_max() or perc < elem.get_min():
                    message = 'Das geht so nicht!', perc, 'Mindesttemp:', elem.get_min(
                    ), 'Maxtemp:', elem.get_max()
                    print(message)
                    mindest_jal = elem.get_min()
                    maximal_jal = elem.get_max()
                    return {"type": "0", "min": mindest_jal, "max": maximal_jal}
                else:
                    trigger = True
            else:
                trigger = True
        trigger = True
        if trigger:
            jalousies = []
            status = JalousienStatusBO()
            status.set_percentage(perc)
            perc = status.get_percentage()
            status.set_date(date2)
            jalousies.append(self.get_all_jalousies())
            for elem in jalousies:
                for x in elem:
                    if x.get_id() == id:
                        loc_key = x.get_local_key()
                        ip = x.get_ip_address()
                        dev_id = x.get_device_id()
                        print(loc_key, ip, dev_id)
                        dev = tinytuya.OutletDevice(
                            dev_id=dev_id, address=ip, local_key=loc_key)
                        dev.set_version(3.3)
                        dev.set_value(2, perc)
                        status.set_status(str(dev.status()))
                        status.set_device(id)
            with JalousienStatusMapper() as mapper:
                return mapper.insert(status)

### Jalousien Status-Operationen ###

    def get_status_of_jalousie_by_id(self, id):
        '''
        Status einer Jalousie mithilfe der Status-Id aus der Datenbank laden.
        :param id: StatusId
        :return: JalousienStatusBO
        '''
        with JalousienStatusMapper() as mapper:
            return mapper.find_by_key(id)

    def delete_status_by_id(self, id):
        '''
        Status einer Jalousie mithilfe der Status-Id aus der Datenbank löschen.
        :param id: StatusId
        '''
        status = self.get_status_of_jalousie_by_id(id)
        with JalousienStatusMapper() as mapper:
            mapper.delete(status)

    def get_last_jal_status(self):
        '''
        Letzten Status einer Jalousie aus der Datenbank laden.
        :return: letzter Listeneintrag
        '''
        status = self.get_all_jal_status()
        return status[-1]

    def get_all_jal_status(self):
        '''
        Alle Jalousienstatuse zurückbekommen
        :return: Array (Liste) mit allen Statusen
        '''
        with JalousienStatusMapper() as mapper:
            return mapper.find_all()

    def get_last_jal_ist_entry_of_hour_for_day(self, day, hour):
        '''
        Gibt für eine angegebene Stunde eines angegebenen Tages den letzten Ist-Wert zurück.
        Beispielsweise: 26.06.2022 16 Uhr letzter ISt-Wert der Jalousie beträgt 70.
        :param day: gesuchter Tag
        :param hour: gesuchte Stunde eines Tages
        :return: Prozentsatz des Jalousienstand
        '''
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
            return_value = 0
            for elem in hourly_rate:
                if elem > return_value:
                    return_value = elem
            return return_value
        else:
            return 0

    def get_last_soll_jal_entry_of_hour_for_day(self, day, hour):
        '''
        Gibt für eine angegebene Stunde eines angegebenen Tages den letzten Soll-Celsius-Wert zurück.
        Beispielsweise: 26.06.2022 16 Uhr letzter SOLL-Wert des Thermostats beträgt 22.
        :param day: gesuchter Tag
        :param hour: gesuchte Stunde eines Tages
        :return: Soll-Temperatur
        '''
        stats_for_weekday = []
        hourly_rate = []
        weekday = datetime.datetime.strptime(day, '%Y-%m-%d').isoweekday()
        if weekday == 1:
            a = self.get_all_jal_standard_entries_monday()
            for elem in a:
                stats_for_weekday.append(elem)
        if weekday == 2:
            b = self.get_all_jal_standard_entries_tuesday()
            for elem in b:
                stats_for_weekday.append(elem)
        if weekday == 3:
            c = self.get_all_jal_standard_entries_wednesday()
            for elem in c:
                stats_for_weekday.append(elem)
        if weekday == 4:
            d = self.get_all_jal_standard_entries_thursday()
            for elem in d:
                stats_for_weekday.append(elem)
        if weekday == 5:
            e = self.get_all_jal_standard_entries_friday()
            for elem in e:
                stats_for_weekday.append(elem)
        for elem in stats_for_weekday:
            start_hour = datetime.datetime.strptime(
                elem.get_start_time(), '%H:%M:%S').hour
            if start_hour == hour:
                hourly_rate.append(elem.get_value())
        if len(hourly_rate) >= 1:

            return hourly_rate[-1]
        else:
            return 0

    def get_last_ist_temp_entry_of_hour_for_day(self, day, hour):
        """
        Gibt für eine angegebene Stunde eines angegebenen Tages den letzten Ist-Celsius-Wert zurück.
        Beispielsweise: 26.06.2022 16 Uhr letzter ISt-Wert des Thermostats beträgt 22.
        :param day: gesuchter Tag
        :param hour: gesuchte Stunde eines Tages
        :return: Ist-Temperatur
        """
        all_temp_stats = self.get_all_thermostat_status()
        stats_for_weekday = []
        hourly_rate = []
        for elem in all_temp_stats:
            vergleich = elem.get_date().strftime('%Y-%m-%d')
            if vergleich == day:
                stats_for_weekday.append(elem)
        for elem in stats_for_weekday:
            if elem.get_date().hour == hour:
                hourly_rate.append(elem.get_temp())
        if len(hourly_rate) >= 1:
            return hourly_rate[-1]
        else:
            return 0

    def get_last_soll_temp_entry_of_hour_for_day(self, day, hour):
        '''
        Gibt für eine angegebene Stunde eines angegebenen Tages den letzten Soll-Celsius-Wert zurück.
        Beispielsweise: 26.06.2022 16 Uhr letzter SOLL-Wert des Thermostats beträgt 22.
        :param day: gesuchter Tag
        :param hour: gesuchte Stunde eines Tages
        :return: Soll-Temperatur
        '''
        stats_for_weekday = []
        hourly_rate = []
        weekday = datetime.datetime.strptime(day, '%Y-%m-%d').isoweekday()
        if weekday == 1:
            a = self.get_all_temp_standard_entries_monday()
            for elem in a:
                stats_for_weekday.append(elem)
        if weekday == 2:
            b = self.get_all_temp_standard_entries_tuesday()
            for elem in b:
                stats_for_weekday.append(elem)
        if weekday == 3:
            c = self.get_all_temp_standard_entries_wednesday()
            for elem in c:
                stats_for_weekday.append(elem)
        if weekday == 4:
            d = self.get_all_temp_standard_entries_thursday()
            for elem in d:
                stats_for_weekday.append(elem)
        if weekday == 5:
            e = self.get_all_temp_standard_entries_friday()
            for elem in e:
                stats_for_weekday.append(elem)
        for elem in stats_for_weekday:
            start_hour = datetime.datetime.strptime(
                elem.get_start_time(), '%H:%M:%S').hour
            if start_hour == hour:
                hourly_rate.append(elem.get_value())
        if len(hourly_rate) >= 1:

            return hourly_rate[-1]
        else:
            return 0

    '''    def get_jal_mean_per_day(self, day):
            result = []
            i = 6
            while i <= 20:
                x = self.get_last_jal_ist_entry_of_hour_for_day(day, i)
                result.append(x)
                i += 1
            return statistics.mean(result)
    
        def get_temp_mean_per_day(self, day):
            result = []
            i = 6
            while i <= 20:
                x = self.get_last_ist_temp_entry_of_hour_for_day(day, i)
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
    
        def get_temp_median_per_week(self, week):
            liste = self.get_all_thermostat_status()
            stats_for_week = []
            weekly_stats = []
            for elem in liste:
                if elem.get_date().isocalendar()[1] == week:
                    stats_for_week.append(elem)
            for elem in stats_for_week:
                elem_week = elem.get_date().isocalendar()[1]
                day = elem.get_date().strftime('%Y-%m-%d')
                if elem_week == week:
                    x = self.get_temp_mean_per_day(day)
                    weekly_stats.append(x)
            if len(weekly_stats) > 1:
                return statistics.median(weekly_stats)
            elif len(weekly_stats) == 1:
                return weekly_stats[0]
            else:
                return 0'''

    def get_ist_value_jal_for_timespan(self, von, bis, day):
        values = []
        for elem in range(von, bis + 1):
            x = self.get_last_jal_ist_entry_of_hour_for_day(day, elem)
            values.append(x)
        return values

    def get_soll_value_jal_for_timespan(self, von, bis, day):
        """
          Gibt pro Stunde einer angegebenen Zeitspanne (bspw. 14 -18 Uhr) den letzten Soll-Wert zurück
          :param von: Ab wann soll Zeitspanne beginnen
          :param bis: Wann endet Zeitspanne
          :param day: Von welchem Tag soll berechnet werden
          :return: Soll-Werte für angegebene Zeitspanne
        """
        values = []
        for elem in range(von, bis + 1):
            x = self.get_last_soll_jal_entry_of_hour_for_day(day, elem)
            values.append(x)
        return values

    def get_ist_temp_for_timespan(self, von, bis, day):
        """
          Gibt pro Stunde einer angegebenen Zeitspanne (bspw. 14 -18 Uhr) die letzte Ist-Temperatur zurück
          :param von: Ab wann soll Zeitspanne beginnen
          :param bis: Wann endet Zeitspanne
          :param day: Von welchem Tag soll berechnet werden
          :return: Ist-Temperatur für angegebene Zeitspanne
          """
        values = []
        for elem in range(von, bis + 1):
            x = self.get_last_ist_temp_entry_of_hour_for_day(day, elem)
            values.append(x)
        return values

    def get_soll_temp_for_timespan(self, von, bis, day):
        """
          Gibt pro Stunde einer angegebenen Zeitspanne (bspw. 14 -18 Uhr) die letzte Soll-Temperatur zurück
          :param von: Ab wann soll Zeitspanne beginnen
          :param bis: Wann endet Zeitspanne
          :param day: Von welchem Tag soll berechnet werden
          :return: Soll-Temperatur für angegebene Zeitspanne
          """
        values = []
        for elem in range(von, bis + 1):
            x = self.get_last_soll_temp_entry_of_hour_for_day(day, elem)
            values.append(x)
        return values

    def get_ist_values_jal(self, day):
        values = []
        k = self.get_ist_value_jal_for_timespan(7, 10, day)
        return_value_k = 0
        for elem in k:
            print(elem)
            if elem > return_value_k:
                return_value_k = elem
        values.append(return_value_k)
        m = self.get_ist_value_jal_for_timespan(10, 13, day)
        return_value_m = 0
        for elem in m:
            print(elem)
            if elem > return_value_m:
                return_value_m = elem
        values.append(return_value_m)
        n = self.get_ist_value_jal_for_timespan(13, 16, day)
        return_value_n = 0
        for elem in n:
            if elem > return_value_n:
                return_value_n = elem
        values.append(return_value_n)
        l = self.get_ist_value_jal_for_timespan(16, 19, day)
        return_value_l = 0
        for elem in l:
            if elem > return_value_l:
                return_value_l = elem
        values.append(return_value_l)
        return values

    def get_median_soll_values_jal(self, day):
        """
        Gibt für jeweils die Zeitspannen 7-10 Uhr, 10-13 Uhr, 13-16 Uhr und 16-19 Uhr die letzten Soll-Werte der
        Jalousien-Statuse an.
        :param day: Tag, welcher angezeigt werden soll
        :return: 4 Soll-Werte von gegebenen Tag
        """
        values = []
        k = self.get_soll_value_jal_for_timespan(7, 10, day)
        return_value_k = 0
        for elem in k:
            if elem > return_value_k:
                return_value_k = elem
        values.append(return_value_k)
        m = self.get_soll_value_jal_for_timespan(10, 13, day)
        return_value_m = 0
        for elem in m:
            if elem > return_value_m:
                return_value_m = elem
        values.append(return_value_m)
        n = self.get_soll_value_jal_for_timespan(13, 16, day)
        return_value_n = 0
        for elem in n:
            if elem > return_value_n:
                return_value_n = elem
        values.append(return_value_n)
        l = self.get_soll_value_jal_for_timespan(16, 19, day)
        return_value_l = 0
        for elem in l:
            if elem > return_value_l:
                return_value_l = elem
        values.append(return_value_l)
        return values

    def get_median_ist_values_temp(self, day):
        """
        Gibt für jeweils die Zeitspannen 7-10 Uhr, 10-13 Uhr, 13-16 Uhr und 16-19 Uhr die letzten Ist-Temperaturen der
        Thermostat-Statuse an.
        :param day: Tag, welcher angezeigt werden soll
        :return: 4 Ist-Temperatur von gegebenen Tag
        """
        values = []
        k = self.get_ist_temp_for_timespan(7, 10, day)
        return_value_k = 0
        for elem in k:
            print(elem)
            if elem > return_value_k:
                return_value_k = elem
        values.append(return_value_k)
        m = self.get_ist_temp_for_timespan(10, 13, day)
        return_value_m = 0
        for elem in m:
            print(elem)
            if elem > return_value_m:
                return_value_m = elem
        values.append(return_value_m)
        n = self.get_ist_temp_for_timespan(13, 16, day)
        return_value_n = 0
        for elem in n:
            if elem > return_value_n:
                return_value_n = elem
        values.append(return_value_n)
        l = self.get_ist_temp_for_timespan(16, 19, day)
        return_value_l = 0
        for elem in l:
            if elem > return_value_l:
                return_value_l = elem
        values.append(return_value_l)
        return values

    def get_median_soll_values_temp(self, day):
        """
        Gibt für jeweils die Zeitspannen 7-10 Uhr, 10-13 Uhr, 13-16 Uhr und 16-19 Uhr die letzten Soll-Temperaturen der
        Thermostat-Statuse an.
        :param day: Tag, welcher angezeigt werden soll
        :return: 4 Soll-Temperatur von gegebenen Tag
        """
        values = []
        k = self.get_soll_temp_for_timespan(7, 10, day)
        return_value_k = 0
        for elem in k:
            if elem > return_value_k:
                return_value_k = elem
        values.append(return_value_k)
        m = self.get_soll_temp_for_timespan(10, 13, day)
        return_value_m = 0
        for elem in m:
            if elem > return_value_m:
                return_value_m = elem
        values.append(return_value_m)
        n = self.get_soll_temp_for_timespan(13, 16, day)
        return_value_n = 0
        for elem in n:
            if elem > return_value_n:
                return_value_n = elem
        values.append(return_value_n)
        l = self.get_soll_temp_for_timespan(16, 19, day)
        return_value_l = 0
        for elem in l:
            if elem > return_value_l:
                return_value_l = elem
        values.append(return_value_l)
        return values

    def in_between_times(self, searched_time, start, end):
        """
        Hilfsfunktion.
        Checkt ob sich eine gesuchte Zeit innerhalb einer Zeitspanne befinden.
        :param searched_time: Zeit, die gesucht wird
        :param start: Beginn Zeitspanne
        :param end: Ende der Zeitspanne
        :return: Boolean Wert, True wenn es sich in der Zeitspanne befindet, False wenn nicht.
        """
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

    def get_all_jal_stats_by_timeperiod(self, start, end):
        """
        Alle Jalousienstatuse innerhalb einer bestimmten Zeitspanne
        :param start: Beginn Zeitspanne
        :param end: Ende Zeitspanne
        :return: Liste von JalousienStatusBOs
        """
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

    def get_last_temp_status(self):
        '''

        :return:
        '''
        status = self.get_all_thermostat_status()
        return status[-1]

    def delete_thermostat_status_by_id(self, id):
        status = self.get_status_of_thermostat_by_id(id)
        with ThermostatStatusMapper() as mapper:
            mapper.delete(status)

    def get_last_thermostat_status(self):
        status = self.get_all_thermostat_status()
        return status[-1]

    def get_all_thermostat_status(self):
        with ThermostatStatusMapper() as mapper:
            return mapper.find_all()


########Thermostat-spezifische Methoden########

    def generate_sid(self, box_url, user_name, password):
        sid = get_sid(box_url, user_name, password)
        return sid

    def add_thermostat(self, ain):
        """
        Thermostat hinzufügen und in die Datenbank laden
        :param ain: AIN des Geräts
        :return: ThermostatBO
        """
        thermostat = ThermostatBO()
        thermostat.set_ain(ain)
        with ThermostatMapper() as mapper:
            return mapper.insert(thermostat)

    def get_thermostat_by_ain(self, ain):
        """
        Thermostat mithilfe der AIN aus der Datenbank laden.
        :param ain: AIN des Thermostats
        :return: ThermostatBO
        """
        with ThermostatMapper() as mapper:
            return mapper.find_by_ain(ain)

    def get_thermostat_by_id(self, id):
        """
        Thermostat mithilfe der Datenbank-ID aus der Datenbank laden
        :param id: ID des Thermostats
        :return: ThermostatBO
        """
        with ThermostatMapper() as mapper:
            return mapper.find_by_key(id)

    def get_all_thermostats(self):
        """
        Alle Thermostate aus der Datenbank laden
        :return: Array (Liste) von Thermostaten
        """
        with ThermostatMapper() as mapper:
            return mapper.find_all()

    def save_thermostat(self, thermostat):
        """
        Thermostat updaten
        :param thermostat: ThermostatBO
        """
        with ThermostatMapper() as mapper:
            mapper.update(thermostat)

### Thermostat Steuerungsoperationen ###

    def set_temperature(self, temp, device_id=1):
        """
        Setzen der Temperatur an einem bestimmten Thermostat. Für jede Verwendung wird automatisch ein neuer Eintrag
        im Thermostat-Status hinzugefügt.
        :param temp: einzustellende Temperatur
        :param device_id: Datenbank-ID des Thermostats
        :return: ThermostatStatusBO
        """
        date = datetime.datetime.now()
        date_for_stat = date.strftime('%Y-%m-%d %H:%M:%S')
        date = date.strftime('%H:%M:%S')
        trigger = False
        rules = self.get_all_temp_rules()
        min = False
        max = False
        if len(rules) == 0:
            trigger = True
        for elem in rules:
            if elem.get_min() is None and elem.get_max() is None:
                if self.in_between_times(date, elem.get_start_time(), elem.get_end_time()):
                    message = 'Die No_Access Zeit ist eingetroffen'
                    return message
            elif elem.get_min() is None:
                if temp > elem.get_max():
                    mindest_temp = elem.get_min()
                    maximal_temp = elem.get_max()
                    return {"type": "0", "max": maximal_temp}
                else:
                    max = True
            elif elem.get_max() is None:
                if temp < elem.get_min():
                    mindest_temp = elem.get_min()
                    maximal_temp = elem.get_max()
                    return {"type": "1", "min": mindest_temp}
                else:
                    min = True
            elif elem.get_max() is None and elem.get_min() is None:
                trigger = True
            if trigger or (min and max):
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
        """
        Komfort-Temperatur des Geräts auslesen
        :return: Temperatur in Celcius
        """
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
        """
        Ist-Temperatur aus dem Gerät laden
        :return: Ist-Temperatur in Celcius
        """
        conn = http.client.HTTPSConnection("192.168.2.254", 8254)
        payload = ''
        sid = self.generate_sid(
            'https://192.168.2.254:8254/', 'admin', 'QUANTO_Solutions')
        headers = {
            'Content-Type': 'application/json'
        }
        conn.request("GET",
                     "/webservices/homeautoswitch.lua?sid={}&ain=139790057201&switchcmd=gettemperature".format(
                         sid),
                     payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        return data

    def get_soll_temp(self):
        date = datetime.datetime.now()
        weekday = date.isoweekday()
        if weekday == 1:
            mon = self.get_latest_temp_standard_entry_monday()
            if mon is None or mon == 0:
                return self.get_min_temp()
            else:
                return mon.get_value()
        if weekday == 2:
            tue = self.get_latest_temp_standard_entry_tuesday()
            if tue == None or tue == 0:
                return self.get_min_temp()
            else:
                return tue.get_value()
        if weekday == 3:
            wed = self.get_latest_temp_standard_entry_wednesday()
            if wed == None or wed == 0:
                return self.get_min_temp()
            else:
                return wed.get_value()
        if weekday == 4:
            thurs = self.get_latest_temp_standard_entry_thursday()
            if thurs == None or thurs == 0:
                return self.self.get_min_temp()
            else:
                return thurs.get_value()
        if weekday == 5:
            fri = self.get_latest_temp_standard_entry_friday()
            if fri == None or fri == 0:
                return self.get_min_temp()
            else:
                return fri.get_value()

    def set_min_temp_of_device(self, temp):
        conn = http.client.HTTPSConnection("192.168.2.254", 8254)
        payload = ''
        sid = self.generate_sid(
            'https://192.168.2.254:8254/', 'admin', 'QUANTO_Solutions')
        headers = {
            'Content-Type': 'application/json'
        }
        conn.request("POST",
                     "/webservices/homeautoswitch.lua?sid={}&ain=139790057201&switchcmd=sethkrtsoll&param={}".format(
                         sid, temp),
                     payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        return data

######## Standardwochenplan Operationen ########

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
                    mindest_jal = elem.get_min()
                    maximal_jal = elem.get_max()
                    return {"type": "0", "min": mindest_jal, "max": maximal_jal}
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
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()) is True:
                    for y in liste:
                        if y.get_monday_id() == elem.get_id():
                            self.delete_entry_in_standard_weeklyplan_jal(y)
                            self.delete_standard_entry_monday(elem)
                            print(elem, 'wurde gelöscht.')
                            elem_id = elem.get_id()
                            start = elem.get_start_time()
                            end = elem.get_end_time()
                            with MondayMapper() as mapper:
                                mapper.insert(monday)
                            standard_entry = WeeklyPlanTempBO()
                            last_entry = self.get_latest_jal_standard_entry_monday()
                            standard_entry.set_monday_id(last_entry.get_id())
                            standard_entry.set_weekday(1)
                            with WeeklyPlanJalMapper() as mapper:
                                mapper.insert(standard_entry)
                            return {"type": "1", "element": elem_id, "start": start, "end": end}
            with MondayMapper() as mapper:
                mapper.insert(monday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_jal_standard_entry_monday()
            standard_entry.set_monday_id(last_entry.get_id())
            standard_entry.set_weekday(1)
            with WeeklyPlanJalMapper() as mapper:
                mapper.insert(standard_entry)

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
            if elem.get_min() is not None and elem.get_max() is not None and self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()) is True:
                if perc > elem.get_max() or perc < elem.get_min():
                    message = 'Das geht so nicht!', perc, 'Mindesttemp:', elem.get_min(
                    ), 'Maxtemp:', elem.get_max()
                    print(message)
                    mindest_jal = elem.get_min()
                    maximal_jal = elem.get_max()
                    return {"type": "0", "min": mindest_jal, "max": maximal_jal}
                else:
                    trigger = True
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
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()) is True:
                    for y in liste:
                        if y.get_tuesday_id() == elem.get_id():
                            self.delete_entry_in_standard_weeklyplan_jal(y)
                            self.delete_standard_entry_tuesday(elem)
                            print(elem, 'wurde gelöscht.')
                            elem_id = elem.get_id()
                            start = elem.get_start_time()
                            end = elem.get_end_time()
                            with TuesdayMapper() as mapper:
                                mapper.insert(tuesday)
                            standard_entry = WeeklyPlanTempBO()
                            last_entry = self.get_latest_jal_standard_entry_tuesday()
                            standard_entry.set_tuesday_id(last_entry.get_id())
                            standard_entry.set_weekday(2)
                            with WeeklyPlanJalMapper() as mapper:
                                mapper.insert(standard_entry)
                            return {"type": "1", "element": elem_id, "start": start, "end": end}

            with TuesdayMapper() as mapper:
                mapper.insert(tuesday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_jal_standard_entry_tuesday()
            standard_entry.set_tuesday_id(last_entry.get_id())
            standard_entry.set_weekday(2)
            with WeeklyPlanJalMapper() as mapper:
                mapper.insert(standard_entry)

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
            if elem.get_min() is not None and elem.get_max() is not None and self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()) is True:
                if perc > elem.get_max() or perc < elem.get_min():
                    message = 'Das geht so nicht!', perc, 'Mindesttemp:', elem.get_min(
                    ), 'Maxtemp:', elem.get_max()
                    print(message)
                    mindest_jal = elem.get_min()
                    maximal_jal = elem.get_max()
                    return {"type": "0", "min": mindest_jal, "max": maximal_jal}
                else:
                    trigger = True
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
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()) is True:
                    for y in liste:
                        if y.get_wednesday_id() == elem.get_id():
                            self.delete_entry_in_standard_weeklyplan_jal(y)
                            self.delete_standard_entry_wednesday(elem)
                            print(elem, 'wurde gelöscht.')
                            elem_id = elem.get_id()
                            start = elem.get_start_time()
                            end = elem.get_end_time()
                            with WednesdayMapper() as mapper:
                                mapper.insert(wednesday)
                            standard_entry = WeeklyPlanTempBO()
                            last_entry = self.get_latest_jal_standard_entry_wednesday()
                            standard_entry.set_wednesday_id(
                                last_entry.get_id())
                            standard_entry.set_weekday(3)
                            with WeeklyPlanJalMapper() as mapper:
                                mapper.insert(standard_entry)
                            return {"type": "1", "element": elem_id, "start": start, "end": end}

            with WednesdayMapper() as mapper:
                mapper.insert(wednesday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_jal_standard_entry_wednesday()
            standard_entry.set_wednesday_id(last_entry.get_id())
            standard_entry.set_weekday(3)
            with WeeklyPlanJalMapper() as mapper:
                mapper.insert(standard_entry)

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
            if elem.get_min() is not None and elem.get_max() is not None and self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()) is True:
                if perc > elem.get_max() or perc < elem.get_min():
                    message = 'Das geht so nicht!', perc, 'Mindesttemp:', elem.get_min(
                    ), 'Maxtemp:', elem.get_max()
                    print(message)
                    mindest_jal = elem.get_min()
                    maximal_jal = elem.get_max()
                    return {"type": "0", "min": mindest_jal, "max": maximal_jal}
                else:
                    trigger = True
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
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()) is True:
                    for y in liste:
                        if y.get_thursday_id() == elem.get_id():
                            self.delete_entry_in_standard_weeklyplan_jal(y)
                            self.delete_standard_entry_thursday(elem)
                            print(elem, 'wurde gelöscht.')
                            elem_id = elem.get_id()
                            start = elem.get_start_time()
                            end = elem.get_end_time()
                            with ThursdayMapper() as mapper:
                                mapper.insert(thursday)
                            standard_entry = WeeklyPlanTempBO()
                            last_entry = self.get_latest_jal_standard_entry_thursday()
                            standard_entry.set_thursday_id(last_entry.get_id())
                            standard_entry.set_weekday(4)
                            with WeeklyPlanJalMapper() as mapper:
                                mapper.insert(standard_entry)
                            return {"type": "1", "element": elem_id, "start": start, "end": end}

            with ThursdayMapper() as mapper:
                mapper.insert(thursday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_jal_standard_entry_thursday()
            standard_entry.set_thursday_id(last_entry.get_id())
            standard_entry.set_weekday(4)
            with WeeklyPlanJalMapper() as mapper:
                mapper.insert(standard_entry)

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
            if elem.get_min() is not None and elem.get_max() is not None and self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()) is True:
                if perc > elem.get_max() or perc < elem.get_min():
                    message = 'Das geht so nicht!', perc, 'Mindesttemp:', elem.get_min(
                    ), 'Maxtemp:', elem.get_max()
                    print(message)
                    mindest_jal = elem.get_min()
                    maximal_jal = elem.get_max()
                    return {"type": "0", "min": mindest_jal, "max": maximal_jal}
                else:
                    trigger = True
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
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()) is True:
                    for y in liste:
                        if y.get_friday_id() == elem.get_id():
                            self.delete_entry_in_standard_weeklyplan_jal(y)
                            self.delete_standard_entry_friday(elem)
                            print(elem, 'wurde gelöscht.')
                            elem_id = elem.get_id()
                            start = elem.get_start_time()
                            end = elem.get_end_time()

                            with FridayMapper() as mapper:
                                mapper.insert(friday)
                            standard_entry = WeeklyPlanTempBO()
                            last_entry = self.get_latest_jal_standard_entry_friday()
                            standard_entry.set_friday_id(last_entry.get_id())
                            standard_entry.set_weekday(5)
                            with WeeklyPlanJalMapper() as mapper:
                                mapper.insert(standard_entry)
                            return {"type": "1", "element": elem_id, "start": start, "end": end}

            with FridayMapper() as mapper:
                mapper.insert(friday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_jal_standard_entry_friday()
            standard_entry.set_friday_id(last_entry.get_id())
            standard_entry.set_weekday(5)
            with WeeklyPlanJalMapper() as mapper:
                mapper.insert(standard_entry)

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
            if elem.get_min() is not None and elem.get_max() is not None and self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()) is True:
                if temp > elem.get_max() or temp < elem.get_min():
                    message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(
                    ), 'Maxtemp:', elem.get_max()
                    print(message)
                    mindest_temp = elem.get_min()
                    maximal_temp = elem.get_max()
                    return {"type": "0", "min": mindest_temp, "max": maximal_temp}
                else:
                    trigger = True
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
                            elem_id = elem.get_id()
                            start = elem.get_start_time()
                            end = elem.get_end_time()
                            with MondayMapper() as mapper:
                                mapper.insert(monday)
                            standard_entry = WeeklyPlanTempBO()
                            last_entry = self.get_latest_temp_standard_entry_monday()
                            standard_entry.set_monday_id(last_entry.get_id())
                            standard_entry.set_weekday(1)
                            with WeeklyPlanTempMapper() as mapper:
                                mapper.insert(standard_entry)
                            return {"type": "1", "element": elem_id, "start": start, "end": end}

            with MondayMapper() as mapper:
                mapper.insert(monday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_temp_standard_entry_monday()
            standard_entry.set_monday_id(last_entry.get_id())
            standard_entry.set_weekday(1)
            with WeeklyPlanTempMapper() as mapper:
                mapper.insert(standard_entry)

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
            if elem.get_min() is not None and elem.get_max() is not None and self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()) is True:
                if temp > elem.get_max() or temp < elem.get_min():
                    message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(
                    ), 'Maxtemp:', elem.get_max()
                    print(message)
                    mindest_temp = elem.get_min()
                    maximal_temp = elem.get_max()
                    return {"type": "0", "min": mindest_temp, "max": maximal_temp}
                else:
                    trigger = True
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
                            elem_id = elem.get_id()
                            start = elem.get_start_time()
                            end = elem.get_end_time()
                            with TuesdayMapper() as mapper:
                                mapper.insert(tuesday)
                            standard_entry = WeeklyPlanTempBO()
                            last_entry = self.get_latest_temp_standard_entry_tuesday()
                            standard_entry.set_tuesday_id(last_entry.get_id())
                            standard_entry.set_weekday(2)
                            with WeeklyPlanTempMapper() as mapper:
                                mapper.insert(standard_entry)
                            return {"type": "1", "element": elem_id, "start": start, "end": end}

            with TuesdayMapper() as mapper:
                mapper.insert(tuesday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_temp_standard_entry_tuesday()
            standard_entry.set_tuesday_id(last_entry.get_id())
            standard_entry.set_weekday(2)
            with WeeklyPlanTempMapper() as mapper:
                mapper.insert(standard_entry)

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
            if elem.get_min() is not None and elem.get_max() is not None and self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()) is True:
                if temp > elem.get_max() or temp < elem.get_min():
                    message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(
                    ), 'Maxtemp:', elem.get_max()
                    print(message)
                    mindest_temp = elem.get_min()
                    maximal_temp = elem.get_max()
                    return {"type": "0", "min": mindest_temp, "max": maximal_temp}
                else:
                    trigger = True
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
                if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()) is True:
                    for y in liste:
                        if y.get_wednesday_id() == elem.get_id():
                            self.delete_entry_in_standard_weeklyplan_temp(y)
                            self.delete_standard_entry_wednesday(elem)
                            print(elem, 'wurde gelöscht.')
                            elem_id = elem.get_id()
                            start = elem.get_start_time()
                            end = elem.get_end_time()
                            with WednesdayMapper() as mapper:
                                mapper.insert(wednesday)
                            standard_entry = WeeklyPlanTempBO()
                            last_entry = self.get_latest_temp_standard_entry_wednesday()
                            standard_entry.set_wednesday_id(
                                last_entry.get_id())
                            standard_entry.set_weekday(3)
                            with WeeklyPlanTempMapper() as mapper:
                                mapper.insert(standard_entry)
                            return {"type": "1", "element": elem_id, "start": start, "end": end}
            with WednesdayMapper() as mapper:
                mapper.insert(wednesday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_temp_standard_entry_wednesday()
            standard_entry.set_wednesday_id(last_entry.get_id())
            standard_entry.set_weekday(3)
            with WeeklyPlanTempMapper() as mapper:
                mapper.insert(standard_entry)

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
            if elem.get_min() is not None and elem.get_max() is not None and self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()) is True:
                if temp > elem.get_max() or temp < elem.get_min():
                    message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(
                    ), 'Maxtemp:', elem.get_max()
                    print(message)
                    mindest_temp = elem.get_min()
                    maximal_temp = elem.get_max()
                    return {"type": "0", "min": mindest_temp, "max": maximal_temp}
                else:
                    trigger = True
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
                            elem_id = elem.get_id()
                            start = elem.get_start_time()
                            end = elem.get_end_time()
                            with ThursdayMapper() as mapper:
                                mapper.insert(thursday)
                            standard_entry = WeeklyPlanTempBO()
                            last_entry = self.get_latest_temp_standard_entry_thursday()
                            standard_entry.set_thursday_id(last_entry.get_id())
                            standard_entry.set_weekday(4)
                            with WeeklyPlanTempMapper() as mapper:
                                mapper.insert(standard_entry)
                            return {"type": "1", "element": elem_id, "start": start, "end": end}

            with ThursdayMapper() as mapper:
                mapper.insert(thursday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_temp_standard_entry_thursday()
            standard_entry.set_thursday_id(last_entry.get_id())
            standard_entry.set_weekday(4)
            with WeeklyPlanTempMapper() as mapper:
                mapper.insert(standard_entry)

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
            if elem.get_min() is not None and elem.get_max() is not None and self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()) is True:
                if temp > elem.get_max() or temp < elem.get_min():
                    message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(
                    ), 'Maxtemp:', elem.get_max()
                    print(message)
                    mindest_temp = elem.get_min()
                    maximal_temp = elem.get_max()
                    return {"type": "0", "min": mindest_temp, "max": maximal_temp}
                else:
                    trigger = True
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
                            elem_id = elem.get_id()
                            start = elem.get_start_time()
                            end = elem.get_end_time()
                            with FridayMapper() as mapper:
                                mapper.insert(friday)
                            standard_entry = WeeklyPlanTempBO()
                            last_entry = self.get_latest_temp_standard_entry_friday()
                            standard_entry.set_friday_id(last_entry.get_id())
                            standard_entry.set_weekday(5)
                            with WeeklyPlanTempMapper() as mapper:
                                mapper.insert(standard_entry)
                            return {"type": "1", "element": elem_id, "start": start, "end": end}

            with FridayMapper() as mapper:
                mapper.insert(friday)
            standard_entry = WeeklyPlanTempBO()
            last_entry = self.get_latest_temp_standard_entry_friday()
            standard_entry.set_friday_id(last_entry.get_id())
            standard_entry.set_weekday(5)
            with WeeklyPlanTempMapper() as mapper:
                mapper.insert(standard_entry)

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
            if self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()) is True:
                print(elem, 'wurde gelöscht.')
                self.delete_rule(elem)
                elem_id = elem.get_id()
                start = elem.get_start_time()
                end = elem.get_end_time()
                with RulesMapper() as mapper:
                    mapper.insert(rule)
                return {"type": "0", "element": elem_id, "start": start, "end": end}
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
                    max_of_db.append(elem.get_max())
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