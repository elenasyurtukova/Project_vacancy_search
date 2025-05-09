class Vacancy():
    """Класс для работы с вакансиями"""
    name: str
    vacancy_url: str
    description: str
    salary: int


    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url
        self.description = description
        self.__validate_salary(salary)

    def __validate_salary(self, salary):
        if not salary:
            self.salary_from = 0
            self.salary_to = 0
        else:
            self.salary_from = salary['from'] if salary['from'] else 0
            self.salary_to = salary['to'] if salary['to'] else 0

    def __lt__(self, other):
        return self.salary_from < other.salary_from


    def __str__(self):
        return f'''Название вакансии: {self.name}, 
Ссылка на вакансию: {self.url}, 
Зарплата: от {self.salary_from} до {self.salary_to}
Описание: {self.description}
'''

if __name__ == '__main__':
    vac1 = Vacancy('Python-разработчик', 'https://hh.ru/vacancy/120331701', None, 'Опыт работы с <highlighttext>Python</highlighttext> от 1-го года . Опыт работы с одним или несколькими фреймворками: FastApi, Flask, Django, Django REST.')
    vac2 = Vacancy('Junior backend разработчик', 'https://hh.ru/vacancy/120288418', {'from': None, 'to': 250000, 'currency': 'KZT', 'gross': False}, 'Опыт на любом языке программирования, как: C, C++, C#, Java, Go и т.д. (приветствуется опыт на функциональных языках программирования). - ')
    print(vac1.salary_from)
    print(vac1.salary_to)
    print(vac2.salary_from)
    print(vac2.salary_to)


