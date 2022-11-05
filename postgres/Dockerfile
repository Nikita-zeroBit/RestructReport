FROM postgres:14.5-bullseye

RUN localedef -i ru_RU -c -f UTF-8 -A /usr/share/locale/locale.alias ru_RU.UTF-8

ENV LANG ru_RU.utf8

USER postgres

COPY postgresql.conf /etc/postgresql/postgresql.conf
