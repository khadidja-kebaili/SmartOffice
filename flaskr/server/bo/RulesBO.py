from flaskr.server.bo.BusinessObject import Businessobject


class RulesBO(Businessobject):

    def __init__(self):
        super().__init__()
        self._type = None
        self._min = None
        self._max = None
        self._start = None
        self._end = None

    def set_type(self, type):
        self._type = type

    def get_type(self):
        return self._type

    def set_min(self, value):
        self._min = value

    def get_min(self):
        return self._min

    def set_max(self, value):
        self._max = value

    def get_max(self):
        return self._max

    def set_start_time(self, start_time):
        self._start = start_time

    def get_start_time(self):
        return self._start

    def set_end_time(self, end_time):
        self._end = end_time

    def get_end_time(self):
        return self._end


    def __str__(self):
        return "id:{}, type_of_device:{}, min-value:{}, max-value:{}, start_of_rule: {}, end_of_rule: {}".format(
                self.get_id(), self.get_type(), self.get_min(), self.get_max(), self.get_start_time(), self.get_end_time())

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = RulesBO()
        obj.set_id(dictionary['id'])
        obj.set_type(dictionary['type'])
        obj.set_min(dictionary['min'])
        obj.set_max(dictionary['max'])
        obj.set_start_time(dictionary['start'])
        obj.set_end_time(dictionary['end'])

