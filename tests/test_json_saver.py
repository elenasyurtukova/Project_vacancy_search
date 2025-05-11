import json
import unittest
from unittest.mock import patch

from src.json_saver import JSONSaver


class TestJsonReader(unittest.TestCase):
    @patch("builtins.open")
    @patch("json.load")
    def test_get_vacancies(self: "TestJsonReader", mock_json_load, mock_open):
        # Задаю тестовые данные
        mock_json_load.return_value = [
            {"name": "Аналитик данных",
             "url": "https://api.hh.ru/vacancies/120353943?host=hh.ru",
             "salary": {"from": 4000000, "to": 7000000, "currency": "UZS", "gross": True},
             "description": "Опыт работы с BI-системами (Power BI, Tableau, Metabase и др.)"
            }
        ]

        # Вызываю функцию и проверяю результат
        result = JSONSaver().get_vacancies()
        self.assertEqual(
            result,
            [
                {"name": "Аналитик данных",
                 "url": "https://api.hh.ru/vacancies/120353943?host=hh.ru",
                 "salary": {"from": 4000000, "to": 7000000, "currency": "UZS", "gross": True},
                 "description": "Опыт работы с BI-системами (Power BI, Tableau, Metabase и др.)"
                }
            ],
        )
        mock_json_load.return_value = []

        # Вызываю функцию и проверяю результат
        result = JSONSaver().get_vacancies()
        self.assertEqual(result, [])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_open):
        # Вызываю свою функцию и проверяю, что она возвращает пустой список
        result = JSONSaver("path/to/nonexistent/file.json").get_vacancies()
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
