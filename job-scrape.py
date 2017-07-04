#! python3
# This program is designed to check a series of webpages for changes in certain parts of their
# code and email me with the changes

import requests
import smtplib
import bs4
import pprint


res = requests.get('https://multcolib.org/about/jobs-library') # Multnomah County
res.raise_for_status()
MCLsoup = bs4.BeautifulSoup(res.text, "lxml")
newMCL = MCLsoup.select('#content')

# opening and reading the old html doc as a string
oldMCL = open('/home/ian/libsitehtml/oldMCL')
oldMCL = oldMCL.read()

#this successfully changes the old document to the new website
if str(newMCL) != str(oldMCL):
    #saves the page as a file to the HD if there are changes
    file = open('/home/ian/libsitehtml/oldMCL', 'w') 
    file.write(str(newMCL))
    file.close()
    #emails me if there are changes
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('noreply.job.updates@gmail.com', 'zxcvbnm1029384756')
    server.sendmail('noreply.job.updates@gmail.com', 'holmesian17@gmail.com', 'Subject: MCL jobs page has changed\n' '\n Here is a link: https://multcolib.org/about/jobs-library')
    server.quit()

res = requests.get('https://libwww.freelibrary.org/jobs/JobList.cfm') # Philadelphia Free Library
res.raise_for_status()
PFLsoup = bs4.BeautifulSoup(res.text, "lxml")
newPFL = PFLsoup.select('.col-md-12')
file = open('/home/ian/libsitehtml/newPFL', 'w')
file.write(str(newPFL))
file.close()

newPFL = open('/home/ian/libsitehtml/newPFL')
newPFL = newPFL.read()

# opening and reading the old html doc as a string
oldPFL = open('/home/ian/libsitehtml/oldPFL')
oldPFL = oldPFL.read()

#this successfully changes the old document to the new website
if str(newPFL) != str(oldPFL):
    #saves the page as a file to the HD if there are changes
    file = open('/home/ian/libsitehtml/oldPFL', 'w') 
    file.write(str(newPFL))
    file.close()
    #emails me if there are changes
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('noreply.job.updates@gmail.com', 'zxcvbnm1029384756')
    server.sendmail('noreply.job.updates@gmail.com', 'holmesian17@gmail.com', 'Subject: PFL jobs page has changed\n' '\n Here is a link: https://multcolib.org/about/jobs-library')
    server.quit()

    


