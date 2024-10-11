#!/bin/sh

# Run migrations
make run_migrations

# Start the application
exec uvicorn main:app --host 0.0.0.0 --port 80
