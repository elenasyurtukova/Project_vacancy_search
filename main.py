from src.api_get_vacancies import HeadHunterAPI
from src.json_saver import JSONSaver
from src.utils import (filtered_vacancies_by_words, filtered_vacancies_rur,
                       get_vacancies_by_salary, print_top_vacancies,
                       sort_vacancies)
from src.vacancies import Vacancy


def main():
    print("Добро пожаловать на HeadHunter!")
    keyword = input("введите слово для поиска вакансий\n")
    number = int(
        input(
            "введите количество вакансий, которые вы хотите получить - число от 10 до 100\n"
        )
    )

    pages = round(number / 10, 0)
    hh_api = HeadHunterAPI()
    data = hh_api.get_vacancies(keyword, pages)
    hh_vacancies = hh_api.new_view_vacancies(data)
    vacancies_for_write = JSONSaver().vacancies_for_write(hh_vacancies)
    JSONSaver().save_vacancies(vacancies_for_write)

    list_vacancies = []
    for vacancy in hh_vacancies:
        new_vacancy = Vacancy(**vacancy)
        list_vacancies.append(new_vacancy)
    list_of_dict = [
        {attr: getattr(vacancy, attr) for attr in vacancy.__slots__}
        for vacancy in list_vacancies
    ]
    cur_filter = input(
        "показать только вакансии с зарплатой в рублях? " "введите да или нет\n"
    )

    if cur_filter == "да":
        vacancies_cur = filtered_vacancies_rur(list_of_dict)
    else:
        vacancies_cur = list_of_dict

    salary_range = input("Введите диапазон зарплат (например 0-500000): \n").split("-")

    ranged_vacancies = get_vacancies_by_salary(vacancies_cur, salary_range)

    filter_words = input(
        "Введите слова для фильтрации вакансий по описанию: \n"
    ).split()

    filtered_vacancies = filtered_vacancies_by_words(ranged_vacancies, filter_words)

    flag = input(
        "Отсортировать по возрастанию(1) или по убыванию(2)?\n"
        "введите 1 или 2. Если сортировать не нужно, нажмите 0\n"
    )

    sorted_vacancies = sort_vacancies(filtered_vacancies, int(flag))

    top_n = int(input("Введите количество вакансий для вывода в топ N: \n"))
    print_top_vacancies(sorted_vacancies, top_n)


if __name__ == "__main__":
    main()
