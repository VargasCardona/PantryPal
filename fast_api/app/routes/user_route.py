"""
This module defines the routes for user-related operations in the FastAPI application.
Routes:
    - POST /users/: Create a new user.
    - GET /users: Retrieve a list of all users.
    - GET /users/{user_id}: Retrieve a specific user by their ID.
    - PUT /users/{user_id}: Update a specific user by their ID.
    - DELETE /users/{user_id}: Delete a specific user by their ID.
Functions:
    - create_users(user: User): Creates a new user with the provided details.
    - get_users(): Retrieves a list of all users from the database.
    - get_user(user_id: int): Retrieves a specific user by their ID. 
      Returns an error message if the user is not found.
    - update_user(user_id: int, user: User): Updates a specific user by their ID.
    - delete_user(user_id: int): Deletes a specific user by their ID.
Dependencies:
    - UserModel: The database model for users.
    - User: The Pydantic model for user data validation.
    - APIRouter: FastAPI router for defining routes.
    - Body: FastAPI dependency for parsing request bodies.
"""

from fastapi import APIRouter, Body

# pylint: disable=import-error
from database import UserModel
from fast_api.app.models.user import User

# pylint: enable=import-error

user_route = APIRouter()


@user_route.post("/users/")
def create_users(user: User = Body(...)):
    """
    Create a new user.

    Args:
        user (User): The user object containing the name, age, email,
        address, is_employed and salary.

    Returns:
        None
    """
    UserModel.create(
        user=user.user,
        password=user.password,
        full_name=user.full_name,
        profile_picture=user.profile_picture,
    )
    return {"message": "User created successfully"}


@user_route.get("/users")
def get_users():
    """
    Retrieve a list of users from the database.

    This function queries the UserModel to select all users with an ID greater than 0,
    converts the result to a dictionary format, and returns it as a list.

    Returns:
        list: A list of dictionaries, each representing a user.
    """
    user = UserModel.select().where(UserModel.id > 0).dicts()
    return list(user)


@user_route.get("/users/{user_id}")
def get_user(user_id: int):
    """
    Retrieve a user by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        UserModel: The user object if found.
        dict: An error message if the user is not found.
    """
    try:
        user = UserModel.get(UserModel.id == user_id)
        return user
    except UserModel.DoesNotExist:
        return {"error": "User not found"}


@user_route.put("/users/{user_id}")
def update_user(user_id: int, user: User = Body(...)):
    """
    Update a user by their ID.

    Args:
        user_id (int): The ID of the user to update.
        user (User): The user object containing the updated details.

    Returns:
        None
    """
    UserModel.update(
        password=user.password,
        full_name=user.full_name,
        profile_picture=user.profile_picture,
    ).where(UserModel.id == user_id).execute()
    return {"message": "User updated successfully"}


@user_route.delete("/users/{user_id}")
def delete_user(user_id: int):
    """
    Delete a user by their ID.

    Args:
        user_id (int): The ID of the user to delete.

    Returns:
        None
    """
    UserModel.delete().where(UserModel.id == user_id).execute()
    return {"message": "User deleted successfully"}
