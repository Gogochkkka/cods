import requests

city = 'Москва, РФ'
appid = 'f90c51351aca9b163c5166b959835520'

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print('Погода на данный момент')
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Cкорость ветра:", data['wind']['speed'])
print("Видимость", data['visibility'], 'м')


res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",
    '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
    i['weather'][0]['description'], ">")
    print("Cкорость ветра:", '<', i['wind']['speed'], '>')
    print("Видимость", '<',i['visibility'], 'м >')
    print("____________________________")
