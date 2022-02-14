import re
import os
import re

with open ('C:\\Users\\Arseny\\Desktop\\грамоты.txt') as file:
	file = file.read()

no_num = re.sub(r'[0-9]', '', file)
no_spc = re.sub(r'\s', '', no_num)
print(re.findall('с[ь][][]'))	
