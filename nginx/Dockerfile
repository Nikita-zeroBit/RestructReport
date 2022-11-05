FROM nginx:1.23.1-alpine

RUN rm /etc/nginx/conf.d/default.conf /etc/nginx/nginx.conf \
    && mkdir -p /data/log 
COPY nginx.conf /etc/nginx/nginx.conf
COPY app.conf /etc/nginx/conf.d/app.conf

VOLUME [ "/data/log", ]
