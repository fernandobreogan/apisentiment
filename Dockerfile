FROM python:3.7.6

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3","src/api_endpoints.py"]