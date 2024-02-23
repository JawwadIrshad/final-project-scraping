# import csv
# from bs4 import BeautifulSoup
# import requests

# def save_jobs(jobs_info):
#     with open('jobs.csv', 'w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Company Name', 'Job Link'])
#         for job in jobs_info:
#             writer.writerow([job['company_name'], job['job_link']])

# def find_jobs(skill):
#     job_info_list = []
#     page = 1
#     while len(job_info_list) < 12:
#         html_text = requests.get(f'https://pk.linkedin.com/jobs/jobs-in-karachi-division?keywords={skill}&position=1&pageNum={page}').text
#         soup = BeautifulSoup(html_text, 'lxml')
#         jobs = soup.find_all('ul', class_='jobs-search__results-list')
#         for job in jobs:
#             job_links = job.find_all('a', class_='base-card__full-link')
#             company_names = job.find_all('h3', class_="base-search-card__title")
#             job_soup = BeautifulSoup( 'lxml')
#             job_description = job_soup.find('div', class_='jobs-box__html-content jobs-description-content__text t-14 t-normal jobs-description-content__text--stretch')
#             for link, name in zip(job_links, company_names):
#                 job_info = {
#                     'company_name': name.text.strip(),
#                     'job_link': link['href'],
#                      'job_description': job_description
#                 }
#                 job_info_list.append(job_info)
#         page += 1
#     save_jobs(job_info_list)

# skill = input("Enter the skill you're looking for: ")
# find_jobs(skill)  


# import csv
# from bs4 import BeautifulSoup
# import requests

# def save_jobs(jobs_info):
#     with open('jobs.csv', 'w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Company Name', 'Job Link', 'Job Description'])
#         for job in jobs_info:
#             writer.writerow([job['company_name'], job['job_link'], job['job_description']])

# def find_jobs(skill):
#     job_info_list = []
#     page = 1
#     while len(job_info_list) < 12:
#         html_text = requests.get(f'https://pk.linkedin.com/jobs/jobs-in-karachi-division?keywords={skill}&position=1&pageNum={page}').text
#         soup = BeautifulSoup(html_text, 'lxml')
#         jobs = soup.find_all('ul', class_='jobs-search__results-list')
#         for job in jobs:
#             job_links = job.find_all('a', class_='base-card__full-link')
#             company_names = job.find_all('h3', class_="base-search-card__title")
#             for link, name in zip(job_links, company_names):
#                 job_url = 'https://pk.linkedin.com' + link['href']
#                 job_html = requests.get(job_url).text
#                 job_soup = BeautifulSoup(job_html, 'lxml')
#                 job_description = job_soup.find('div', class_='jobs-box__html-content jobs-description-content__text t-14 t-normal jobs-description-content__text--stretch')
#                 if job_description:
#                     job_info = {
#                         'company_name': name.text.strip(),
#                         'job_link': job_url,
#                         'job_description': job_description.text.strip()
#                     }
#                     job_info_list.append(job_info)
#                     if len(job_info_list) >= 12:
#                         break
#         page += 1
#     save_jobs(job_info_list)

# skill = input("Enter the skill you're looking for: ")
# find_jobs(skill)


# import csv
# from bs4 import BeautifulSoup
# import requests

# def save_jobs(jobs_info):
#     with open('jobs.csv', 'w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Company Name', 'Job Link', 'Job Description'])
#         for job in jobs_info:
#             writer.writerow([job['company_name'], job['job_link'], job['job_description']])

# def find_jobs(skill):
#     job_info_list = []
#     page = 1
#     while len(job_info_list) < 12:
#         url = f'https://pk.linkedin.com/jobs/jobs-in-karachi-division?keywords={skill}&position=1&pageNum={page}'
#         html_text = requests.get(url).text
#         soup = BeautifulSoup(html_text, 'lxml')
#         jobs = soup.find_all('body')
#         for job in jobs:
#             job_links = job.find_all('a', class_='base-card__full-link')
#             company_names = job.find_all('h3', class_="base-search-card__title")
#             for link, name in zip(job_links, company_names):
#                 job_url = 'https://pk.linkedin.com' + link['href']
#                 try:
#                     job_html = requests.get(job_url).text
#                     job_soup = BeautifulSoup(job_html, 'lxml')
#                     job_description = job_soup.find('div', class_='jobs-box__html-content jobs-description-content__text t-14 t-normal jobs-description-content__text--stretch')
#                     if job_description:
#                         job_info = {
#                             'company_name': name.text.strip(),
#                             'job_link': job_url,
#                             'job_description': job_description.text.strip()
#                         }
#                         job_info_list.append(job_info)
#                         if len(job_info_list) >= 12:
#                             break
#                 except Exception as e:
#                     print(f"An error occurred while fetching job details: {e}")
#         page += 1
#     save_jobs(job_info_list)

# skill = input("Enter the skill you're looking for: ")
# find_jobs(skill)


# import csv
# from bs4 import BeautifulSoup
# import requests

# def save_jobs(jobs_info):
#     with open('jobs.csv', 'w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Company Name', 'Job Link', 'Job Description'])
#         for job in jobs_info:
#             writer.writerow([job['company_name'], job['job_link'], job['job_description']])


# def find_jobs(skill):
#     job_info_list = []
#     page = 1
#     while len(job_info_list) < 1:
#         html_text = requests.get(f'https://pk.linkedin.com/jobs/jobs-in-karachi-division?keywords={skill}&position=1&pageNum={page}').text
#         soup = BeautifulSoup(html_text, 'lxml')
#         jobs = soup.find_all('body')
#         for job in jobs:
#             job_links = job.find_all('a', class_='base-card__full-link')
#             company_names = job.find_all('h3', class_="base-search-card__title")
#             job_descriptions = job.find_all('div', class_='show-more-less-html__markup relative overflow-hidden')
#             print(f".....................{job_descriptions}")
#             for link, name, desc_div in zip(job_links, company_names, job_descriptions):
#                 job_description_paragraphs = desc_div.find_all('p')
#                 job_description_text = '\n'.join(p.text.strip() for p in job_description_paragraphs)
#                 job_info = {
#                     'company_name': name.text.strip(),
#                     'job_link': link['href'],
#                     'job_description': desc_div.get_text(separator='\n')  # Extracting text from div
#                 }
#                 job_info_list.append(job_info)
#         page += 1
#     save_jobs(job_info_list)

# skill = input("Enter the skill you're looking for: ")
# find_jobs(skill)  


import csv
from bs4 import BeautifulSoup
import requests

def save_jobs(jobs_info):
    with open('jobs.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Job Description', 'Company Name', 'Job Link'])  # Changed the order to print job_description first
        for job in jobs_info:
            writer.writerow([job['job_description'], job['company_name'], job['job_link']])

def find_jobs(skill):
    job_info_list = []
    page = 1
    while len(job_info_list) < 12:
        html_text = requests.get(f'https://pk.linkedin.com/jobs/jobs-in-karachi-division?keywords={skill}&position=1&pageNum={page}').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('body')
        for job in jobs:
            job_descriptions = job.find_all('h4', class_='base-search-card__subtitle')
            job_links = job.find_all('a', class_='base-card__full-link')
            company_names = job.find_all('h3', class_="base-search-card__title")
            for link, name, desc in zip(job_links, company_names, job_descriptions):
                job_info = {
                    'job_description': desc.text.strip(), 
                    'company_name': name.text.strip(),
                    'job_link': link['href']
                }
                job_info_list.append(job_info)
        page += 1
    save_jobs(job_info_list)

skill = input("Enter the skill you're looking for: ")
find_jobs(skill)
