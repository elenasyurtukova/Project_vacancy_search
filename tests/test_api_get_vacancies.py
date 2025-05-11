from unittest.mock import Mock, patch

from src.api_get_vacancies import HeadHunterAPI


def test_HHAPI_get_vacancies():
    mock_response = Mock()
    mock_response.json.return_value = {
        "items": [
            {
                "id": "120353943",
                "name": "Аналитик данных",
                "salary": {
                    "from": 4000000,
                    "to": 7000000,
                    "currency": "UZS",
                    "gross": True,
                },
                "created_at": "2025-05-10T08:08:48+0300",
                "url": "https://api.hh.ru/vacancies/120353943?host=hh.ru",
                "snippet": {
                    "requirement": "Опыт работы с BI-системами (Power BI, Tableau, Metabase и др.)",
                    "responsibility": None,
                },
            },
            {
                "id": "120331701",
                "name": "Python-разработчик",
                "salary": None,
                "created_at": "2025-05-07T16:12:50+0300",
                "url": "https://api.hh.ru/vacancies/120331701?host=hh.ru",
                "snippet": {
                    "requirement": "Опыт работы с <highlighttext>Python</highlighttext> от 1-го года",
                    "responsibility": None,
                },
            },
        ]
    }
    with patch("requests.get", return_value=mock_response):
        result = HeadHunterAPI().get_vacancies("Python", 1)
        assert len(result) == 2
        assert result == [
            {
                "id": "120353943",
                "name": "Аналитик данных",
                "salary": {
                    "from": 4000000,
                    "to": 7000000,
                    "currency": "UZS",
                    "gross": True,
                },
                "created_at": "2025-05-10T08:08:48+0300",
                "url": "https://api.hh.ru/vacancies/120353943?host=hh.ru",
                "snippet": {
                    "requirement": "Опыт работы с BI-системами (Power BI, Tableau, Metabase и др.)",
                    "responsibility": None,
                },
            },
            {
                "id": "120331701",
                "name": "Python-разработчик",
                "salary": None,
                "created_at": "2025-05-07T16:12:50+0300",
                "url": "https://api.hh.ru/vacancies/120331701?host=hh.ru",
                "snippet": {
                    "requirement": "Опыт работы с <highlighttext>Python</highlighttext> от 1-го года",
                    "responsibility": None,
                },
            },
        ]


def test_HHAPI_new_view_vacancies(vacancies):
    assert HeadHunterAPI().new_view_vacancies(vacancies) == [
        {
            "name": "Аналитик данных",
            "url": "https://api.hh.ru/vacancies/120353943?host=hh.ru",
            "salary": {
                "from": 4000000,
                "to": 7000000,
                "currency": "UZS",
                "gross": True,
            },
            "description": "Опыт работы с BI-системами (Power BI, Tableau, Metabase и др.)",
        },
        {
            "name": "Python-разработчик",
            "url": "https://api.hh.ru/vacancies/120331701?host=hh.ru",
            "salary": None,
            "description": "Опыт работы с <highlighttext>Python</highlighttext> от 1-го года",
        },
    ]
