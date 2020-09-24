FROM python:3.7

WORKDIR /updater/

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/updater"

CMD python run.py
