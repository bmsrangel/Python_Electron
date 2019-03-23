# coding: iso-8859-1
import requests
import sys

cidade = sys.argv[1]
cidade_formatada = cidade.replace(' ', '+').lower().strip()

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=affd802027fb6de23f9747fc5860c449&q='
url = api_address + cidade
json_data = requests.get(url).json()
# json_data = {"coord":{"lon":-0.13,"lat":51.51},
#              "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],
#              "base":"stations","main":{"temp":286.49,"pressure":1032,"humidity":62,"temp_min":284.82,"temp_max":288.15},
#              "visibility":10000,"wind":{"speed":2.1,"deg":230},"clouds":{"all":75},"dt":1553185045,
#              "sys":{"type":1,"id":1414,"message":0.0069,"country":"GB","sunrise":1553148110,"sunset":1553192025},
#              "id":2643743,"name":"London","cod":200}

clima = json_data['weather'][0]['description']
temperatura = json_data['main']['temp']
temp_min = json_data['main']['temp_min']
temp_max = json_data['main']['temp_max']
pressao = json_data['main']['pressure']
velocidade_vento = json_data['wind']['speed']
direcao_vento = json_data['wind']['deg']
pais = json_data['sys']['country']

print(f'A temperatura atual em {cidade.title()}, {pais.upper()} é {round(temperatura-273)}°C \
      com mínima de {round(temp_min-273)}°C e máxima de {round(temp_max-273)}°C')
sys.stdout.flush()


