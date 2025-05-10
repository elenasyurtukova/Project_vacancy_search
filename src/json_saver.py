import json
from abc import ABC, abstractmethod

from src.vacancies import Vacancy


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
        with open(self.__path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        vacancies = []
        for vacancy in data:
            vacancies.append(Vacancy(**vacancy))
        return vacancies


    def save_vacancies(self, vacancies: list[dict]):
        # json_data = JSONSaver.get_vacancies()
        # data_in_list = [elem.__dict__ for elem in json_data]
        # vacancies_for_append = []
        # for vacancy in vacancies:
        #     if vacancy not in data_in_list:
        #         vacancies_for_append.append(vacancy)
        with open (self.__path, 'a', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)


    def delete_vacancies(self):
        open(self.__path, 'w').close()