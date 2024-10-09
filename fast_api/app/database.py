"""
This module sets up the database connection and defines the ORM models for the application.
Classes:
    UserModel(Model): ORM model for the 'users' table.
"""

import os
from dotenv import load_dotenv

from peewee import (
    AutoField,
    CharField,
    Model,
    MySQLDatabase,
)


load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class UserModel(Model):
    """
    UserModel is a database model representing a user with various attributes.
    """

    id = AutoField(primary_key=True)
    user = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)
    full_name = CharField(max_length=50)
    profile_picture = CharField(max_length=50)

    # pylint: disable=R0903
    class Meta:
        """
        Meta class for configuring database settings.
        Attributes:
            database: The database connection instance.
            table_name (str): The name of the table in the database.
        """

        database = database
        table_name = "users"
