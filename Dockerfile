FROM python:2-slim

RUN mkdir /kapost.py

WORKDIR /kapost.py

COPY requirements.txt /kapost.py
RUN pip install –no-cache-dir -r requirements.txt

COPY kapost.py /kapost

ENTRYPOINT [ “python”, “-u”, “./kapost.py”]
