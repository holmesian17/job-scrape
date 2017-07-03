
import requests
import smtplib


libraries = {'Multnomah County Library': {'Abbv' : 'MCL', 'URL' : 'https://multcolib.org/about/jobs-library', 'Doc' : 'Multnomah County Library Old'} ,
             'Philadelphia Free Library': {'Abbv' : 'PFL', 'URL' : 'https://libwww.freelibrary.org/jobs/JobList.cfm', 'Doc' : 'Philly Free Library Old'}}

abbvs = ['MCL', 'PFL']
urls = ['https://multcolib.org/about/jobs-library', 'https://libwww.freelibrary.org/jobs/JobList.cfm']
docs = ['Multnomah County Library Old', 'Philly Free Library Old']

for url in urls: 
    res = requests.get(url)
    res.raise_for_status()
    current = res.text
    for doc in docs:
        open(doc)
    if current != doc:
        playFile = open(doc, 'wb')
        for chunk in res.iter_content(100000):
            playFile.write(chunk)
        playFile.close()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('noreply.job.updates@gmail.com', 'zxcvbnm1029384756')
        server.sendmail('noreply.job.updates.com', 'holmesian17@gmail.com', 'Subject: ' + str(abbvs) +' jobs page has changed\n' + str(url))
        server.quit()
    
