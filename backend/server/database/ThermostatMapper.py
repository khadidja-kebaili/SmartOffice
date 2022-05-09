from .Mapper import Mapper
from ..bo.Thermostat import Thermostat


class ThermostatMapper(Mapper):

    def __init__(self):
        super().__init__()

    def insert(self, thermostat):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM demo.demo ")
        tuples = cursor.fetchall()
        for (maxid) in tuples:
            if maxid[0] is not None:
                thermostat.set_ain(maxid[0] + 1)

            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                thermostat.set_ain(1)

        command = "INSERT INTO demo.demo (ain, port) VALUES (%s, %s)"
        data = (
            thermostat.get_ain(),
            thermostat.get_port()
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return thermostat

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, dateoflastchange, time FROM demo.demo"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, port) in tuples:
            thermostat = Thermostat()
            thermostat.set_ain(id)
            thermostat.set_port(port)
            result.append(thermostat)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_ain(self, ain):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT ain, port, time FROM demo.demo WHERE id={}".format(
            ain)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (ain, port) = tuples[0]
            thermostat = Thermostat()
            thermostat.set_ain(ain)
            thermostat.set_port(port)
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

        command = "UPDATE demo.demo " + \
            "SET x=%s WHERE id=%s"
        data = (thermostat.get_port(),
                thermostat.get_ain())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return thermostat

    def delete(self, thermostat):
        cursor = self._cnx.cursor()

        command = "DELETE FROM demo.demo WHERE id={}".format(
            thermostat.get_ain())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
