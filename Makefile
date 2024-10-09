run_migrations:
	@echo "Running migrations"
	@alembic revision --autogenerate -m "commit"
	@alembic upgrade head