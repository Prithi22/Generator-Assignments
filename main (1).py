'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def MyRange(start, stop=None,stepSize = 1):
    if stop is None:
        stop = start
        start = 0
    
    i = start
    
    if(stepSize > 0):
        while(i < stop):
            yield i
            i = i + stepSize
    elif(stepSize < 0):
        while(i > stop):
            yield i
            i = i + stepSize

GetInput = input("Get the input for range function:")

args = (int(i) for i in GetInput.split(","))
  
for i in MyRange(*args):
    print(i)
    
    