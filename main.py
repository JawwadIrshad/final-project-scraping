from bs4 import BeautifulSoup
import requests
import time
import os

print('Put some skill that you are interested')
unfamiliar_skill=input('>')
print(f'Filtering out {unfamiliar_skill}')

def save_jobs(jobs_info):
    with open('jobs.txt', 'w') as file:  
        for job in jobs_info:
            job_str = f"Company Name: {job['company_name']}\nRequired Skills: {job['skills']}\nMore Info: {job['more_info']}"
            file.write(job_str + '\n\n')


def find_all_jobs():
    job_info_list = [] 
    page=1
    while len(job_info_list)<1000: 
        html_text =requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
        soup =BeautifulSoup(html_text,'lxml')
        jobs =soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
        for job in jobs:
            
            published_date =job.find('span',class_='sim-posted').span.text
            if 'month' in published_date:
                company_name =job.find('h3',class_='joblist-comp-name').text.replace(' ','')
                skills=job.find('span',class_='srp-skills').text.replace(' ','')
                more_info = job.header.h2.a['href']
                if unfamiliar_skill in skills:
                    job_info = {
                    "company_name": company_name.strip(),
                    "skills": skills.strip(),
                    "more_info": more_info
                }
                job_info_list.append(job_info)  # Append job information to the list
                print(f"company name: {company_name.strip()}")
                print(f"required skills: {skills.strip()}")
                print(f'more info: {more_info}')
                print('')
                if len(job_info_list)>=1000:
                    break 
            page +=1
    return job_info_list  # Return the list of job information


if __name__ =='__main__':
    while True:
        jobs_info=find_all_jobs()
        time_wait =10
        save_jobs(jobs_info)
        print(f'Waiting{time_wait} minutes...')
        time.sleep(time_wait*60)
              