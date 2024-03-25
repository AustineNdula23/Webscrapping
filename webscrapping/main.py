from bs4 import BeautifulSoup
import requests

print('put some skills that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35'

html_text = requests.get(url)

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ ='clearfix job-bx-shd-bx')
for index, job in enumerate(jobs):
    published_date = job.find('span', class_ ='sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_='joblist-como-name').text.replace(' ','')
        Skills = job.find('span', class_='srp-skills').text.replaxce(' ','')
        more_info = job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            with open(f'posts/{index}.txt','w')as f:
                f.write(f"Company Name: {company_name.strip()}")
                f.write(f"Required Skills: {skills.strip()}")
                f.write(f"More Info: {more_info}")
            print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)