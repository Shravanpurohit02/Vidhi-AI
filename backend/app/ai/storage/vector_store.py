from __future__ import annotations

import json
import math
import sqlite3
from pathlib import Path


class PersistentVectorStore:

    def __init__(
        self,
        db_path: str = "vector_store.db",
    ):

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
        text: str,
        metadata: dict,
        embedding: list[float],
    ) -> None:

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

    def all(self) -> list[dict]:

        cursor = self.conn.execute("SELECT id,text,metadata,embedding FROM vectors")

        rows = []

        for row_id, text, metadata, embedding in cursor.fetchall():

            rows.append(
                {
                    "id": row_id,
                    "text": text,
                    "metadata": json.loads(metadata),
                    "embedding": json.loads(embedding),
                }
            )

        return rows

    def count(self) -> int:

        cursor = self.conn.execute("SELECT COUNT(*) FROM vectors")

        return int(cursor.fetchone()[0])

    def clear(self) -> None:

        self.conn.execute("DELETE FROM vectors")
        self.conn.commit()

    def delete(
        self,
        vector_id: int,
    ) -> None:

        self.conn.execute(
            "DELETE FROM vectors WHERE id=?",
            (vector_id,),
        )

        self.conn.commit()

    @staticmethod
    def _cosine(
        a: list[float],
        b: list[float],
    ) -> float:

        if not a or not b:
            return 0.0

        dot = sum(x * y for x, y in zip(a, b))

        na = math.sqrt(sum(x * x for x in a))
        nb = math.sqrt(sum(y * y for y in b))

        if na == 0 or nb == 0:
            return 0.0

        return dot / (na * nb)

    def search(
        self,
        embedding: list[float],
        top_k: int = 5,
    ) -> list[dict]:

        scored = []

        for item in self.all():

            score = self._cosine(
                embedding,
                item["embedding"],
            )

            item = dict(item)
            item["score"] = score

            scored.append(item)

        scored.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        return scored[:top_k]

    def close(self) -> None:

        if self.conn:
            self.conn.close()

    def __enter__(self):

        return self

    def __exit__(
        self,
        exc_type,
        exc,
        tb,
    ):

        self.close()

    def __del__(self):

        try:
            self.close()
        except Exception as exc:
            print(exc)
