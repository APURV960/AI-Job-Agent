from memory.database import get_connection


def save_resume(user_id, resume_text):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO resumes (user_id, content) VALUES (%s,%s)",
        (user_id, resume_text)
    )

    conn.commit()
    conn.close()


def save_jobs(user_id, jobs):

    conn = get_connection()
    cur = conn.cursor()

    for job in jobs:

        cur.execute(
            """
            INSERT INTO job_results
            (user_id, job_title, company, match_score)
            VALUES (%s,%s,%s,%s)
            """,
            (
                user_id,
                job["title"],
                job["company"],
                job["match_score"]
            )
        )

    conn.commit()
    conn.close()