'''
Name: John Niagwan
ID: 121092225
'''
import re 
 
tel_num = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') 
mo = tel_num.search('My telephone number is 555-877-5678. Or you can reach me on my cell: 555-212-0771. Call me!') 
print('Found phone number: ' + mo.group())
print(f"Test commit")