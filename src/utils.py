from src.vacancies import Vacancy


def filtered_vacancies_rur(vacancies: list[Vacancy]) -> list[Vacancy]
    """Функция: фильтрует только вакансии с зарплатой в рублях"""
    vacancies_rur = []
    for vacancy in vacancies:
        if vacancy.salary_currency == 'RUR':
            vacancies_rur.append(vacancy)
    return vacancies_rur
