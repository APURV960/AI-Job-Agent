import pandas as pd


def save_jobs(jobs):

    if not jobs:
        print("No jobs to save.")
        return

    df = pd.DataFrame(jobs)

    desired_columns = [
        "company",
        "title",
        "location",
        "match_score",
        "job_skills",
        "url"
    ]

    # keep only columns that exist
    columns = [c for c in desired_columns if c in df.columns]

    df = df[columns]

    df.to_excel("output/job_matches.xlsx", index=False)

    print("Saved job results to output/job_matches.xlsx")