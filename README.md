---

# Задание и выполненные по ним пункты

Создать полный глоссарий употребляемых терминов и спроектировать доступ к нему в виде  Web API в докер-контейнере с использованием **FastAPI**
Глоссарий должен поддерживать следующие операции:
- Получение списка всех терминов.
- Получение информации о конкретном термине по ключевому слову.
- Добавление нового термина с описанием.
- Обновление существующего термина.
- Удаление термина из глоссария.

## Выполненные пункты:
✅ У вас должен применяться Pydantic для валидации входных данных и формирования схем. 
✅ реализуйте  решение в виде контейнера (Dockerfile) или реализуйте решение с помощью Docker Compose; 
✅ используете для хранения данных  SQLite (или другую легковесную БД);
✅ обеспечите автоматическую миграцию структуры данных при старте приложения. 
🟩 разверните словарь на публичном сервере в вебе. 

## Описание API:

- `GET /allWords`  Получение всех терминов в глоссарии
- `GET /words/{name}` Получить данные о слове по параметру `name`
- `POST /words`  Добавить новое слово в глоссарий.
   ```json
   {
     "name": "certificate",
     "definition": "...Definition..."
   }
   ```
- `PUT /words/{name}` Изменить определение текущего слова  
   ```json
   {
     "definition": "...Definition2...."
   }
   ```
- `DELETE /words/{id}` Удалить слово из глоссария по идентификатору

## Как запускать?

Склонировать проект себе на машину и перейти в директорию проекта (там где расположен Readme.md)
Далее, запустить venv (чтобы не ставить локально зависимости) и установить все зависимости
   ```bash
   virtualenv env
   source env/bin/activate
   pip install -r req.txt
   ```
Приложение запустится и будет доступно по локально на порту 8000
   ```bash
   uvicorn app.main:app --reload
   ```

Для удобного использования ручек перейдите в Swagger UI [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Кроме того, есть возможность поднять приложение в Docker-контейнере. Для этого запустить команды из той же главное директории команду:
   ```bash
   docker build -t glossary-app . #собрать образ
   docker run -d --name glossary_container -p 8000:8000 glossary-app #поднять контейнер с приложением
   ```
