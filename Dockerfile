FROM python:2.7

RUN mkdir /kapost

WORKDIR /kapost

COPY requirements.txt /kapost
RUN pip install –no-cache-dir -r requirements.txt

COPY kapost.py /kapost

ENTRYPOINT [ “python”, “-u”, “./kapost.py”]

