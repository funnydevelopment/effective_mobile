# Тестовое задание компании Effective Mobile

## Описание задания
### Реализовать телефонный справочник со следующими возможностями:
1. Вывод постранично записей из справочника на экран
2. Добавление новой записи в справочник
3. Возможность редактирования записей в справочнике
4. Поиск записей по одной или нескольким характеристикам
### Требования к программе:
1. Реализация интерфейса через консоль (без веб- или графического интерфейса)
2. Хранение данных должно быть организовано в виде текстового файла, формат которого придумывает сам программист
3. В справочнике хранится следующая информация: фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)
### Плюсом будет:
1. Аннотирование функций и переменных
2. Документирование функций
3. Подробно описанный функционал программы
4. Размещение готовой программы и примера файла с данными на github

## Установка и запуск
1. Склонируйте репозиторий: 
`git clone git@github.com:funnydevelopment/effective_mobile.git`
2. Создайте и активируйте виртуальное окружение:
`python3 -m venv venv`
`source venv/bin/activate`
3. Установите зависимости:
`pip install -r requirements.txt`
4. Запустите проект:
`python3 app.py`
---
### Данные будут храниться в JSON формате
#### Пример:
```json
[
    {
        "last_name": "Name_1",
        "first_name": "Surname_1",
        "middle_name": "Middle_name_1",
        "organization_name": "Example_Ltd_1",
        "work_phone": "8 (123) 123-0000",
        "personal_phone": "8 (123) 000-0000"
    },
    {
        "last_name": "Name_2",
        "first_name": "Surname_2",
        "middle_name": "Middle_name_2",
        "organization_name": "Example_Ltd_2",
        "work_phone": "8 (123) 123-0001",
        "personal_phone": "8 (123) 000-0001"
    }
]
```
---

