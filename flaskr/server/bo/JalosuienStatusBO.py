from flaskr.server.bo.BusinessObject import Businessobject as bo


class JalousienStatusBO(bo):
    """
    Klasse für Jalousien
    """

    def __init__(self):
        super().__init__()
        self._jalousieid = None
        self._status = ''
        self._percentage = None
        self._date = None

    def set_percentage(self, perc):
        '''
        Setzen des Jalousienstands
        :param perc: 0 - 100, wobei 0 = geschlossen und 100 = ganz offen
        '''
        self._percentage = perc

    def get_percentage(self):
        '''
        Gibt den Jalousienstand zurück
        :return: Jalousienstand (integer)
        '''
        return self._percentage

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
        return "JalousieStatus: id {}, percentage: {}, status {}, jalousieid {}, date:{}".format(
            self.get_id(), self.get_percentage(), self.get_status(), self.get_device(), self.get_date())

    @staticmethod
    def from_dict(dictionary=dict()):
        '''
        Pickt Werte aus einem dictionary und setzt sie ins Objekt ein
        :param dictionary: Dict mit Werten (dict kommt aus dem Frontend und wird per Flask bzw. restX automatisch
        aus einer JSON-Datei erstellt)
        '''
        obj = JalousienStatusBO()
        obj.set_id(dictionary["id"])
        obj.set_percentage(dictionary["percentage"])
        obj.set_status(dictionary["status"])
        obj.set_device(dictionary["jalousieid"])
        obj.set_date(dictionary["date"])
        return obj
