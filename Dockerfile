FROM python:3.8

RUN apt update && apt install sqlite3


WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python3","app.py"]

