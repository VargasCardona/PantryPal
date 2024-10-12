"""
This module initializes the FastAPI application and sets up the database connection
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from starlette.responses import RedirectResponse

# pylint: disable=W0613, W0621
# pylint: disable=W0613, W0613
# pylint: disable=import-error
from helpers.api_key_auth import get_api_key
from routes.user_route import user_route
from config.database import database as connection

# pylint: enable=import-error


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager that runs the startup and shutdown events of the FastAPI application.
    """
    if connection.is_closed():
        connection.connect()
    try:
        yield
    finally:
        if not connection.is_closed():
            connection.close()


app = FastAPI(
    lifespan=lifespan,
    title="Microservice for PantryPal",
    version="2.0",
    contact={
        "name": "Nicolás Vargas Cardona - Mateo Loaiza García",
        "url": "https://github.com/VargasCardona",
    },
)


@app.get("/", include_in_schema=False)
def read_root():
    """
    Root endpoint that redirects to the API documentation.

    Returns:
        RedirectResponse: A response object that redirects the client to the "/docs" URL.
    """
    return RedirectResponse(url="/docs")


# -------- User --------
app.include_router(
    user_route,
    prefix="/api/users",
    tags=["Users"],
    dependencies=[Depends(get_api_key)],
)
