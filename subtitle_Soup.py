import requests
from bs4 import BeautifulSoup
 
count = 0
usearch = input("Movie Name? : ")
search_url = "https://www.yifysubtitles.com/search?q="+usearch.replace(" ","+")
base_url = "https://www.yifysubtitles.com"
#print(search_url)
resp = requests.get(search_url)
soup = BeautifulSoup(resp.content, 'lxml')
for link in soup.find_all("div",{"class": "media-body"}):       #Get the exact class:'media-body'
    imdb = link.find('a')['href']                               #Find the link in that class, which is the exact link we want
    movie_url = base_url+imdb                                   #Merge the result with base string to navigate to the movie page
   # print("Movie URL : {}".format(movie_url))                   #Print the URL just to check.. :p
 
    next_page = requests.get(movie_url)                         #Soup number 2 begins here, after navigating to the movie page
    soup2 = BeautifulSoup(next_page.content,'lxml')
    #print(soup2.prettify())
    for links in soup2.find_all("tr",{"class": "high-rating"}): #Navigate to subtitle options with class as high-rating
        for flags in links.find("td", {"class": "flag-cell"}):  #Look for all the flags of subtitles with high-ratings
            if flags.text == "English":                         #If flag is set to English then get the download link
                for dlink in links.find_all("td",{"class": "download-cell"}):   #Once English check is done, navigate to the download class "download-cell" where the download href exists
                    half_link = dlink.find('a')['href']         #The problem was in the line before this one, I used find() instead of find_all()
                    download = base_url + half_link
                    print("Movie subtitle-link:  {}".format(download))