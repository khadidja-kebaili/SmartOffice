from flaskr.server.database.Mapper import Mapper
from flaskr.server.bo.WochenplanThermoBO import WeeklyPlanTempBO


class WeeklyPlanTempMapper(Mapper):

    def __init__(self):
        super().__init__()

    def insert(self, weeklyplantemp):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM standard_temp ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                weeklyplantemp.set_id(1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                weeklyplantemp.set_id(maxid[0] + 1)

        command = "INSERT INTO standard_temp (id, weekday, monday_id, tuesday_id, wednesday_id, thursday_id, friday_id) \
                  VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (
            weeklyplantemp.get_id(),
            weeklyplantemp.get_weekday(),
            weeklyplantemp.get_monday_id(),
            weeklyplantemp.get_tuesday_id(),
            weeklyplantemp.get_wednesday_id(),
            weeklyplantemp.get_thursday_id(),
            weeklyplantemp.get_friday_id()
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return weeklyplantemp

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM standard_temp"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, weekday, monday_id, tuesday_id, wednesday_id, thursday_id, friday_id) in tuples:
            weeklyplanjal = WeeklyPlanTempBO()
            weeklyplanjal.set_id(id)
            weeklyplanjal.set_weekday(weekday),
            weeklyplanjal.set_monday_id(monday_id),
            weeklyplanjal.set_tuesday_id(tuesday_id),
            weeklyplanjal.set_wednesday_id(wednesday_id),
            weeklyplanjal.set_thursday_id(thursday_id),
            weeklyplanjal.set_friday_id(friday_id)
            result.append(weeklyplanjal)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        cursor = self._cnx.cursor()
        command = "SELECT * FROM standard_temp WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, weekday, monday_id, tuesday_id, wednesday_id, thursday_id, friday_id) = tuples[0]
            weeklyplanjal = WeeklyPlanTempBO()
            weeklyplanjal.set_id(id)
            weeklyplanjal.set_weekday(weekday),
            weeklyplanjal.set_monday_id(monday_id),
            weeklyplanjal.set_tuesday_id(tuesday_id),
            weeklyplanjal.set_wednesday_id(wednesday_id),
            weeklyplanjal.set_thursday_id(thursday_id),
            weeklyplanjal.set_friday_id(friday_id)
            result = weeklyplanjal

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_weekday(self, weekday):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM standard_temp WHERE weekday={}".format(weekday)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, weekday, monday_id, tuesday_id, wednesday_id, thursday_id, friday_id) in tuples:
            entry = WeeklyPlanTempBO()
            entry.set_id(id)
            entry.set_weekday(weekday),
            entry.set_monday_id(monday_id),
            entry.set_tuesday_id(tuesday_id),
            entry.set_wednesday_id(wednesday_id),
            entry.set_thursday_id(thursday_id),
            entry.set_friday_id(friday_id)
            result.append(entry)

        self._cnx.commit()
        cursor.close()

        return result


    def update(self, weeklyplanjal):
        cursor = self._cnx.cursor()

        command = "UPDATE standard_temp" + \
                  "SET weekday=%s, monday_id=%s, tuesday_id=%s, wednesday_id=%s, thursday_id=%s, friday_id=%s WHERE " \
                  "id=%s "
        data = (weeklyplanjal.get_id(),
                weeklyplanjal.get_weekday(),
                weeklyplanjal.get_monday_id(),
                weeklyplanjal.get_tuesday_id(),
                weeklyplanjal.get_wednesday_id(),
                weeklyplanjal.get_thursday_id(),
                weeklyplanjal.get_friday_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return weeklyplanjal

    def delete(self, entry):
        cursor = self._cnx.cursor()

        command = "DELETE FROM standard_temp WHERE id={}".format(
            entry.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
