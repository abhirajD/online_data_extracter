import os
import re
import simplejson
import mechanize
import unicodedata
import sys
import itertools
import csv

reload(sys)
print "DEFAULT ENCODING : ",sys.getdefaultencoding().upper()


region = "mumbai"
img_tagname = 'mum' 
os.chdir("./"+region)


def table_extract(file_name , cp1, cp_tag):
	f=open(file_name,"r+")
	html=f.read()
	f.close()

	# html=unicodedata.normalize('NFD', unicode(html)).encode('ascii','ignore')

	html=html.split(cp1)
	html=html[1]
	html=html.split(cp_tag)
	html=html[1]
	html=html.split("</"+cp_tag[1:])
	html=html[0]
	return html

file_name = "..   Directorate of Technical Education, Maharashtra State, Mumbai   ...html"
cp1 =       "Click on the Institute Code to view the Institute information."
cp_tag =    "<tbody>"

data_html=table_extract(file_name , cp1, cp_tag)

def write_temp(data_html,formt):
	f=open(str(region), "w+") 
	f.seek(0)
	f.write(str(data_html))
	# # simplejson.dump(data_html, f)
	# f.seek(-1,2)
	# #print "::::::::",f.read(1)
	# f.write(" ")
	# f.seek(0)
	# f.write(" ")
	f.close()

#write_temp(data_html)

data_html=data_html.split("<tr>")

for i in range(0,len(data_html)):
	data_html[i]=re.sub("</tr>","",data_html[i])
	data_html[i]=re.sub("\n","",data_html[i])
	data_html[i]=re.sub("\r","",data_html[i])
	data_html[i]=re.sub("&amp","&",data_html[i])
	data_html[i]=re.sub(";","",data_html[i])
	data_html[i]=re.sub("'","",data_html[i])
	data_html[i]=re.sub("","",data_html[i])

#print "List created.\n<tr> removed\nTHINGS_LEFT:\ncapture required data\nFollow links\nGet college data"


for i in range(2,len(data_html)):
	pattern = '<td.*?>(.*?)</td>'
	data_html[i] = re.findall(pattern , data_html[i])
	pattern_link = '<a href="(.*?)">'
	temp=str(re.findall(pattern_link , data_html[i][1])); temp = temp[2:-2]
	data_html[i].append(temp)
	pattern_code = '<a href=.*?>(.*?)</a>'
	temp1 =str(re.findall(pattern_code , data_html[i][1])); temp1 = temp1[2:-2]
	data_html[i][1] = temp1


final_list = []

for i in range(2,len(data_html)):
	k = i-2;
	id_str='A'+str(k).zfill(3)
	
	temp={
	'sr_no':data_html[i][0],
	'ins_code':data_html[i][1],
	'aicte_no':data_html[i][2],
	'name':data_html[i][3],
	'intake':data_html[i][4],
	'link':data_html[i][5],
	'id':id_str
	}
	final_list.append(temp)


#write_temp(final_list,"json")


def get_course(link):
	print "get_course:Connecting to link"
	br = mechanize.Browser()
	response = br.open(link)
	data_html = response.read()
	print "get_course:Connected. Data fetch Successful"
	#data_html = re.sub("</tr>","",data_html)
	data_html = re.sub("\n","",data_html)
	data_html = re.sub("\r","",data_html)
	data_html = re.sub("\t","",data_html)
	data_html = re.sub("&amp","&",data_html)
	data_html = re.sub(";","",data_html)	

	data_html = data_html.split("AICTE Approved Bachelor of Engineering"); data_html = data_html[1]
	data_html = data_html.split("</div>"); data_html = data_html[0]

	pattern = '<table.*?>(.*?)</table>'
	data_html = str(re.findall(pattern , data_html)); data_html = data_html[2:-2]	
	
	#List Populate
	pattern_list = '<tr>(.*?)</tr>'
	course_list = re.findall(pattern_list , data_html)
	
	pattern_row_header = '<th.*?>(.*?)</th>'
	course_list[0] = re.findall(pattern_row_header , course_list[0])

	for i in range(1,len(course_list)):
		pattern_row = '<td.*?>(.*?)</td>'
		course_list[i] = re.findall(pattern_row , course_list[i])


	course_final = []
	for i in range(1,len(course_list)-1):
		temp ={
			'course_name' : course_list[i][1],
			'type' : course_list[i][2],
			'intake' : course_list[i][6]
		}
		course_final.append(temp)

	#write_temp(course_final,"txt")
	return course_final


