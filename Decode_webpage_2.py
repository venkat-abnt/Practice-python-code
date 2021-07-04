'''This program did not executed at first in the command line but executing in the Jupiter note book.
After installing requests, bs4 and lxml packages/libraries in command line using pip install, this got executed in command line.
This Program asks decodes a web page and get you the titles or items/elements associated to a particular class of the webpage 
'''
import requests, bs4, lxml
link = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
res = requests.get(link)
soup = bs4.BeautifulSoup(res.text, 'lxml')

'''below is to get the titles'''
result = soup.select('P')#'P' stands for paragraph contents
for i in result:
	print(i.getText()) #for each element of the soup, we are fetching its text


