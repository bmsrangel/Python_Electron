class Location(object):
    def __init__(self, location_data):
        self._location_data = location_data

    @property
    def city(self):
        return self._location_data['city']

    @property
    def country(self):
        return self._location_data['country']

    @property
    def region(self):
        return self._location_data['region']
