import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="ai_agent",
    user="postgres",
    password="Apurvaa825000#",
    port=5432
)

print("Connected!")