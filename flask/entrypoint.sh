#!/bin/sh

# Загружаем переменные виртуального окружения из файла ./.env
load_enviroment () {
  if [ -f /home/flask/.env ]
  then
    export $(grep -v '^#' /home/flask/.env | xargs)
  else
    echo "File does not exist: /home/flask/.env"
    exit 1
  fi
}

# Проверяем доступность PostgreSQL
check_postgres () {
    echo "Waiting for PostgreSQL on ${DB_HOST}:${DB_PORT} ..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 1
    done

    echo "PostgreSQL started!"
}
#
## Проверяем доступность Redis
#check_redis () {
#    echo "Waiting for Redis on ${REDIS_HOST}:${REDIS_PORT} ..."
#
#    while ! nc -z $REDIS_HOST $REDIS_PORT; do
#      sleep 1
#    done
#
#    echo "Redis started!"
#}

start_server () {
  echo "Starting '${APP_NAME}' on ${APP_HOST}:${APP_PORT} ..."
  
  gunicorn --worker-class gevent --workers 1 --bind $APP_HOST:$APP_PORT api.geventapp:app
  # GUNICORN_CMD_ARGS="--bind=${APP_HOST} --workers=1" gunicorn -k uvicorn.workers.UvicornWorker 'api:create_app()'
}

load_enviroment
check_postgres
#check_redis
start_server

exec "$@"