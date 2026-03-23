import requests
from bs4 import BeautifulSoup

def fetch_jobs():
    url = "https://realpython.github.io/fake-jobs/"

    #Takes whole html code from provided url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    #Looks for divs with class in html code
    job_elements = soup.find_all("div", class_="card-content")

    #Takes both title and company name from each div
    for job in job_elements:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
    
        #Saves title and company name in an array
        jobs.append({
            "title": title,
            "company": company
        })

    return jobs
