# Sprint_5 — UI автотесты (Сервис «Доска»)

URL: https://qa-desk.stand.praktikum-services.ru/

## Покрытие
- Регистрация (успех, невалидный email, уже существующий пользователь)
- Login
- Logout
- Создание объявления (неавторизованный / авторизованный)

## Запуск
Из корня проекта:
```bash
pip install -r requirements.txt
pytest -v