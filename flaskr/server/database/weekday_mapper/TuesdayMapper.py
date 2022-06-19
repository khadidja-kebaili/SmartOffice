from flaskr.server.database.Mapper import Mapper
from flaskr.server.bo.weekdays_jal.TuesdayBO import Tuesday

class TuesdayMapper(Mapper):

    def __init__(self):
        super().__init__()

    def insert(self, tuesday):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM tuesday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                tuesday.set_id(1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                tuesday.set_id(maxid[0]+1)

        command = "INSERT INTO tuesday (id, type, start_time, end_time, value) VALUES (%s, %s, %s, %s, %s)"
        data = (
            tuesday.get_id(),
            tuesday.get_type(),
            tuesday.get_start_time(),
            tuesday.get_end_time(),
            tuesday.get_value()
            )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return tuesday

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM tuesday"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            tuesday = Tuesday()
            tuesday.set_id(id)
            tuesday.set_type(type)
            tuesday.set_start_time(start_time)
            tuesday.set_end_time(end_time)
            tuesday.set_value(value)
            result.append(tuesday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT * FROM tuesday WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, type, start_time, end_time, value) = tuples[0]
            tuesday = Tuesday()
            tuesday.set_id(id)
            tuesday.set_type(type)
            tuesday.set_start_time(start_time)
            tuesday.set_end_time(end_time)
            tuesday.set_value(value)
            result = tuesday

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_all_jal_entries(self):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM tuesday WHERE type='J'"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            tuesday = Tuesday()
            tuesday.set_id(id)
            tuesday.set_type(type)
            tuesday.set_start_time(start_time)
            tuesday.set_end_time(end_time)
            tuesday.set_value(value)
            result.append(tuesday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_all_temp_entries(self):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM tuesday WHERE type='T'"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            tuesday = Tuesday()
            tuesday.set_id(id)
            tuesday.set_type(type)
            tuesday.set_start_time(start_time)
            tuesday.set_end_time(end_time)
            tuesday.set_value(value)
            result.append(tuesday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_latest_jal_entry(self):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM tuesday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            command = "SELECT * FROM tuesday WHERE id={} and type='J'".format(maxid[0])
            cursor.execute(command)
            tuples = cursor.fetchall()

            try:
                (id, type, start_time, end_time, value) = tuples[0]
                tuesday = Tuesday()
                tuesday.set_id(id)
                tuesday.set_type(type)
                tuesday.set_start_time(start_time)
                tuesday.set_end_time(end_time)
                tuesday.set_value(value)
                result = tuesday

            except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
                keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
                result = None

            self._cnx.commit()
            cursor.close()

            return result

    def find_latest_temp_entry(self):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM tuesday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            command = "SELECT * FROM tuesday WHERE id={} and type='T'".format(maxid[0])
            cursor.execute(command)
            tuples = cursor.fetchall()

            try:
                (id, type, start_time, end_time, value) = tuples[0]
                tuesday = Tuesday()
                tuesday.set_id(id)
                tuesday.set_type(type)
                tuesday.set_start_time(start_time)
                tuesday.set_end_time(end_time)
                tuesday.set_value(value)
                result = tuesday

            except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
                keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
                result = None

            self._cnx.commit()
            cursor.close()

            return result

    def update(self, tuesday):
        cursor = self._cnx.cursor()

        command = "UPDATE tuesday " + \
            "SET value=%s, start_time=%s, end_time=%s WHERE id=%s and type=%s"
        data = (tuesday.get_value(), tuesday.get_start_time(), tuesday.get_end_time(), tuesday.get_id(), tuesday.get_type())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return tuesday

    def delete(self, tuesday):
        cursor = self._cnx.cursor()

        command = "DELETE FROM tuesday WHERE id={} and type=%s".format(
            tuesday.get_id(), tuesday.get_type())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

