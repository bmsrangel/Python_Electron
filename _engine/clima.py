import requests
import sys

cidade = sys.argv[1]

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=affd802027fb6de23f9747fc5860c449&q='
url = api_address + cidade
# json_data = requests.get(url).json()
json_data = {"coord":{"lon":-0.13,"lat":51.51},
             "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],
             "base":"stations","main":{"temp":286.49,"pressure":1032,"humidity":62,"temp_min":284.82,"temp_max":288.15},
             "visibility":10000,"wind":{"speed":2.1,"deg":230},"clouds":{"all":75},"dt":1553185045,
             "sys":{"type":1,"id":1414,"message":0.0069,"country":"GB","sunrise":1553148110,"sunset":1553192025},
             "id":2643743,"name":"London","cod":200}

clima = json_data['weather'][0]['description']
temperatura = json_data['main']['temp']
temp_min = json_data['main']['temp_min']
temp_max = json_data['main']['temp_max']
pressão = json_data['main']['pressure']
velocidade_vento = json_data['wind']['speed']
direção_vento = json_data['wind']['deg']

print(f'A temperatura atual é {temperatura}°C com mínima de {temp_min}°C e máxima de {temp_max}°C')


sys.stdout.flush()


