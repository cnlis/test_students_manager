python -m venv venv
call .\venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata db.json
start python manage.py runserver --insecure
timeout 2
start python -m webbrowser http://127.0.0.1:8000