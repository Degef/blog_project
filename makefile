all:
	docker run -p 8000:8000 -d blog

build:
	docker build -t blog .

