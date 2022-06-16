from abc import ABC, abstractmethod


class Weekday(ABC):

    def __init__(self):
        super().__init__()
        self._id = None
        self._start_time = None
        self._end_time = None
        self._value = None
        self._type = None

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_start_time(self, start_time):
        self._start_time = start_time

    def get_start_time(self):
        return self._start_time

    def set_end_time(self, end_time):
        self._end_time = end_time

    def get_end_time(self):
        return self._end_time

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def set_type(self, type):
        self._type = type

    def get_type(self):
        return self._type