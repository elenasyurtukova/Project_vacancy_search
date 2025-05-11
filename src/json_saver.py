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
        # json_data = JSONSaver.get_vacancies()
        # data_in_list = [elem.__dict__ for elem in json_data]
        # vacancies_for_append = []
        # for vacancy in vacancies:
        #     if vacancy not in data_in_list:
        #         vacancies_for_append.append(vacancy)
        with open (self.__path, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)


    def delete_vacancies(self):
        open(self.__path, 'w').close()


    def vacancies_for_write(self, vacancies):
        data = JSONSaver().get_vacancies()
        if data != []:
            for vacancy in vacancies:
                if vacancy not in data:
                    data.append(vacancy)
            return data
        else:
            return vacancies


# if __name__ == '__main__':
#     pass
