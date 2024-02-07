# Test Project of Referral system

## Technologies that were used

1. Django
3. PostgreSQL
4. Redis
5. JWT
6. Swagger
7. Docker
8. Celery

---

> **Note: You have to add environment variables, if u want email sender to work! EMAIL_HOST_USER, EMAIL_HOST_PASSWORD**

---

## How to run

```bash
docker-compose up
```

---

**Make sure that you have python setup that can be referenced with command python to easily follow the tutorial. If your python is referenced with python, then replace all pythons with python**

## Install Docker

### For Linux

```
sudo apt install -y \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
                "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
                $(lsb_release -cs) \
                stable"

sudo apt update && sudo apt upgrade

sudo apt install -y docker-ce docker-ce-cli containerd.io

sudo usermod -aG docker "$USER"
```

### For Windows

Follow the steps [here](https://docs.docker.com/docker-for-windows/install/)

## Download postgres image and run it with Docker

### For Linux

```
sudo apt update && sudo apt upgrade
sudo apt install python-pip python-dev libpq-dev
```

### For Windows

```
python -m pip install --upgrade pip
```

## Run postgres

```
docker run -d --name postgres --restart always -p 127.0.0.1:5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=gozle_ads postgres:14.8-alpine
```

## Run redis for caching

```
docker run -d --name redis -p 6379:6379 -d redis:7.0.5-alpine
```

**Your terminal must be in the root of the gozle ads project for all the commands below !!**


## Install Dependencies

> **Note: If you have incompatible python version, you can install [pyenv](https://github.com/pyenv/pyenv) to manage python versions!**

### Activate venv

### For linux

```
source .venv/bin/activate
```

### For Windows

```
./.venv/bin/activate
```

### Install packages for local development

```
pip install -r requirements.txt
```

## Migrate

```
python manage.py migrate
```

## Run Celery

```
celery -A gozle_ads worker -l info
```

## Run Celery Beat

```
celery -A gozle_ads beat -l INFO
```

## Create superuser

```
python manage.py createsuperuser
```

## Runserver

```
python manage.py runserver
```
