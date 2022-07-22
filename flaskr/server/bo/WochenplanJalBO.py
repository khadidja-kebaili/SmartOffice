from flaskr.server.bo.BusinessObject import Businessobject


class WeeklyPlanJalBO(Businessobject):
    '''
    Klassenimplementierung für die Wochenplaneinträge der Jalousien
    '''

    def __init__(self):
        super().__init__()
        self._weekday = None
        self._monday_id = None #Fremdschlüssel
        self._tuesday_id = None #Fremdschlüssel
        self._wednesday_id = None #Fremdschlüssel
        self._thursday_id = None #Fremdschlüssel
        self._friday_id = None #Fremdschlüssel

    def set_weekday(self, weekday):
        '''
        Setzt den Wochentag
        :param weekday: 1-5 wobei 1 = Montag und 5 = Freitag
        '''
        self._weekday = weekday

    def get_weekday(self):
        '''
        Gibt den Wochentag zurück
        :return: 1 - 5 (integer)
        '''
        return self._weekday

    def set_monday_id(self, id):
        '''
        Setzt die Id des Montag-Eintrags
        :param id: MondayBO-Id
        '''
        self._monday_id = id

    def get_monday_id(self):
        '''
        Gibt die Id des Montag-Eintrags zurück
        :return: MondayBO-Id
        '''
        return self._monday_id

    def set_tuesday_id(self, id):
        '''
        Setzt die Id des Dienstag-Eintrags
        :param id: TuesdayBO-Id
        '''
        self._tuesday_id = id

    def get_tuesday_id(self):
        '''
        Gibt die Id des Dienstag-Eintrags zurück
        :return: TuesdayBO-Id
        '''
        return self._tuesday_id

    def set_wednesday_id(self, id):
        '''
        Setzt die Id des Mittwochtag-Eintrags
        :param id: WednesdayBO-Id
        '''
        self._wednesday_id = id

    def get_wednesday_id(self):
        '''
        Gibt die Id des Mittwoch-Eintrags zurück
        :return: WednesdayBO-Id
        '''
        return self._wednesday_id

    def set_thursday_id(self, id):
        '''
        Setzt die Id des Donnerstag-Eintrags
        :param id: ThursdayBO-Id
        '''
        self._thursday_id = id

    def get_thursday_id(self):
        '''
        Gibt die Id des Donnerstag-Eintrags zurück
        :return: ThursdayBO-Id
        '''
        return self._thursday_id

    def set_friday_id(self, id):
        '''
        Setzt die Id des Freitag-Eintrags
        :param id: FridayBO-Id
        '''
        self._friday_id = id

    def get_friday_id(self):
        '''
        Gibt die Id des Freitag-Eintrags zurück
        :return: FridayBO-Id
        '''
        return self._friday_id

    def __str__(self):
        '''
        Gibt eine lesbare Representation des Objekts zurück
        '''
        return "id: {}, weekday: {}, monday_id: {}, tuesday_id: {}, wednesday_id: {}, thursday_id: {}, friday_id: {}".format(
            self.get_id(), self.get_weekday(), self.get_monday_id(), self.get_tuesday_id(),
            self.get_wednesday_id(), self.get_thursday_id(), self.get_friday_id())

