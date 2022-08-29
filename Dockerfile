FROM python:3.10.4-alpine

RUN pip install -r requirements.txt

COPY . /botenv

WORKDIR /botenv

CMD ["python", "bot.py"]


