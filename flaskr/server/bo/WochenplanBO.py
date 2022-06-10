from bo.BusinessObject import Businessobject
from datetime import date, datetime, timedelta
import time
import calendar
import asyncio


class WochenplanBO(Businessobject):

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
        task = asyncio.create_task(self.reset_trigger())

    #Hilfsfunktion
    def set_trigger_to_last_day_of_week(self, s_time):
        dt = datetime.strptime(s_time, '%Y-%m-%d %H:%M:%S')
        start = dt - timedelta(days=dt.weekday())
        end = start + timedelta(days=5)
        self._time_of_trigger = end

    def set_trigger_date(self, date):
        if date == None:
            self._time_of_trigger = None
        else:
            self.set_trigger_to_last_day_of_week(date)

    def get_trigger_date(self):
        return self._time_of_trigger

    async def reset_trigger(self):
        if self._time_of_trigger == None:
            print('Trigger not switched on')
        else:
            t = datetime.strptime('2022-06-10 14:13:45', '%Y-%m-%d %H:%M:%S')
            x = (self._time_of_trigger - datetime.now()).total_seconds()
            while x >= 0:
                print('something')
                time.sleep
                x = (self._time_of_trigger- datetime.now()).total_seconds()
            else:
                self._triggered = False
                self._time_of_trigger = None
                print('trigger was reset')

    def get_current_valide_weeklyplan(self):
        if not self._triggered:
            return self._standard
        else:
            return self._customized



ex = WochenplanBO()
asyncio.run(ex.set_customized_weekly_plan(260, '2022-06-10 10:00:00'))

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def print_event(name):
    print ('EVENT:', time.time(), name)

print ('START:', time.time())
scheduler.enter(1, 1, print_event, ('first',))
scheduler.enter(1, 1, print_event, ('second',))

scheduler.run()

print(ex.get_current_valide_weeklyplan())

'''starttime = time.time()
i = 0
while i <= 5:
    print("tick", i)
    time.sleep(432000- ((time.time() - starttime) % 432000))
    i += 1'''



new = {1: []}
#print(new)
new[1] = [{'08:00 - 10:00': None}, {'10:00 - 12:00': None}, {'12:00 - 14:00': None}, {'14:00 - 16:00': None},
          {'14:00 - 16:00': None}]

#print(type(new[1][0]))


def in_between_times(timeframe, start, end):
    if start <= timeframe <= end:
        return True
    else:
        return False

#print(in_between_times('2022-05-06 07:15:00', '2022-05-06 08:00:00', '2022-05-06 10:00'))

'''customized = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: []
        }

stand = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: []
        }'''
trigger = False


def set_standard_weekly_plan(temperature, time):
    stand = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }
    new_dict = stand
    transformed_into_date_object = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    new_dict[date.isoweekday(transformed_into_date_object)].append({time[-8:-2]: temperature})
    stand = new_dict
    print(stand, trigger)


def set_customized_weekly_plan(temperature, time):
    customized = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }
    trigger = True
    new_dict = customized
    transformed_into_date_object = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    new_dict[date.isoweekday(transformed_into_date_object)].append({time[-8:-2]: temperature})
    customized = new_dict
    print(customized, trigger)


'''set_standard_weekly_plan(240, '2022-05-06 08:00:00')
set_customized_weekly_plan(240, '2022-05-06 08:00:00')'''










