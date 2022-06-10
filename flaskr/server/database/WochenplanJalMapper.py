from database.Mapper import Mapper
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

        command = "INSERT INTO weeklyplanjal (id, 1, 2, 3, 4, 5) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (
            weeklyplanjal.get_id(),

        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return weeklyplanjal

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM weeklyplanjal"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id) in tuples:
            weeklyplanjal = WeeklyPlanJalBO()
            weeklyplanjal.set_id(id)
            result.append(weeklyplanjal)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        cursor = self._cnx.cursor()
        command = "SELECT * FROM weeklyplanjal WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id) = tuples[0]
            weeklyplanjal = WeeklyPlanJalBO()
            weeklyplanjal.set_id(id)
            result = weeklyplanjal

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, weeklyplanjal):
        cursor = self._cnx.cursor()

        command = "UPDATE weeklyplanjal " + \
            "SET ain=%s WHERE id=%s"
        data = (weeklyplanjal.get_current_valid_weekly_plan())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return weeklyplanjal

    def delete(self, weeklyplanjal):
        cursor = self._cnx.cursor()

        command = "DELETE FROM weeklyplanjal WHERE id={}".format(
            weeklyplanjal.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


ex = WeeklyPlanJalBO()
ex.set_standard_weekly_plan(240, '2022-06-09 08:00:00')
ex.set_standard_weekly_plan(245, '2022-06-09 09:00:00')
ex.set_standard_weekly_plan(230, '2022-06-08 11:00:00')
ex.set_standard_weekly_plan(220, '2022-06-08 13:00:00')
ex.set_standard_weekly_plan(210, '2022-06-08 14:00:00')


ex.set_id(1)

l = WeeklyPlanJalMapper()
with l as mapper:
    mapper.insert(ex)