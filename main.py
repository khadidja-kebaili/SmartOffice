from flaskr import app
from flaskr.server.DeviceAdministration import DeviceAdministration
from datetime import datetime
import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    '''
    Implementierung des Multi-Threading Ansatzes.
    '''

    def __init__(self, name, n):
        threading.Thread.__init__(self)
        self.name = name
        self.n = n

    def run(self):
        '''
        Die verschiedenen Threads, die weiter unten definiert wurden, werden hier über deren Namen aufgerufen.
        Bei check_jal_stat() und check_temp_stat() ist  auch die Zeitspanne,
        in welcher diese wiederholt werden sollen anzugeben.
        '''
        print("Starting " + self.name)
        if self.name == 'Thread1':
            check_jal_stat(self.name, 3550)
            print("Exiting " + self.name)
        elif self.name == 'main_server_thread':
            flask_app()
        elif self.name == 'Thread2':
            check_temp_stat(self.name, 3550)
            print('nothings going on')
        else:
            print('Nothing is going on')


def check_jal_stat(thread_name, delay):
    '''
    Stündlicher Check ob der jetztige Jalousienstand dem Planwert entspricht.
    :param thread_name: Name des Threads
    :param delay: Wie lange bis zur Wiederholung des Threads
    '''
    date = datetime.now()
    weekday = date.isoweekday()
    adm = DeviceAdministration()
    stats = []
    if weekday == 1:
        entries = adm.get_all_jal_standard_entries_monday()
        for elem in entries:
            print(elem)
            stats.append(elem)
    elif weekday == 2:
        entries = adm.get_all_jal_standard_entries_tuesday()
        for elem in entries:
            stats.append(elem)
    elif weekday == 3:
        entries = adm.get_all_jal_standard_entries_wednesday()
        for elem in entries:
            stats.append(elem)
    elif weekday == 4:
        entries = adm.get_all_jal_standard_entries_thursday()
        for elem in entries:
            stats.append(elem)
    elif weekday == 5:
        entries = adm.get_all_jal_standard_entries_friday()
        for elem in entries:
            stats.append(elem)
    else:
        print('It´s the weekend!')
    count = True
    while count:
        count = 0
    while count < len(stats):
        for elem in stats:
            date_hour = datetime.strftime(date, '%H:%M:%S')
            print('Hier ist die Datehour:', date_hour, 'hier ist elem_get_start_time:', elem.get_start_time())
            if adm.in_between_times(date_hour, elem.get_start_time(), elem.get_end_time()) is True:
                print('It is overlapping!')
                adm.set_status_to_percentage_by_id(1, 60)
                adm.set_status_to_percentage_by_id(1, elem.get_value())
                count += 1
            else:
                print('keine overlapping')
                time.sleep(delay)
                count += 1
    if exitFlag:
        thread_name.exit()
    print("%s" % thread_name, count)


def check_temp_stat(thread_name, delay):
    '''
    Stündlicher Check ob der jetztige Temperatur dem Planwert entspricht.
    :param thread_name: Name des Threads
    :param delay: Wie lange bis zur Wiederholung des Threads
    '''
    date = datetime.now()
    weekday = date.isoweekday()
    print(date, weekday)
    adm = DeviceAdministration()
    stats = []
    if weekday == 1:
        entries = adm.get_all_temp_standard_entries_monday()
        for elem in entries:
            print(elem)
            stats.append(elem)
    elif weekday == 2:
        entries = adm.get_all_temp_standard_entries_tuesday()
        if len(entries) > 0:
            print('Heute ist Dienstag')
            for elem in entries:
                stats.append(elem)
        else:
            return 0
    elif weekday == 3:
        entries = adm.get_all_temp_standard_entries_wednesday()
        if len(entries) > 0:
            print('Heute ist Mittwoch')
            for elem in entries:
                stats.append(elem)
        else:
            return 0
    elif weekday == 4:
        entries = adm.get_all_temp_standard_entries_thursday()
        if len(entries) > 0:
            print('Heute ist Donnerstag')
            for elem in entries:
                stats.append(elem)
        else:
            return 0
    elif weekday == 5:
        entries = adm.get_all_temp_standard_entries_friday()
        if len(entries) > 0:
            print('Heute ist Freitag')
            for elem in entries:
                stats.append(elem)
        else:
            return 0
    else:
        print('It´s the weekend!')
    count = True
    while count:
        for elem in stats:
            elem_hour = datetime.strptime(elem.get_start_time(), '%H:%M:%S').hour
            if elem_hour == date.hour:
                print('Geh runter!')
            else:
                time.sleep(delay)
    if exitFlag:
        thread_name.exit()
    print("%s" % thread_name, count)


def flask_app():
    '''
    Flask-App Ausführung durch diesen Thread
    '''
    if __name__ == "__main__":
        app.run('192.168.2.187', debug=False, ssl_context='adhoc')


# Create new threads
checking_jal = myThread('Thread1', 0)
checking_temp = myThread('Thread2', 0)
main_server_thread = myThread('main_server_thread', 0)

# Start new Threads
checking_jal.start()
checking_temp.start()
main_server_thread.start()

print("Exiting Main Thread")


