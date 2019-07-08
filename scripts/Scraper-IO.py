import requests
from bs4 import BeautifulSoup

input_urls = input('Enter urls separated by a comma. Be sure to include http:// or https:// and www. etc.' + '\r\n');
list_urls = input_urls.split(',');

#urls string list
urls = list_urls;

def getResults(url):
    result = requests.get(url);
    return result;

for url in urls:
    print('processing: ' + url + '\r\n');
    result = getResults(url);
    status = 'Ok';
    if result.status_code >= 500:
        status = 'Error';
    print('status: ' + str(result.status_code));
    source = result.content;
    soup = BeautifulSoup(source, 'lxml');
    links = soup.find_all('a');
    print(links);
    divs = soup.find_all('div');
    print(divs);

#use reqest module to provide access to web page.

#result = requests.get('https://www.google.com');

#to make sure page was accessed:
#print(result.status_code);

#headers if you need them.
#print(result.headers);

#extract content from request url page.
#source = result.content;
#print(source);

#parse source to BS object
#sourceSoup = BeautifulSoup(source, 'lxml');

#links
#links = sourceSoup.find_all('a');
#print(links);
#print('\n');

#getting a single link by text content, and href attr.

#for link in links:
 #   if "About" in link.text:
 #       print(link);
 #       print(link.attrs['href']);


#divs = sourceSoup.find_all('div');
#print(divs);
