python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata db.json &&
python manage.py runserver --insecure &
sleep 2 &&
python -m webbrowser http://127.0.0.1:8000
