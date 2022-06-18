# from server.bo.Jalousien import JalousienBO
# from server.database.JalousienMapper import JalousienMapper
# from server.bo.Thermostat import ThermostatBO
# from server.database.ThermostatMapper import ThermostatMapper
# from server.bo.JalosuienStatusBO import JalousienStatusBO
# from server.database.JalousienStatusMapper import JalousienStatusMapper
# from server.bo.WochenplanJalBO import WeeklyPlanJalBO
# from server.database.WochenplanJalMapper import WeeklyPlanJalMapper
# from server.bo.WochenplanThermoBO import WeeklyPlanTempBO
# from server.database.WochenplanTempMapper import WeeklyPlanTempMapper
# from server.bo.weekdays_jal.MondayBO import Monday
# from server.bo.weekdays_jal.TuesdayBO import Tuesday
# from server.bo.weekdays_jal.WednesdayBO import Wednesday
# from server.bo.weekdays_jal.ThursdayBO import Thursday
# from server.bo.weekdays_jal.FridayBO import Friday
# from server.database.weekday_mapper.MondayMapper import MondayMapper
# from server.database.weekday_mapper.TuesdayMapper import TuesdayMapper
# from server.database.weekday_mapper.WednesdayMapper import WednesdayMapper
# from server.database.weekday_mapper.ThursdayMapper import ThursdayMapper
# from server.database.weekday_mapper.FridayMapper import FridayMapper
# from server.bo.RulesBO import RulesBO
# from server.database.RulesMapper import RulesMapper
# from server.AuthGen import get_sid
# import time
# import http.client
# from datetime import datetime
# import datetime
#
#
# class DeviceAdministration(object):
#     """Realisierung eines exemplarischen Bankkontos.
#
#     Ein Konto besitzt einen Inhaber sowie eine Reihe von Buchungen (vgl. Klasse Transaction),
#     mit deren Hilfe auch der Kontostand berechnet werden kann.
#     """
#
#     def __init__(self):
#         pass
#
#     """
#     Jalousie-spezifische Methoden
#     """
#
#     def add_device(self, device_id, ip_address, local_key):
#         j = JalousienBO()
#         j.set_device_id(device_id)
#         j.set_ip_address(ip_address)
#         j.set_local_key(local_key)
#         j.set_device()
#         with JalousienMapper() as mapper:
#             return mapper.insert(j)
#
#     def get_jalousie_by_device_id(self, device_id):
#         """Alle Benutzer mit Namen name auslesen."""
#         with JalousienMapper() as mapper:
#             return mapper.find_by_device_id(device_id)
#
#     def get_jalousie_by_id(self, id):
#         pass
#         """Alle Benutzer mit Namen name auslesen."""
#         with JalousienMapper() as mapper:
#             return mapper.find_by_id(id)
#
#     def get_jalousie_by_ip_address(self, ip_address):
#         """Alle Benutzer mit gegebener E-Mail-Adresse auslesen."""
#         with JalousienMapper() as mapper:
#             return mapper.find_by_ip_address(ip_address)
#
#     def get_jalousie_by_local_key(self, local_key):
#         """Den Benutzer mit der gegebenen Google ID auslesen."""
#         with JalousienMapper() as mapper:
#             return mapper.find_by_key(local_key)
#
#     def get_all_jalousies(self):
#         """Alle Benutzer auslesen."""
#         with JalousienMapper() as mapper:
#             return mapper.find_all()
#
#     def save_jalousie(self, jalousie):
#         """Den gegebenen Benutzer speichern."""
#         with JalousienMapper() as mapper:
#             mapper.update(jalousie)
#
#     def delete_jalousie(self, jalousie):
#         """Den gegebenen Benutzer aus unserem System löschen."""
#         with JalousienMapper() as mapper:
#             mapper.delete(jalousie)
#
#     def get_all_status(self):
#         with JalousienStatusMapper() as mapper:
#             return mapper.find_all()
#
#     '''    def open_all_jalousies(self):
#             jalousies = []
#             status = []
#             with JalousienMapper() as mapper:
#                 jalousies.append(mapper.find_all())
#             for elem in jalousies:
#                 for x in elem:
#                     x.set_device()
#                     dev = x.get_device()
#                     dev.set_value(1, 'open')
#                     status.append(dev.status())
#             return status
#
#         def close_all_jalousies(self):
#             jalousies = []
#             status = JalousienStatusBO()
#             jalousies.append(self.get_all_jalousies())
#             for elem in jalousies:
#                 for x in elem:
#                         x.set_device()
#                         dev = x.get_device()
#                         dev.set_value(1, 'close')
#                         time.sleep(10)
#                         status.set_status(str(dev.status()))
#                         status.set_device(id)
#             return status'''
#
#     def open_jalousie_by_id(self, id):
#         jalousies = []
#         status = JalousienStatusBO()
#         jalousies.append(self.get_all_jalousies())
#         dev_stat = None
#         for elem in jalousies:
#             for x in elem:
#                 if x.get_id() == id:
#                     x.set_device()
#                     dev = x.get_device()
#                     dev.set_value(1, 'open')
#                     time.sleep(10)
#                     status.set_status(str(dev.status()))
#                     status.set_device(id)
#                     date = datetime.now()
#                     status.set_date(date)
#                     dev_stat = dev.status()
#         new_list = []
#         for key in dev_stat:
#             for elem in dev_stat[key].values():
#                 new_list.append(elem)
#         status.set_percentage(new_list[1])
#         return status
#
#     def close_jalousie_by_id(self, id):
#         jalousies = []
#         status = JalousienStatusBO()
#         jalousies.append(self.get_all_jalousies())
#         dev_stat = None
#         for elem in jalousies:
#             for x in elem:
#                 if x.get_id() == id:
#                     x.set_device()
#                     dev = x.get_device()
#                     dev.set_value(1, 'close')
#                     time.sleep(10)
#                     status.set_status(str(dev.status()))
#                     status.set_device(id)
#                     date = datetime.now()
#                     status.set_date(date)
#                     dev_stat = dev.status()
#         new_list = []
#         for key in dev_stat:
#             for elem in dev_stat[key].values():
#                 new_list.append(elem)
#         status.set_percentage(new_list[1])
#         return status
#
#     def set_status_to_percentage_by_id(self, id, percentage=int):
#         date = datetime.now()
#         rule = self.get_all_jal_rules()
#         for elem in rule:
#             if self.in_between_times(str(date), str(elem.get_start_time()), str(
#                     elem.get_end_time())) and elem.get_min() > percentage or elem.get_max() < percentage:
#                 return 'Regelverstoß!'
#             else:
#                 jalousies = []
#                 status = JalousienStatusBO()
#                 status.set_percentage(percentage)
#                 perc = status.get_percentage()
#                 status.set_date(date)
#                 jalousies.append(self.get_all_jalousies())
#                 for elem in jalousies:
#                     for x in elem:
#                         if x.get_id() == id:
#                             x.set_device()
#                             dev = x.get_device()
#                             dev.set_value(2, perc)
#                             status.set_status(str(dev.status()))
#                             status.set_device(id)
#                 with JalousienStatusMapper() as mapper:
#                     return mapper.insert(status)
#
#     def get_status_of_jalousie_by_id(self, id):
#         with JalousienStatusMapper() as mapper:
#             return mapper.find_by_key(id)
#
#     def delete_status_by_id(self, id):
#         status = self.get_status_of_jalousie_by_id(id)
#         with JalousienStatusMapper() as mapper:
#             mapper.delete(status)
#
#     def get_last_status(self):
#         status = self.get_all_status()
#         return status[-1]
#
#     def in_between_times(self, timeframe, start, end):
#         if start <= timeframe <= end:
#             return True
#         else:
#             return False
#
#     def get_all_stats_by_timeperiod(self, start, end):
#         enddate = datetime.now().fromisoformat(str(end))
#         startdate = datetime.now().fromisoformat(str(start))
#         stats = self.get_all_status()
#         interval = []
#         for elem in stats:
#             if self.in_between_times(elem.get_date(), startdate, enddate):
#                 print(elem.get_date())
#                 interval.append(elem)
#             else:
#                 pass
#         return interval
#
#     """
#     Thermostat-spezifische Methoden
#     """
#
#     def generate_sid(self, box_url, user_name, password):
#         sid = get_sid(box_url, user_name, password)
#         return sid
#
#     '''    def add_thermostat(self, ain, box_url, user_name, password):
#         """Einen Kunden anlegen."""
#         thermostat = ThermostatBO()
#         thermostat.set_ain(ain)
#         with ThermostatMapper() as mapper:
#             return mapper.insert(thermostat)'''
#
#     def get_thermostat_by_ain(self, ain):
#         """Alle Kunden mit übergebenem Nachnamen auslesen."""
#         with ThermostatMapper() as mapper:
#             return mapper.find_by_ain(ain)
#
#     def get_thermostat_by_id(self, id):
#         """Alle Kunden mit übergebenem Nachnamen auslesen."""
#         with ThermostatMapper() as mapper:
#             return mapper.find_by_key(id)
#
#     '''    def get_all_thermostats(self):
#         with ThermostatMapper() as mapper:
#             return mapper.find_all()
#
#     def save_thermostat(self, thermostat):
#         """Den gegebenen Kunden speichern."""
#         with ThermostatMapper() as mapper:
#             mapper.update(thermostat)'''
#
#     def set_temperature(self, temp):
#         date = datetime.now()
#         rule = self.get_all_temp_rules()
#         for elem in rule:
#             if self.in_between_times(str(date), str(elem.get_start_time()),
#                                      str(elem.get_end_time())) and elem.get_min() > temp or elem.get_max() < temp:
#                 return 'Regelverstoß!'
#             else:
#                 conn = http.client.HTTPSConnection(
#                     "gmhn0evflkdlpmbw.myfritz.net", 8254)
#                 payload = ''
#                 headers = {}
#                 sid = self.generate_sid(
#                     'https://192.168.2.254:8254/', 'admin', 'QUANTO_Solutions')
#                 conn.request("GET",
#                              "/webservices/homeautoswitch.lua?sid={}&ain=139790057201&switchcmd=sethkrtsoll&param={}".format(
#                                  sid, temp),
#                              payload, headers)
#                 res = conn.getresponse()
#                 data = res.read()
#                 data = data.decode("utf-8")
#                 return data
#
#     def get_temperature(self):
#         conn = http.client.HTTPSConnection("192.168.2.254", 8254)
#         payload = ''
#         headers = {}
#         sid = self.generate_sid(
#             'https://192.168.2.254:8254/', 'admin', 'QUANTO_Solutions')
#         conn.request("GET",
#                      "/webservices/homeautoswitch.lua?ain=139790057201&switchcmd=gethrktsoll&sid={}".format(
#                          sid),
#                      payload, headers)
#         res = conn.getresponse()
#         data = res.read()
#         data = data.decode("utf-8")
#         return data
#
#     '''    def get_min_temp(self):
#             conn = http.client.HTTPSConnection("192.168.2.254", 8254)
#             payload = ''
#             sid = self.generate_sid(
#                 'https://192.168.2.254:8254/', 'admin', 'QUANTO_Solutions')
#             headers = {
#                 'Content-Type': 'application/json'
#             }
#             conn.request("GET",
#                          "/webservices/homeautoswitch.lua?sid={}&ain=139790057201&switchcmd=gethkrtsoll".format(sid),
#                          payload, headers)
#             res = conn.getresponse()
#             data = res.read()
#             data = data.decode("utf-8")
#             return data
#
#         def set_min_temp(self, temp):
#             conn = http.client.HTTPSConnection("192.168.2.254", 8254)
#             payload = ''
#             sid = self.generate_sid(
#                 'https://192.168.2.254:8254/', 'admin', 'QUANTO_Solutions')
#             headers = {
#                 'Content-Type': 'application/json'
#             }
#             conn.request("GET",
#                          "/webservices/homeautoswitch.lua?sid={}&ain=139790057201&switchcmd=sethkrtsoll&param={}".format(
#                              sid, temp),
#                          payload, headers)
#             res = conn.getresponse()
#             data = res.read()
#             data = data.decode("utf-8")
#             return data'''
#
#     ####################################################################################
#     '''Für Statistik Soll , Ist (Durchschnitt der Stunden nehmen)'''
#
#     # dateofLastChange -> Lösche alle Einträge, die nicht von heute sind.
#     # Lösche alle Einträge bei denen es Überlappung gibt
#     # Er macht einen Check und wenn die neue Zeit sich mit einem anderen Timeintervall überlappt, wird der alte gelöscht.
#
#     def set_jal_standard_entry_monday(self, start, end, jal):
#         rules = self.get_all_jal_rules()
#         start = time.strptime(start.split(',')[0], '%H:%M:%S')
#         start = datetime.timedelta(hours=start.tm_hour, minutes=start.tm_min, seconds=start.tm_sec).total_seconds()
#         end = time.strptime(end.split(',')[0], '%H:%M:%S')
#         end = datetime.timedelta(hours=end.tm_hour, minutes=end.tm_min, seconds=end.tm_sec).total_seconds()
#         for elem in rules:
#             if self.in_between_times(start, elem.get_start_time().total_seconds(),
#                                      elem.get_end_time().total_seconds()) or \
#                     self.in_between_times(end, elem.get_start_time().total_seconds(),
#                                           elem.get_end_time().total_seconds()):
#                 message = 'Das geht so nicht!', jal, 'Mindestperc:', elem.get_min(), 'Maxperc:', elem.get_max()
#                 return message
#             elif self.in_between_times(start, elem.get_start_time().total_seconds(),
#                                        elem.get_end_time().total_seconds()) == False or \
#                     self.in_between_times(end, elem.get_start_time().total_seconds(),
#                                           elem.get_end_time().total_seconds()) == False \
#                     and jal > elem.get_max() or jal < elem.get_min():
#                 message = 'Zu hoch oder zu niedrig!'
#                 return message
#             else:
#                 monday = Monday()
#                 monday.set_type('J')
#                 monday.set_start_time(start)
#                 monday.set_end_time(end)
#                 monday.set_value(jal)
#                 liste = self.get_all_standard_weekly_jal_entries_by_weekday(1)
#                 entries = self.get_all_jal_standard_entries_monday()
#                 for elem in entries:
#                     if self.in_between_times(start, elem.get_start_time().total_seconds(),
#                                              elem.get_end_time().total_seconds()) or \
#                             self.in_between_times(end, elem.get_start_time().total_seconds(),
#                                                   elem.get_end_time().total_seconds()):
#                         for y in liste:
#                             if y.get_monday_id() == elem.get_id():
#                                 self.delete_entry_in_standard_weeklyplan_jal(y)
#                                 self.delete_standard_entry_monday(elem)
#                         print(elem, 'wurde gelöscht.')
#                 with MondayMapper() as mapper:
#                     mapper.insert(monday)
#                 standard_entry = WeeklyPlanTempBO()
#                 last_entry = self.get_latest_jal_standard_entry_monday()
#                 standard_entry.set_monday_id(last_entry.get_id())
#                 standard_entry.set_weekday(1)
#                 with WeeklyPlanTempMapper() as mapper:
#                     return mapper.insert(standard_entry)
#
#     def get_all_jal_standard_entries_monday(self):
#         with MondayMapper() as mapper:
#             return mapper.find_all_jal_entries()
#
#     def get_latest_jal_standard_entry_monday(self):
#         with MondayMapper() as mapper:
#             return mapper.find_latest_jal_entry()
#
#     def set_jal_standard_entry_tuesday(self, start, end, jal):
#         rules = self.get_all_jal_rules()
#         for elem in rules:
#             if jal > elem.get_max() or jal < elem.get_min():
#                 message = 'Das geht so nicht!', jal, 'Mindestperc:', elem.get_min(), 'Maxperc:', elem.get_max()
#                 return message
#             else:
#                 tuesday = Tuesday()
#                 tuesday.set_type('J')
#                 tuesday.set_start_time(start)
#                 tuesday.set_end_time(end)
#                 tuesday.set_value(jal)
#                 liste = self.get_all_standard_weekly_jal_entries_by_weekday(2)
#                 entries = self.get_all_jal_standard_entries_tuesday()
#                 for elem in entries:
#                     if self.overlapping(str(elem.get_end_time()), str(start)) is True:
#                         for y in liste:
#                             if y.get_tuesday_id() == elem.get_id():
#                                 self.delete_entry_in_standard_weeklyplan_jal(y)
#                                 self.delete_standard_entry_tuesday(elem)
#                         print(elem, 'wurde gelöscht.')
#                 with TuesdayMapper() as mapper:
#                     mapper.insert(tuesday)
#                 standard_entry = WeeklyPlanTempBO()
#                 last_entry = self.get_latest_jal_standard_entry_tuesday()
#                 standard_entry.set_tuesday_id(last_entry.get_id())
#                 standard_entry.set_weekday(2)
#                 with WeeklyPlanTempMapper() as mapper:
#                     return mapper.insert(standard_entry)
#
#     def get_all_jal_standard_entries_tuesday(self):
#         with TuesdayMapper() as mapper:
#             return mapper.find_all_jal_entries()
#
#     def get_latest_jal_standard_entry_tuesday(self):
#         with TuesdayMapper() as mapper:
#             return mapper.find_latest_jal_entry()
#
#     def set_jal_standard_entry_wednesday(self, start, end, jal):
#         rules = self.get_all_jal_rules()
#         for elem in rules:
#             if jal > elem.get_max() or jal < elem.get_min():
#                 message = 'Das geht so nicht!', jal, 'Mindestperc:', elem.get_min(), 'Maxperc:', elem.get_max()
#                 return message
#             else:
#                 wednesday = Wednesday()
#                 wednesday.set_type('J')
#                 wednesday.set_start_time(start)
#                 wednesday.set_end_time(end)
#                 wednesday.set_value(jal)
#                 liste = self.get_all_standard_weekly_jal_entries_by_weekday(3)
#                 entries = self.get_all_jal_standard_entries_wednesday()
#                 for elem in entries:
#                     if self.overlapping(str(elem.get_end_time()), str(start)) is True:
#                         for y in liste:
#                             if y.get_wednesday_id() == elem.get_id():
#                                 self.delete_entry_in_standard_weeklyplan_jal(y)
#                                 self.delete_standard_entry_wednesday(elem)
#                         print(elem, 'wurde gelöscht.')
#                 with WednesdayMapper() as mapper:
#                     mapper.insert(wednesday)
#                 standard_entry = WeeklyPlanTempBO()
#                 last_entry = self.get_latest_jal_standard_entry_wednesday()
#                 standard_entry.set_wednesday_id(last_entry.get_id())
#                 standard_entry.set_weekday(3)
#                 with WeeklyPlanTempMapper() as mapper:
#                     return mapper.insert(standard_entry)
#
#     def get_all_jal_standard_entries_wednesday(self):
#         with WednesdayMapper() as mapper:
#             return mapper.find_all_jal_entries()
#
#     def get_latest_jal_standard_entry_wednesday(self):
#         with WednesdayMapper() as mapper:
#             return mapper.find_latest_jal_entry()
#
#     def set_jal_standard_entry_thursday(self, start, end, jal):
#         rules = self.get_all_jal_rules()
#         for elem in rules:
#             if jal > elem.get_max() or jal < elem.get_min():
#                 message = 'Das geht so nicht!', jal, 'Mindestjal:', elem.get_min(), 'Maxjal:', elem.get_max()
#                 return message
#             else:
#                 thursday = Thursday()
#                 thursday.set_type('J')
#                 thursday.set_start_time(start)
#                 thursday.set_end_time(end)
#                 thursday.set_value(jal)
#                 liste = self.get_all_standard_weekly_jal_entries_by_weekday(4)
#                 entries = self.get_all_jal_standard_entries_thursday()
#                 for elem in entries:
#                     if self.overlapping(str(elem.get_end_time()), str(start)) is True:
#                         for y in liste:
#                             if y.get_thursday_id() == elem.get_id():
#                                 self.delete_entry_in_standard_weeklyplan_jal(y)
#                                 self.delete_standard_entry_thursday(elem)
#                         print(elem, 'wurde gelöscht.')
#                 with ThursdayMapper() as mapper:
#                     mapper.insert(thursday)
#                 standard_entry = WeeklyPlanTempBO()
#                 last_entry = self.get_latest_jal_standard_entry_thursday()
#                 standard_entry.set_thursday_id(last_entry.get_id())
#                 standard_entry.set_weekday(4)
#                 with WeeklyPlanTempMapper() as mapper:
#                     return mapper.insert(standard_entry)
#
#     def get_all_jal_standard_entries_thursday(self):
#         with ThursdayMapper() as mapper:
#             return mapper.find_all_jal_entries()
#
#     def get_latest_jal_standard_entry_thursday(self):
#         with ThursdayMapper() as mapper:
#             return mapper.find_latest_jal_entry()
#
#     def set_jal_standard_entry_friday(self, start, end, jal):
#         rules = self.get_all_jal_rules()
#         for elem in rules:
#             if jal > elem.get_max() or jal < elem.get_min():
#                 message = 'Das geht so nicht!', jal, 'Mindestjal:', elem.get_min(), 'Maxjal:', elem.get_max()
#                 return message
#             else:
#                 friday = Friday()
#                 friday.set_type('J')
#                 friday.set_start_time(start)
#                 friday.set_end_time(end)
#                 friday.set_value(jal)
#                 liste = self.get_all_standard_weekly_jal_entries_by_weekday(5)
#                 entries = self.get_all_jal_standard_entries_friday()
#                 for elem in entries:
#                     if self.overlapping(str(elem.get_end_time()), str(start)) is True:
#                         for y in liste:
#                             if y.get_friday_id() == elem.get_id():
#                                 self.delete_entry_in_standard_weeklyplan_jal(y)
#                                 self.delete_standard_entry_friday(elem)
#                         print(elem, 'wurde gelöscht.')
#                 with FridayMapper() as mapper:
#                     mapper.insert(friday)
#                 standard_entry = WeeklyPlanTempBO()
#                 last_entry = self.get_latest_jal_standard_entry_friday()
#                 standard_entry.set_friday_id(last_entry.get_id())
#                 standard_entry.set_weekday(5)
#                 with WeeklyPlanTempMapper() as mapper:
#                     return mapper.insert(standard_entry)
#
#     def get_all_jal_standard_entries_friday(self):
#         with FridayMapper() as mapper:
#             return mapper.find_all_jal_entries()
#
#     def get_latest_jal_standard_entry_friday(self):
#         with FridayMapper() as mapper:
#             return mapper.find_latest_jal_entry()
#
#     def set_temp_standard_entry_monday(self, start, end, temp):
#         rules = self.get_all_temp_rules()
#         for elem in rules:
#             if temp > elem.get_max() or temp < elem.get_min():
#                 message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(), 'Maxtemp:', elem.get_max()
#                 return message
#             else:
#                 monday = Monday()
#                 monday.set_type('T')
#                 monday.set_start_time(start)
#                 monday.set_end_time(end)
#                 monday.set_value(temp)
#                 liste = self.get_all_standard_weekly_temp_entries_by_weekday(1)
#                 entries = self.get_all_temp_standard_entries_monday()
#                 for elem in entries:
#                     if self.overlapping(str(elem.get_end_time()), str(start)) is True:
#                         for y in liste:
#                             if y.get_monday_id() == elem.get_id():
#                                 self.delete_entry_in_standard_weeklyplan_temp(y)
#                                 self.delete_standard_entry_monday(elem)
#                         print(elem, 'wurde gelöscht.')
#                         self.delete_rule(elem)
#                 with MondayMapper() as mapper:
#                     mapper.insert(monday)
#                 standard_entry = WeeklyPlanTempBO()
#                 last_entry = self.get_latest_temp_standard_entry_monday()
#                 standard_entry.set_monday_id(last_entry.get_id())
#                 standard_entry.set_weekday(1)
#                 with WeeklyPlanTempMapper() as mapper:
#                     return mapper.insert(standard_entry)
#
#     def get_all_temp_standard_entries_monday(self):
#         with MondayMapper() as mapper:
#             return mapper.find_all_temp_entries()
#
#     def get_latest_temp_standard_entry_monday(self):
#         with MondayMapper() as mapper:
#             return mapper.find_latest_temp_entry()
#
#     def delete_standard_entry_monday(self, entry):
#         with MondayMapper() as mapper:
#             return mapper.delete(entry)
#
#     def set_temp_standard_entry_tuesday(self, start, end, temp):
#         rules = self.get_all_temp_rules()
#         for elem in rules:
#             if temp > elem.get_max() or temp < elem.get_min():
#                 message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(), 'Maxtemp:', elem.get_max()
#                 return message
#             else:
#                 tuesday = Tuesday()
#                 tuesday.set_type('T')
#                 tuesday.set_start_time(start)
#                 tuesday.set_end_time(end)
#                 tuesday.set_value(temp)
#                 liste = self.get_all_standard_weekly_temp_entries_by_weekday(2)
#                 entries = self.get_all_temp_standard_entries_tuesday()
#                 for elem in entries:
#                     if self.overlapping(str(elem.get_end_time()), str(start)) is True:
#                         for y in liste:
#                             if y.get_tuesday_id() == elem.get_id():
#                                 self.delete_entry_in_standard_weeklyplan_temp(y)
#                                 self.delete_standard_entry_tuesday(elem)
#                         print(elem, 'wurde gelöscht.')
#                         self.delete_rule(elem)
#                 with TuesdayMapper() as mapper:
#                     mapper.insert(tuesday)
#                 standard_entry = WeeklyPlanTempBO()
#                 last_entry = self.get_latest_temp_standard_entry_tuesday()
#                 standard_entry.set_tuesday_id(last_entry.get_id())
#                 standard_entry.set_weekday(2)
#                 with WeeklyPlanTempMapper() as mapper:
#                     return mapper.insert(standard_entry)
#
#     def get_all_temp_standard_entries_tuesday(self):
#         with TuesdayMapper() as mapper:
#             return mapper.find_all_temp_entries()
#
#     def get_latest_temp_standard_entry_tuesday(self):
#         with TuesdayMapper() as mapper:
#             return mapper.find_latest_temp_entry()
#
#     def delete_standard_entry_tuesday(self, entry):
#         with TuesdayMapper() as mapper:
#             return mapper.delete(entry)
#
#     def set_temp_standard_entry_wednesday(self, start, end, temp):
#         rules = self.get_all_temp_rules()
#         for elem in rules:
#             if temp > elem.get_max() or temp < elem.get_min():
#                 message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(), 'Maxtemp:', elem.get_max()
#                 return message
#             else:
#                 wednesday = Wednesday()
#                 wednesday.set_type('T')
#                 wednesday.set_start_time(start)
#                 wednesday.set_end_time(end)
#                 wednesday.set_value(temp)
#                 liste = self.get_all_standard_weekly_temp_entries_by_weekday(3)
#                 entries = self.get_all_temp_standard_entries_wednesday()
#                 for elem in entries:
#                     if self.overlapping(str(elem.get_end_time()), str(start)) is True:
#                         for y in liste:
#                             if y.get_wednesday_id() == elem.get_id():
#                                 self.delete_entry_in_standard_weeklyplan_temp(y)
#                                 self.delete_standard_entry_wednesday(elem)
#                         print(elem, 'wurde gelöscht.')
#                         self.delete_rule(elem)
#                 with WednesdayMapper() as mapper:
#                     mapper.insert(wednesday)
#                 standard_entry = WeeklyPlanTempBO()
#                 last_entry = self.get_latest_temp_standard_entry_wednesday()
#                 standard_entry.set_wednesday_id(last_entry.get_id())
#                 standard_entry.set_weekday(3)
#                 with WeeklyPlanTempMapper() as mapper:
#                     return mapper.insert(standard_entry)
#
#     def get_all_temp_standard_entries_wednesday(self):
#         with WednesdayMapper() as mapper:
#             return mapper.find_all_temp_entries()
#
#     def get_latest_temp_standard_entry_wednesday(self):
#         with WednesdayMapper() as mapper:
#             return mapper.find_latest_temp_entry()
#
#     def delete_standard_entry_wednesday(self, entry):
#         with WednesdayMapper() as mapper:
#             return mapper.delete(entry)
#
#     def set_temp_standard_entry_thursday(self, start, end, temp):
#         rules = self.get_all_temp_rules()
#         for elem in rules:
#             if temp > elem.get_max() or temp < elem.get_min():
#                 message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(), 'Maxtemp:', elem.get_max()
#                 return message
#             else:
#                 thursday = Thursday()
#                 thursday.set_type('T')
#                 thursday.set_start_time(start)
#                 thursday.set_end_time(end)
#                 thursday.set_value(temp)
#                 liste = self.get_all_standard_weekly_temp_entries_by_weekday(4)
#                 entries = self.get_all_temp_standard_entries_thursday()
#                 for elem in entries:
#                     if self.overlapping(str(elem.get_end_time()), str(start)) is True:
#                         for y in liste:
#                             if y.get_thursday_id() == elem.get_id():
#                                 self.delete_entry_in_standard_weeklyplan_temp(y)
#                                 self.delete_standard_entry_thursday(elem)
#                         print(elem, 'wurde gelöscht.')
#
#                 with ThursdayMapper() as mapper:
#                     mapper.insert(thursday)
#                 standard_entry = WeeklyPlanTempBO()
#                 last_entry = self.get_latest_temp_standard_entry_thursday()
#                 standard_entry.set_thursday_id(last_entry.get_id())
#                 standard_entry.set_weekday(4)
#                 with WeeklyPlanTempMapper() as mapper:
#                     return mapper.insert(standard_entry)
#
#     def get_all_temp_standard_entries_thursday(self):
#         with ThursdayMapper() as mapper:
#             return mapper.find_all_temp_entries()
#
#     def get_latest_temp_standard_entry_thursday(self):
#         with ThursdayMapper() as mapper:
#             return mapper.find_latest_temp_entry()
#
#     def delete_standard_entry_thursday(self, entry):
#         with ThursdayMapper() as mapper:
#             return mapper.delete(entry)
#
#     def set_temp_standard_entry_friday(self, start, end, temp):
#         rules = self.get_all_temp_rules()
#         for elem in rules:
#             if temp > elem.get_max() or temp < elem.get_min():
#                 message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(), 'Maxtemp:', elem.get_max()
#                 return message
#             else:
#                 friday = Friday()
#                 friday.set_type('T')
#                 friday.set_start_time(start)
#                 friday.set_end_time(end)
#                 friday.set_value(temp)
#                 liste = self.get_all_standard_weekly_temp_entries_by_weekday(5)
#                 entries = self.get_all_temp_standard_entries_friday()
#                 for elem in entries:
#                     if self.overlapping(str(elem.get_end_time()), str(start)) is True:
#                         for y in liste:
#                             if y.get_friday_id() == elem.get_id():
#                                 self.delete_entry_in_standard_weeklyplan_temp(y)
#                                 self.delete_standard_entry_friday(elem)
#                         print(elem, 'wurde gelöscht.')
#                 with FridayMapper() as mapper:
#                     mapper.insert(friday)
#                 standard_entry = WeeklyPlanTempBO()
#                 last_entry = self.get_latest_temp_standard_entry_friday()
#                 standard_entry.set_friday_id(last_entry.get_id())
#                 standard_entry.set_weekday(5)
#                 with WeeklyPlanTempMapper() as mapper:
#                     return mapper.insert(standard_entry)
#
#     def get_all_temp_standard_entries_friday(self):
#         with FridayMapper() as mapper:
#             return mapper.find_all_temp_entries()
#
#     def get_latest_temp_standard_entry_friday(self):
#         with FridayMapper() as mapper:
#             return mapper.find_latest_temp_entry()
#
#     def delete_standard_entry_friday(self, entry):
#         with FridayMapper() as mapper:
#             mapper.delete(entry)
#
#     def get_all_entries_standard_weekly_plan_jal(self):
#         with WeeklyPlanJalMapper() as mapper:
#             return mapper.find_all()
#
#     def get_all_standard_weekly_jal_entries_by_weekday(self, weekday):
#         with WeeklyPlanJalMapper() as mapper:
#             return mapper.find_by_weekday(weekday)
#
#     def get_all_standard_weekly_temp_entries_by_weekday(self, weekday):
#         with WeeklyPlanTempMapper() as mapper:
#             return mapper.find_by_weekday(weekday)
#
#     def delete_entry_in_standard_weeklyplan_jal(self, entry):
#         with WeeklyPlanJalMapper() as mapper:
#             mapper.delete(entry)
#
#     def delete_entry_in_standard_weeklyplan_temp(self, entry):
#         with WeeklyPlanTempMapper() as mapper:
#             mapper.delete(entry)
#
#     '''Regel-Operationen'''
#
#     def set_jal_rule(self, min, max, start, end):
#         rule = RulesBO()
#         rule.set_min(min)
#         rule.set_max(max)
#         rule.set_type('J')
#         rule.set_start_time(start)
#         rule.set_end_time(end)
#         rules = self.get_all_jal_rules()
#         start = time.strptime(start.split(',')[0], '%H:%M:%S')
#         start = datetime.timedelta(hours=start.tm_hour, minutes=start.tm_min, seconds=start.tm_sec).total_seconds()
#         end = time.strptime(end.split(',')[0], '%H:%M:%S')
#         end = datetime.timedelta(hours=end.tm_hour, minutes=end.tm_min, seconds=end.tm_sec).total_seconds()
#         for elem in rules:
#             if self.in_between_times(start, elem.get_start_time().total_seconds(),
#                                      elem.get_end_time().total_seconds()) or \
#                     self.in_between_times(end, elem.get_start_time().total_seconds(),
#                                           elem.get_end_time().total_seconds()):
#                 self.delete_rule(elem)
#                 print(elem, 'wurde gelöscht.')
#         with RulesMapper() as mapper:
#             return mapper.insert(rule)
#
#     def delete_rule(self, rule):
#         with RulesMapper() as mapper:
#             mapper.delete(rule)
#
#     def set_temp_rule(self, min, max, start, end):
#         rule = RulesBO()
#         rule.set_min(min)
#         rule.set_max(max)
#         rule.set_type('T')
#         rule.set_start_time(start)
#         rule.set_end_time(end)
#         rules = self.get_all_temp_rules()
#         start = time.strptime(start.split(',')[0], '%H:%M:%S')
#         start = datetime.timedelta(hours=start.tm_hour, minutes=start.tm_min, seconds=start.tm_sec).total_seconds()
#         end = time.strptime(end.split(',')[0], '%H:%M:%S')
#         end = datetime.timedelta(hours=end.tm_hour, minutes=end.tm_min, seconds=end.tm_sec).total_seconds()
#         for elem in rules:
#             if self.in_between_times(start, elem.get_start_time().total_seconds(),
#                                      elem.get_end_time().total_seconds()) or \
#                     self.in_between_times(end, elem.get_start_time().total_seconds(),
#                                           elem.get_end_time().total_seconds()):
#                 self.delete_rule(elem)
#                 print(elem, 'wurde gelöscht.')
#                 self.delete_rule(elem)
#         with RulesMapper() as mapper:
#             return mapper.insert(rule)
#
#     def get_all_rules(self):
#         with RulesMapper() as mapper:
#             return mapper.find_all()
#
#     def get_all_jal_rules(self):
#         with RulesMapper() as mapper:
#             return mapper.find_by_type('J')
#
#     def get_all_temp_rules(self):
#         with RulesMapper() as mapper:
#             return mapper.find_by_type('T')
#
#     def get_rule_by_id(self, id):
#         with RulesMapper() as mapper:
#             return mapper.find_by_key(id)
#
#     def overlapping(self, new_start, old_end):
#         new_start = datetime.strptime(new_start, '%H:%M:%S').time()
#         old_end = datetime.strptime(old_end, '%H:%M:%S').time()
#         if old_end <= new_start:
#             return True
#         else:
#             return False
#
#     ##### Customized Entries ######
#
#     '''def set_jal_customized_entry_monday(self, start, end, perc):
#         monday = Monday()
#         monday.set_type('J')
#         monday.set_start_time(start)
#         monday.set_end_time(end)
#         monday.set_value(perc)
#         with MondayMapper() as mapper:
#             return mapper.insert(monday)
#
#     def get_all_jal_customized_entries_monday(self):
#         with MondayMapper() as mapper:
#             return mapper.find_all()
#
#     def set_jal_customized_entry_tuesday(self, start, end, perc):
#         tuesday = Tuesday()
#         tuesday.set_type('J')
#         tuesday.set_start_time(start)
#         tuesday.set_end_time(end)
#         tuesday.set_value(perc)
#         with TuesdayMapper() as mapper:
#             return mapper.insert(tuesday)
#
#     def get_all_jal_customized_entries_tuesday(self):
#         with TuesdayMapper() as mapper:
#             return mapper.find_all()
#
#     def set_jal_customized_entry_wednesday(self, start, end, perc):
#         wednesday = Wednesday()
#         wednesday.set_type('J')
#         wednesday.set_start_time(start)
#         wednesday.set_end_time(end)
#         wednesday.set_value(perc)
#         with WednesdayMapper() as mapper:
#             return mapper.insert(wednesday)
#
#     def get_all_jal_customized_entries_wednesday(self):
#         with WednesdayMapper() as mapper:
#             return mapper.find_all()
#
#     def set_jal_customized_entry_thursday(self, start, end, perc):
#         thursday = Thursday()
#         thursday.set_type('J')
#         thursday.set_start_time(start)
#         thursday.set_end_time(end)
#         thursday.set_value(perc)
#         with ThursdayMapper() as mapper:
#             return mapper.insert(thursday)
#
#     def get_all_jal_customized_entries_thursday(self):
#         with ThursdayMapper() as mapper:
#             return mapper.find_all()
#
#     def set_jal_customized_entry_friday(self, start, end, perc):
#         friday = Friday()
#         friday.set_type('J')
#         friday.set_start_time(start)
#         friday.set_end_time(end)
#         friday.set_value(perc)
#         with FridayMapper() as mapper:
#             return mapper.insert(friday)
#
#     def get_all_jal_customized_entries_friday(self):
#         with FridayMapper() as mapper:
#             return mapper.find_all()
#
#     def set_temp_customized_entry_monday(self, start, end, temp):
#         monday = Monday()
#         monday.set_type('T')
#         monday.set_start_time(start)
#         monday.set_end_time(end)
#         monday.set_value(temp)
#         with MondayMapper() as mapper:
#             return mapper.insert(monday)
#
#     def get_all_temp_customized_entries_monday(self):
#         with MondayMapper() as mapper:
#             return mapper.find_all()
#
#     def set_temp_customized_entry_tuesday(self, start, end, temp):
#         tuesday = Tuesday()
#         tuesday.set_type('T')
#         tuesday.set_start_time(start)
#         tuesday.set_end_time(end)
#         tuesday.set_value(temp)
#         with TuesdayMapper() as mapper:
#             return mapper.insert(tuesday)
#
#     def get_all_temp_customized_entries_tuesday(self):
#         with TuesdayMapper() as mapper:
#             return mapper.find_all()
#
#     def set_temp_customized_entry_wednesday(self, start, end, temp):
#         wednesday = Wednesday()
#         wednesday.set_type('T')
#         wednesday.set_start_time(start)
#         wednesday.set_end_time(end)
#         wednesday.set_value(temp)
#         with WednesdayMapper() as mapper:
#             return mapper.insert(wednesday)
#
#     def get_all_temp_customized_entries_wednesday(self):
#         with WednesdayMapper() as mapper:
#             return mapper.find_all()
#
#     def set_temp_customized_entry_thursday(self, start, end, temp):
#         thursday = Thursday()
#         thursday.set_type('T')
#         thursday.set_start_time(start)
#         thursday.set_end_time(end)
#         thursday.set_value(temp)
#         with ThursdayMapper() as mapper:
#             return mapper.insert(thursday)
#
#     def get_all_temp_customized_entries_thursday(self):
#         with ThursdayMapper() as mapper:
#             return mapper.find_all()
#
#     def set_temp_customized_entry_friday(self, start, end, temp):
#         friday = Friday()
#         friday.set_type('T')
#         friday.set_start_time(start)
#         friday.set_end_time(end)
#         friday.set_value(temp)
#         with FridayMapper() as mapper:
#             return mapper.insert(friday)
#
#     def get_all_temp_customized_entries_friday(self):
#         with FridayMapper() as mapper:
#             return mapper.find_all()'''
#
#
# '''d = DeviceAdministration()
# i = d.get_all_jal_rules()
# for elem in i:
#     print(elem)
# print(d.set_jal_standard_entry_monday('09:00:00', '11:00:00', 25))'''
#
#

