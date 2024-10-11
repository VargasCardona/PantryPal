"""
This module defines the routes for user-related operations in the FastAPI application.
Routes:
    - POST /: Create a new user.
    - GET /: Retrieve a list of users from the database.
    - GET /{user_id}: Retrieve a user by their ID.
    - PUT /{user_id}: Update a user by their ID.
    - DELETE /{user_id}: Delete a user by their ID.
Functions:
    - create_users(user: UserCreate): Create a new user.
    - get_users(): Retrieve a list of users from the database.
    - get_user(user_id: int): Retrieve a user by their ID.
    - update_user(user_id: int, user: UserUpdate): Update a user by their ID.
    - delete_user(user_id: int): Delete a user by their ID.
"""

from fastapi import APIRouter, Body
from peewee import IntegrityError

# pylint: disable=import-error
from config.database import UserModel
from models.user import UserCreate, UserUpdate

# pylint: enable=import-error

user_route = APIRouter()


@user_route.post("/")
def create_users(user: UserCreate = Body(...)):
    """
    Create a new user.

    Args:
        user (User): The user object containing the name, age, email,
        address, is_employed and salary.

    Returns:
        None
    """
    try:
        UserModel.create(
            user=user.user,
            password=user.password,
            full_name=user.full_name,
            profile_picture=user.profile_picture,
        )
        return {"message": "User created successfully"}
    except IntegrityError:
        return {"error": "User already exists"}


@user_route.get("/")
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


@user_route.get("/{user_id}")
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


@user_route.put("/{user_id}")
def update_user(user_id: int, user: UserUpdate = Body(...)):
    """
    Update a user by their ID.

    Args:
        user_id (int): The ID of the user to update.
        user (User): The user object containing the updated details.

    Returns:
        None
    """
    try:
        UserModel.update(
            password=user.password,
            full_name=user.full_name,
            profile_picture=user.profile_picture,
        ).where(UserModel.id == user_id).execute()
        return {"message": "User updated successfully"}
    except UserModel.DoesNotExist:
        return {"error": "User not found"}


@user_route.delete("/{user_id}")
def delete_user(user_id: int):
    """
    Delete a user by their ID.

    Args:
        user_id (int): The ID of the user to delete.

    Returns:
        None
    """
    try:
        UserModel.delete().where(UserModel.id == user_id).execute()
        return {"message": "User deleted successfully"}
    except UserModel.DoesNotExist:
        return {"error": "User not found"}
