from server.bo.Jalousien import JalousienBO
from server.database.JalousienMapper import JalousienMapper
from server.bo.Thermostat import ThermostatBO
from server.database.ThermostatMapper import ThermostatMapper
from server.bo.JalosuienStatusBO import JalousienStatusBO
from server.database.JalousienStatusMapper import JalousienStatusMapper
from server.AuthGen import get_sid, get_login_state, send_response, calculate_md5_response
import time
import tinytuya
import http.client
from datetime import datetime


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

    def get_all_status(self):
        with JalousienStatusMapper() as mapper:
            return mapper.find_all()

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

    def open_jalousie_by_id(self, id):
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
        return status

    def set_status_to_percentage_by_id(self, id, percentage=int):
        jalousies = []
        status = JalousienStatusBO()
        status.set_percentage(percentage)
        perc = status.get_percentage()
        date = datetime.now()
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
        status = self.get_all_status()
        return status[-1].get_percentage()

    def in_between_times(self, timeframe, start, end):
        if timeframe >= start and timeframe <= end:
            return True
        else:  # over midnight e.g., 23:30-04:15
            return False

    def get_all_stats_by_timeperiod(self, start, end):
        enddate = datetime.now().fromisoformat(str(end))
        startdate = datetime.now().fromisoformat(str(start))
        stats = self.get_all_status()
        interval = []
        for elem in stats:
            if self.in_between_times(elem.get_date(), startdate, enddate) == True:
                print(elem.get_date())
                interval.append(elem)
            else:
                pass
        return interval

    def set_weekly_plan_jal(self, start, ende):
        pass

    """
    Thermostat-spezifische Methoden
    """

    def generate_sid(self, box_url, user_name, password):
        sid = get_sid(box_url, user_name, password)
        return sid

    def add_thermostat(self, ain, box_url, user_name, password):
        """Einen Kunden anlegen."""
        thermostat = ThermostatBO()
        thermostat.set_ain(ain)
        with ThermostatMapper() as mapper:
            return mapper.insert(thermostat)

    def get_thermostat_by_ain(self, ain):
        """Alle Kunden mit übergebenem Nachnamen auslesen."""
        with ThermostatMapper() as mapper:
            return mapper.find_by_ain(ain)

    def get_thermostat_by_id(self, id):
        """Alle Kunden mit übergebenem Nachnamen auslesen."""
        with ThermostatMapper() as mapper:
            return mapper.find_by_key(id)

    def get_all_thermostats(self):
        with ThermostatMapper() as mapper:
            return mapper.find_all()

    def save_thermostat(self, thermostat):
        """Den gegebenen Kunden speichern."""
        with ThermostatMapper() as mapper:
            mapper.update(thermostat)

    def delete_thermostat(self, thermostat):
        """Den gegebenen Kunden löschen."""
        with ThermostatMapper() as mapper:
            thermostat = self.get_thermostat(thermostat)
            mapper.delete(thermostat)

    def set_temperature(self, temp):
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
        print(data.decode("utf-8"))

    def get_temperature(self):
        conn = http.client.HTTPSConnection("192.168.2.254", 8254)
        payload = ''
        headers = {}
        sid = self.generate_sid(
            'https://192.168.2.254:8254/', 'admin', 'QUANTO_Solutions')
        conn.request("GET",
                     "/webservices/homeautoswitch.lua?ain=139790057201&switchcmd=gettemperature&sid={}".format(
                         sid),
                     payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
