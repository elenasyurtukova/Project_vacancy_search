class Vacancy():
    """Класс для работы с вакансиями"""
    __slots__ = ('name', 'url', 'salary_from', 'salary_to', 'salary_currency', 'description')
    name: str
    url: str
    description: str
    salary: dict


    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url
        self.description = description
        self.__validate_salary(salary)

    def __validate_salary(self, salary):
        if not salary:
            self.salary_from = 0
            self.salary_to = 0
            self.salary_currency = 'RUR'
        else:
            self.salary_from = salary['from'] if salary['from'] else 0
            self.salary_to = salary['to'] if salary['to'] else 0
            self.salary_currency = salary['currency'] if salary['currency'] else 'RUR'

    def __lt__(self, other):
        if type(other) is Vacancy:
            if self.salary_currency == 'RUR' and other.salary_currency == 'RUR':
                return self.salary_from < other.salary_from
            else:
                raise TypeError('Объекты сравнить нельзя ввиду разности валют')
        else:
            raise TypeError('Невозможно сравнить объекты разных типов')


    def __str__(self):
        return f'''Название вакансии: {self.name}, 
Ссылка на вакансию: {self.url}, 
Зарплата: от {self.salary_from} до {self.salary_to}
Валюта зарплаты: {self.salary_currency}
Описание: {self.description}
'''

if __name__ == '__main__':
    vac1 = Vacancy('Python-разработчик', 'https://hh.ru/vacancy/120331701', None, 'Опыт работы с <highlighttext>Python</highlighttext> от 1-го года . Опыт работы с одним или несколькими фреймворками: FastApi, Flask, Django, Django REST.')
    vac2 = Vacancy('Junior backend разработчик', 'https://hh.ru/vacancy/120288418', {'from': None, 'to': 250000, 'currency': 'KZT', 'gross': False}, 'Опыт на любом языке программирования, как: C, C++, C#, Java, Go и т.д. (приветствуется опыт на функциональных языках программирования). - ')
    vac3 = Vacancy('Junior backend разработчик', 'https://hh.ru/vacancy/120288418', {'from': None, 'to': 250000, 'currency': 'RUR', 'gross': False}, 'Опыт на любом языке программирования, как: C, C++, C#, Java, Go и т.д.')
    # print(vac1.salary_from)
    # print(vac1.salary_to)
    # print(vac1.salary_currency)
    # print(vac2.salary_from)
    # print(vac2.salary_to)
    # print(vac2.salary_currency)
    # print(vac3.salary_currency)
    print(vac1.__lt__(vac3))


