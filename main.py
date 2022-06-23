from flaskr import app
from flaskr.server.DeviceAdministration import DeviceAdministration
from datetime import datetime

import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, name, n):
        threading.Thread.__init__(self)
        self.name = name
        self.n = n

    def run(self):
        print("Starting " + self.name)
        if self.name == 'Thread1':
            check_jal_stat(self.name, 3570)
            print("Exiting " + self.name)
        elif self.name == 'main_server_thread':
            something()
        elif self.name == 'Thread2':
            check_temp_stat(self.name, 3570)
            print('nothings going on')
        else:
            print('Nothing is going on')


def check_jal_stat(thread_name, delay):
    date = datetime.now()
    weekday = date.isoweekday()
    adm = DeviceAdministration()
    if weekday == 1:
        stats = adm.get_all_jal_standard_entries_monday()
    elif weekday == 2:
        stats = adm.get_all_jal_standard_entries_tuesday()
    elif weekday == 3:
        stats = adm.get_all_jal_standard_entries_wednesday()
    elif weekday == 4:
        stats = adm.get_all_jal_standard_entries_thursday()
    elif weekday == 5:
        stats = adm.get_all_jal_standard_entries_friday()
    else:
        print('It´s the weekend!')

    count = True
    while count:
        for elem in stats:
            elem_hour = datetime.strptime(elem.get_start_time(), '%H:%M:%S').hour
            if elem_hour == date.hour:
                adm.set_status_to_percentage_by_id(1, elem.get_value())
            else:
                time.sleep(delay)
    if exitFlag:
        thread_name.exit()
    print("%s" % thread_name, count)


def check_temp_stat(thread_name, delay):
    date = datetime.now()
    weekday = date.isoweekday()
    adm = DeviceAdministration()
    if weekday == 1:
        stats = adm.get_all_temp_standard_entries_monday()
    elif weekday == 2:
        stats = adm.get_all_temp_standard_entries_tuesday()
    elif weekday == 3:
        stats = adm.get_all_temp_standard_entries_wednesday()
    elif weekday == 4:
        stats = adm.get_all_temp_standard_entries_thursday()
    elif weekday == 5:
        stats = adm.get_all_temp_standard_entries_friday()
    else:
        print('It´s the weekend!')

    count = True
    while count:
        for elem in stats:
            elem_hour = datetime.strptime(elem.get_start_time(), '%H:%M:%S').hour
            if elem_hour == date.hour:
                adm.set_status_to_percentage_by_id(1, elem.get_value())
            else:
                time.sleep(delay)
    if exitFlag:
        thread_name.exit()
    print("%s" % thread_name, count)


def something():
    if __name__ == "__main__":
        app.run(debug=False)


# Create new threads
checking_jal = myThread('Thread1', 0)
checking_temp = myThread('Thread2', 0)
main_server_thread = myThread('main',0)

# Start new Threads
checking_jal.start()
checking_temp.start()
main_server_thread.start()

print("Exiting Main Thread")