def get_college_data(link):
	print "get_college_data:Connecting to link"
	br = mechanize.Browser()
	response = br.open(link)
	data_html = response.read()
	print "get_college_data:Connected. Data fetch Successful"
	#data_html = re.sub("</tr>","",data_html)
	data_html = re.sub("\n","",data_html)
	data_html = re.sub("\r","",data_html)
	data_html = re.sub("\t","",data_html)
	data_html = re.sub("&amp","&",data_html)
	data_html = re.sub(";","",data_html)

	data_html = data_html.split("Institute Summary"); data_html = data_html[1]

	pattern = '<table.*?>(.*?)</table>'
	data_html = re.findall(pattern , data_html); data_html = data_html[0]; 

	pattern_list = '<tr>(.*?)</tr>'
	data_html = re.findall(pattern_list , data_html)

	for i in range(0,len(data_html)):
		pattern_row = '<td.*?>(.*?)</td>'
		data_html[i] = re.findall(pattern_row , data_html[i])

		for j in range(0,len(data_html[i])):
			pattern_span = '<span.*?>(.*?)</span>'

			if len(re.findall(pattern_span , data_html[i][j])) is not 0:
				data_html[i][j] = re.findall(pattern_span , data_html[i][j])


	address =str(data_html[7][1]); address = address[2:-2]

	s1 = str(data_html[28][1]); s1 = s1[2:-2]
	s2 = str(data_html[28][3]); s2 = s2[2:-2]
	s3 = str(data_html[29][1]); s3 = s3[2:-2]
	status = str(s1+" - "+s2+" - "+s3)
	
	email = str(data_html[11][1]); email = email[2:-2]
	contact_name = str(data_html[20][1]); contact_name = contact_name[2:-2]
	contact = str(data_html[21][1]); contact = contact[2:-2]
	website = str(data_html[10][3]); website = website[2:-2]


	college_data = []
	
	f_temp = {
		'address' : address,
		'status' : status,
		'email' :email,
		'contact' : contact,
		'contact_name' : contact_name,
		'website' : website
	}

	college_data.append(f_temp)
	return f_temp

def location_extractor():
	file_name = region+'_map.txt'
	f = open(file_name , 'r+')
	data = f.read().strip()
	f.close()

	map_data = re.sub('\r', '' ,data)
	map_data = map_data.split('\n')
	# print '\n'.join(map_data)
	map_dict = {}

	limit = len(map_data) if (len(map_data) % 2 is 1) else int(len(map_data)-1)

	print ":::Length_map_data = ",limit

	for i in range(0, len(map_data)):
		map_data[i] = map_data[i].split('\t')
		# print map_data
		map_data[i] = {map_data[i][0] : map_data[i][1]}
		map_dict = dict(map_dict.items() + map_data[i].items())
	# print '\n'.join(map_dict)
	return map_dict

def process_course_string(courses,flag):
	#  Set flag as 0 for json formatting
	#  Set flag as 1 for map formatting
	flag = int(flag)
	# print flag
	sorted_course = {}
	sorted_intake = {}

	for key, group in itertools.groupby(courses, lambda item: item['type']):
		sorted_course[key]=[item["course_name"] for item in group] 

	for key, group in itertools.groupby(courses, lambda item: item['type']):
		sorted_intake[key]=[item["intake"] for item in group] 

	# sorted_final = sorted_course.copy()
	# sorted_final.update(sorted_intake)

	# sorted_final = dict( [ (n, sorted_course.get(n, 0)+sorted_intake.get(n, 0)) for n in set(sorted_course)|set(sorted_intake) ] )

	sorted_final = dict(sorted_course)
	for elem in sorted_course:
	    sorted_final[elem] = [sorted_course.get(elem) , sorted_intake[elem]]

	course_final_string = ""
	for elem in sorted_final:
		course_final_string = course_final_string + elem.upper()+" -\\n"
		
		bullet = '-'

		print bullet
		for i in range(0,len(sorted_final[elem][1])):
			if flag is 0:
				course_final_string = course_final_string + bullet + str(sorted_final[elem][0][i])+". Intake- "+str(sorted_final[elem][1][i])+"\\n"
			if flag is 1:
				course_final_string = course_final_string + bullet + str(sorted_final[elem][0][i])+" - "+str(sorted_final[elem][1][i])+"\\n"

	course_final_string = course_final_string[:-2]
	return course_final_string

