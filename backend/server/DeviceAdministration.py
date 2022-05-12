from .bo.Jalousien import Jalousien
from .bo.Thermostat import Thermostat
#from .AuthGen import LoginState


class Device_Administration():
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
        pass
        """Einen Benutzer anlegen"""
        jalousie = Jalousien()
        jalousie.set_device_id(device_id)
        jalousie.set_ip_address(ip_address)
        jalousie.set_local_key(local_key)

#        with JalousieMapper() as mapper:
#            return mapper.insert(jalousie)

    def get_jalousie_by_device_id(self, device_id):
        pass
        """Alle Benutzer mit Namen name auslesen."""
#        with JalousieMapper() as mapper:
#            return mapper.find_by_name(name)

    def get_jalousie_by_ip_address(self, ip_address):
        pass
        """Alle Benutzer mit gegebener E-Mail-Adresse auslesen."""
#        with JalousieMapper() as mapper:
#            return mapper.find_by_ip_address(ip_address)

    def get_jalousie_by_local_key(self, local_key):
        pass
        """Den Benutzer mit der gegebenen Google ID auslesen."""
#        with JalousieMapper() as mapper:
#            return mapper.find_by_local_key(id)

    def get_all_jalousies(self):
        pass
        """Alle Benutzer auslesen."""
#        with JalousieMapper() as mapper:
#            return mapper.find_all()

    def save_jalousie(self, jalousie):
        pass
        """Den gegebenen Benutzer speichern."""
#        with JalousieMapper() as mapper:
#            mapper.update(jalousie)

    def delete_jalousie(self, jalousie):
        pass
        """Den gegebenen Benutzer aus unserem System löschen."""
#        with JalousieMapper() as mapper:
#            mapper.delete(jalousie)

    def open_jalousien(self):
        pass

    def close_jalousien(self):
        pass

    def set_to_percentage(self, percent):
        pass

    """
    Thermostat-spezifische Methoden
    """

    def add_thermostat(self, ain, port):
        """Einen Kunden anlegen."""
        thermostat = Thermostat()
        thermostat.set_ain(ain)
        thermostat.set_port(port)

#        with ThermostatMapper() as mapper:
#            return mapper.insert(thermostat)

    def get_thermostat_by_ain(self, ain):
        pass
        """Alle Kunden mit übergebenem Nachnamen auslesen."""
#        with ThermostatMapper() as mapper:
#            return mapper.find_by_port(port)

    def get_all_thermostats(self):
        pass
        """Alle Kunden auslesen."""
#        with ThermostatMapper() as mapper:
#            return mapper.find_all()

    def save_thermostat(self, thermostat):
        pass
        """Den gegebenen Kunden speichern."""
#        with ThermostatMapper() as mapper:
#            mapper.update(thermostat)

    def delete_thermostat(self, thermostat):
        pass
        """Den gegebenen Kunden löschen."""
#        with ThermostatMapper() as mapper:
#            thermostats = self.get_thermostat(thermostat)
#            mapper.delete(thermostat)

    def set_temperature(self, temp):
        pass

    def get_temperature(self):
        pass
