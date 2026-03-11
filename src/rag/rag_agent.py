import os
from google import genai
from rag.vector_store import search, build_index
from rag.ingest_docs import load_documents


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# build index when module loads
docs = load_documents()
build_index(docs)


def career_advice(question):

    docs = search(question)

    context = "\n".join(docs)

    prompt = f"""
You are a career advisor.

Use the following knowledge to answer the question.

Knowledge:
{context}

Question:
{question}

Provide clear career advice.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        # If Gemini is rate/quotas limited, return retrieved context as a fallback.
        if _is_quota_error(e):
            return (
                "Gemini quota/rate limit hit; here are the most relevant notes from your career docs:\n"
                + context
            )
        raise


def _is_quota_error(exc: Exception) -> bool:
    msg = str(exc).lower()
    return ("resource_exhausted" in msg) or ("quota" in msg) or ("429" in msg)