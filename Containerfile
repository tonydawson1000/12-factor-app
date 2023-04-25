FROM python:3.11-slim-bullseye

WORKDIR /twelve-factor-app

COPY requirements.txt /twelve-factor-app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

COPY . /twelve-factor-app

CMD python app.py