# Common developer commands. Run e.g.  make dev   or   make test
.PHONY: install dev up down logs migrate revision fmt test

install:        ## install runtime + dev dependencies
	pip install -r requirements-dev.txt

dev:            ## run the API locally with autoreload
	uvicorn main:app --app-dir src --reload

up:             ## build and start the full Docker stack
	docker compose up --build

down:           ## stop the Docker stack
	docker compose down

logs:           ## follow the api container logs
	docker compose logs -f api

migrate:        ## apply all Alembic migrations
	alembic upgrade head

revision:       ## create a migration:  make revision m="add foo"
	alembic revision --autogenerate -m "$(m)"

fmt:            ## format code with black
	black src alembic tests

test:           ## run the test suite
	pytest
