width = 40
print(f"{'x' : <{width}}")
print(f"{'x' : ^{width}}")
print(f"{'x' : >{width}}")
print(f"|{'x' : <20}|{'y' : <20}|")
mydict = {'brand': 'subaru', 'model': 'impreza', 'color': 'green', 'year': '2017'} 
 
for k, v in mydict.items():
    print(f"Key is: {k} and value is: {v}.")