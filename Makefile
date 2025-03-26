build:
	@[ -f .env ] || cp .env.example .env
	@docker-compose build

format: up ## Style code
	@docker-compose exec app /bin/bash -c 'isort . && blue . && flake8 .'

test: up ## Run tests
	@docker-compose exec app /bin/bash -c 'pytest app/tests -x -vvv -W ignore'

restart: ## Restart the container
	@docker-compose restart app

cmd: up ## Access bash
	@docker-compose exec app /bin/bash

shell: up ## Access django shell
	@docker-compose exec app /bin/bash -c 'ipython'

up:
	@docker-compose up -d

api: up 
	@docker-compose exec app /bin/bash -c 'uvicorn app.api.app:app --host 0.0.0.0 --port 8000 --reload'

log: 
	@docker-compose logs app -f 

down: 
	@docker-compose down || true

migration: up
	@docker-compose exec app alembic revision --autogenerate -m $(name)

migration_upgrade_head: up
	@docker-compose exec app alembic upgrade head

migration_downgrade_one: up
	@docker-compose exec app alembic downgrade -1

createdb: up
	@docker-compose exec app python3 -m app.cli create-db