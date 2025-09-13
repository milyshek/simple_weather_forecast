import requests

def status_code_ok(x):
    if x.status_code != 200:
        print('error', x.status_code)
        exit()

def get_city():
    x = input("Input the city's name:\n")
    return x

def is_validate_city(city):
    for i in range(len(city)):
        if city[i].isdigit():
            print('you have input not string type')
            exit()
        i += 1
    return True



city = get_city()
is_validate_city(city)

address = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid=0cc128837a98394a8b7fe0b39fd015a2'

address_response = requests.get(address)
status_code_ok(address_response)


info_by_address = address_response.json()
try:
    lat = info_by_address[0].get('lat')
    lon = info_by_address[0].get('lon')
except IndexError:
    print("You haven't input city's name")
    exit()

url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=0cc128837a98394a8b7fe0b39fd015a2&units=metric'
url_response = requests.get(url)
status_code_ok(url_response)
data = url_response.json()

print('        Date            Temp')
for i in range(40):
    print(f'{data['list'][i]['dt_txt']}    {data['list'][i]['main']['temp']}')