from server.bo.Jalousien import JalousienBO
from server.database.JalousienMapper import JalousienMapper
from server.bo.Thermostat import ThermostatBO
from server.database.ThermostatMapper import ThermostatMapper
from server.bo.JalosuienStatusBO import JalousienStatusBO
from server.database.JalousienStatusMapper import JalousienStatusMapper
from server.bo.WochenplanJalBO import WeeklyPlanJalBO
from server.database.WochenplanJalMapper import WeeklyPlanJalMapper
from server.bo.WochenplanThermoBO import WeeklyPlanTempBO
from server.database.WochenplanTempMapper import WeeklyPlanTempMapper
from server.bo.weekdays_jal.MondayBO import Monday
from server.bo.weekdays_jal.TuesdayBO import Tuesday
from server.bo.weekdays_jal.WednesdayBO import Wednesday
from server.bo.weekdays_jal.ThursdayBO import Thursday
from server.bo.weekdays_jal.FridayBO import Friday
from server.database.weekday_mapper.MondayMapper import MondayMapper
from server.database.weekday_mapper.TuesdayMapper import TuesdayMapper
from server.database.weekday_mapper.WednesdayMapper import WednesdayMapper
from server.database.weekday_mapper.ThursdayMapper import ThursdayMapper
from server.database.weekday_mapper.FridayMapper import FridayMapper
from server.bo.RulesBO import RulesBO
from server.database.RulesMapper import RulesMapper
from server.AuthGen import get_sid
import time
import http.client
from datetime import datetime, timedelta
import datetime


