from bo.BusinessObject import Businessobject
from datetime import date, datetime, timedelta
import time
import calendar
import asyncio


class WeeklyPlanThermoBO(Businessobject):

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

    def set_standard_weekly_plan(self, temperature, time):
        new_dict = self._standard
        transformed = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        new_dict[date.isoweekday(transformed)].append({transformed.strftime('%Y-%m-%d %H:%M'): temperature})
        self._standard = new_dict
        return self._standard

    async def set_customized_weekly_plan(self, temperature, time):
        new_dict = self._standard
        transformed = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        self._triggered = True
        self._time_of_trigger = datetime.now()
        new_dict[date.isoweekday(transformed)].append({transformed.strftime('%Y-%m-%d %H:%M'): temperature})
        self._customized = new_dict
        self.set_trigger_date(time)
        task1 = asyncio.create_task(self.get_current_valid_weekly_plan())
        task = asyncio.create_task(self.reset_trigger())
        await asyncio.gather(task, task1)

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

    async def reset_trigger(self):
        if self._time_of_trigger is None:
            print('Trigger not switched on')
        else:
            t = datetime.strptime('2022-06-10 14:13:45', '%Y-%m-%d %H:%M:%S')
            x = (self._time_of_trigger - datetime.now()).total_seconds()
            while x >= 0:
                print('Countdown started,', x, ' seconds left')
                time.sleep(1)
                x = (self._time_of_trigger - datetime.now()).total_seconds()
            else:
                self._triggered = False
                self._time_of_trigger = None
                print('trigger was reset')

    async def get_current_valid_weekly_plan(self):
        if not self._triggered:
            print('not triggered')
            return self._standard
        else:
            print('triggered')
            return self._customized
