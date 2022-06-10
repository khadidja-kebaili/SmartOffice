from bo.BusinessObject import Businessobject
from datetime import date, datetime, timedelta
import time
import calendar
import asyncio


class WeeklyPlanJalBO(Businessobject):

    def __init__(self):
        super().__init__()
        self._triggered = False
        self._time_of_trigger = None
        self._standard = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: []
        }
        self._customized = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: []
        }

    def set_standard_weekly_plan(self, temperature, timeframe):
        new_dict = self._standard
        transformed = datetime.strptime(timeframe, '%Y-%m-%d %H:%M:%S')
        new_dict[date.isoweekday(transformed)].append({transformed.strftime('%Y-%m-%d %H:%M'): temperature})
        self._standard = new_dict
        return self._standard

    def get_temp_for_a_weekday(self, num):
        temp = []
        if self._triggered is False:
            for elem in self._standard[num]:
                for i in elem:
                    temp.append(elem[i])
        else:
            for elem in self._customized[num]:
                for i in elem:
                    temp.append(elem[i])
        return temp

    def get_time_for_a_weekday(self, num):
        times = []
        if self._triggered is False:
            for elem in self._standard[num]:
                for i in elem:
                    times.append(i[-5:])
        else:
            for elem in self._customized[num]:
                for i in elem:
                    times.append(i[-5:])
        return times

    def set_customized_weekly_plan(self, temperature, time):
        new_dict = self._standard
        transformed = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        self._triggered = True
        self._time_of_trigger = datetime.now()
        new_dict[date.isoweekday(transformed)].append({transformed.strftime('%Y-%m-%d %H:%M'): temperature})
        self._customized = new_dict
        self.set_trigger_date(time)
        self.get_current_valid_weekly_plan()
        #self.reset_trigger()

    # Hilfsfunktion
    def set_trigger_to_last_day_of_week(self, s_time):
        dt = datetime.strptime(s_time, '%Y-%m-%d %H:%M:%S')
        start = dt - timedelta(days=dt.weekday())
        end = start + timedelta(days=5)
        self._time_of_trigger = end

    def set_trigger_date(self, date):
        if date is None:
            self._time_of_trigger = None
        else:
            self.set_trigger_to_last_day_of_week(date)

    def get_trigger_date(self):
        return self._time_of_trigger

    def get_trigger_status(self):
        return self._triggered

    def reset_trigger(self):
        if self._time_of_trigger is None:
            print('Trigger not switched on')
        else:
            x = (self._time_of_trigger - datetime.now()).total_seconds()
            while x >= 0:
                print('Countdown started,', x, ' seconds left')
                x = (self._time_of_trigger - datetime.now()).total_seconds()
            else:
                self._triggered = False
                self._time_of_trigger = None
                print('trigger was reset')

    def get_current_valid_weekly_plan(self):
        if not self._triggered:
            print('not triggered')
            return self._standard
        else:
            print('triggered')
            return self._customized

