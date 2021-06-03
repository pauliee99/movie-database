# movie-database
gdsgs
Django database system for devops assignment
test
jenkins-test2

## Clone and run project
```bash
git clone https://github.com/pauliee99/movie-database.git
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
cd database
cp database/.env.example database/.env
```

[Install MySQL](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/)

[Create Database](https://dev.mysql.com/doc/refman/8.0/en/creating-database.html)

Edit database/.env to define the MySQL Database you have just created

```bash
SECRET_KEY='test123'

DB_NAME='name of database created'
DB_USER='your db username'
DB_PASSWORD='your db password'
DB_HOST='the host db is running'
DB_PORT='the port e.g. 3306 by default for MySQL'
```
Apply the database migrations running
```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser (admin) running
```bash
python manage.py createsuperuser
```
and fill the required fields

## Run development server in port 3000 (strictly)
```bash
python manage.py runserver 3000
```

## Check for proper running
First, log in using your superuser credentials: [Link](http://127.0.0.1:3000/movies/api/)

