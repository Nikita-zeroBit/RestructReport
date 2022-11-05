FROM python:3.10.7-slim-bullseye as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN useradd -m -s /bin/sh flask \
     && mkdir -p /home/flask

WORKDIR /home/flask

COPY requirements.txt .
RUN apt-get update \
     && apt-get install --no-install-recommends \
     build-essential=12.9 gcc=4:10.2.1-1 \
     netcat=1.10-46 dos2unix=7.4.1-1 -y \
     && apt-get clean && rm -rf /var/lib/apt/lists/* \
     && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN find . -type f -print0 | xargs -0 dos2unix \
     && chown -R flask:flask /home/flask \
     && chmod u+x /home/flask/entrypoint.sh \
     && chmod u+x /home/flask/api/geventapp.py

FROM base as api

USER flask

EXPOSE 5000

ENTRYPOINT ["/home/flask/entrypoint.sh"]