# Описание
Сервис позволяет клиенту создавать заявку на найм рекрутера по определённым условиям.

Сайт: http://hrspace.ddns.net/api
Доки: http://hrspace.ddns.net/api/docs

### Команда

- [Денис Панасенко](https://github.com/pandenic)
- [Всеволод Паньшин](https://github.com/VPanshin)
- [Никита Сенгилейцев](https://github.com/NikAfraim)

### Технологии
- https://img.shields.io/badge/fastAPI-009485?logo=fastapi&logoColor=white&style=for-the-badge
- https://img.shields.io/badge/PostgreSQL-blue?logo=postgresql&logoColor=white&style=for-the-badge
- https://img.shields.io/badge/SQLalchemy-778877?logo=sqlalchemy&logoColor=white&style=for-the-badge
- https://img.shields.io/badge/docker-blue?logo=docker&logoColor=white&style=for-the-badge
- https://img.shields.io/badge/UVcorn-purple?logo=uvcorn&logoColor=white&style=for-the-badge
- https://img.shields.io/badge/poetry-ad998b?logo=poetry&logoColor=white&style=for-the-badge
- https://img.shields.io/badge/alembic-yellow?logo=alembic&logoColor=white&style=for-the-badge
- https://img.shields.io/badge/githubactions-black?logo=githubactions&logoColor=white&style=for-the-badge


## Запуск локально из образов
1. Создайте файл .env в корне согласно примера infra/.env.example
2. Запустите docker compose
```bash
docker compose up
```
3. Проект будет доступен по адресу: http://localhost:715/.
4. API: http://localhost:715/api/

## Запуск локально из образов
### Установка

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
## Запуск:
1. Запустите docker compose для сборки:
```bash
docker compose -f infra/docker-compose.dev.yml up -d --build
```

2. Проект будет доступен по адресу: http://localhost:715/.
3. API: http://localhost:715/api/
