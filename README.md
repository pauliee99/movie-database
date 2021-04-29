# movie-database
Django database for devops assignment

## clone and run project
```bash
git clone https://github.com/pauliee99/movie-database.git
```
(if it isn't already in your machine)
```bash
python -m venv myvenv
```
(or python3)
```bash
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
cd myproject
``` 
edit settings.py to configure the MySQL Database you have installed on your machine

## run development server
```bash
python manage.py runserver 3000
```

click [here](http://127.0.0.1:3000/movies/api/)

