FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY requirements.txt /tmp/

RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

COPY app.py /app/main.py
COPY models.py /app/models.py
COPY manage.py /app/manage.py

RUN python manage.py db init
RUN python manage.py db migrate
RUN python manage.py db upgrade

COPY templates/ /app/templates/
COPY static/ /app/static/
