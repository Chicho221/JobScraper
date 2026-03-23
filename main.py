from scraper import fetch_jobs

def main():
    jobs = fetch_jobs()
    for i, job in enumerate(jobs, 1):
        print(f"{i}. {job['title']} - {job['company']}")

if __name__ == "__main__":
    main()