# Define the flag file
MIGRATIONS_FLAG = .migrations_done
alembic_commit = ''

# Target to copy migrations
copy_migrations:
	@docker cp -r alembic/versions ./fast_api/app/alembic

# Target to run migrations
run_migrations:
	@if [ ! -f $(MIGRATIONS_FLAG) ]; then \
		echo "${GREEN}--> RUN MIGRATIONS"; \
		echo "COMMIT--> $(alembic_commit)"; \
		alembic merge heads; \
		alembic stamp heads; \
		alembic revision --autogenerate -m '$(alembic_commit)'; \
		alembic upgrade head; \
		touch $(MIGRATIONS_FLAG); \
	else \
		echo "${GREEN}--> Migrations already run. Skipping."; \
	fi

# Target to clean up (remove flag)
clean_migrations:
	@rm -f $(MIGRATIONS_FLAG)
