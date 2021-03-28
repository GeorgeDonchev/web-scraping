import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://dev.bg/company/?s=python&post_type=job_listing'


def url_to_html(url):
    res = requests.get(url)
    if res.status_code == 200:
        html_text = res.text
        with open('data/file.html', 'w', encoding = 'utf8') as fl:
            fl.write(html_text)
        return html_text
    return ''


def html_to_csv(url):
    soup = BeautifulSoup(url_to_html(url), 'html.parser')
    jobs = soup.find_all('div', class_='job-details-left')
    headers = ['Company', 'Description', 'Features', 'More Details']
    jobs_list = []
    for job in jobs:
        features_list = []
        features = job.div.find_all('span', class_='search-job-category-name')
        for feature in features:
            features_list.append(feature.text)
        description = job.find('h3').text.strip()
        job_details = job.h3.a['href']
        company_name, location = job.find('div', class_='small-txt txt-grey').text.split(' | ')
        current_job = [company_name, description, ", ".join(features_list), job_details]
        jobs_list.append(current_job)

    db = pd.DataFrame(jobs_list, columns = headers)
    db.to_csv('data/jobs.csv', index = True)