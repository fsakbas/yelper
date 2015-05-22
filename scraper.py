import scraperwiki
import lxml.html
import re
import time

yelpurl = "http://www.yelp.ca/search?cflt=gyms&find_loc=Calgary%2C+AB#find_desc&start="

html = scraperwiki.scrape(yelpurl)
time.sleep(.2)
root = lxml.html.fromstring(html)

name = root.cssselect('a.biz-name')
address = root.cssselect('address')
phone = root.cssselect('span.biz-phone')

for i in range(len(names)):
    print name[i].text
    print address[i].text
    print phone[i].text

    
