#Age calculator  for 100 years

'''
this program calculates the year when  someone turns into their 100 years.
'''

import datetime
NAME = input('What is your name: ')
AGE = int(input('Enter your age: '))

today_date = str(datetime.date.today())
current_year = int(today_date[:4])
result = 100 - AGE
year_needed = current_year + result

copies = int(input('How many copies you may need to print'))

print(copies * f'Hello {NAME}, you will celebrate your 100th birthday in the year {year_needed} \n')
