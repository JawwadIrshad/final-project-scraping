    
import csv
from bs4 import BeautifulSoup
import requests

def save_jobs(jobs_info):
    with open('jobs.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for job in jobs_info:
            writer.writerow([job['company_name'], job['skills'], job['more_info']])

def find_jobs(unfamiliar_skill):
    job_info_list = []
    page = 1
    while len(job_info_list) < 1200:
        html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText={unfamiliar_skill}&txtKeywords={unfamiliar_skill}&txtLocation&page={page}').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        for job in jobs:
            published_date = job.find('span', class_='sim-posted').span.text
            if 'few' in published_date:
                company_name = job.find('h3', class_='joblist-comp-name').text.strip()
                skills = job.find('span', class_='srp-skills').text.strip()
                more_info = job.header.h2.a['href']
                if unfamiliar_skill in skills:
                    job_info = {
                        "company_name": company_name,
                        "skills": skills,
                        "more_info": more_info
                    }
                    job_info_list.append(job_info)
           
        page += 1
       
       
    return job_info_list

if __name__ =='__main__':
    print('Put some skill that you are interested')
    unfamiliar_skill = input('>')
    print(f'Filtering out {unfamiliar_skill} wait a few minutes')
    
    jobs_info = find_jobs(unfamiliar_skill)
    save_jobs(jobs_info)
    print("****Jobs details saved to jobs.csv****")
