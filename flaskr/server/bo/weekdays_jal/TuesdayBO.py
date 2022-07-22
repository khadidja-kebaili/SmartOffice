from flaskr.server.bo.weekdays_jal.WeekdayBO import Weekday


class Tuesday(Weekday):

    def __init__(self):
        super().__init__()

    def __str__(self):
        '''
        Gibt eine lesbare Representation des Objekts zurück
        '''
        return "Id: {}, Type of entry: {}, Start of timeinterval: {}, End of timeinterval: {},  Percentage: {}".format(
            self.get_id(), self.get_type(), self.get_start_time(), self.get_end_time(), self.get_value())

    @staticmethod
    def from_dict(dictionary=dict()):
        '''
        Pickt Werte aus einem dictionary und setzt sie ins Objekt ein
        :param dictionary: Dict mit Werten (dict kommt aus dem Frontend und wird per Flask bzw. restX automatisch
        aus einer JSON-Datei erstellt)
        '''
        obj = Tuesday()
        obj.set_id(dictionary['id'])
        obj.set_type(dictionary['type'])
        obj.set_start_time(dictionary['starttime'])
        obj.set_end_time(dictionary['endtime'])
