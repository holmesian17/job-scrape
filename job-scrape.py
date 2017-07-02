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

import bs4
import requests
import smtplib

MCLchange = []
res = requests.get('https://multcolib.org/about/jobs-library') # Multnomah County
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

MCLtext = soup.select('#content')
print(MCLtext)

MCLchange.append(MCLtext)
oldMCL = open('Multnomah County library Old')

if MCLchange != oldMCL:
    #saves the page as a file to the HD
    playFile = open('Multnomah County library Old', 'wb') 
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()
    msg = 'Subject: MCL jobs page has changed'
    fromaddr = 'ianatnorthfield@gmail.com'
    toaddrs = ['holmesian17@gmail.com']

    


