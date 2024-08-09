from psycopg2.extensions import connection


class Pg:
    def __init__(self, conn: connection):
        self.conn = conn
        self.cursor = conn.cursor()

    def commit(self):
        self.conn.commit()

    def add_chat(self, chat_id: int, title: str) -> None:
        query = "INSERT INTO chats (id, title) VALUES (%s, %s) ON CONFLICT DO NOTHING"
        self.cursor.execute(query, (chat_id, title))

    def add_user(self, user_id: int, username: str = None, first_name: str = None, last_name: str = None) -> None:
        queri = "INSERT INTO users (id, username, first_name, last_name) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING"
        self.cursor.execute(queri, (user_id, username, first_name, last_name))

    def add_user_with_chat(
            self,
            user_id: int,
            chat_id: int,
            username: str = None,
            first_name: str = None,
            last_name: str = None,
    ) -> bool:
        self.add_user(user_id, username, first_name, last_name)

        query = "INSERT INTO chat_users (chat_id, user_id) VALUES (%s, %s) ON CONFLICT DO NOTHING RETURNING 1"
        self.cursor.execute(query, (chat_id, user_id))
        res = self.cursor.fetchone()
        return bool(res) and res[0] == 1
