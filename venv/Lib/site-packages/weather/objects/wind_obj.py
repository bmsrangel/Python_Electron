class Wind(object):
    def __init__(self, data):
        self._wind_data = data

    @property
    def chill(self):
        return self._wind_data['chill']

    @property
    def direction(self):
        return self._wind_data['direction']

    @property
    def speed(self):
        return self._wind_data['speed']
