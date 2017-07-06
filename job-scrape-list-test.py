
import requests
import smtplib
import bs4

#TODO: make it so these lists can be imported from elsewhere - have files that are the list items

openabbvs = open('/home/ian/PythonPrograms/job-scrape/abbvs', 'r')
abbvs = openabbvs.read().strip('\n').split(',') 
openurls = open('/home/ian/PythonPrograms/job-scrape/urls', 'r')
urls = openurls.read().strip('\n').split(',')
openolddocs = open('/home/ian/PythonPrograms/job-scrape/olddocs', 'r')
olddocs = openolddocs.read().strip('\n').split(',')
opennewdocs =  open('/home/ian/PythonPrograms/job-scrape/newdocs', 'r')
newdocs = opennewdocs.read().strip('\n').split(',')
openbstags = open('/home/ian/PythonPrograms/job-scrape/bstags', 'r')
bstags = openbstags.read().strip('\n').split(',')   

#TODO: write script for if the document doesn't exist, then it creates it

for url in urls: 
    res = requests.get(url)
    res.raise_for_status()
for bstag in bstags: 
    currentsoup = bs4.BeautifulSoup(res.text, "lxml")
    newsoup = currentsoup.select(bstag)
for newdoc in newdocs: #this could trip me up, olddoc might need to be under here too
    file = open('/home/ian/PythonPrograms/job-scrape/libsitehtml/'+newdoc, 'w')
    file.write(str(newsoup)) #this could trip me up
    file.close()

    new = open('/home/ian/PythonPrograms/job-scrape/libsitehtml/'+newdoc)
    new = new.read()
for olddoc in olddocs:
    old = open('/home/ian/PythonPrograms/job-scrape/libsitehtml/'+olddoc)
    old = old.read()
def equal_elements(urls, abbvs):
    return [abbv for abbv, url in zip(urls, abbvs) if abbv == url]
if str(old) != str(new):
    equal_elements()
    file = open('/home/ian/PythonPrograms/job-scrape/libsitehtml/'+olddoc, 'w') 
    file.write(str(new))
    file.close()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('noreply.job.updates@gmail.com', 'zxcvbnm1029384756')
    server.sendmail('noreply.job.updates.com', 'holmesian17@gmail.com', 'Subject: ' + str(abbv) +' jobs page has changed\n' '\n' + 'Here\'s the URL:' + str(url))
    server.quit()