from flaskr.server.database.Mapper import Mapper
from flaskr.server.bo.weekdays_jal.FridayBO import Friday


class FridayMapper(Mapper):

    def __init__(self):
        super().__init__()

    def insert(self, friday):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM friday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                friday.set_id(1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                friday.set_id(maxid[0] + 1)

        command = "INSERT INTO friday (id, type, start_time, end_time, value) VALUES (%s, %s, %s, %s, %s)"
        data = (
            friday.get_id(),
            friday.get_type(),
            friday.get_start_time(),
            friday.get_end_time(),
            friday.get_value()
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return friday

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM friday"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            friday = Friday()
            friday.set_id(id)
            friday.set_type(type)
            friday.set_start_time(start_time)
            friday.set_end_time(end_time)
            friday.set_value(value)
            result.append(friday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT * FROM friday WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, type, start_time, end_time, value) = tuples[0]
            friday = Friday()
            friday.set_id(id)
            friday.set_type(type)
            friday.set_start_time(start_time)
            friday.set_end_time(end_time)
            friday.set_value(value)
            result = friday

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
        command = "SELECT * FROM friday WHERE type='J'"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            friday = Friday()
            friday.set_id(id)
            friday.set_type(type)
            friday.set_start_time(start_time)
            friday.set_end_time(end_time)
            friday.set_value(value)
            result.append(friday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_all_temp_entries(self):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM friday WHERE type='T'"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            friday = Friday()
            friday.set_id(id)
            friday.set_type(type)
            friday.set_start_time(start_time)
            friday.set_end_time(end_time)
            friday.set_value(value)
            result.append(friday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_latest_jal_entry(self):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM friday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            command = "SELECT * FROM friday WHERE id={} and type='J'".format(maxid[0])
            cursor.execute(command)
            tuples = cursor.fetchall()

            try:
                (id, type, start_time, end_time, value) = tuples[0]
                friday = Friday()
                friday.set_id(id)
                friday.set_type(type)
                friday.set_start_time(start_time)
                friday.set_end_time(end_time)
                friday.set_value(value)
                result = friday

            except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
                keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
                result = None

            self._cnx.commit()
            cursor.close()

            return result

    def find_latest_temp_entry(self):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM friday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            command = "SELECT * FROM friday WHERE id={} and type='T'".format(maxid[0])
            cursor.execute(command)
            tuples = cursor.fetchall()

            try:
                (id, type, start_time, end_time, value) = tuples[0]
                friday = Friday()
                friday.set_id(id)
                friday.set_type(type)
                friday.set_start_time(start_time)
                friday.set_end_time(end_time)
                friday.set_value(value)
                result = friday

            except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
                keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
                result = None

            self._cnx.commit()
            cursor.close()

            return result

    def update(self, friday):
        cursor = self._cnx.cursor()

        command = "UPDATE friday " + \
                  "SET value=%s, start_time=%s, end_time=%s WHERE id=%s and type=%s"
        data = (friday.get_value(), friday.get_start_time(), friday.get_end_time(), friday.get_id(), friday.get_type())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return friday

    def delete(self, friday):
        cursor = self._cnx.cursor()

        command = "DELETE FROM friday WHERE id=%s and type=%s"
        data = (friday.get_id(), friday.get_type())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
