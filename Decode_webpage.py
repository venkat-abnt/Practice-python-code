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

"""
incase if you want to write the results/extracts from the webpage to a file
you can use the below code to do so.
if you dont want it into a file, you can ignore this below section of code
"""
FILE_NAME = input('Enter the filename to store the content of the webpage: ')
for i in range(len(Title)):#as this Title is a beautiful soup type object, we need to loop through it as it may have many items depending upon the webpage
	with open(FILE_NAME,'a') as file:
		file.write('\n' + Title[i].getText())

