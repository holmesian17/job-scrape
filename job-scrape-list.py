
import requests
import smtplib
import bs4

abbvs = ['MCL', 'PFL', 'OPPL', '']
urls = ['https://multcolib.org/about/jobs-library', 'https://libwww.freelibrary.org/jobs/JobList.cfm', 'http://oppl.org/get-involved/jobs']
olddocs = ['oldMCL', 'oldPFL', 'oldOPPL']
newdocs = ['newMCL', 'newPFL', 'newOPPL']
bstags = ['#content', '.col-md-12', '#main']

for url in urls: 
    res = requests.get(url)
    res.raise_for_status()
    for bstag in bstags: 
        currentsoup = bs4.BeautifulSoup(res.text, "lxml")
        newsoup = currentsoup.select(bstag)
    for newdoc in newdocs: #this could trip me up, olddoc might need to be under here too
        file = open('/home/ian/libsitehtml/'+newdoc, 'w')
        file.write(str(newsoup)) #this could trip me up
        file.close()

        new = open('/home/ian/libsitehtml/'+newdoc)
        new = new.read()
    for olddoc in olddocs:
        old = open('/home/ian/libsitehtml/'+olddoc)
        old = old.read()
    if str(old) != str(new):
        file = open('/home/ian/libsitehtml/'+olddoc, 'w') 
        file.write(str(new))
        file.close()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('noreply.job.updates@gmail.com', 'zxcvbnm1029384756')
        server.sendmail('noreply.job.updates.com', 'holmesian17@gmail.com', 'Subject: ' + str(abbvs) +' jobs page has changed\n' '\n' + 'Here\'s the URL:' + str(url))
        server.quit()
        