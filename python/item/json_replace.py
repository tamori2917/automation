def Json_replace(file):
##import pyload json  as dictionary
	f = open(file, 'r')
##change as string
	Allf = f.read()
##delete new line for linux and mac and windows
	text = Allf.replace('\n','')
	jsonData = text.replace('\r','')
	return jsonData	
