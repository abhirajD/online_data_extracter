import mechanize
import cookielib

def write_file(file_name,data):
	f=open(file_name,"w+")
	f.write(data)
	print "Data written to file: " + file_name
	f.close()

	
def page_to_file(page_url):
	br = mechanize.Browser()
	print "Connecting to: "+page_url+"\n"
	page1 = br.open(page_url)
	print "Reading Source code.."
	page1_source = page1.read()
	print "Sending source code to file.."
	write_file("root.txt",page1_source)

browser = mechanize.Browser()
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
cj = cookielib.LWPCookieJar()
browser.set_cookiejar(cj)

page_url = "http://www.dtemaharashtra.gov.in/approvedinstitues/StaticPages/frmSearchInstitute.aspx?did=64"

browser.open(page_url)

browser.follow_link(text="Click Here for Advance Search")


refe = browser.geturl()

req = urllib2.Request(url=page_url)
req.add_header('Referer', refe)

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
f = opener.open(req)

htm = f.read()

print "\n\n\n\n", htm	

print "FOLLOW_LINK: Click Here for Advance Search"
