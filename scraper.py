import scraperwiki
import lxml.html
import re
import time

yelpurl = "http://www.yelp.ca/search?cflt=gyms&find_loc=Calgary%2C+AB#find_desc&start="
index = 1

for x in range(0, 205, 10):
    print x
    html = scraperwiki.scrape(yelpurl + x)
    time.sleep(.2)
    root = lxml.html.fromstring(html)
    
    name = root.cssselect('a.biz-name')
    address = root.cssselect('address')
    phone = root.cssselect('span.biz-phone')
    
    for i in range(len(name)):
        scraperwiki.sqlite.save(unique_keys=["pk"], data={
                'pk': index,
                'name': name[i].text.encode('utf8'),
                'address': address[i].text.encode('utf8'),
                'phone': phone[i].text.encode('utf8'),
            })
        index += 1
        #print name[i].text.encode('utf8')
       # print address[i].text.encode('utf8')
       # print phone[i].text.encode('utf8')

    
