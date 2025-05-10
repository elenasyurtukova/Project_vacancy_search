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




