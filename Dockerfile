FROM python:latest
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt


EXPOSE 8000
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["/bin/sh", "-c", "while sleep 1000; do :; done"]