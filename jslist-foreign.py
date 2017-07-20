import requests
import smtplib
import bs4
import os

abbvs = ['VanPL', 'VicPL',  'BurnPL', 'CoqPL', 'TorPL', 'HamPL', 'StC', 'Burl']
openurls = open('/home/ian/PythonPrograms/job-scrape/foreign_urls', 'r')
urls = openurls.read().strip('\n').split(',')
bstags = ['#searchResultsShell', '#main', '.large-9.push-3.main.columns', '.sfContentBlock', '#grid_10', '.field-item.even', '.blog', '#content']

for abbv, url, bstag in zip(abbvs, urls, bstags):
    res = requests.get(url)
    res.raise_for_status()
    olddoc = 'old'+abbv
    currentsoup = bs4.BeautifulSoup(res.text, "lxml")
    newsoup = str(currentsoup.select(bstag))

    filepath = '/home/ian/PythonPrograms/job-scrape/libsiteforeign/'+olddoc

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
        server.sendmail('noreply.job.updates.com', 'email', 'Subject: A foreign library\'s jobs page has changed\n' '\n' + 'Here\'s the URL:' + str(url))
        server.quit()
