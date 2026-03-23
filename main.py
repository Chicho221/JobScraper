from scraper import fetch_jobs
import json

def main():
    jobs = fetch_jobs()
    for i, job in enumerate(jobs, 1):
        print(f"{i}. {job['title']} - {job['company']}")

    #Saves in JSON file
    with open("JobScraper/jobs.json", "w") as file:
        json.dump(jobs, file, indent=4)

    #Asks for keyword and filters array
    while True:
        keyword = input("Enter keyword: ").lower()
        filtered = [job for job in jobs if keyword in job["title"].lower()]

        #Prints all jobs with keyward entered
        for job in filtered:
            print(f"{job['title']} - {job['company']}")

if __name__ == "__main__":
    main()