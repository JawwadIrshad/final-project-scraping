import csv
from bs4 import BeautifulSoup
import requests

def save_jobs(jobs_info):
    with open('jobs.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Company Name', 'Job Link'])
        for job in jobs_info:
            writer.writerow([job['company_name'], job['job_link']])

def find_jobs(skill):
    job_info_list = []
    page = 1
    while len(job_info_list) < 12:
        html_text = requests.get(f'https://pk.linkedin.com/jobs/jobs-in-karachi-division?keywords={skill}&position=1&pageNum={page}').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('ul', class_='jobs-search__results-list')
        for job in jobs:
            job_links = job.find_all('a', class_='base-card__full-link')
            company_names = job.find_all('h3', class_="base-search-card__title")
            for link, name in zip(job_links, company_names):
                job_info = {
                    'company_name': name.text.strip(),
                    'job_link': link['href'],
                     
                }
                job_info_list.append(job_info)
        page += 1
    save_jobs(job_info_list)

skill = input("Enter the skill you're looking for: ")
find_jobs(skill)  
