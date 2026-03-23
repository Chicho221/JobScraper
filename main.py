from scraper import fetch_jobs
from datetime import datetime
import json

def main():

    #Takes timestamp and formats it    
    def timestamp():
        time = datetime.now()
        formatted_time = time.strftime("%Y-%m-%d %H:%M")
        return formatted_time
    
    jobs = fetch_jobs()
    for i, job in enumerate(jobs, 1):
        print(f"{i}. {job['title']} - {job['company']}")   
    print(f"\nScraped at: {timestamp()}\n")

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
        print(f"\nFiltered at: {timestamp()}\n")
if __name__ == "__main__":
    main()