'''
Name: John Niagwan
ID: 121092225
'''
import os
x = os.system('ping google.com -c 4')
uname = os.popen('whoami')
name = uname.read()
if x == 0:
    utime = os.popen('uptime')
    uptime = utime.read()
    print(f"Welcome, {name}", end='')
    print("The internet is UP")
    print(f"uptime is:\n{uptime}")
else:
    print(f"Welcome, {name}", end='')
    print("The internet is DOWN")