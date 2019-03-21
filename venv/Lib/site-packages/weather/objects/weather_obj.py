from .forecast_obj import Forecast
from .condition_obj import Condition
from .location_obj import Location
from .unit_obj import Unit
from .wind_obj import Wind
from .astronomy_obj import Astronomy
from .atmosphere_obj import Atmosphere


class WeatherObject(object):
    def __init__(self, weather_data):
        self._weather_data = weather_data

    def __str__(self):
        return self._weather_data

    @property
    def last_build_date(self):
        return self._weather_data['lastBuildDate']

    @property
    def title(self):
        return self._weather_data['title']

    @property
    def description(self):
        return self._weather_data['description']

    @property
    def language(self):
        return self._weather_data['language']

    @property
    def astronomy(self):
        return Astronomy(self._weather_data['astronomy'])

    @property
    def atmosphere(self):
        return Atmosphere(self._weather_data['atmosphere'])

    @property
    def image(self):
        return self._weather_data['image']

    @property
    def condition(self):
        return Condition(self._weather_data['item']['condition'])

    @property
    def units(self):
        return Unit(self._weather_data['units'])

    @property
    def forecast(self):
        forecasts = []
        [forecasts.append(Forecast(res)) for res in self._weather_data['item']['forecast']]
        return forecasts

    @property
    def latitude(self):
        return self._weather_data['item']['lat']

    @property
    def longitude(self):
        return self._weather_data['item']['long']

    @property
    def location(self):
        return Location(self._weather_data['location'])

    @property
    def wind(self):
        return Wind(self._weather_data['wind'])

    @property
    def print_obj(self):
        return self._weather_data
