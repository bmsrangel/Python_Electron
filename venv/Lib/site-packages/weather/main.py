from argparse import ArgumentParser
from .weather import Weather
from prettytable import PrettyTable
import sys
import colorful


def main():
    pa = ArgumentParser()
    pa.add_argument('location', help='The location to lookup.')
    pa.add_argument('--unit', help='The unit to be used. Default is Celsius.', default='c', nargs='?',
                    choices=['c', 'f'])
    pa.add_argument('--log', help='Pass this argument to output logging', default=False, action='store_true',
                    dest='log')
    pa.add_argument("--start", nargs="?", help="The forecast start")
    pa.add_argument("--end", nargs="?", help="The forecast end")
    args = pa.parse_args()
    weather = Weather(args.unit, args.log)
    loc = weather.lookup_by_location(args.location)
    condition = loc.condition
    print(colorful.bold("Weather report for %s, %s" % (loc.location.city, loc.location.country)))
    row = PrettyTable()
    row.field_names = ["Condition", "Temperature"]
    row.align = 'l'
    row.add_row([condition.text, condition.temp])
    print(row)
    print(colorful.cyan("Weather Forecasts"))
    row = PrettyTable()
    row.field_names = ["Date", "Condition", "High", "Low"]
    row.align = 'l'
    start = 0 if not args.start else int(args.start)
    end = len(loc.forecast) if not args.end else int(args.end)
    for forecast in loc.forecast[start:end]:
        row.add_row([forecast.date, forecast.text, forecast.high, forecast.low])
    print(row)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
