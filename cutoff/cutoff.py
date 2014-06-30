import re
import sys

# REGION DICTIONARY
rc_file = open('data_region_code','r+')
rc_data = rc_file.read()
rc_file.close()
rc_data = rc_data.strip()
rc_data = rc_data.split('\n')

rc_dict = {}

for i in range(0, len(rc_data)):
	rc_data[i] = rc_data[i].split(",")
	rc_dict[rc_data[i][2]] = rc_data[i][1] 


def cap_junk_remover(cap_file_name, header, foot_begin, foot_end, my_cap_file_name):
	cap_file = open(cap_file_name, 'r+')
	cap_data = cap_file.read()
	cap_file.close()
	cap_data = re.sub(header , '' , cap_data)
	footer = str(foot_begin+'(.*?)'+foot_end)
	print footer
	smart_string = re.match(footer , cap_data)
	smart_string = smart_string.group()
	cap_data = re.sub(smart_string , '' , cap_data)

	my_cap_file = open(my_cap_file_name ,'w+')
	my_cap_file.write(cap_data)
	my_cap_file.close()


head = 'Directorate of Technical Education, Maharashtra State, Mumbai Cut Off List of CAP Round - I for Admission to First Year of Four Year Full Time Degree Courses in Engineering/Technology for the Academic Year 2013-2014'
foot_begin = 'Legends: Starting character G-General'
foot_end = 'JEE Main 2013(Paper-I))'
cap_junk_remover('c1.txt', head, foot_begin, foot_end, 'c1.new')


