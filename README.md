# questions_api
API for saving questions in database from another public API (written with FastAPI Python)

Сервис позволяет сохранять вопросы из открытого API https://jservice.io/api/random в базу данных, 
развернутую в Docker. Для сохранения определенного количества вопросов с необходимо сделать POST запрос
на localhost/question, указав в теле количество требуемых вопросов:
```
{
    "questions_num": количество
}
```

Если один из полученных вопросов уже сохранен в базе данных, сервис отправляет дополнительные запросы, чтобы сохранить 
определенное количество уникальных вопросов в БД.

Для запуска сериса на локальном устройстве (должен быть установлен Docker, Python3):
  1. make docker - для создания и запуска контейнера
  2. make run - для запуска приложения (скачивает зависимости из requirements.txt перед запуском)
  3. make all - запсукает пункт 1, за ним пункт 2
