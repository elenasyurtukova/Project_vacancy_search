from src.api_get_vacancies import HeadHunterAPI
from src.utils import JSONSaver
from src.vacancies import Vacancy

hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies('Python', 2)
vacancies = hh_api.new_view_vacancies(hh_vacancies)
JSONSaver().save_vacancies(vacancies)
JSONSaver().delete_vacancies()
# vac = []
# for vacancy in vacancies:
#     vac.append(Vacancy(**vacancy))
# for elem in vac:
#     print(elem)
#     print('------------------')
