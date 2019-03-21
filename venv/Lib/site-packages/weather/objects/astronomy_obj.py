from weather.helpers import add_leading_zero


class Astronomy(object):

    def __init__(self, astronomy_data):
        self._astronomy_data = astronomy_data

    @property
    def sunrise(self):
        return add_leading_zero(self._astronomy_data['sunrise'])

    @property
    def sunset(self):
        return add_leading_zero(self._astronomy_data['sunset'])

