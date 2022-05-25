FROM python:3.10

WORKDIR /src

COPY requirements.txt . 

RUN pip install -r requirements.txt 

COPY . . 

ENV PYTHONPATH=$PATH

CMD ["python3", "bot/game.py"]