def json_writer():
	j = len(final_list)
	#j = 2
	data_json = ""
	map_data = location_extractor()

	for i in range(0,j-1):
		print "Site:"+str(i)

		courses = get_course(final_list[i]['link'])
		college_data = get_college_data(final_list[i]['link'])
		
		
		# print final_list[i]
		# print courses
		course_string = process_course_string(courses,0)
		
		# print '\n',map_data[str(final_list[i]['ins_code'])]

		# print college_data['contact_name']
		final_json= '{"'+str(final_list[i]['id'])+'" : [{"data" : "NA-Course", "desc1" : "'+str(final_list[i]['name'])+' Code-'+str(final_list[i]['ins_code'])+'", "desc0" : "'+str(course_string)+'", "id" : "'+str(final_list[i]['id'])+'B00", "name" : "Courses", "type" : "0"}, {"data" : "NA-Address", "desc0" : "'+str(college_data['address'])+'\\n'+str(college_data['contact_name'])+'\\n'+str(college_data['contact'])+'\\n'+str(college_data['email'])+'\\nwebsite: '+str(college_data['website'])+'", "desc1" : "NA", "id" : "'+str(final_list[i]['id'])+'B01", "name" : "Address", "type" : "0"}, {"data" : "NA-Status", "desc0" : "'+str(college_data['status'])+'", "desc1" : "NA", "id" : "'+str(final_list[i]['id'])+'B02", "name" : "Status", "type" : "0"}, {"data" : "'+map_data[str(final_list[i]['ins_code'])]+'", "desc0" : "'+str(final_list[i]['name'])+'", "desc1" : "Code-'+str(final_list[i]['ins_code'])+'", "id" : "'+str(final_list[i]['id'])+'B03", "name" : "Map", "type" : "2"} ], "id" : "'+str(final_list[i]['id'])+'", "img" : "'+img_tagname+'", "name" : "'+str(final_list[i]['name'])+' Code-'+str(final_list[i]['ins_code'])+'"},'
		# print "\n",course_string

		data_json = data_json + final_json

	data_json = data_json[:-1]
	data_json = data_json +']}'
	data_json = '{"A":[' +data_json

	write_temp(str(data_json),'json')



def db_writer():
	csv_in = open('../database_format','r+')
	csv_out = open(img_tagname, 'w+')

	csv_data = csv.reader(csv_in, delimiter = '|' , quotechar="\"")
	csv_writer = csv.writer(csv_out, delimiter = '|' , quotechar="\"", quoting=csv.QUOTE_ALL)
	
	header = csv_data.next()
	# print header

	csv_writer.writerow(header)

	j = len(final_list)
	#j = 2
	map_data = location_extractor()
	for i in range(0, j-1):
		print "Site:"+str(i)
		

		courses = get_course(final_list[i]['link'])
		college_data = get_college_data(final_list[i]['link'])
		
		course_string = process_course_string(courses,1)
		
		row_data = []
		row_data.append(str(i))
		row_data.append(str(img_tagname.upper()))
		row_data.append(str(final_list[i]['ins_code']))
		row_data.append(str(final_list[i]['name'])+' Code-'+str(final_list[i]['ins_code']))
		row_data.append((str(college_data['address'])+'\\n'+str(college_data['contact_name'])+'\\n'+str(college_data['contact'])+'\\n'+str(college_data['email'])+'\\nwebsite: '+str(college_data['website'])))
		row_data.append((re.sub("\n\n", "\\n", re.sub('\n', '\\n', course_string))))
		
		row_data.append(str(re.sub(" ", "", map_data[str(final_list[i]['ins_code'])]).split(',')[0]))
		# print "usefullllll\n"
		# print final_list[i]['ins_code']
		# print map_data[str(final_list[i]['ins_code'])]
		
		row_data.append(str(re.sub(" ", "", map_data[str(final_list[i]['ins_code'])]).split(',')[1]))

		csv_writer.writerow(row_data)


def email_extractor():

	f = open(region+'_email.txt',"w+")
	j = len(final_list)
	
	for i in range(0,j-1):
		print "Site:"+str(i)

		college_data = get_college_data(final_list[i]['link'])	
		
		out_str = college_data['email'] + '\n' 

		f.write(out_str)

	f.close()

# json_writer()
# db_writer()
email_extractor()
