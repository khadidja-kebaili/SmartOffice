from .Mapper import Mapper
from server.bo.WochenplanJalBO import WeeklyPlanJalBO

class WeeklyPlanJalMapper(Mapper):

    def __init__(self):
        super().__init__()

    def insert(self, weeklyplanjal):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM weeklyplanjal ")
        tuples = cursor.fetchall()
        for (maxid) in tuples:
            if len(maxid) == 1:
                weeklyplanjal.set_id(1)
            else:
                weeklyplanjal.set_id(int(maxid[0]) + 1)

        command = "INSERT INTO weeklyplanjal (id, ain) VALUES (%s, %s)"
        data = (
            weeklyplanjal.get_id(),
            weeklyplanjal.get_current_valid_weekly_plan(),
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return weeklyplanjal

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, 1, 2, 3, 4, 5 FROM weeklyplanjal"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id) in tuples:
            weeklyplanjal = WeeklyPlanJalBO
            weeklyplanjal.set_id(id)
            result.append(weeklyplanjal)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_ain(self, ain):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT ain FROM weeklyplanjal WHERE ain={}".format(
            ain)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (ain) = tuples[0]
            thermostat = ThermostatBO()
            thermostat.set_ain(ain)
            result = thermostat

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, id):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT ain  FROM weeklyplanjal WHERE id={}".format(
            id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id) = tuples[0]
            thermostat = ThermostatBO()
            thermostat.set_id(id)
            result = thermostat

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, thermostat):
        cursor = self._cnx.cursor()

        command = "UPDATE weeklyplanjal " + \
            "SET ain=%s WHERE id=%s"
        data = (thermostat.get_ain())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return thermostat

    def delete(self, thermostat):
        cursor = self._cnx.cursor()

        command = "DELETE FROM weeklyplanjal WHERE id={}".format(
            thermostat.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
