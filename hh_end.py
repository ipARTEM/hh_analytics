import requests
import pprint

hh_data={}

DOMAIN = 'https://api.hh.ru/'

url_vacancies = f'{DOMAIN}vacancies'

# vacancy = input('Введите интересующую вакансию: ')
params = {
    'text': 'Python',
    # страница
    # 'page': 1
}
result = requests.get(url_vacancies, params=params)
data=result.json()
# print(result.status_code)
pprint.pprint(type(data))
pprint.pprint(data)
pprint.pprint(data['found'])
hh_data['found']=data['found']

pprint.pprint(hh_data)

count_pages=int(data['pages'])
print(count_pages)

# Вывод зп по данному запросу
for page in range(count_pages):
    print(f'***** {page+1} *****')
    for item in data['items']:
        pprint.pprint(item['salary'])

print('*'*20)

count_req=1
# Вывод требований к данному запросу
for page in range(count_pages):
    print(f'***** {page+1} *****')
    for item in data['items']:
        count_req+=1
        req=item['snippet']['requirement']
        print(f'Требования  {count_req}:')
        print(req)






# numbers_of_vacancies=result['found']
#
# pprint.pprint(numbers_of_vacancies.json())


