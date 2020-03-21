import requests
import pprint
URL = 'https://api.hh.ru/vacancies'
params ={'text': 'Python AND Москва',
        'only_with_salary': True,
        'page': 1,
        'per_page': 20 }
result = requests.get(URL, params=params).json()
found_vacancies = result['found']
pages = result['pages']
salary_from = []
salary_to =[]

print('найдено вакансий {} штук на {} страницах'. format(result['found'], result['pages']))

for i in range(1, pages):
    URL = 'https://api.hh.ru/vacancies'
    params = {'text': 'Python AND Москва',
              'only_with_salary': True,
              'page': i,
              'per_page': 20}
    result = requests.get(URL, params=params).json()
    items = result['items']

    for i in items:
        salary = i['salary']
        sal_from = salary['from']
        sal_to = salary['to']
        if sal_from != None: salary_from.append(sal_from)
        if sal_to != None: salary_to.append(sal_to)

mid_sal_from = round(sum(salary_from)/len(salary_from))
mid_sal_to = round(sum(salary_to)/len(salary_to))
print ('зарплата Python-разработчика в Москве составляет в среднем  от {}руб. до {}руб.'.format(mid_sal_from, mid_sal_to ))
