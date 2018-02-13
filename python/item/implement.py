from classlist_get import Classlist_get
from a10 import A10

a10 = A10(username='admin',password='a10',ipaddr='192.168.201.15')
classlist_get = Classlist_get(username='admin',password='a10',ipaddr='192.168.201.15')
a10.login()
#sign = (a10.signature)
#print (a10)
print (a10.signature)
#a10 = A10(username='admin',password='a10',ipaddr='192.168.201.15')
Classlist_get()

