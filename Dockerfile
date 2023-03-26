FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./req.txt /app/req.txt

RUN pip install -U pip && \
    pip install -r req.txt

COPY ./app /app
