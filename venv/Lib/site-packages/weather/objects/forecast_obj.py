from weather.helpers import add_leading_zero


class Forecast(object):
    def __init__(self, forecast_data):
        self._forecast_data = forecast_data

    @property
    def text(self):
        return self._forecast_data['text']

    @property
    def date(self):
        return add_leading_zero(self._forecast_data['date'])

    @property
    def high(self):
        return self._forecast_data['high']

    @property
    def low(self):
        return self._forecast_data['low']

    @property
    def code(self):
        return self._forecast_data['code']

    @property
    def day(self):
        return self._forecast_data['day']
