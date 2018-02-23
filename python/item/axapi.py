from a102 import A10
import json

a10 = A10(hostname='a10', username='admin',password='a10',ipaddr='192.168.201.31' ,device_type='a10')
a10.login()
a10.login_ssh()


### initialize and delete test
response = a10.calist("class","del")
code = response.status_code
if str(code) == "200":
	print ("class-list has been deleted")
else:
	print ("class-list hasn't been deleted")

###### judge whether create new class-list accurately
response = a10.calist("class","new")
code = response.status_code
if str(code) == "200":
	print ("class-list has been created")
else:
	print ("class-list hasn't been created")

###### judge whether get class-list accurately
response = a10.calist("class","get")
code = response.status_code

output = a10.ssh.send_command("show run class-list");
print (output)
if str(code) == "200":
	if "postmation" in output:
		print("ok")
	else:
		print("ng")
else:
	print ("http error has occured")
newlist = json.loads(response.text)
"""
###### judge whether replace existing class-list accurately
### only change contents
response = a10.calist("class","edit")
new2list = json.loads(response.text)
code = response.status_code
if str(code) == "200":
	if newlist == new2list:
		print("FAILD post method has not overwrited")
	elif "new2" in str(new2list):
		print("post method has overwrited")
	else:
		print("unexpected process has occured")
else:
	print("http error has occured")

###### judge whether replace exsting class-list accurately
### change both list and contents
response = a10.calist("class","put")
new3list = json.loads(response.text)
code = response.status_code
print (code)
if str(code) == "200":
	if "putmation" in str(new3list):
		pass
		if "new2" in str(new3list):
			print("there is possible to be inserted")
		else:
			print("put method has overwrited")
	elif "new2" in new2list:
		print("put method has not overwrited")
	else:
		print("unexpected process has occured")
else:
	print("http error has occured")

"""
