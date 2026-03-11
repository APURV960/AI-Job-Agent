import os
from google import genai
import dotenv
dotenv.load_dotenv()   

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_cover_letter(resume_text, job):
    def _is_quota_error(exc: Exception) -> bool:
        msg = str(exc).lower()
        return ("resource_exhausted" in msg) or ("quota" in msg) or ("429" in msg)

    def _fallback_letter() -> str:
        title = job.get("title", "the role")
        company = job.get("company", "your company")
        return (
            f"Dear Hiring Manager at {company},\n\n"
            f"I’m writing to express my interest in the {title} position. "
            "My experience aligns well with the role, and I’m confident I can contribute value quickly.\n\n"
            "I’d welcome the opportunity to discuss how my background matches your needs. "
            "Thank you for your time and consideration.\n\n"
            "Sincerely,\n"
            "Your Name\n"
        )

    prompt = f"""
Write a short professional cover letter.

Resume:
{resume_text}

Job Title: {job['title']}
Company: {job['company']}

Job Description:
{job['description']}

Keep it concise and tailored.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        # If Gemini quota/rate limit is hit, return a usable template instead of failing.
        if _is_quota_error(e):
            return _fallback_letter()
        raise