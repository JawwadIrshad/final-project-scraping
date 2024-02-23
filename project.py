
import csv
from bs4 import BeautifulSoup
import requests

def save_jobs(jobs_info):
    with open('jobs.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Posted-name', 'Company Name', 'Job Link', 'Posting Time'])  # Added 'Posting Time' to the header
        for job in jobs_info:
            writer.writerow([job['posted_name'], job['company_name'], job['job_link'], job['posting_time']])

def find_jobs(skill):
    job_info_list = []
    page = 1
    while len(job_info_list) < 1200:
        html_text = requests.get(f'https://pk.linkedin.com/jobs/jobs-in-karachi-division?keywords={skill}&position=1&pageNum={page}').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('body')
        for job in jobs:
            posted_name = job.find_all('h4', class_='base-search-card__subtitle')
            job_links = job.find_all('a', class_='base-card__full-link')
            company_names = job.find_all('h3', class_="base-search-card__title")
            posting_time = job.find_all('time', class_='job-search-card__listdate')
            for link, name, desc,time in zip(job_links, company_names, posted_name,posting_time):
                job_info = {
                    'posted_name': desc.text.strip(), 
                    'company_name': name.text.strip(),
                    'job_link': link['href'],
                    'posting_time':time .text.strip()
                }
                job_info_list.append(job_info)
        page += 1
    save_jobs(job_info_list)

skill = input("Enter the skill you're looking for: ")
find_jobs(skill)