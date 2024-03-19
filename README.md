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

8. Установите pre-commit hook
```bash
pre-commit install
```

8. Создайте файл .env из infra/.env.example

9. Запустите docker compose с БД:
```bash
docker compose -f infra/docker-compose.dev.yml up -d --build
```
