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
