a = 10
b = 10
#display memory id of a and b
print("Memory id of a:", id(a))
print("Memory id of b:", id(b))
#check if a and b refer to the same object
if a is b:
    print("a and b refer to the same object")
else:
    print("a and b refer to different objects")