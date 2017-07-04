
import requests
import smtplib
import bs4

abbvs = ['MCL', 'PFL', 'OPPL']
urls = ['https://multcolib.org/about/jobs-library', 'https://libwww.freelibrary.org/jobs/JobList.cfm', 'http://oppl.org/get-involved/jobs']
docs = ['oldMCL', 'oldPFL', 'oldOPPL']

for url in urls: 
    res = requests.get(url)
    res.raise_for_status()
    current = res.text
    for doc in docs:
        open('/home/ian/libsitehtml/'+doc)
    if str(current) != str(doc):
        file = open('/home/ian/libsitehtml/'+doc, 'w') 
        file.write(current)
        file.close()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('noreply.job.updates@gmail.com', 'zxcvbnm1029384756')
        server.sendmail('noreply.job.updates.com', 'holmesian17@gmail.com', 'Subject: ' + str(abbvs) +' jobs page has changed\n' '\n' + 'Here\'s the URL:' + str(url))
        server.quit()
        