x = 25
if (type(x) is int):
    print("true")
else:
    print("false")
    
x = 5.7
if(type(x) is not float):
    print("true")
else:
    print("false")
    
x = 20
y = 20
if (x is y):
    print("X & Y SAME identity")
y =30
if ( x is not y):
    print("X & Y different identity")