# check website html against the html of the previous day
# if != then send me an email
# can i get it to send me the job title too?
# have a look at what chase has done

# download the webstie html for the jobs (not the whole site, that could change and i won't care)
# save it into a list or file or dictionary - whatever is easiest
# have the program download the current day's html for the jobs
# if previous change != new html then save new html as previous change
    # and email me a notification and the new job 
# need to do this for multiple (30+) webpages - can this be done all in one code?
# need to find the relevant html parts for each site
# loop through the list of websites? - save to different things for comparison?     

#! python3
# This program is designed to check a series of webpages for changes in certain parts of their
# code and email me with the changes

import requests
import smtplib


res = requests.get('https://multcolib.org/about/jobs-library') # Multnomah County
res.raise_for_status()

newMCL = res.text

# opening and reading the old html doc as a string
oldMCL = open('Multnomah County library Old')
oldMCL = oldMCL.read()

#this successfully changes the old document to the new website
if newMCL != oldMCL:
    #saves the page as a file to the HD
    playFile = open('Multnomah County library Old', 'wb') 
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()
    #emails me if there are changes
    #TODO: right now it emails me regardless -> need it to only email if there have been changes    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('noreply.job.updates@gmail.com', 'zxcvbnm1029384756')
    server.sendmail('noreply.job.updates@gmail.com', 'holmesian17@gmail.com', 'Subject: MCL jobs page has changed\nhttps://multcolib.org/about/jobs-library')
    server.quit()



    


