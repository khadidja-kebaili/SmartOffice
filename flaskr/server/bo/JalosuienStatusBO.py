from server.bo.BusinessObject import Businessobject as bo


class JalousienStatusBO(bo):
    """
    Klasse für Jalousien
    """

    def __init__(self):
        super().__init__()
        self._jalousieid = None
        self._status = ''
        self._percentage = None

    def set_percentage(self, perc):
        self._percentage = perc

    def get_percentage(self):
        return self._percentage

    def set_status(self, status):
        self._status = status

    def get_status(self):
        return self._status

    def get_device(self):
        return self._jalousieid

    def set_device(self, id):
        self._jalousieid = id

    def __str__(self):
        """Erzeugen einer einfachen textuellen Repräsentation der jeweiligen Kontoinstanz."""
        return "JalousieStatus: id {}, percentage: {}, status {}, jalousieid {}".format(
            self.get_id(), self.get_percentage(), self.get_status(), self.get_device())

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Account()."""
        obj = JalousienStatusBO()
        obj.set_id(dictionary["id"])
        obj.set_percentage(dictionary["percentage"])
        obj.set_status(dictionary["status"])
        obj.set_device(dictionary["jalousieid"])
        return obj
