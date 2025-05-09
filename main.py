from src.api_get_vacancies import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancies import Vacancy

hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies('Python', 2)
vacancies = hh_api.new_view_vacancies(hh_vacancies)
JSONSaver().save_vacancies(vacancies)
vac = JSONSaver().get_vacancies()

for elem in vacancies:
    print(elem)
    print('------------------')
