'''This program is not executing in the command line but executing in the Jupiter note book.
After installing requests, bs4 and lxml packages/libraries in command line using pip install, this got executed in command line.
This Program asks decodes a web page and get you the titles or items/elements associated to a particular class of the webpage 
'''
import requests, bs4, lxml
link = 'https://www.deccanchronicle.com/'
res = requests.get(link)
soup = bs4.BeautifulSoup(res.text, 'lxml')

'''below is to get the titles'''
Title = soup.select('title')
print(Title)

'''Below code is to get all the elements/things from a class.
Here the class is 'col-sm-12 noPadding stry-top-big-a', i have used . inplace for space as per syntax in webscrapping in below code.
so now we will get all the things associated with that class
'''
item = 0
result = soup.select('.col-sm-12.noPadding.stry-top-big-a')
while item < len(result):
	print(result[item].getText())
	item += 1

