import requests

#json_data = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {
    "usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":7.0800692033675e-5,"date":"Sat, 28 Nov 2020 00:00:01 GMT","inverseRate":14124.155728935},
    "eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":5.9385877045597e-5,"date":"Sat, 28 Nov 2020 00:00:01 GMT","inverseRate":16839.020483476}
}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])
