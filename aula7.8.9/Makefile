

docker.install:
	docker-compose build --force-rm

docker.run:
	docker-compose up

start:
	poetry run bot start

docker.import.model: docker run
	docker-compose exec ollama ollama