# DevOps Learning Initiative #DevOpsInitiative
This project is a part of devops learning initiave to get all related project
search #devOpsInitiative
1.  Test
2.  Build
3.  Release
4.  Deploy

# todobackend
It is a sample django rest framework TodoApp 

### 1.  Setup Guide
```
# clone this repo 
git clone https://github.com/abhishek-jaiswal/todobackend.git

# go to project directory
cd todobackend/src

# install requirements
pip install -r requirements.txt

# run migrations and 
python manage.py makemigrations --settings=todobackend.settings.base
python manage.py migrate --settings=todobackend.settings.base

# start app 
python manage.py runserver --settings=todobackend.settings.base


# to run unit tests
python manage.py test --settings=todobackend.settings.test
```
