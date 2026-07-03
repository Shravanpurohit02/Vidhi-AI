from sqlalchemy import inspect

from app.database.database import engine


def test_workspace_tables():

    tables = inspect(engine).get_table_names()

    assert "notes" in tables
    assert "evidence" in tables
    assert "bookmarks" in tables
    assert "annotations" in tables
