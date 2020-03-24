import requests
import string
import pprint
URL = 'https://api.hh.ru/vacancies'
params ={'text': 'Python AND Москва',
        'only_with_salary': True,
        'page': 1,
        'per_page':20 }
result = requests.get(URL, params=params).json()
found_vacancies = result['found']
pages = result['pages']


print('найдено вакансий {} штук на {} страницах'. format(result['found'], result['pages']))
text = ''
for i in range(1, pages):
    URL = 'https://api.hh.ru/vacancies'
    params = {'text': 'Python AND Москва',
              'only_with_salary': True,
              'page': i,
              'per_page': 20}
    result = requests.get(URL, params=params).json()
    items = result['items']

    for i in items:
        snippet = i['snippet']
        requirement = snippet['requirement']
        responsibility =snippet['responsibility']
        text += str(responsibility)
        text += str(requirement)

for i in string.punctuation:
    text = text.replace(i, ' ')
text = text.lower()
text = text.split()
skills = ['python', 'django', 'sql', 'c++', 'php', 'flask', 'tensorflow','postgresql','pandas','api']
dict = {}
for i in text:
    dict[i] = text.count(i)
list = list(dict.items())
for i in range(len(list)):
    if list[i][0] in skills:
       print(f'встречаемость:{list[i]}, т.е. в {round(list[i][1]*100/found_vacancies)} % вакансий')