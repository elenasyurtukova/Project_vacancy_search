from src.utils import (
    filtered_vacancies_by_words,
    filtered_vacancies_rur,
    get_vacancies_by_salary,
    sort_vacancies,
)


def test_filtered_vacancies_rur(vacancies_for_rur):
    result = filtered_vacancies_rur(vacancies_for_rur)
    assert result == [
        {
            "name": "Python-разработчик",
            "url": "https://api.hh.ru/vacancies/120331701?host=hh.ru",
            "salary_from": 0,
            "salary_to": 350000,
            "salary_currency": "RUR",
            "description": "Опыт работы с <highlighttext>Python</highlighttext> от 1-го года.",
        },
        {
            "name": "Web-программист - стажер",
            "url": "https://api.hh.ru/vacancies/118711736?host=hh.ru",
            "salary_from": 0,
            "salary_to": 0,
            "salary_currency": "RUR",
            "description": "Carfast- Первый онлайн авто аукцион в Казахстане. Командный игрок.",
        },
    ]


def test_sorted_vacancies(vacancies_for_rur):
    assert sort_vacancies(vacancies_for_rur, flag=1) == [
        {
            "name": "Web-программист - стажер",
            "url": "https://api.hh.ru/vacancies/118711736?host=hh.ru",
            "salary_from": 0,
            "salary_to": 0,
            "salary_currency": "RUR",
            "description": "Carfast- Первый онлайн авто аукцион в Казахстане. Командный игрок.",
        },
        {
            "name": "Python-разработчик",
            "url": "https://api.hh.ru/vacancies/120331701?host=hh.ru",
            "salary_from": 0,
            "salary_to": 350000,
            "salary_currency": "RUR",
            "description": "Опыт работы с <highlighttext>Python</highlighttext> от 1-го года.",
        },
        {
            "name": "Аналитик данных",
            "url": "https://api.hh.ru/vacancies/120353943?host=hh.ru",
            "salary_from": 4000000,
            "salary_to": 7000000,
            "salary_currency": "UZS",
            "description": "Опыт работы с BI-системами (Power BI, Tableau, Metabase и др.)",
        },
    ]


def test_sorted_vacancies_2(vacancies_for_rur):
    assert sort_vacancies(vacancies_for_rur, flag=2) == [
        {
            "name": "Аналитик данных",
            "url": "https://api.hh.ru/vacancies/120353943?host=hh.ru",
            "salary_from": 4000000,
            "salary_to": 7000000,
            "salary_currency": "UZS",
            "description": "Опыт работы с BI-системами (Power BI, Tableau, Metabase и др.)",
        },
        {
            "name": "Python-разработчик",
            "url": "https://api.hh.ru/vacancies/120331701?host=hh.ru",
            "salary_from": 0,
            "salary_to": 350000,
            "salary_currency": "RUR",
            "description": "Опыт работы с <highlighttext>Python</highlighttext> от 1-го года.",
        },
        {
            "name": "Web-программист - стажер",
            "url": "https://api.hh.ru/vacancies/118711736?host=hh.ru",
            "salary_from": 0,
            "salary_to": 0,
            "salary_currency": "RUR",
            "description": "Carfast- Первый онлайн авто аукцион в Казахстане. Командный игрок.",
        },
    ]


def test_filtered_vacancies_by_words(vacancies_for_rur):
    assert filtered_vacancies_by_words(vacancies_for_rur, ["опыт", "работы"]) == [
        {
            "name": "Аналитик данных",
            "url": "https://api.hh.ru/vacancies/120353943?host=hh.ru",
            "salary_from": 4000000,
            "salary_to": 7000000,
            "salary_currency": "UZS",
            "description": "Опыт работы с BI-системами (Power BI, Tableau, Metabase и др.)",
        },
        {
            "name": "Python-разработчик",
            "url": "https://api.hh.ru/vacancies/120331701?host=hh.ru",
            "salary_from": 0,
            "salary_to": 350000,
            "salary_currency": "RUR",
            "description": "Опыт работы с <highlighttext>Python</highlighttext> от 1-го года.",
        },
    ]


def test_get_vacancies_by_salary(vacancies_for_rur):
    assert get_vacancies_by_salary(vacancies_for_rur, ["100000", "1000000"]) == []
    assert get_vacancies_by_salary(vacancies_for_rur, ["0", "1000000"]) == [
        {
            "name": "Python-разработчик",
            "url": "https://api.hh.ru/vacancies/120331701?host=hh.ru",
            "salary_from": 0,
            "salary_to": 350000,
            "salary_currency": "RUR",
            "description": "Опыт работы с <highlighttext>Python</highlighttext> от 1-го года.",
        },
        {
            "name": "Web-программист - стажер",
            "url": "https://api.hh.ru/vacancies/118711736?host=hh.ru",
            "salary_from": 0,
            "salary_to": 0,
            "salary_currency": "RUR",
            "description": "Carfast- Первый онлайн авто аукцион в Казахстане. Командный игрок.",
        },
    ]
