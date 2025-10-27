
#Create a generator to mimic range() in builtin. The name of the generator could be myRange - 
#I would like an exact mimic of functionality alone. Caution: when the step is negative.

# Range Based For loop Generator

def MyRange(start,stop,step):
    for i in range(start,stop,step):
        print("Start For Loop")
        yield i;
        print("Continuing For Loop")
        

print("Input the values for Range based for Loop")
start = int(input("Enter the start value:"))
stop = int(input("Enter the stop value:"))
step = int(input("Enter the step Size:"))

GeneratorObj = MyRange(start,stop,step)

print(next(GeneratorObj))

while(1):
    try:
        print(next(GeneratorObj))
    except StopIteration:
        print("For Loop End")
        break

