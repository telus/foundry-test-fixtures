"""Database utilities."""

import sqlite3


def get_connection(db_path: str = "app.db") -> sqlite3.Connection:
    """Return a database connection."""
    return sqlite3.connect(db_path)


def get_user(conn: sqlite3.Connection, user_id: int) -> dict | None:
    """Fetch a user by ID."""
    cursor = conn.execute(
        "SELECT id, name, email FROM users WHERE id = ?", (user_id,)
    )
    row = cursor.fetchone()
    if row:
        return {"id": row[0], "name": row[1], "email": row[2]}
    return None
