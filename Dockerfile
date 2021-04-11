FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/rest

COPY . requirements.txt /usr/src/

RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/sampleproject

EXPOSE 8000

#CMD python /usr/src/sampleproject/manage.py makemigrations && python /usr/src/sampleproject/manage.py migrate && python /usr/src/sampleproject/manage.py loaddatdoca data.json && python /usr/src/sampleproject/manage.py runserver 0.0.0.0:8000