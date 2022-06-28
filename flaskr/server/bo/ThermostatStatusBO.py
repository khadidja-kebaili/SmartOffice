from flaskr.server.bo.BusinessObject import Businessobject as bo


class ThermostatStatusBO(bo):
    """
    Klasse für Thermostat
    """

    def __init__(self):
        super().__init__()
        self._device_id = None
        self._status = ''
        self._temp = None
        self._date = None

    def set_temp(self, temp):
        self._temp = temp

    def get_temp(self):
        return self._temp

    def set_status(self, status):
        self._status = status

    def get_status(self):
        return self._status

    def get_device(self):
        return self._device_id

    def set_device(self, id):
        self._device_id = id

    def set_date(self, date):
        self._date = date

    def get_date(self):
        return self._date

    def __str__(self):
        """Erzeugen einer einfachen textuellen Repräsentation der jeweiligen Kontoinstanz."""
        return "ThermostatStatus: id {}, temp: {}, status {}, device_id {}, date:{}".format(
            self.get_id(), self.get_temp(), self.get_status(), self.get_device(), self.get_date())

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Account()."""
        obj = ThermostatStatusBO()
        obj.set_id(dictionary["id"])
        obj.set_temp(dictionary["temp"])
        obj.set_status(dictionary["status"])
        obj.set_device(dictionary["device_id"])
        obj.set_date(dictionary["date"])
        return obj
