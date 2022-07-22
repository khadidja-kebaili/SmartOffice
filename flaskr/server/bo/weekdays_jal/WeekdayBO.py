from abc import ABC


class Weekday(ABC):
    '''
    Superklasse für allen WochentagBOs
    Vererbt ihre Attribute und Methoden an ihre Subklassen
    '''

    def __init__(self):
        super().__init__()
        self._id = None
        self._start_time = None
        self._end_time = None
        self._value = None
        self._type = None

    def set_id(self, id):
        '''
        Setzen der Id
        :param id: Id
        '''
        self._id = id

    def get_id(self):
        '''
        Gibt Id zurück
        :return: Id
        '''
        return self._id

    def set_start_time(self, start_time):
        '''
        Setzen des Startzeitpunkts
        :param start_time: Startzeit im Format (HH:MM:SS)
        '''
        self._start_time = start_time

    def get_start_time(self):
        '''
        Gibt den Startzeitpunkt zurück
        :return: Startzeitpunkt
        '''
        return self._start_time

    def set_end_time(self, end_time):
        '''
        Setzen des Endzeitpunkts
        :param end_time: Endzeit im Format (HH:MM:SS)
        '''
        self._end_time = end_time

    def get_end_time(self):
        '''
        Gibt den Endzeitpunkt zurück
        :return: Endzeitpunkt
        '''
        return self._end_time

    def set_value(self, value):
        '''
        Setzt den Wert
        :param value: Temperatur oder Jalousienstand (integer)
        '''
        self._value = value

    def get_value(self):
        '''
        Gibt den Wert zurück
        :return: Temperatur oder Jalousienstand (integer)
        '''
        return self._value

    def set_type(self, type):
        '''
        Setzt den Typ des Eintrags
        :param type: nur 'J' für Jalousien oder 'T' für Thermostat eintragen!
        '''
        self._type = type

    def get_type(self):
        '''
        Gibt den Typ des Eintrags zurück
        :return: 'J' oder 'T' (string)
        '''
        return self._type
