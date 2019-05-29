FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY requirements.txt /tmp/

RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

COPY app.py /app/main.py
COPY models.py /app/models.py
COPY manage.py /app/manage.py
COPY templates/ /app/templates/
COPY static/ /app/static/
