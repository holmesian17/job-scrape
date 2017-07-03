
import requests
import smtplib
import bs4

abbvs = ['MCL', 'PFL', 'OPPL']
urls = ['https://multcolib.org/about/jobs-library', 'https://libwww.freelibrary.org/jobs/JobList.cfm', 'http://oppl.org/get-involved/jobs']
docs = ['Multnomah County Library Old', 'Philly Free Library Old', 'Oak Park Library Old']

for url in urls: 
    res = requests.get(url)
    res.raise_for_status()
    current = res.text
    for doc in docs:
        open('/home/ian/libsitehtml/'+doc)
    if current == doc:
        break
    else:
        playFile = open('/home/ian/libsitehtml/'+doc, 'wb')
        for chunk in res.iter_content(100000):
            playFile.write(chunk)
        playFile.close()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('noreply.job.updates@gmail.com', 'zxcvbnm1029384756')
        server.sendmail('noreply.job.updates.com', 'holmesian17@gmail.com', 'Subject: ' + str(abbvs) +' jobs page has changed\n' '\n' + 'Here\'s the URL:' + str(url))
        server.quit()
