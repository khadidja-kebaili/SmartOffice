from bo.BusinessObject import Businessobject


class RulesBO(Businessobject):

    def __init__(self):
        super().__init__()
        self._min_temperature = None
        self._max_temperature = None
        self._min_percentage_at_daytime = {}
        self._max_percentage_at_daytime = {}
        self._no_access_time = None

    def set_min_temperature(self, temperature):
        self._min_temperature = temperature

    def get_min_temperature(self):
        return self._min_temperature

    def set_max_temperature(self, temperature):
        self._max_temperature = temperature

    def get_max_temperature(self):
        return self._max_temperature

    def set_min_percentage(self, daytime, percentage):
        self._min_percentage_at_daytime[daytime] = percentage

    def get_min_percentage(self):
        return self._min_percentage_at_daytime

    def set_max_percentage(self, daytime, percentage):
        self._max_percentage_at_daytime[daytime] = percentage

    def get_max_percentage(self):
        return self._max_percentage_at_daytime

    def set_no_access_time(self, time):
        self._no_access_time = time

    def get_no_access_time(self):
        return self._no_access_time
