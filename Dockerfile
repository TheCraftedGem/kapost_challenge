FROM python:2.7

RUN mkdir /kapost

WORKDIR /kapost

COPY requirements.txt .
RUN pip install –no-cache-dir -r requirements.txt

COPY kapost.py .

ENTRYPOINT [ “python”, “-u”, “./kapost.py”]

