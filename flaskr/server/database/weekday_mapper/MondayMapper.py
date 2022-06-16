from server.database.Mapper import Mapper
from server.bo.weekdays_jal.MondayBO import Monday

class MondayMapper(Mapper):

    def __init__(self):
        super().__init__()

    def insert(self, monday):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM monday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                monday.set_id(1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                monday.set_id(maxid[0]+1)

        command = "INSERT INTO monday (id, type, start_time, end_time, value) VALUES (%s, %s, %s, %s, %s)"
        data = (
            monday.get_id(),
            monday.get_type(),
            monday.get_start_time(),
            monday.get_end_time(),
            monday.get_value()
            )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return monday

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM monday"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            monday = Monday()
            monday.set_id(id)
            monday.set_type(type)
            monday.set_start_time(start_time)
            monday.set_end_time(end_time)
            monday.set_value(value)
            result.append(monday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT * FROM monday WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, type, start_time, end_time, value) = tuples[0]
            monday = Monday()
            monday.set_id(id)
            monday.set_type(type)
            monday.set_start_time(start_time)
            monday.set_end_time(end_time)
            monday.set_value(value)
            result = monday

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, monday):
        cursor = self._cnx.cursor()

        command = "UPDATE monday " + \
            "SET value=%s, start_time=%s, end_time=%s WHERE id=%s and type=%s"
        data = (monday.get_value(), monday.get_start_time(), monday.get_end_time(), monday.get_id(), monday.get_type())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return monday

    def delete(self, monday):
        cursor = self._cnx.cursor()

        command = "DELETE FROM monday WHERE id={} and type=%s".format(
            monday.get_id(), monday.get_type())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

