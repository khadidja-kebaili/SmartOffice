from flaskr.server.bo.weekdays_jal.WeekdayBO import Weekday


class Thursday(Weekday):

    def __init__(self):
        super().__init__()


    def __str__(self):
        return "Id: {}, Type of entry: {}, Start of timeinterval: {}, End of timeinterval: {},  Percentage: {}".format(
            self.get_id(), self.get_type(), self.get_start_time(), self.get_end_time(), self.get_percentage())

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Thursday()
        obj.set_id(dictionary['id'])
        obj.set_type(dictionary['type'])
        obj.set_start_time(dictionary['starttime'])
        obj.set_end_time(dictionary['endtime'])
