import requests
from bs4 import BeautifulSoup

def scrape_job_postings():
    url = 'https://www.indeed.com/jobs?q=software+developer&l=Remote'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    jobs = []
    for job_elem in soup.find_all('div', class_='jobsearch-SerpJobCard'):
        title = job_elem.find('h2', class_='title').text.strip()
        company = job_elem.find('span', class_='company').text.strip()
        location = job_elem.find('div', class_='location').text.strip() if job_elem.find('div', class_='location') else 'Remote'
        summary = job_elem.find('div', class_='summary').text.strip()
        
        jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'summary': summary
        })

    return jobs

# Example usage
if __name__ == "__main__":
    job_listings = scrape_job_postings()
    for job in job_listings:
        print(f"Title: {job['title']}")
        print(f"Company: {job['company']}")
        print(f"Location: {job['location']}")
        print(f"Summary: {job['summary']}")
        print('-' * 40)
