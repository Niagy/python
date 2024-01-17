import os
x = os.system('cp lab8a.py lab8a.py.backup') 
print(x)
if x: 
    print('Command failed.') 
else: 
    print('Command succeeded.') 

f = os.popen('whoami')  # f is an object, not a readable datatype. 
output = f.read()  # will contain the output from the command. 
print("Hello " + output + "!")  # Hello eric!  
 
print(os.getcwd())