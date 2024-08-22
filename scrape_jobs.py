from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
import time

def scrape_jobs_with_selenium(url):
    # Path to the chromedriver executable
    chromedriver_path = os.path.join(os.getcwd(), 'chromedriver.exe')  # Use 'chromedriver' on macOS/Linux
    
    # Initialize the Chrome WebDriver with the Service object
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service)
    
    # Open the URL
    driver.get(url)
    
    # Wait for job listings to load (adjust the class name if necessary)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'jobsearch-SerpJobCard'))  # Update class name if needed
        )
    except Exception as e:
        print(f"Error waiting for job listings: {e}")
    
    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    jobs = []
    
    # Find all job listing elements (update the class name if needed)
    job_elements = soup.find_all('div', class_='jobsearch-SerpJobCard')  # Update class name if needed
    print(f"Found {len(job_elements)} job listings.")
    
    # Extract job details
    for job_element in job_elements:
        title = job_element.find('h2', class_='title')
        company = job_element.find('span', class_='company')
        location = job_element.find('div', class_='location')

        jobs.append({
            'title': title.get_text(strip=True) if title else 'N/A',
            'company': company.get_text(strip=True) if company else 'N/A',
            'location': location.get_text(strip=True) if location else 'N/A',
        })
    
    # Optional: Keep the browser open for a few seconds before closing
    time.sleep(5)
    driver.quit()
    
    return jobs

# Example usage
url = 'https://www.indeed.com/jobs?q=software+developer&l=Remote'
scraped_data = scrape_jobs_with_selenium(url)

# Print the scraped job data
for job in scraped_data:
    print(f"Title: {job['title']}, Company: {job['company']}, Location: {job['location']}")
