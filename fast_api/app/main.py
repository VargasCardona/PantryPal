"""
This module initializes the FastAPI application and sets up the database connection
"""

from fastapi import FastAPI, Depends
from starlette.responses import RedirectResponse

# pylint: disable=import-error
from helpers.api_key_auth import get_api_key
from fast_api.app.routes.user_route import user_route

# pylint: enable=import-error

app = FastAPI(
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
