class Unit(object):
    def __init__(self, data):
        self._unit_data = data

    @property
    def distance(self):
        return self._unit_data['distance']

    @property
    def pressure(self):
        return self._unit_data['pressure']

    @property
    def speed(self):
        return self._unit_data['speed']

    @property
    def temperature(self):
        return self._unit_data['temperature']
