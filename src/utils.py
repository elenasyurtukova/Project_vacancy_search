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
    def __init__(self, path = 'data/vacancies.json'):
        self.__path = path

    def get_vacancies(self):
        pass


    def save_vacancies(self, vacancies: list[dict]):
        with open (self.__path, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)




    def delete_vacancies(self):
        open(self.__path, 'w').close()