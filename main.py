from scraper import fetch_jobs
import json

def main():
    jobs = fetch_jobs()
    for i, job in enumerate(jobs, 1):
        print(f"{i}. {job['title']} - {job['company']}")

    with open("JobScraper/jobs.json", "w") as file:
        json.dump(jobs, file, indent=4)
if __name__ == "__main__":
    main()