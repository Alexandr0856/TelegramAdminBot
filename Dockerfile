FROM python:3.12

WORKDIR /app

COPY telegram/requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY telegram /app

ENV ENV=production

CMD ["python3", "run.py"]