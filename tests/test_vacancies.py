import pytest


def test_vacancy_init(vacancy2):
    assert vacancy2.name == "Junior backend разработчик"
    assert vacancy2.salary_from == 0
    assert vacancy2.salary_to == 250000
    assert vacancy2.salary_currency == "KZT"
    assert (
        vacancy2.description
        == "Опыт на любом языке программирования, как: C, C++, C#, Java, Go и т.д."
    )


def test_vacancy_validate_salary(vacancy1):
    assert vacancy1.salary_from == 0
    assert vacancy1.salary_to == 0
    assert vacancy1.salary_currency == "RUR"


def test_vacancy_lt(vacancy1, vacancy3):
    assert vacancy1.__lt__(vacancy3) is False


def test_vacancy_lt_error(vacancy1, vacancy2):
    with pytest.raises(TypeError, match="Объекты сравнить нельзя ввиду разности валют"):
        vacancy1.__lt__(vacancy2)

    with pytest.raises(TypeError, match="Невозможно сравнить объекты разных типов"):
        vacancy1.__lt__(1000)


def test_vacancy_gt(vacancy1, vacancy3):
    assert vacancy1.__gt__(vacancy3) is False


def test_vacancy_gt_error(vacancy1, vacancy2):
    with pytest.raises(TypeError, match="Объекты сравнить нельзя ввиду разности валют"):
        vacancy1.__gt__(vacancy2)

    with pytest.raises(TypeError, match="Невозможно сравнить объекты разных типов"):
        vacancy1.__gt__(1000)


def test_vacancy_le(vacancy1, vacancy3):
    assert vacancy1.__le__(vacancy3) is True


def test_vacancy_le_error(vacancy1, vacancy2):
    with pytest.raises(TypeError, match="Объекты сравнить нельзя ввиду разности валют"):
        vacancy1.__le__(vacancy2)

    with pytest.raises(TypeError, match="Невозможно сравнить объекты разных типов"):
        vacancy1.__le__(1000)


def test_vacancy_eq(vacancy1, vacancy3):
    assert vacancy1.__eq__(vacancy3) is True


def test_vacancy_eq_error(vacancy1, vacancy2):
    with pytest.raises(TypeError, match="Объекты сравнить нельзя ввиду разности валют"):
        vacancy1.__eq__(vacancy2)

    with pytest.raises(TypeError, match="Невозможно сравнить объекты разных типов"):
        vacancy1.__le__(1000)


def test_vacancy_ne(vacancy1, vacancy3):
    assert vacancy1.__ne__(vacancy3) is False


def test_vacancy_ne_error(vacancy1, vacancy2):
    with pytest.raises(TypeError, match="Объекты сравнить нельзя ввиду разности валют"):
        vacancy1.__ne__(vacancy2)

    with pytest.raises(TypeError, match="Невозможно сравнить объекты разных типов"):
        vacancy1.__ne__(1000)


def test_vacancy_str(vacancy3):
    assert str(vacancy3) == (
        "Название вакансии: Backend разработчик, \n"
        "Ссылка на вакансию: https://hh.ru/vacancy/120288418, \n"
        "Зарплата: от 0 до 350000\n"
        "Валюта зарплаты: RUR\n"
        "Описание: Опыт на любом языке программирования, как: C, C++, C#, Java, Go и т.д.\n"
    )
