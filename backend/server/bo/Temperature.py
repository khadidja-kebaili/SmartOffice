from .BusinessObject import Businessobject


class ThermostatBO(Businessobject):
    """
    Klasse für Thermostat
    """

    def __init__(self, temperature):
        super().__init__()
        self._temperature = temperature

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, temperature):
        self._temperature = temperature

    def __str__(self):
        """Erzeugen einer einfachen textuellen Repräsentation der jeweiligen Kontoinstanz."""
        return "Jalousie: id {}, temperature {}".format(self.get_id(), self.get_temperature())

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Account()."""
        obj = Thermostat()
        obj.set_id(dictionary["id"])
        obj.set_temperature(dictionary["temperature"])
        return obj
