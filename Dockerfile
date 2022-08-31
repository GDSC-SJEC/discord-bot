FROM python:3.10.4-alpine

COPY . /BOT

WORKDIR /BOT

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
