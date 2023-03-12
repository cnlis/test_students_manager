# Менеджер студентов (тестовое задание)

Django-приложение с таблицами Студент, Преподаватель и Кафедра.
Таблицы Студент и Преподаватели содержат поря PK, Пол, Имя, Фамилия, Отчество.
Кроме того, таблица Студент содержит поле Кафедра.
Таблица Кафедра содержит поля PK, Название, Преподаватели (связь к таблице 
Преподаватели многие-ко-многим).
Приложение позволяет создавать, удалять, редактировать записи в каждой из
таблиц через web-интерфейс.
Применяется валидация на уникальность ФИО и проверка отсутствия в ФИО цифр и
специальных символов.

## Технологии
- Python 3.10
- Django 4.1.7
- django-select2 8.1.1 

### Для запуска должны быть установлены
- Python последней версии https://www.python.org/downloads/
- Git Bash (для клонирования репозитория через командную строку) https://git-scm.com/downloads

### Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/cnlis/test_students_manager.git
cd test_students_manager
```
или скопировать архив со страницы проекта (Code > Download ZIP), разархивировать 
в папку, перейти в папку в командной строке.

2. Запустить скрипт **start_win.bat** в Windows или **start_linux.sh** в 
Linux/MacOS **или** выполнить шаги 3-8 вручную.
```
# Linux/MacOS
chmod 775 start_linux.sh
./start_linux.sh
# Windows
.\start_win.bat
```

3. Создать и активировать виртуальное окружение:
```
# При использовании PowerShell разрешить выполнение скриптов
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
# Windows
python -m venv venv
.\venv\Scripts\activate
```

4. Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

5. Выполнить миграции:
```
python manage.py migrate
```

6. Загрузить тестовые данные (опционально):
```
python manage.py loaddata db.json
```

7. Запустить проект локально:
```
python manage.py runserver --insecure
```

8. Перейти по адресу http://127.0.0.1:8000
