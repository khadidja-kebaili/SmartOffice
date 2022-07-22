from flaskr.server.bo.BusinessObject import Businessobject as bo


class ThermostatStatusBO(bo):
    """
    Klasse für ThermostatStatus
    """

    def __init__(self):
        super().__init__()
        self._device_id = None
        self._status = ''
        self._temp = None
        self._date = None

    def set_temp(self, temp):
        '''
        Setzen der Temperatur
        :param temp: 16 - 34 (integer)
        '''
        self._temp = temp

    def get_temp(self):
        '''
        Gibt die Temperatur zurück
        :return: Temperatur (integer)
        '''
        return self._temp

    def set_status(self, status):
        '''
        Setzen des Status
        '''
        self._status = status

    def get_status(self):
        '''
        Gibt den Status zurück
        :return: string
        '''
        return self._status

    def set_device(self, id):
        '''
        Setzen der Device-Id
        :param id: integer
        '''
        self._device_id = id

    def get_device(self):
        '''
        Gibt die Device-Id zurück
        :return: Device-Id (integer)
        '''
        return self._device_id

    def set_date(self, date):
        '''
        Setzen des Datums
        '''
        self._date = date

    def get_date(self):
        '''
        Gibt Datum zurück
        :return:
        '''
        return self._date

    def __str__(self):
        '''
        Gibt eine lesbare Representation des Objekts zurück
        '''
        return "ThermostatStatus: id {}, temp: {}, status {}, device_id {}, date:{}".format(
            self.get_id(), self.get_temp(), self.get_status(), self.get_device(), self.get_date())

    @staticmethod
    def from_dict(dictionary=dict()):
        '''
        Pickt Werte aus einem dictionary und setzt sie ins Objekt ein
        :param dictionary: Dict mit Werten (dict kommt aus dem Frontend und wird per Flask bzw. restX automatisch
        aus einer JSON-Datei erstellt)
        '''
        obj = ThermostatStatusBO()
        obj.set_id(dictionary["id"])
        obj.set_temp(dictionary["temp"])
        obj.set_status(dictionary["status"])
        obj.set_device(dictionary["device_id"])
        obj.set_date(dictionary["date"])
        return obj
