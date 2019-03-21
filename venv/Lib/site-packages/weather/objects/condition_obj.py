class Condition(object):
    def __init__(self, condition_data):
        self._condition_data = condition_data

    @property
    def date(self):
        return self._condition_data['date']

    @property
    def text(self):
        return self._condition_data['text']

    @property
    def code(self):
        return self._condition_data['code']

    @property
    def temp(self):
        return self._condition_data['temp']
