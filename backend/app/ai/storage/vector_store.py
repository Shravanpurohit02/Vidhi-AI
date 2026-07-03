import json
import sqlite3
from pathlib import Path


class PersistentVectorStore:

    def __init__(self, db_path="vector_store.db"):

        self.db_path = Path(db_path)

        self.conn = sqlite3.connect(self.db_path)

        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS vectors(
            id INTEGER PRIMARY KEY,
            text TEXT,
            metadata TEXT,
            embedding TEXT
        )
        """)

        self.conn.commit()

    def add(
        self,
        text,
        metadata,
        embedding,
    ):

        self.conn.execute(
            """
            INSERT INTO vectors(
                text,
                metadata,
                embedding
            )
            VALUES(?,?,?)
            """,
            (
                text,
                json.dumps(metadata),
                json.dumps(embedding),
            ),
        )

        self.conn.commit()

    def all(self):

        cursor = self.conn.execute(
            "SELECT text,metadata,embedding FROM vectors"
        )

        return cursor.fetchall()
