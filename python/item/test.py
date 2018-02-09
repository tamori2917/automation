from a10 import A10

a10 = A10(username='admin',password='a10',ipaddr='192.168.201.15')
a10.login()


print (a10)

print(a10.signature)

a10.logoff()

