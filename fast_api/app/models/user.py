"""
This module defines the Pydantic model for a user.
"""

from pydantic import BaseModel


class User(BaseModel):
    """Pydantic model for a user."""

    id: int
    user: str
    password: str
    full_name: str
    profile_picture: str


class UserCreate(BaseModel):
    """Pydantic model for creating a user."""

    user: str
    password: str
    full_name: str
    profile_picture: str


class UserUpdate(BaseModel):
    """Pydantic model for updating a user."""

    password: str
    full_name: str
    profile_picture: str
