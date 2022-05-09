class Thermostat():
    """
    Klasse für Thermostat
    """

    def __init__(self, ain, port):
        self._ain = ain
        self._port = port

    def get_ain(self):
        return self._ain

    def set_ain(self, ain):
        self._ain = ain

    def get_port(self):
        return self._port

    def set_port(self, port):
        self._port = port

    def __str__(self):
        """Erzeugen einer einfachen textuellen Repräsentation der jeweiligen Kontoinstanz."""
        return "Jalousie: ain {}, port {}".format(self.get_ain(), self.get_port())

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Account()."""
        obj = Thermostat()
        obj.set_ain(dictionary["ain"])
        obj.set_port(dictionary["port"])
        return obj
