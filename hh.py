import requests
import pprint

DOMAIN = 'https://api.hh.ru/'

url_vacancies = f'{DOMAIN}vacancies'

params = {
    'text': 'Python',
    # страница
    'page': 1
}
result = requests.get(url_vacancies, params=params)

print(result.status_code)
pprint.pprint(result.json())
print('*'*20)

result = requests.get(url_vacancies, params=params).json()

items=result['items']
first=items[0]

pprint.pprint(first)

