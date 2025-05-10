import pytest
from _pytest.fixtures import fixture

from src.vacancies import Vacancy


@pytest.fixture
def vacancy1():
    return Vacancy('Python-разработчик', 'https://hh.ru/vacancy/120331701', None,
                   'Опыт работы с <highlighttext>Python</highlighttext> от 1-го года. Опыт работы с фреймворками: FastApi, Flask, Django, Django REST.')


@pytest.fixture
def vacancy2():
    return Vacancy('Junior backend разработчик', 'https://hh.ru/vacancy/120288418',
                   {'from': None, 'to': 250000, 'currency': 'KZT', 'gross': False},
                   'Опыт на любом языке программирования, как: C, C++, C#, Java, Go и т.д.')


@pytest.fixture
def vacancy3():
    return Vacancy('Backend разработчик', 'https://hh.ru/vacancy/120288418',
                   {'from': None, 'to': 350000, 'currency': 'RUR', 'gross': False},
                   'Опыт на любом языке программирования, как: C, C++, C#, Java, Go и т.д.')