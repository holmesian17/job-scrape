import requests
import smtplib
import bs4
import os

abbvs = ['MCL', 'PFL', 'OPPL', 'FCPL', 'AnyPL', 'NOLS', 'VanWaPL', 'SLCPL', 'ProPL', 'ArapPL']
openurls = open('/home/ian/PythonPrograms/job-scrape/urls', 'r')
urls = openurls.read().strip('\n').split(',')
bstags = ['#content', '.col-md-12', '#main', '#containedInVSplit', '.col-sm-7', '.statement-left-div', '#main', '#main', '#componentBox', '.list-group.job-listings']

for abbv, url, bstag in zip(abbvs, urls, bstags):
    res = requests.get(url)
    res.raise_for_status()
    olddoc = 'old'+abbv
    currentsoup = bs4.BeautifulSoup(res.text, "lxml")
    newsoup = str(currentsoup.select(bstag))

    filepath = '/home/ian/PythonPrograms/job-scrape/libsite/'+olddoc

    if os.path.isfile(filepath):
        with open(filepath) as old:
            oldsoup = old.read()
    else:
        oldsoup = ''

    if newsoup != oldsoup:
        with open(filepath, 'w') as new:
            new.write(newsoup)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('noreply.job.updates@gmail.com', 'password')
        server.sendmail('noreply.job.updates.com', 'email', 'Subject: A library\'s jobs page has changed\n' '\n' + 'Here\'s the URL:' + str(url))
        server.quit()
