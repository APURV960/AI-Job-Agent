import psycopg2
import os
import dotenv
dotenv.load_dotenv()


def get_connection():

    return psycopg2.connect(
        host="localhost",
        database="ai_agent",
        user="postgres",
        password=os.getenv("DB_PASSWORD")
    )