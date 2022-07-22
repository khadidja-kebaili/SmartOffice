from flaskr.server.database.Mapper import Mapper
from flaskr.server.bo.weekdays_jal.ThursdayBO import Thursday

class ThursdayMapper(Mapper):
    '''
    Implemenierung der Mapper-Klasse für Wochenplaneinträge am Donnerstag.
    Hierzu wird eine Reihe von Methoden zur Verfügung gestellt, mit deren Hilfe z.B.
    Objekte gesucht, erzeugt, modifiziert und gelöscht werden können.
    Das Mapping ist bidirektional. D.h., Objekte können in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    '''

    def __init__(self):
        super().__init__()

    def insert(self, thursday):
        """Einfügen eines Thursday-Objekts in die Datenbank.

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft und ggf.
        berichtigt.

        :param thursday das zu speichernde Objekt
        :return das bereits übergebene Objekt, jedoch mit ggf. korrigierter ID.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM thursday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                thursday.set_id(1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                thursday.set_id(maxid[0]+1)

        command = "INSERT INTO thursday (id, type, start_time, end_time, value) VALUES (%s, %s, %s, %s, %s)"
        data = (
            thursday.get_id(),
            thursday.get_type(),
            thursday.get_start_time(),
            thursday.get_end_time(),
            thursday.get_value()
            )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return thursday

    def find_all(self):
        """
        Auslesen aller Einträge zu Donnerstag.
        :return: Array mit ThursdayBOs
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM thursday"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            thursday = Thursday()
            thursday.set_id(id)
            thursday.set_type(type)
            thursday.set_start_time(start_time)
            thursday.set_end_time(end_time)
            thursday.set_value(value)
            result.append(thursday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        """
        Lädt einen Donnerstagseintrag aus der Datenbank mithilfe der Id
        :param id: ThursdayBO-Id
        :return: ThursdayBO
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT * FROM thursday WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, type, start_time, end_time, value) = tuples[0]
            thursday = Thursday()
            thursday.set_id(id)
            thursday.set_type(type)
            thursday.set_start_time(start_time)
            thursday.set_end_time(end_time)
            thursday.set_value(value)
            result = thursday

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_all_jal_entries(self):
        '''
        Lädt alle  Jalousien-Eintrage am Donnertstag aus der Datenbank
        :return: Liste mit ThursdayBOs
        '''
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM thursday WHERE type='J'"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            thursday = Thursday()
            thursday.set_id(id)
            thursday.set_type(type)
            thursday.set_start_time(start_time)
            thursday.set_end_time(end_time)
            thursday.set_value(value)
            result.append(thursday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_all_temp_entries(self):
        '''
        Lädt alle  Thermostat-Eintrage am Donnertstag aus der Datenbank
        :return: Liste mit ThursdayBOs
        '''
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM thursday WHERE type='T'"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type, start_time, end_time, value) in tuples:
            thursday = Thursday()
            thursday.set_id(id)
            thursday.set_type(type)
            thursday.set_start_time(start_time)
            thursday.set_end_time(end_time)
            thursday.set_value(value)
            result.append(thursday)

        self._cnx.commit()
        cursor.close()

        return result

    def find_latest_jal_entry(self):
        '''
        Lädt den letzten Jalousien-Eintrag am Donnerstag aus der Datenbank
        :return: ThursdayBO
        '''
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM thursday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            command = "SELECT * FROM thursday WHERE id={} and type='J'".format(maxid[0])
            cursor.execute(command)
            tuples = cursor.fetchall()

            try:
                (id, type, start_time, end_time, value) = tuples[0]
                thursday = Thursday()
                thursday.set_id(id)
                thursday.set_type(type)
                thursday.set_start_time(start_time)
                thursday.set_end_time(end_time)
                thursday.set_value(value)
                result = thursday

            except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
                keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
                result = None

            self._cnx.commit()
            cursor.close()

            return result

    def find_latest_temp_entry(self):
        '''
        Lädt den letzten Thermostat-Eintrag am Donnerstag aus der Datenbank
        :return: ThursdayBO
        '''
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM thursday")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            command = "SELECT * FROM thursday WHERE id={} and type='T'".format(maxid[0])
            cursor.execute(command)
            tuples = cursor.fetchall()

            try:
                (id, type, start_time, end_time, value) = tuples[0]
                thursday = Thursday()
                thursday.set_id(id)
                thursday.set_type(type)
                thursday.set_start_time(start_time)
                thursday.set_end_time(end_time)
                thursday.set_value(value)
                result = thursday

            except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
                keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
                result = None

            self._cnx.commit()
            cursor.close()

            return result

    def update(self, thursday):
        """Wiederholtes Schreiben eines Objekts in die Datenbank.

        :param jalousie das Objekt, das in die DB geschrieben werden soll
        """
        cursor = self._cnx.cursor()

        command = "UPDATE thursday " + \
            "SET value=%s, start_time=%s, end_time=%s WHERE id=%s and type=%s"
        data = (thursday.get_value(), thursday.get_start_time(), thursday.get_end_time(), thursday.get_id(), thursday.get_type())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return thursday

    def delete(self, thursday):
        """
        Löschen eines Donnerstag-Objekts aus der Datenbank.

        :param thursday: das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM thursday WHERE id=%s and type=%s"
        data = (thursday.get_id(), thursday.get_type())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

