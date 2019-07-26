# -*- coding: utf-8 -*-
"""
Scraping data from the pypi website
Last modified: 15/7/19
"""

import bs4
import requests
import csv
from tqdm import tqdm
import re
import codecs

def scrape_package(name):
    """
    Returns name, dates, versions, project description for given input
    Example return value:    
    ["Name", [("07 Oct, 2018", "3.0.1")], "Project Description"]
    """
    project_link = 'https://pypi.org/project/' + name
    history_link = project_link + "#history"
    description_link = project_link + "#description"
    history_page = requests.get(history_link)
    description_page = requests.get(description_link)
    #project no longer exists
    if (history_page.status_code != 200):
        return []
    history_soup = bs4.BeautifulSoup(history_page.text, 'lxml')
    description_soup = bs4.BeautifulSoup(description_page.text, 'lxml')
    #shortlisting the area where the required information is
    list_of_releases = history_soup.find_all("a", class_ \
                            = re.compile('release.*'))
    #extracting dates of release
    dates = []
    for stuff in list_of_releases:
        dates2 = stuff.find_all('time')
        for date in dates2:
            temp_date = date.get_text()
            dates.append(temp_date[3:-1])
    #extracting all version numbers
    versions = []       
    for stuff in list_of_releases:
        versions2 = stuff.find_all(class_ = 'release__version')
        for version in versions2:
            temp_version = version.get_text()
            versions.append(temp_version[19:-18])
    #extracting project description
    description = description_soup.find(class_ \
                    = "package-description__summary")
    proj_description = description.get_text()
    date_vers_list = []
    for i in range(len(dates)):
        date_vers_list.append((versions[i], dates[i]))
    return [name, date_vers_list, proj_description]

#reading the data off the list of all projects
response = requests.get('https://pypi.org/simple/')
soup = bs4.BeautifulSoup(response.text, 'lxml')

#curates list of project names
names = []
for link in soup.find_all('a'):
    name = link.get('href')
    names.append(name[8:-1])

#writes the scraped data to a CSV file
with codecs.open('project_and_date.csv','w',encoding = "utf-8") as csvFile:
    writer = csv.writer(csvFile)
    for name in tqdm(names[:]):
        writer.writerow(scrape_package(name))