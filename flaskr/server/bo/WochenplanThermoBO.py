from bo.BusinessObject import Businessobject


class WeeklyPlanTempBO(Businessobject):

    def __init__(self):
        super().__init__()
        self._weekday = None
        self._monday_id = None
        self._tuesday_id = None
        self._wednesday_id = None
        self._thursday_id = None
        self._friday_id = None

    def set_weekday(self, weekday):
        self._weekday = weekday

    def get_weekday(self):
        return self._weekday

    def set_monday_id(self, id):
        self._monday_id = id

    def get_monday_id(self):
        return self._monday_id

    def set_thursday_id(self, id):
        self._thursday_id = id

    def get_thursday_id(self):
        return self._thursday_id

    def set_wednesday_id(self, id):
        self._wednesday_id = id

    def get_wednesday_id(self):
        return self._wednesday_id

    def set_tuesday_id(self, id):
        self._tuesday_id = id

    def get_tuesday_id(self):
        return self._tuesday_id

    def set_friday_id(self, id):
        self._friday_id = id

    def get_friday_id(self):
        return self._friday_id

    def __str__(self):
        return "id: {}, weekday: {}, monday_id: {}, tuesday_id: {}, wednesday_id: {}, thursday_id: {}, friday_id: {}".format(
            self.get_id(), self.get_weekday(), self.get_monday_id(), self.get_tuesday_id(), self.get_wednesday_id(),
            self.get_thursday_id(), self.get_friday_id())

