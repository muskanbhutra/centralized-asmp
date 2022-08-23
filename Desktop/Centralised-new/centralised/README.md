# SARC_Centralised
The Official Website of SARC (Student Alumni Relations Cell) of IIT Bombay where we try to foster a friendly Relationship between Students and Alumns

# Installing MySQl Workbench
https://www.youtube.com/watch?v=WuBcTJnIuzo

# Create Virtual Environment and activate it
virtualenv venv
venv\scripts\activate.bat

# Install all Packages from requirements.txt
pip install -r requirements.txt

# Create a .env file inside SARC folder and paste the following variables in it
SECRET_KEY=django-insecure-2%$_=3+^_j!&x#)mf!&hj%r-51o!2qz*@zcp*cuqqxr%@s^s$r
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=<your email id>
EMAIL_HOST_PASSWORD=<your email password>
NAME=<name of your SQL Database>
USER=<your sql user name>
PASSWORD=<your sql password>
HOST=localhost

# Create a git ignore file
run "touch .gitignore" in git bash

# Ignore files
/venv
/SARC/.env

# Run the web app
python manage.py makemigrations
python manage.py migrate
python manage.py runserver