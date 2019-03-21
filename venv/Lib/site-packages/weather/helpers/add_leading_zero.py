import re


def add_leading_zero(time):
    compiled_date_regex = re.compile('(:\d\s)')
    if re.search(compiled_date_regex, time):
        return re.sub(':', ':0', time)
    else:
        return time
