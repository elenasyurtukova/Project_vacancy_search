import json
from abc import ABC, abstractmethod


class JSONAbstract(ABC):
    """Класс для добавления данных о вакансиях в файл,
    получения данных из файла и удаления информации о вакансиях"""

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def save_vacancies(self, vacancies):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass


class JSONSaver(JSONAbstract):
    """Класс для записи/добавления в указанный файл или удаления данных из файла"""

    def __init__(self, path="data/vacancies.json"):
        self.__path = path

    def get_vacancies(self):
        """Метод получения данных о вакансиях из указанного файла"""
        try:
            with open(self.__path, encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    return data
                except json.JSONDecodeError:
                    # print("Ошибка декодирования файла")
                    return []
        except FileNotFoundError:
            # print("Файл не найден")
            return []

    def save_vacancies(self, vacancies: list[dict]):
        """Метод сохранения вакансий в файл"""
        with open(self.__path, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def delete_vacancies(self):
        """Метод очистки содержимого файла"""
        open(self.__path, "w").close()

    def vacancies_for_write(self, vacancies):
        """Метод получения данных о вакансиях для записи в файл, минуя дубликаты"""
        data = JSONSaver().get_vacancies()
        if data != []:
            for vacancy in vacancies:
                if vacancy not in data:
                    data.append(vacancy)
            return data
        else:
            return vacancies
