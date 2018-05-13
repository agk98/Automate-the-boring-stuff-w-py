#! python 3
#lucky.py-Opens several Google search results


import bs4,requests, webbrowser, sys
print('Googling...')#display text while downloading the google page
res=requests.get('http://google.com/search?q='+' '.join(sys.argv[1:]))
res.raise_for_status()
#TODO: Retrieve top search result links
soup=bs4.BeautifulSoup(res.text)

#TODO: Open a browser tab for each results
linkElems=soup.select('.r a')
numOpen=min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com'+linkElems[i].get('href'))
