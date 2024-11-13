# fast-api-celery-docker-rabbitmq

docker-compose down && docker-compose up -d --build

Run ./createdbs.sh to create de batabases

docker exec -it db psql -U postgres -c "CREATE DATABASE fastapirob;"
docker exec -it api uvicorn main:app --host=0.0.0.0 --port=8000 --reload

docker exec -it celery celery -A celery.celery worker -l info
docker exec -it celery celery -A celery.celery worker -l info


docker exec -it flower celery -A src.celery.celery flower --broker=amqp://guest:guest@rabbit:5672//


http://localhost:8000/docs#/

Flower
http://localhost:5555/

pytest . -v

