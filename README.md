<h2 align="center">MMORPG board</h2>



### Описание проекта:
Фанатский сервер  одной известной MMORPG — что-то вроде доски объявлений


### Инструменты разработки

**Стек:**
- Python >= 3.11
- Django == 3.2.4
- sqlite3

## Разработка

##### 1) Поставить звездочку) (понравиля рипозиторий) 

##### 2) Клонировать репозиторий

    git clone https://github.com/ProgramistYa/Poster_Board_MMORPG.git

##### 3) Создать виртуальное окружение

    cd board
    
    python -m venv venv
    
##### 4) Активировать виртуальное окружение
    
Linux

    source venv/bin/activate
    
Windows

    ./venv/Scripts/activate

##### 5) Устанавливить зависимости:

    pip install -r req.txt

##### 6) Выполнить команду для выполнения миграций

    python manage.py migrate
    
##### 8) Создать суперпользователя

    python manage.py createsuperuser
    
##### 9) Запустить сервер

    python manage.py runserver

##### 10) Ссылки

- Сайт http://127.0.0.1:8000/

- Админ панель http://127.0.0.1:8000/admin

