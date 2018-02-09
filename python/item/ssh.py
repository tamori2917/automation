
from netmiko import ConnectHandler

myPc = { 'device_type': 'linux',
         'ip': '127.0.0.1',
         'username': 'khaianna',
         'password': 'kanna1231'
         }

test = ConnectHandler(**myPc)

print(test.send_command("ps aux | egrep 'ssh' "))


