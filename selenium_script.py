from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def post_job_to_portal(job_details):
    driver = webdriver.Chrome(executable_path='C:/path_to_chromedriver/chromedriver.exe')  # Update this path
    driver.get('https://example-job-portal.com/login')

    # Log in to the job portal
    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')
    username.send_keys('your_username')
    password.send_keys('your_password')
    password.send_keys(Keys.RETURN)

    # Navigate to the job posting page
    driver.get('https://example-job-portal.com/post_job')

    # Fill in job details
    job_title = driver.find_element_by_name('job_title')
    job_description = driver.find_element_by_name('job_description')
    job_location = driver.find_element_by_name('job_location')
    job_title.send_keys(job_details['title'])
    job_description.send_keys(job_details['description'])
    job_location.send_keys(job_details['location'])

    # Submit the job posting
    driver.find_element_by_name('submit').click()

    # Close the browser
    driver.quit()
