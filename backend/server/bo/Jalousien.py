from bo.BusinessObject import BusinessObject


class Jalousien(BusinessObject):
    """
    Klasse für Jalousien
    """

    def __init__(self, device_id, ip_address, local_key):
        super().__init__()
        self._device_id = device_id
        self._ip_address = ip_address
        self._local_key = local_key
        self._temperature = None

    def set_device_id(self):
        return self._device_id

    def get_device_id(self, device_id):
        self._device_id = device_id

    def set_ip_address(self):
        return self._ip_address

    def get_ip_address(self, ip_address):
        self._ip_address = ip_address

    def set_local_key(self):
        return self._local_key

    def get_local_key(self, local_key):
        self._local_key = local_key

    def set_temperature(self, temp):
        self._temperature = temp

    def get_temperature(self):
        return self._temperature

    def __str__(self):
        """Erzeugen einer einfachen textuellen Repräsentation der jeweiligen Kontoinstanz."""
        return "Jalousie: id {}, device_id {}, ip_address {}, local_key {}, temperature {}".format(
            self.get_id(), self.get_device_id(), self.get_ip_address(), self.get_local_key(), self.get_temperature())

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Account()."""
        obj = Jalousien()
        obj.set_id(dictionary["id"])
        obj.set_device_id(dictionary["device_id"])
        obj.set_ip_address(dictionary["ip_address"])
        obj.set_local_key(dictionary['local_key'])
        obj.set_temperature(dictionary['temperature'])
        return obj
