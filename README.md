# Описание
Сервис позволяет клиенту создавать заявку на найм рекрутера по определённым условиям.

Технологии
- Poetry
- FastAPI
- Uvicorn
- Docker
- PostgreSQL
- SQLAlchemy
- Alembic

# Установка

1. Клонируйте репозиторий с помощью SSH:
```bash
git clone git@github.com:team-6x/backend.git hr_builder_backend
```

2. Перейдите в каталог проекта:
```bash
cd hr_builder_backend
```

3. Создайте файл .env в корне проекта, используя шаблон /infra/.env.example

4. Запустите poetry shell командой, либо через pycharm, например, можно выбрать poetry как интерпретатор
```bash
poetry shell
```

5. Установите все зависимости
```bash
poetry install
```

6. Добавление новых пакетов
```bash 
poetry add название
```

7. Добавление новых пакетов в dev
```bash 
poetry add название --group dev
```

~~6. Запустите docker compose:~~
```bash
docker compose up -d
```




