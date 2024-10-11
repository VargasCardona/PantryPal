#!make
#alembic_commit = ''

copy_migrations:
	@docker cp backend:/alembic/versions ./FastApi/app/alembic

run_migrations:
	@echo "${GREEN}--> RUN MIGRATIONS"
	@echo "COMMIT--> $(alembic_commit)"
	@docker exec -it backend /bin/bash -c "alembic merge heads"
	@docker exec -it backend /bin/bash -c "alembic stamp heads"
	@docker exec -it backend /bin/bash -c "alembic revision --autogenerate -m '$(alembic_commit)"
	@docker exec -it backend /bin/bash -c "alembic upgrade head"
	@docker cp backend:/app/alembic/versions ./FastApi/app/alembic

