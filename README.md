# eXpertHub-authority-backend

## Start
```bash
python manage.py runserver 0.0.0.0:12307
```

## Migrate
```bash
python manage.py makemigrations authority_backend
python manage.py migrate
```

## Preparation
```bash
conda install django mysqlclient
```

```sql
create database auth_backend;
```