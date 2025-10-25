import datetime

class Utils:
    def conversor_de_data(o):
        if isinstance(o, datetime.date):
            return o.isoformat()