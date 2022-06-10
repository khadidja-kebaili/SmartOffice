from database.Mapper import Mapper
from bo.RulesBO import RulesBO

class RulesMapper(Mapper):

    def __init__(self):
        super().__init__()

    def insert(self, rule):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM rules ")
        tuples = cursor.fetchall()
        for (maxid) in tuples:
            if len(maxid) == 1:
                rule.set_id(1)
            else:
                rule.set_id(int(maxid[0]) + 1)

        command = "INSERT INTO rules (id, ain) VALUES (%s, %s)"
        data = (
            rule.get_max_temperature(),
            rule.get_min_temperature(),
        )

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return rule

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, ain FROM rules"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id) in tuples:
            rule = RuleBO()
            rule.set_id(id)
            result.append(rule)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_ain(self, ain):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT ain FROM rules WHERE ain={}".format(
            ain)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (ain) = tuples[0]
            rule = RuleBO()
            rule.set_ain(ain)
            result = rule

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
        command = "SELECT ain  FROM rules WHERE id={}".format(
            id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id) = tuples[0]
            rule = RuleBO()
            rule.set_id(id)
            result = rule

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def update(self, rule):
        cursor = self._cnx.cursor()

        command = "UPDATE rules " + \
            "SET ain=%s WHERE id=%s"
        data = (rule.get_ain())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return rule

    def delete(self, rule):
        cursor = self._cnx.cursor()

        command = "DELETE FROM rules WHERE id={}".format(
            rule.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
