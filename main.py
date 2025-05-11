from src.api_get_vacancies import HeadHunterAPI
from src.json_saver import JSONSaver
from src.utils import filtered_vacancies_rur, sorted_vacancies, print_top_vacancies, filtered_vacancies_by_words, get_vacancies_by_salary
from src.vacancies import Vacancy

print('Добро пожаловать на HeadHunter!')
keyword = input('введите слово для поиска вакансий\n')
number = int(input('введите количество вакансий, которые вы хотите получить - число от 10 до 100\n'))
pages = round(number/10, 0)
hh_api = HeadHunterAPI()
data = hh_api.get_vacancies(keyword, pages)
hh_vacancies = hh_api.new_view_vacancies(data)
vacancies_for_write = JSONSaver().vacancies_for_write(hh_vacancies)
JSONSaver().save_vacancies(vacancies_for_write)
# print(json_data_list_of_dicts)
list_vacancies = []
for vacancy in hh_vacancies:
    new_vacancy = Vacancy(**vacancy)
    list_vacancies.append(new_vacancy)
list_of_dict = [
    {attr: getattr(vacancy, attr) for attr in vacancy.__slots__}
    for vacancy in list_vacancies
]
# print(list_of_dict)
cur_filter = input('показать только вакансии с зарплатой в рублях? '
                   'введите да или нет\n')
if cur_filter == 'да':
    vacancies_cur = filtered_vacancies_rur(list_of_dict)
else:
    vacancies_cur = list_of_dict
# print(vacancies_cur)

salary_range = input("Введите диапазон зарплат: \n").split('-') # Пример: 100000 - 150000
ranged_vacancies = get_vacancies_by_salary(vacancies_cur, salary_range)
print(salary_range)
print(len(ranged_vacancies))
filter_words = input("Введите слова для фильтрации вакансий по описанию: \n").split()
filtered_vacancies = filtered_vacancies_by_words(ranged_vacancies, filter_words)
# print(filter_words)
# print(len(filtered_vacancies))
flag = input('Отсортировать по возрастанию(1) или по убыванию(2)?\n'
                      'введите 1 или 2. Если сортировать не нужно, нажмите 0\n')
sorted_vacancies = sorted_vacancies(filtered_vacancies, int(flag))

top_n = int(input("Введите количество вакансий для вывода в топ N: \n"))
print_top_vacancies(sorted_vacancies, top_n)

# vacancies = hh_api.new_view_vacancies(hh_vacancies)
# JSONSaver().save_vacancies(vacancies)
# vac = JSONSaver().get_vacancies()

