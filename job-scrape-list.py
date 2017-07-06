
import requests
import smtplib
import bs4
import os

abbvs = ['MCL', 'PFL', 'OPPL', 'VanPL', 'VicPL', 'FCPL', 'AnyPL', 'BurnPL', 'CoqPL', 'TorPL']
openurls = open('/home/ian/PythonPrograms/job-scrape/urls', 'r')
urls = openurls.read().strip('\n').split(',')
olddocs = ['oldMCL', 'oldPFL', 'oldOPPL', 'oldVanPL', 'oldVicPL', 'oldFCPL', 'oldAnyPL', 'oldBurnPL', 'oldCoqPL', 'oldTorPL']
newdocs = ['newMCL', 'newPFL', 'newOPPL', 'newVanPL', 'newVicPL', 'newFCPL', 'newAnyPL', 'newBurnPL', 'newCoqPL', 'newTorPL']
bstags = ['#content', '.col-md-12', '#main', '#searchResultsShell', '#main', '#containedInVSplit', '.col-sm-7', '.large-9.push-3.main.columns', '.sfContentBlock', '#grid_10']

#TODO: write script for if the document doesn't exist, then it creates it

for url in urls: 
    res = requests.get(url)
    res.raise_for_status()
for bstag in bstags: 
    currentsoup = bs4.BeautifulSoup(res.text, "lxml")
    newsoup = currentsoup.select(bstag)
for newdoc in newdocs:
    if os.path.isfile('/home/ian/Pythonprograms/job-scrape/libsitehtml/'+newdoc) == False:
        createnew = open('/home/ian/PythonPrograms/job-scrape/libsitehtml/'+newdoc, 'w')

    file = open('/home/ian/PythonPrograms/job-scrape/libsitehtml/'+newdoc, 'w')
    file.write(str(newsoup)) 
    file.close()

    new = open('/home/ian/PythonPrograms/job-scrape/libsitehtml/'+newdoc)
    new = new.read()
for olddoc in olddocs:
    if os.path.isfile('/home/ian/Pythonprograms/job-scrape/libsitehtml/'+olddoc) == False:
        createold = open('/home/ian/PythonPrograms/job-scrape/libsitehtml/'+olddoc, 'w')

    old = open('/home/ian/PythonPrograms/job-scrape/libsitehtml/'+olddoc)
    old = old.read()
        
if str(old) != str(new):
    file = open('/home/ian/PythonPrograms/job-scrape/libsitehtml/'+olddoc, 'w') 
    file.write(str(new))
    file.close()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('noreply.job.updates@gmail.com', 'zxcvbnm1029384756')
    server.sendmail('noreply.job.updates.com', 'holmesian17@gmail.com', 'Subject: A library\'s jobs page has changed\n' '\n' + 'Here\'s the URL:' + str(url))
    server.quit()
