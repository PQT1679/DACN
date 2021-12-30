import requests
from bs4 import BeautifulSoup

URL = "https://itviec.com/viec-lam-it/android"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
jobs = soup.find_all(class_="job_content",limit=5)

for job in jobs:
    companyname=job.find(class_="logo-wrapper")['title']
    location=job.find(class_="text").text
    print('Tên Công Ty: '+companyname+' Thành Phố: '+location)
    skills=job.find_all(class_="job__skill")
    # jobskills= list()
    jobskills = ''
    for j in skills:
        jobskill=j.span.text
        jobskill=jobskill[1:-1]
        # jobskills.append(jobskill)
        jobskills +=jobskill +','
    jobskills=jobskills[:-1]   #remove dumb ,
    print('Công Ty: '+companyname+' -Vị Trí: '+location+' -Yêu Cầu: '+jobskills)