class DeviceAdministration(object):
    """Realisierung eines exemplarischen Bankkontos.

    Ein Konto besitzt einen Inhaber sowie eine Reihe von Buchungen (vgl. Klasse Transaction),
    mit deren Hilfe auch der Kontostand berechnet werden kann.
    """

    def __init__(self):
        pass

    """
    Jalousie-spezifische Methoden
    """

    def add_device(self, device_id, ip_address, local_key):
        j = JalousienBO()
        j.set_device_id(device_id)
        j.set_ip_address(ip_address)
        j.set_local_key(local_key)
        j.set_device()
        with JalousienMapper() as mapper:
            return mapper.insert(j)

    def get_jalousie_by_device_id(self, device_id):
        """Alle Benutzer mit Namen name auslesen."""
        with JalousienMapper() as mapper:
            return mapper.find_by_device_id(device_id)

    def get_jalousie_by_id(self, id):
        pass
        """Alle Benutzer mit Namen name auslesen."""
        with JalousienMapper() as mapper:
            return mapper.find_by_id(id)

    def get_jalousie_by_ip_address(self, ip_address):
        """Alle Benutzer mit gegebener E-Mail-Adresse auslesen."""
        with JalousienMapper() as mapper:
            return mapper.find_by_ip_address(ip_address)

    def get_jalousie_by_local_key(self, local_key):
        """Den Benutzer mit der gegebenen Google ID auslesen."""
        with JalousienMapper() as mapper:
            return mapper.find_by_key(local_key)

    def get_all_jalousies(self):
        """Alle Benutzer auslesen."""
        with JalousienMapper() as mapper:
            return mapper.find_all()

    def save_jalousie(self, jalousie):
        """Den gegebenen Benutzer speichern."""
        with JalousienMapper() as mapper:
            mapper.update(jalousie)

    def delete_jalousie(self, jalousie):
        """Den gegebenen Benutzer aus unserem System löschen."""
        with JalousienMapper() as mapper:
            mapper.delete(jalousie)

    def get_all_status(self):
        with JalousienStatusMapper() as mapper:
            return mapper.find_all()

    '''    def open_all_jalousies(self):
            jalousies = []
            status = []
            with JalousienMapper() as mapper:
                jalousies.append(mapper.find_all())
            for elem in jalousies:
                for x in elem:
                    x.set_device()
                    dev = x.get_device()
                    dev.set_value(1, 'open')
                    status.append(dev.status())
            return status

        def close_all_jalousies(self):
            jalousies = []
            status = JalousienStatusBO()
            jalousies.append(self.get_all_jalousies())
            for elem in jalousies:
                for x in elem:
                        x.set_device()
                        dev = x.get_device()
                        dev.set_value(1, 'close')
                        time.sleep(10)
                        status.set_status(str(dev.status()))
                        status.set_device(id)
            return status'''

    def open_jalousie_by_id(self, id):
        jalousies = []
        status = JalousienStatusBO()
        jalousies.append(self.get_all_jalousies())
        dev_stat = None
        for elem in jalousies:
            for x in elem:
                if x.get_id() == id:
                    x.set_device()
                    dev = x.get_device()
                    dev.set_value(1, 'open')
                    time.sleep(10)
                    status.set_status(str(dev.status()))
                    status.set_device(id)
                    date = datetime.now()
                    status.set_date(date)
                    dev_stat = dev.status()
        new_list = []
        for key in dev_stat:
            for elem in dev_stat[key].values():
                new_list.append(elem)
        status.set_percentage(new_list[1])
        return status

    def close_jalousie_by_id(self, id):
        jalousies = []
        status = JalousienStatusBO()
        jalousies.append(self.get_all_jalousies())
        dev_stat = None
        for elem in jalousies:
            for x in elem:
                if x.get_id() == id:
                    x.set_device()
                    dev = x.get_device()
                    dev.set_value(1, 'close')
                    time.sleep(10)
                    status.set_status(str(dev.status()))
                    status.set_device(id)
                    date = datetime.now()
                    status.set_date(date)
                    dev_stat = dev.status()
        new_list = []
        for key in dev_stat:
            for elem in dev_stat[key].values():
                new_list.append(elem)
        status.set_percentage(new_list[1])
        return status

    def set_status_to_percentage_by_id(self, id, percentage=int):
        date = datetime.now()
        rule = self.get_all_jal_rules()
        for elem in rule:
            if self.in_between_times(str(date), str(elem.get_start_time()), str(
                    elem.get_end_time())) and elem.get_min() > percentage or elem.get_max() < percentage:
                return 'Regelverstoß!'
            else:
                jalousies = []
                status = JalousienStatusBO()
                status.set_percentage(percentage)
                perc = status.get_percentage()
                status.set_date(date)
                jalousies.append(self.get_all_jalousies())
                for elem in jalousies:
                    for x in elem:
                        if x.get_id() == id:
                            x.set_device()
                            dev = x.get_device()
                            dev.set_value(2, perc)
                            status.set_status(str(dev.status()))
                            status.set_device(id)
                with JalousienStatusMapper() as mapper:
                    return mapper.insert(status)

    def get_status_of_jalousie_by_id(self, id):
        with JalousienStatusMapper() as mapper:
            return mapper.find_by_key(id)

    def delete_status_by_id(self, id):
        status = self.get_status_of_jalousie_by_id(id)
        with JalousienStatusMapper() as mapper:
            mapper.delete(status)

    def get_last_status(self):
        status = self.get_all_status()
        return status[-1]

    def in_between_times(self, timeframe, start = datetime.timedelta, end = datetime.timedelta):
        timeframe = datetime.datetime.strptime(timeframe, '%H:%M:%S')
        timeframe = timeframe.strftime('%H%M%S')
        timeframe = float(timeframe)
        start = start.total_seconds()
        end = end.total_seconds()
        if start <= timeframe <= end:
            return True
        else:
            return False

    def get_all_stats_by_timeperiod(self, start, end):
        enddate = datetime.now().fromisoformat(str(end))
        startdate = datetime.now().fromisoformat(str(start))
        stats = self.get_all_status()
        interval = []
        for elem in stats:
            if self.in_between_times(elem.get_date(), startdate, enddate):
                print(elem.get_date())
                interval.append(elem)
            else:
                pass
        return interval

    """
    Thermostat-spezifische Methoden
    """

    def generate_sid(self, box_url, user_name, password):
        sid = get_sid(box_url, user_name, password)
        return sid

    '''    def add_thermostat(self, ain, box_url, user_name, password):
        """Einen Kunden anlegen."""
        thermostat = ThermostatBO()
        thermostat.set_ain(ain)
        with ThermostatMapper() as mapper:
            return mapper.insert(thermostat)'''

    def get_thermostat_by_ain(self, ain):
        """Alle Kunden mit übergebenem Nachnamen auslesen."""
        with ThermostatMapper() as mapper:
            return mapper.find_by_ain(ain)

    def get_thermostat_by_id(self, id):
        """Alle Kunden mit übergebenem Nachnamen auslesen."""
        with ThermostatMapper() as mapper:
            return mapper.find_by_key(id)

    '''    def get_all_thermostats(self):
        with ThermostatMapper() as mapper:
            return mapper.find_all()

    def save_thermostat(self, thermostat):
        """Den gegebenen Kunden speichern."""
        with ThermostatMapper() as mapper:
            mapper.update(thermostat)'''

    def set_temperature(self, temp):
        date = datetime.now()
        rule = self.get_all_temp_rules()
        for elem in rule:
            if self.in_between_times(str(date), str(elem.get_start_time()),
                                     str(elem.get_end_time())) and elem.get_min() > temp or elem.get_max() < temp:
                return 'Regelverstoß!'
            else:
                conn = http.client.HTTPSConnection(
                    "gmhn0evflkdlpmbw.myfritz.net", 8254)
                payload = ''
                headers = {}
                sid = self.generate_sid(
                    'https://192.168.2.254:8254/', 'admin', 'QUANTO_Solutions')
                conn.request("GET",
                             "/webservices/homeautoswitch.lua?sid={}&ain=139790057201&switchcmd=sethkrtsoll&param={}".format(
                                 sid, temp),
                             payload, headers)
                res = conn.getresponse()
                data = res.read()
                data = data.decode("utf-8")
                return data

    def get_temperature(self):
        conn = http.client.HTTPSConnection("192.168.2.254", 8254)
        payload = ''
        headers = {}
        sid = self.generate_sid(
            'https://192.168.2.254:8254/', 'admin', 'QUANTO_Solutions')
        conn.request("GET",
                     "/webservices/homeautoswitch.lua?ain=139790057201&switchcmd=gethrktsoll&sid={}".format(
                         sid),
                     payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        return data

    '''    def get_min_temp(self):
            conn = http.client.HTTPSConnection("192.168.2.254", 8254)
            payload = ''
            sid = self.generate_sid(
                'https://192.168.2.254:8254/', 'admin', 'QUANTO_Solutions')
            headers = {
                'Content-Type': 'application/json'
            }
            conn.request("GET",
                         "/webservices/homeautoswitch.lua?sid={}&ain=139790057201&switchcmd=gethkrtsoll".format(sid),
                         payload, headers)
            res = conn.getresponse()
            data = res.read()
            data = data.decode("utf-8")
            return data

        def set_min_temp(self, temp):
            conn = http.client.HTTPSConnection("192.168.2.254", 8254)
            payload = ''
            sid = self.generate_sid(
                'https://192.168.2.254:8254/', 'admin', 'QUANTO_Solutions')
            headers = {
                'Content-Type': 'application/json'
            }
            conn.request("GET",
                         "/webservices/homeautoswitch.lua?sid={}&ain=139790057201&switchcmd=sethkrtsoll&param={}".format(
                             sid, temp),
                         payload, headers)
            res = conn.getresponse()
            data = res.read()
            data = data.decode("utf-8")
            return data'''

    ####################################################################################
    '''Für Statistik Soll , Ist (Durchschnitt der Stunden nehmen)'''

    # dateofLastChange -> Lösche alle Einträge, die nicht von heute sind.
    # Lösche alle Einträge bei denen es Überlappung gibt
    # Er macht einen Check und wenn die neue Zeit sich mit einem anderen Timeintervall überlappt, wird der alte gelöscht.

    def set_jal_standard_entry_monday(self, start, end, jal):
        rules = self.get_all_jal_rules()
        start = time.strptime(start.split(',')[0], '%H:%M:%S')
        start = datetime.timedelta(hours=start.tm_hour, minutes=start.tm_min, seconds=start.tm_sec).total_seconds()
        end = time.strptime(end.split(',')[0], '%H:%M:%S')
        end = datetime.timedelta(hours=end.tm_hour, minutes=end.tm_min, seconds=end.tm_sec).total_seconds()
        for elem in rules:
            if self.in_between_times(start, elem.get_start_time().total_seconds(),
                                     elem.get_end_time().total_seconds()) or \
                    self.in_between_times(end, elem.get_start_time().total_seconds(),
                                          elem.get_end_time().total_seconds()):
                message = 'Das geht so nicht!', jal, 'Mindestperc:', elem.get_min(), 'Maxperc:', elem.get_max()
                return message
            elif self.in_between_times(start, elem.get_start_time().total_seconds(),
                                       elem.get_end_time().total_seconds()) == False or \
                    self.in_between_times(end, elem.get_start_time().total_seconds(),
                                          elem.get_end_time().total_seconds()) == False \
                    and jal > elem.get_max() or jal < elem.get_min():
                message = 'Zu hoch oder zu niedrig!'
                return message
            else:
                monday = Monday()
                monday.set_type('J')
                monday.set_start_time(start)
                monday.set_end_time(end)
                monday.set_value(jal)
                liste = self.get_all_standard_weekly_jal_entries_by_weekday(1)
                entries = self.get_all_jal_standard_entries_monday()
                for elem in entries:
                    if self.in_between_times(start, elem.get_start_time().total_seconds(),
                                             elem.get_end_time().total_seconds()) or \
                            self.in_between_times(end, elem.get_start_time().total_seconds(),
                                                  elem.get_end_time().total_seconds()):
                        for y in liste:
                            if y.get_monday_id() == elem.get_id():
                                self.delete_entry_in_standard_weeklyplan_jal(y)
                                self.delete_standard_entry_monday(elem)
                        print(elem, 'wurde gelöscht.')
                with MondayMapper() as mapper:
                    mapper.insert(monday)
                standard_entry = WeeklyPlanTempBO()
                last_entry = self.get_latest_jal_standard_entry_monday()
                standard_entry.set_monday_id(last_entry.get_id())
                standard_entry.set_weekday(1)
                with WeeklyPlanTempMapper() as mapper:
                    return mapper.insert(standard_entry)

    def get_all_jal_standard_entries_monday(self):
        with MondayMapper() as mapper:
            return mapper.find_all_jal_entries()

    def get_latest_jal_standard_entry_monday(self):
        with MondayMapper() as mapper:
            return mapper.find_latest_jal_entry()

    def set_jal_standard_entry_tuesday(self, start, end, jal):
        rules = self.get_all_jal_rules()
        for elem in rules:
            if jal > elem.get_max() or jal < elem.get_min():
                message = 'Das geht so nicht!', jal, 'Mindestperc:', elem.get_min(), 'Maxperc:', elem.get_max()
                return message
            else:
                tuesday = Tuesday()
                tuesday.set_type('J')
                tuesday.set_start_time(start)
                tuesday.set_end_time(end)
                tuesday.set_value(jal)
                liste = self.get_all_standard_weekly_jal_entries_by_weekday(2)
                entries = self.get_all_jal_standard_entries_tuesday()
                for elem in entries:
                    if self.overlapping(str(elem.get_end_time()), str(start)) is True:
                        for y in liste:
                            if y.get_tuesday_id() == elem.get_id():
                                self.delete_entry_in_standard_weeklyplan_jal(y)
                                self.delete_standard_entry_tuesday(elem)
                        print(elem, 'wurde gelöscht.')
                with TuesdayMapper() as mapper:
                    mapper.insert(tuesday)
                standard_entry = WeeklyPlanTempBO()
                last_entry = self.get_latest_jal_standard_entry_tuesday()
                standard_entry.set_tuesday_id(last_entry.get_id())
                standard_entry.set_weekday(2)
                with WeeklyPlanTempMapper() as mapper:
                    return mapper.insert(standard_entry)

    def get_all_jal_standard_entries_tuesday(self):
        with TuesdayMapper() as mapper:
            return mapper.find_all_jal_entries()

    def get_latest_jal_standard_entry_tuesday(self):
        with TuesdayMapper() as mapper:
            return mapper.find_latest_jal_entry()

    def set_jal_standard_entry_wednesday(self, start, end, jal):
        rules = self.get_all_jal_rules()
        for elem in rules:
            if jal > elem.get_max() or jal < elem.get_min():
                message = 'Das geht so nicht!', jal, 'Mindestperc:', elem.get_min(), 'Maxperc:', elem.get_max()
                return message
            else:
                wednesday = Wednesday()
                wednesday.set_type('J')
                wednesday.set_start_time(start)
                wednesday.set_end_time(end)
                wednesday.set_value(jal)
                liste = self.get_all_standard_weekly_jal_entries_by_weekday(3)
                entries = self.get_all_jal_standard_entries_wednesday()
                for elem in entries:
                    if self.overlapping(str(elem.get_end_time()), str(start)) is True:
                        for y in liste:
                            if y.get_wednesday_id() == elem.get_id():
                                self.delete_entry_in_standard_weeklyplan_jal(y)
                                self.delete_standard_entry_wednesday(elem)
                        print(elem, 'wurde gelöscht.')
                with WednesdayMapper() as mapper:
                    mapper.insert(wednesday)
                standard_entry = WeeklyPlanTempBO()
                last_entry = self.get_latest_jal_standard_entry_wednesday()
                standard_entry.set_wednesday_id(last_entry.get_id())
                standard_entry.set_weekday(3)
                with WeeklyPlanTempMapper() as mapper:
                    return mapper.insert(standard_entry)

    def get_all_jal_standard_entries_wednesday(self):
        with WednesdayMapper() as mapper:
            return mapper.find_all_jal_entries()

    def get_latest_jal_standard_entry_wednesday(self):
        with WednesdayMapper() as mapper:
            return mapper.find_latest_jal_entry()

    def set_jal_standard_entry_thursday(self, start, end, jal):
        rules = self.get_all_jal_rules()
        for elem in rules:
            if jal > elem.get_max() or jal < elem.get_min():
                message = 'Das geht so nicht!', jal, 'Mindestjal:', elem.get_min(), 'Maxjal:', elem.get_max()
                return message
            else:
                thursday = Thursday()
                thursday.set_type('J')
                thursday.set_start_time(start)
                thursday.set_end_time(end)
                thursday.set_value(jal)
                liste = self.get_all_standard_weekly_jal_entries_by_weekday(4)
                entries = self.get_all_jal_standard_entries_thursday()
                for elem in entries:
                    if self.overlapping(str(elem.get_end_time()), str(start)) is True:
                        for y in liste:
                            if y.get_thursday_id() == elem.get_id():
                                self.delete_entry_in_standard_weeklyplan_jal(y)
                                self.delete_standard_entry_thursday(elem)
                        print(elem, 'wurde gelöscht.')
                with ThursdayMapper() as mapper:
                    mapper.insert(thursday)
                standard_entry = WeeklyPlanTempBO()
                last_entry = self.get_latest_jal_standard_entry_thursday()
                standard_entry.set_thursday_id(last_entry.get_id())
                standard_entry.set_weekday(4)
                with WeeklyPlanTempMapper() as mapper:
                    return mapper.insert(standard_entry)

    def get_all_jal_standard_entries_thursday(self):
        with ThursdayMapper() as mapper:
            return mapper.find_all_jal_entries()

    def get_latest_jal_standard_entry_thursday(self):
        with ThursdayMapper() as mapper:
            return mapper.find_latest_jal_entry()

    def set_jal_standard_entry_friday(self, start, end, jal):
        rules = self.get_all_jal_rules()
        for elem in rules:
            if jal > elem.get_max() or jal < elem.get_min():
                message = 'Das geht so nicht!', jal, 'Mindestjal:', elem.get_min(), 'Maxjal:', elem.get_max()
                return message
            else:
                friday = Friday()
                friday.set_type('J')
                friday.set_start_time(start)
                friday.set_end_time(end)
                friday.set_value(jal)
                liste = self.get_all_standard_weekly_jal_entries_by_weekday(5)
                entries = self.get_all_jal_standard_entries_friday()
                for elem in entries:
                    if self.overlapping(str(elem.get_end_time()), str(start)) is True:
                        for y in liste:
                            if y.get_friday_id() == elem.get_id():
                                self.delete_entry_in_standard_weeklyplan_jal(y)
                                self.delete_standard_entry_friday(elem)
                        print(elem, 'wurde gelöscht.')
                with FridayMapper() as mapper:
                    mapper.insert(friday)
                standard_entry = WeeklyPlanTempBO()
                last_entry = self.get_latest_jal_standard_entry_friday()
                standard_entry.set_friday_id(last_entry.get_id())
                standard_entry.set_weekday(5)
                with WeeklyPlanTempMapper() as mapper:
                    return mapper.insert(standard_entry)

    def get_all_jal_standard_entries_friday(self):
        with FridayMapper() as mapper:
            return mapper.find_all_jal_entries()

    def get_latest_jal_standard_entry_friday(self):
        with FridayMapper() as mapper:
            return mapper.find_latest_jal_entry()

    def set_temp_standard_entry_monday(self, start, end, temp):
        rules = self.get_all_temp_rules()
        for elem in rules:
            if temp > elem.get_max() or temp < elem.get_min():
                message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(), 'Maxtemp:', elem.get_max()
                return message
            else:
                monday = Monday()
                monday.set_type('T')
                monday.set_start_time(start)
                monday.set_end_time(end)
                monday.set_value(temp)
                liste = self.get_all_standard_weekly_temp_entries_by_weekday(1)
                entries = self.get_all_temp_standard_entries_monday()
                for elem in entries:
                    if self.overlapping(str(elem.get_end_time()), str(start)) is True:
                        for y in liste:
                            if y.get_monday_id() == elem.get_id():
                                self.delete_entry_in_standard_weeklyplan_temp(y)
                                self.delete_standard_entry_monday(elem)
                        print(elem, 'wurde gelöscht.')
                        self.delete_rule(elem)
                with MondayMapper() as mapper:
                    mapper.insert(monday)
                standard_entry = WeeklyPlanTempBO()
                last_entry = self.get_latest_temp_standard_entry_monday()
                standard_entry.set_monday_id(last_entry.get_id())
                standard_entry.set_weekday(1)
                with WeeklyPlanTempMapper() as mapper:
                    return mapper.insert(standard_entry)

    def get_all_temp_standard_entries_monday(self):
        with MondayMapper() as mapper:
            return mapper.find_all_temp_entries()

    def get_latest_temp_standard_entry_monday(self):
        with MondayMapper() as mapper:
            return mapper.find_latest_temp_entry()

    def delete_standard_entry_monday(self, entry):
        with MondayMapper() as mapper:
            return mapper.delete(entry)

    def set_temp_standard_entry_tuesday(self, start, end, temp):
        rules = self.get_all_temp_rules()
        for elem in rules:
            if temp > elem.get_max() or temp < elem.get_min():
                message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(), 'Maxtemp:', elem.get_max()
                return message
            else:
                tuesday = Tuesday()
                tuesday.set_type('T')
                tuesday.set_start_time(start)
                tuesday.set_end_time(end)
                tuesday.set_value(temp)
                liste = self.get_all_standard_weekly_temp_entries_by_weekday(2)
                entries = self.get_all_temp_standard_entries_tuesday()
                for elem in entries:
                    if self.overlapping(str(elem.get_end_time()), str(start)) is True:
                        for y in liste:
                            if y.get_tuesday_id() == elem.get_id():
                                self.delete_entry_in_standard_weeklyplan_temp(y)
                                self.delete_standard_entry_tuesday(elem)
                        print(elem, 'wurde gelöscht.')
                        self.delete_rule(elem)
                with TuesdayMapper() as mapper:
                    mapper.insert(tuesday)
                standard_entry = WeeklyPlanTempBO()
                last_entry = self.get_latest_temp_standard_entry_tuesday()
                standard_entry.set_tuesday_id(last_entry.get_id())
                standard_entry.set_weekday(2)
                with WeeklyPlanTempMapper() as mapper:
                    return mapper.insert(standard_entry)

    def get_all_temp_standard_entries_tuesday(self):
        with TuesdayMapper() as mapper:
            return mapper.find_all_temp_entries()

    def get_latest_temp_standard_entry_tuesday(self):
        with TuesdayMapper() as mapper:
            return mapper.find_latest_temp_entry()

    def delete_standard_entry_tuesday(self, entry):
        with TuesdayMapper() as mapper:
            return mapper.delete(entry)

    def set_temp_standard_entry_wednesday(self, start, end, temp):
        rules = self.get_all_temp_rules()
        for elem in rules:
            if temp > elem.get_max() or temp < elem.get_min():
                message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(), 'Maxtemp:', elem.get_max()
                return message
            else:
                wednesday = Wednesday()
                wednesday.set_type('T')
                wednesday.set_start_time(start)
                wednesday.set_end_time(end)
                wednesday.set_value(temp)
                liste = self.get_all_standard_weekly_temp_entries_by_weekday(3)
                entries = self.get_all_temp_standard_entries_wednesday()
                for elem in entries:
                    if self.overlapping(str(elem.get_end_time()), str(start)) is True:
                        for y in liste:
                            if y.get_wednesday_id() == elem.get_id():
                                self.delete_entry_in_standard_weeklyplan_temp(y)
                                self.delete_standard_entry_wednesday(elem)
                        print(elem, 'wurde gelöscht.')
                        self.delete_rule(elem)
                with WednesdayMapper() as mapper:
                    mapper.insert(wednesday)
                standard_entry = WeeklyPlanTempBO()
                last_entry = self.get_latest_temp_standard_entry_wednesday()
                standard_entry.set_wednesday_id(last_entry.get_id())
                standard_entry.set_weekday(3)
                with WeeklyPlanTempMapper() as mapper:
                    return mapper.insert(standard_entry)

    def get_all_temp_standard_entries_wednesday(self):
        with WednesdayMapper() as mapper:
            return mapper.find_all_temp_entries()

    def get_latest_temp_standard_entry_wednesday(self):
        with WednesdayMapper() as mapper:
            return mapper.find_latest_temp_entry()

    def delete_standard_entry_wednesday(self, entry):
        with WednesdayMapper() as mapper:
            return mapper.delete(entry)

    def set_temp_standard_entry_thursday(self, start, end, temp):
        rules = self.get_all_temp_rules()
        for elem in rules:
            if temp > elem.get_max() or temp < elem.get_min():
                message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(), 'Maxtemp:', elem.get_max()
                return message
            else:
                thursday = Thursday()
                thursday.set_type('T')
                thursday.set_start_time(start)
                thursday.set_end_time(end)
                thursday.set_value(temp)
                liste = self.get_all_standard_weekly_temp_entries_by_weekday(4)
                entries = self.get_all_temp_standard_entries_thursday()
                for elem in entries:
                    if self.overlapping(str(elem.get_end_time()), str(start)) is True:
                        for y in liste:
                            if y.get_thursday_id() == elem.get_id():
                                self.delete_entry_in_standard_weeklyplan_temp(y)
                                self.delete_standard_entry_thursday(elem)
                        print(elem, 'wurde gelöscht.')

                with ThursdayMapper() as mapper:
                    mapper.insert(thursday)
                standard_entry = WeeklyPlanTempBO()
                last_entry = self.get_latest_temp_standard_entry_thursday()
                standard_entry.set_thursday_id(last_entry.get_id())
                standard_entry.set_weekday(4)
                with WeeklyPlanTempMapper() as mapper:
                    return mapper.insert(standard_entry)

    def get_all_temp_standard_entries_thursday(self):
        with ThursdayMapper() as mapper:
            return mapper.find_all_temp_entries()

    def get_latest_temp_standard_entry_thursday(self):
        with ThursdayMapper() as mapper:
            return mapper.find_latest_temp_entry()

    def delete_standard_entry_thursday(self, entry):
        with ThursdayMapper() as mapper:
            return mapper.delete(entry)

    def set_temp_standard_entry_friday(self, start, end, temp):
        rules = self.get_all_temp_rules()
        for elem in rules:
            if temp > elem.get_max() or temp < elem.get_min():
                message = 'Das geht so nicht!', temp, 'Mindesttemp:', elem.get_min(), 'Maxtemp:', elem.get_max()
                return message
            else:
                friday = Friday()
                friday.set_type('T')
                friday.set_start_time(start)
                friday.set_end_time(end)
                friday.set_value(temp)
                liste = self.get_all_standard_weekly_temp_entries_by_weekday(5)
                entries = self.get_all_temp_standard_entries_friday()
                for elem in entries:
                    if self.overlapping(str(elem.get_end_time()), str(start)) is True:
                        for y in liste:
                            if y.get_friday_id() == elem.get_id():
                                self.delete_entry_in_standard_weeklyplan_temp(y)
                                self.delete_standard_entry_friday(elem)
                        print(elem, 'wurde gelöscht.')
                with FridayMapper() as mapper:
                    mapper.insert(friday)
                standard_entry = WeeklyPlanTempBO()
                last_entry = self.get_latest_temp_standard_entry_friday()
                standard_entry.set_friday_id(last_entry.get_id())
                standard_entry.set_weekday(5)
                with WeeklyPlanTempMapper() as mapper:
                    return mapper.insert(standard_entry)

    def get_all_temp_standard_entries_friday(self):
        with FridayMapper() as mapper:
            return mapper.find_all_temp_entries()

    def get_latest_temp_standard_entry_friday(self):
        with FridayMapper() as mapper:
            return mapper.find_latest_temp_entry()

    def delete_standard_entry_friday(self, entry):
        with FridayMapper() as mapper:
            mapper.delete(entry)

    def get_all_entries_standard_weekly_plan_jal(self):
        with WeeklyPlanJalMapper() as mapper:
            return mapper.find_all()

    def get_all_standard_weekly_jal_entries_by_weekday(self, weekday):
        with WeeklyPlanJalMapper() as mapper:
            return mapper.find_by_weekday(weekday)

    def get_all_standard_weekly_temp_entries_by_weekday(self, weekday):
        with WeeklyPlanTempMapper() as mapper:
            return mapper.find_by_weekday(weekday)

    def delete_entry_in_standard_weeklyplan_jal(self, entry):
        with WeeklyPlanJalMapper() as mapper:
            mapper.delete(entry)

    def delete_entry_in_standard_weeklyplan_temp(self, entry):
        with WeeklyPlanTempMapper() as mapper:
            mapper.delete(entry)

    '''Regel-Operationen'''

    def set_jal_rule(self, min, max, start, end):
        rule = RulesBO()
        rule.set_min(min)
        rule.set_max(max)
        rule.set_type('J')
        rule.set_start_time(start)
        rule.set_end_time(end)
        rules = self.get_all_jal_rules()
        start = time.strptime(start.split(',')[0], '%H:%M:%S')
        start = datetime.timedelta(hours=start.tm_hour, minutes=start.tm_min, seconds=start.tm_sec).total_seconds()
        end = time.strptime(end.split(',')[0], '%H:%M:%S')
        end = datetime.timedelta(hours=end.tm_hour, minutes=end.tm_min, seconds=end.tm_sec).total_seconds()
        for elem in rules:
            if self.in_between_times(start, elem.get_start_time().total_seconds(),
                                     elem.get_end_time().total_seconds()) or \
                    self.in_between_times(end, elem.get_start_time().total_seconds(),
                                          elem.get_end_time().total_seconds()):
                self.delete_rule(elem)
                print(elem, 'wurde gelöscht.')
        with RulesMapper() as mapper:
            return mapper.insert(rule)

    def delete_rule(self, rule):
        with RulesMapper() as mapper:
            mapper.delete(rule)

    def set_temp_rule(self, min, max, start, end):
        rule = RulesBO()
        rule.set_min(min)
        rule.set_max(max)
        rule.set_type('T')
        rule.set_start_time(start)
        rule.set_end_time(end)
        rules = self.get_all_temp_rules()
        for elem in rules:
            if self.in_between_times(start, elem.get_start_time(), elem.get_end_time()):
                print('hier')
            elif self.overlapping(start, end, elem.get_start_time(), elem.get_end_time()):
                self.delete_rule(elem)
                print(elem, 'wurde gelöscht.')
                self.delete_rule(elem)
            else:
                print('nichts passiert', start, end, elem.get_start_time(), elem.get_end_time())
        with RulesMapper() as mapper:
            return mapper.insert(rule)

    def get_all_rules(self):
        with RulesMapper() as mapper:
            return mapper.find_all()

    def get_all_jal_rules(self):
        with RulesMapper() as mapper:
            return mapper.find_by_type('J')

    def get_all_temp_rules(self):
        with RulesMapper() as mapper:
            return mapper.find_by_type('T')

    def get_rule_by_id(self, id):
        with RulesMapper() as mapper:
            return mapper.find_by_key(id)

    def overlapping(self, new_start, new_end, old_start = datetime.timedelta, old_end = datetime.timedelta):
        new_start = datetime.datetime.strptime(new_start, '%H:%M:%S').hour
        new_start = new_start * 3600
        #new_start = float(new_start)
        new_end = datetime.datetime.strptime(new_end, '%H:%M:%S').hour
        new_end = new_end * 60 *60
        #new_end = float(new_end)
        #new_end = new_end
        old_start = 0
        old_end = old_end.total_seconds()
        print(new_start, new_end, old_start, old_end)
        if old_end <= new_start and old_start >= new_end:
            return True
        else:
            return False

    ##### Customized Entries ######

    '''def set_jal_customized_entry_monday(self, start, end, perc):
        monday = Monday()
        monday.set_type('J')
        monday.set_start_time(start)
        monday.set_end_time(end)
        monday.set_value(perc)
        with MondayMapper() as mapper:
            return mapper.insert(monday)

    def get_all_jal_customized_entries_monday(self):
        with MondayMapper() as mapper:
            return mapper.find_all()

    def set_jal_customized_entry_tuesday(self, start, end, perc):
        tuesday = Tuesday()
        tuesday.set_type('J')
        tuesday.set_start_time(start)
        tuesday.set_end_time(end)
        tuesday.set_value(perc)
        with TuesdayMapper() as mapper:
            return mapper.insert(tuesday)

    def get_all_jal_customized_entries_tuesday(self):
        with TuesdayMapper() as mapper:
            return mapper.find_all()

    def set_jal_customized_entry_wednesday(self, start, end, perc):
        wednesday = Wednesday()
        wednesday.set_type('J')
        wednesday.set_start_time(start)
        wednesday.set_end_time(end)
        wednesday.set_value(perc)
        with WednesdayMapper() as mapper:
            return mapper.insert(wednesday)

    def get_all_jal_customized_entries_wednesday(self):
        with WednesdayMapper() as mapper:
            return mapper.find_all()

    def set_jal_customized_entry_thursday(self, start, end, perc):
        thursday = Thursday()
        thursday.set_type('J')
        thursday.set_start_time(start)
        thursday.set_end_time(end)
        thursday.set_value(perc)
        with ThursdayMapper() as mapper:
            return mapper.insert(thursday)

    def get_all_jal_customized_entries_thursday(self):
        with ThursdayMapper() as mapper:
            return mapper.find_all()

    def set_jal_customized_entry_friday(self, start, end, perc):
        friday = Friday()
        friday.set_type('J')
        friday.set_start_time(start)
        friday.set_end_time(end)
        friday.set_value(perc)
        with FridayMapper() as mapper:
            return mapper.insert(friday)

    def get_all_jal_customized_entries_friday(self):
        with FridayMapper() as mapper:
            return mapper.find_all()

    def set_temp_customized_entry_monday(self, start, end, temp):
        monday = Monday()
        monday.set_type('T')
        monday.set_start_time(start)
        monday.set_end_time(end)
        monday.set_value(temp)
        with MondayMapper() as mapper:
            return mapper.insert(monday)

    def get_all_temp_customized_entries_monday(self):
        with MondayMapper() as mapper:
            return mapper.find_all()

    def set_temp_customized_entry_tuesday(self, start, end, temp):
        tuesday = Tuesday()
        tuesday.set_type('T')
        tuesday.set_start_time(start)
        tuesday.set_end_time(end)
        tuesday.set_value(temp)
        with TuesdayMapper() as mapper:
            return mapper.insert(tuesday)

    def get_all_temp_customized_entries_tuesday(self):
        with TuesdayMapper() as mapper:
            return mapper.find_all()

    def set_temp_customized_entry_wednesday(self, start, end, temp):
        wednesday = Wednesday()
        wednesday.set_type('T')
        wednesday.set_start_time(start)
        wednesday.set_end_time(end)
        wednesday.set_value(temp)
        with WednesdayMapper() as mapper:
            return mapper.insert(wednesday)

    def get_all_temp_customized_entries_wednesday(self):
        with WednesdayMapper() as mapper:
            return mapper.find_all()

    def set_temp_customized_entry_thursday(self, start, end, temp):
        thursday = Thursday()
        thursday.set_type('T')
        thursday.set_start_time(start)
        thursday.set_end_time(end)
        thursday.set_value(temp)
        with ThursdayMapper() as mapper:
            return mapper.insert(thursday)

    def get_all_temp_customized_entries_thursday(self):
        with ThursdayMapper() as mapper:
            return mapper.find_all()

    def set_temp_customized_entry_friday(self, start, end, temp):
        friday = Friday()
        friday.set_type('T')
        friday.set_start_time(start)
        friday.set_end_time(end)
        friday.set_value(temp)
        with FridayMapper() as mapper:
            return mapper.insert(friday)

    def get_all_temp_customized_entries_friday(self):
        with FridayMapper() as mapper:
            return mapper.find_all()'''


d = DeviceAdministration()
d.set_temp_rule(200, 400, '17:00:00', '18:30:00')
i = d.get_all_temp_rules()
for elem in i:
    print(elem)

