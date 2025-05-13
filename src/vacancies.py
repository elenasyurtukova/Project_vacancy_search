class Vacancy:
    """Класс для создания вакансий и работы с ними"""

    __slots__ = (
        "name",
        "url",
        "salary_from",
        "salary_to",
        "salary_currency",
        "description",
    )
    name: str
    url: str
    description: str
    salary: dict

    def __init__(self, name, url, salary, description):
        """Метод инициализации экземпляра класса вакансий """
        self.name = name
        self.url = url
        self.description = description
        self.__validate_salary(salary)

    def __validate_salary(self, salary):
        """Метод валидации атрибута зарплаты"""
        if not salary:
            self.salary_from = 0
            self.salary_to = 0
            self.salary_currency = "RUR"
        else:
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else 0
            self.salary_currency = salary["currency"] if salary["currency"] else "RUR"

    def __lt__(self, other):
        """Метод сравнения экземпляра класса вакансий с объектом other (оператор меньше)"""
        if type(other) is Vacancy:
            if self.salary_currency == "RUR" and other.salary_currency == "RUR":
                return self.salary_from < other.salary_from
            else:
                raise TypeError("Объекты сравнить нельзя ввиду разности валют")
        else:
            raise TypeError("Невозможно сравнить объекты разных типов")


    def __le__(self, other):
        """Метод сравнения экземпляра класса вакансий с объектом other (оператор меньше или равно)"""
        if type(other) is Vacancy:
            if self.salary_currency == "RUR" and other.salary_currency == "RUR":
                return self.salary_from <= other.salary_from
            else:
                raise TypeError("Объекты сравнить нельзя ввиду разности валют")
        else:
            raise TypeError("Невозможно сравнить объекты разных типов")


    def __gt__(self, other):
        """Метод сравнения экземпляра класса вакансий с объектом other (оператор больше)"""
        if type(other) is Vacancy:
            if self.salary_currency == "RUR" and other.salary_currency == "RUR":
                return self.salary_from > other.salary_from
            else:
                raise TypeError("Объекты сравнить нельзя ввиду разности валют")
        else:
            raise TypeError("Невозможно сравнить объекты разных типов")


    def __ge__(self, other):
        """Метод сравнения экземпляра класса вакансий с объектом other (оператор больше или равно)"""
        if type(other) is Vacancy:
            if self.salary_currency == "RUR" and other.salary_currency == "RUR":
                return self.salary_from >= other.salary_from
            else:
                raise TypeError("Объекты сравнить нельзя ввиду разности валют")
        else:
            raise TypeError("Невозможно сравнить объекты разных типов")


    def __eq__(self, other):
        """Метод сравнения экземпляра класса вакансий с объектом other (оператор равенства)"""
        if type(other) is Vacancy:
            if self.salary_currency == "RUR" and other.salary_currency == "RUR":
                return self.salary_from == other.salary_from
            else:
                raise TypeError("Объекты сравнить нельзя ввиду разности валют")
        else:
            raise TypeError("Невозможно сравнить объекты разных типов")


    def __ne__(self, other):
        """Метод сравнения экземпляра класса вакансий с объектом other (оператор неравенства)"""
        if type(other) is Vacancy:
            if self.salary_currency == "RUR" and other.salary_currency == "RUR":
                return self.salary_from != other.salary_from
            else:
                raise TypeError("Объекты сравнить нельзя ввиду разности валют")
        else:
            raise TypeError("Невозможно сравнить объекты разных типов")


    def __str__(self):
        """Метод представления экземпляра класса в виде строки"""
        return f"""Название вакансии: {self.name}, 
Ссылка на вакансию: {self.url}, 
Зарплата: от {self.salary_from} до {self.salary_to}
Валюта зарплаты: {self.salary_currency}
Описание: {self.description}
"""

