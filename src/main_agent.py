from dotenv import load_dotenv
load_dotenv()

from excel_writer import save_jobs
from agent.executor import run_agent


def main():

    goal = "Find best jobs and prepare applications"

    print("Goal:", goal)

    try:
        result = run_agent(goal, "data/resume.pdf")
    except Exception as e:
        print("Agent execution failed:", e)
        return

    if not result:
        print("Agent returned no results.")
        return

    ranked_jobs = result.get("ranked_jobs", [])
    gap = result.get("skill_gap", {})
    letters = result.get("letters", [])

    # Skill gap output
    if gap:
        print("\nTop Missing Skills:")
        print(gap.get("missing_skills"))

    # Cover letter output
    if letters:
        print("\nGenerated Cover Letters:")
        for l in letters:
            print(f"{l['company']} -> {l['file']}")

    # Save jobs
    if ranked_jobs:
        save_jobs(ranked_jobs)
        print("\nJob results saved successfully.")
    else:
        print("\nNo ranked jobs found.")


if __name__ == "__main__":
    main()