from flaskr.server.database.Mapper import Mapper
from flaskr.server.bo.weekdays_jal.WednesdayBO import Wednesday

class WednesdayMapper(Mapper):

    def __init__(self):
        super().__init__()

    def insert(self, wednesday):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM wednesday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                wednesday.set_id(1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                wednesday.set_id(maxid[0]+1)

        command = "INSERT INTO wednesday (id, type, start_time, end_time, value) VALUES (%s, %s, %s, %s, %s)"
        data = (
            wednesday.get_id(),
            wednesday.get_type(),
            wednesday.get_start_time(),
            wednesday.get_end_time(),
            wednesday.get_value()
            )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return wednesday

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM wednesday"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            wednesday = Wednesday()
            wednesday.set_id(id)
            wednesday.set_type(type)
            wednesday.set_start_time(start_time)
            wednesday.set_end_time(end_time)
            wednesday.set_value(value)
            result.append(wednesday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT * FROM wednesday WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, type, start_time, end_time, value) = tuples[0]
            wednesday = Wednesday()
            wednesday.set_id(id)
            wednesday.set_type(type)
            wednesday.set_start_time(start_time)
            wednesday.set_end_time(end_time)
            wednesday.set_value(value)
            result = wednesday

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
        command = "SELECT * FROM wednesday WHERE type='J'"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            wednesday = Wednesday()
            wednesday.set_id(id)
            wednesday.set_type(type)
            wednesday.set_start_time(start_time)
            wednesday.set_end_time(end_time)
            wednesday.set_value(value)
            result.append(wednesday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_all_temp_entries(self):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM wednesday WHERE type='T'"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            wednesday = Wednesday()
            wednesday.set_id(id)
            wednesday.set_type(type)
            wednesday.set_start_time(start_time)
            wednesday.set_end_time(end_time)
            wednesday.set_value(value)
            result.append(wednesday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_latest_jal_entry(self):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM wednesday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            command = "SELECT * FROM wednesday WHERE id={} and type='J'".format(maxid[0])
            cursor.execute(command)
            tuples = cursor.fetchall()

            try:
                (id, type, start_time, end_time, value) = tuples[0]
                wednesday = Wednesday()
                wednesday.set_id(id)
                wednesday.set_type(type)
                wednesday.set_start_time(start_time)
                wednesday.set_end_time(end_time)
                wednesday.set_value(value)
                result = wednesday

            except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
                keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
                result = None

            self._cnx.commit()
            cursor.close()

            return result

    def find_latest_temp_entry(self):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM wednesday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            command = "SELECT * FROM wednesday WHERE id={} and type='T'".format(maxid[0])
            cursor.execute(command)
            tuples = cursor.fetchall()

            try:
                (id, type, start_time, end_time, value) = tuples[0]
                wednesday = Wednesday()
                wednesday.set_id(id)
                wednesday.set_type(type)
                wednesday.set_start_time(start_time)
                wednesday.set_end_time(end_time)
                wednesday.set_value(value)
                result = wednesday

            except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
                keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
                result = None

            self._cnx.commit()
            cursor.close()

            return result
    def update(self, wednesday):
        cursor = self._cnx.cursor()

        command = "UPDATE wednesday " + \
            "SET value=%s, start_time=%s, end_time=%s WHERE id=%s and type=%s"
        data = (wednesday.get_value(), wednesday.get_start_time(), wednesday.get_end_time(), wednesday.get_id(), wednesday.get_type())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return wednesday

    def delete(self, wednesday):
        cursor = self._cnx.cursor()

        command = "DELETE FROM wednesday WHERE id=%s and type=%s"
        data = (wednesday.get_id(), wednesday.get_type())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

