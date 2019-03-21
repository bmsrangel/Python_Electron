class Atmosphere(object):

    def __init__(self, atmosphere_data):
        self._atmosphere_data = atmosphere_data

    @property
    def humidity(self):
        return self._atmosphere_data['humidity']

    @property
    def visibility(self):
        return self._atmosphere_data['visibility']

    @property
    def pressure(self):
        return self._atmosphere_data['pressure']

    @property
    def rising(self):
        return self._atmosphere_data['rising']
