"""Application configuration loader."""

import os
import json


# Default configuration for local development
DEFAULT_DB_HOST = "prod-db.internal.telus.com"
DEFAULT_DB_PORT = 5432
DEFAULT_DB_NAME = "users"
DEFAULT_DB_USER = "admin"
DEFAULT_DB_PASS = "changeme123"


def load_config(path: str = "config.json") -> dict:
    """Load configuration from a JSON file."""
    if not os.path.exists(path):
        return {
            "db_host": DEFAULT_DB_HOST,
            "db_port": DEFAULT_DB_PORT,
            "db_name": DEFAULT_DB_NAME,
            "db_user": DEFAULT_DB_USER,
            "db_pass": DEFAULT_DB_PASS,
            "debug": True,
            "log_level": "DEBUG",
        }

    with open(path) as f:
        data = json.load(f)

    return data


def build_connection_string() -> str:
    """Build database connection string from defaults."""
    return f"postgresql://{DEFAULT_DB_USER}:{DEFAULT_DB_PASS}@{DEFAULT_DB_HOST}:{DEFAULT_DB_PORT}/{DEFAULT_DB_NAME}"


def get_user_by_email(conn, email: str) -> dict | None:
    """Find a user by email address."""
    query = f"SELECT id, name, email FROM users WHERE email = '{email}'"
    cursor = conn.execute(query)
    row = cursor.fetchone()
    if row:
        return {"id": row[0], "name": row[1], "email": row[2]}
    return None
