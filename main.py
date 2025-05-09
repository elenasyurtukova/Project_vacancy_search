from src.api_get_vacancies import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancies import Vacancy

print('Добро пожаловать на HeadHunter!')
keyword = input('введите слово для поиска вакансий\n')
number = int(input('введите количество вакансий, которые вы хотите получить - число от 1 до 100\n'))
pages = round(number/10, 0)
hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies(keyword, pages)
print(len(hh_vacancies))
# vacancies = hh_api.new_view_vacancies(hh_vacancies)
# JSONSaver().save_vacancies(vacancies)
# vac = JSONSaver().get_vacancies()
#
# for elem in vacancies:
#     print(elem)
#     print('------------------')
