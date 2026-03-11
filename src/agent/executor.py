from agent.planner import decide_next_action

from tools.resume_tool import analyze_resume
from tools.job_search_tool import find_jobs
from tools.ranking_tool import rank_job_results
from tools.skill_gap_tool import analyze_skill_gap
from tools.cover_letter_tool import create_cover_letters
from memory.memory_store import save_resume, save_jobs
from rag.rag_agent import career_advice

def run_agent(goal, resume_path):

    context = {}

    for _ in range(5):

        action = decide_next_action(goal, context)

        print("Agent action:", action)

        if action == "analyze_resume":

            result = analyze_resume(resume_path)

            context.update(result)

            save_resume(1, context["resume_text"])


        elif action == "search_jobs":

            jobs = find_jobs(context["skills"])

            context["jobs"] = jobs

        elif action == "rank_jobs":

            ranked = rank_job_results(
            context["resume_text"],
            context["jobs"]
            )
            context["ranked_jobs"] = ranked

            save_jobs(1, ranked[:20])

        elif action == "analyze_skill_gap":

            gap = analyze_skill_gap(
                context["skills"],
                context["ranked_jobs"]
            )

            context["skill_gap"] = gap
            advice = career_advice(
                "What skills should I learn to become a machine learning engineer?"
            )

            print("\nCareer Advice:")
            print(advice)

        elif action == "generate_cover_letters":

            letters = create_cover_letters(
                context["resume_text"],
                context["ranked_jobs"]
            )

            context["letters"] = letters

            break

    return context