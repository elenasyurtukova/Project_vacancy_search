def filtered_vacancies_rur(vacancies: list[dict]) -> list[dict]:
    """Функция: фильтрует только вакансии с зарплатой в рублях"""
    vacancies_rur = []
    for vacancy in vacancies:
        if vacancy["salary_currency"] == "RUR":
            vacancies_rur.append(vacancy)
    return vacancies_rur


def sort_vacancies(vacancies: list[dict], flag: int) -> list[dict]:
    """Функция: сортирует по возрастанию или по убыванию зарплаты"""
    if flag == 1:
        return sorted(vacancies, key=lambda vacancy: int(vacancy["salary_to"]))
    elif flag == 2:
        return sorted(
            vacancies, key=lambda vacancy: int(vacancy["salary_to"]), reverse=True
        )
    return vacancies


def filtered_vacancies_by_words(
    vacancies: list[dict], filter_words: list
) -> list[dict]:
    """Фукция фильтрации вакансий по словам в описании"""
    filtered_vacancies = []
    for word in filter_words:
        for vacancy in vacancies:
            if not vacancy["description"]:
                continue
            elif word.lower() in vacancy["description"].lower():
                if vacancy not in filtered_vacancies:
                    filtered_vacancies.append(vacancy)
    return filtered_vacancies


def get_vacancies_by_salary(vacancies: list[dict], salary_range: list):
    ranged_vacancies = []
    for vacancy in vacancies:
        if vacancy["salary_from"] >= int(salary_range[0]) and vacancy[
            "salary_to"
        ] <= int(salary_range[1]):
            ranged_vacancies.append(vacancy)
    return ranged_vacancies


def print_top_vacancies(vacancies: list[dict], top_n):
    for i in range(top_n):
        print(f"""Название вакансии: {vacancies[i]['name']}, 
Ссылка на вакансию: {vacancies[i]['url']}, 
Зарплата: от {vacancies[i]['salary_from']} до {vacancies[i]['salary_to']},
Валюта зарплаты: {vacancies[i]['salary_currency']}, 
Описание: {vacancies[i]['description']}
""")
        print("_________________")
