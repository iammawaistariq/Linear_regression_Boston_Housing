FROM python:3.12
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $port 5000
CMD gunicorn --workers=4 --bind 0.0.0.0:$port app:app
