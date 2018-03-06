import json
from pprint import pprint
import os
def install(a):
	try:
		status=os.system(a)
		if(status==1):
			print(a)+"\t\t\thas failed"

	except:
		print "handled"
	else:
		print (a)+"\t\tinstallation completed"

data = json.load(open('dict.json'))
data=data["dependencies"]
pprint(data)
for key, value in data.iteritems():
	a="pip install %s==%s" %(key,value)
	install(a)