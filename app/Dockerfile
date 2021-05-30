FROM python:3.8.5-alpine
COPY . /app
WORKDIR /app
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt

CMD ["python","app.py"]