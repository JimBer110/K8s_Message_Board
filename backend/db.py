import psycopg2
import os


class DB_Handler:

    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            host=os.environ['DB_HOST'],
            port=os.environ['DB_PORT']
        )
        self.create_table()

    def __del__(self):
        self.conn.close()

    def create_table(self):
        """
        Creates the messages table if it doesn't already exist.
        """
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                message TEXT NOT NULL,
                username TEXT NOT NULL
            );
        """)
        cur.close()
        self.conn.commit()

    def add_message(self, message, username):
        """
        Adds a new message to the database.

        Args:
            message (str): The message to be added.
            username (str): The username of the user who sent the message.

        Returns:
            int: The ID of the newly added message.
        """
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO messages (message, username) VALUES (%s, %s) RETURNING id", (message, username))
        self.conn.commit()
        id = cur.fetchone()[0]
        cur.close()
        return id

    def modify_message(self, id, message):
        """
        Modifies an existing message in the database.

        Args:
            id (int): The ID of the message to be modified.
            message (str): The new message text.

        Returns:
            bool: True if the message was modified successfully, False otherwise.
        """
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE messages SET message = %s WHERE id = %s", (message, id))
        self.conn.commit()
        status = cur.rowcount == 1
        cur.close()
        return status

    def delete_message(self, id):
        """
        Deletes a message from the database.

        Args:
            id (int): The ID of the message to be deleted.

        Returns:
            bool: True if the message was deleted successfully, False otherwise.
        """
        cur = self.conn.cursor()
        cur.execute("DELETE FROM messages WHERE id = %s", (id,))
        self.conn.commit()
        status = cur.rowcount == 1
        cur.close()
        return status
