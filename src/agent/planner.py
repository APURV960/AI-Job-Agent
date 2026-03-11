"""
Planner for selecting the next tool/action.

Default behavior is deterministic to avoid LLM quota/rate limits:
it selects the next step based on what's present in the context.
"""


def decide_next_action(goal, context):
    # Deterministic planner: avoids Gemini API calls entirely.
    # This keeps the pipeline running even on free-tier limits.
    if not context.get("resume_text") or not context.get("skills"):
        return "analyze_resume"

    if not context.get("jobs"):
        return "search_jobs"

    if not context.get("ranked_jobs"):
        return "rank_jobs"

    if not context.get("skill_gap"):
        return "analyze_skill_gap"

    return "generate_cover_letters"