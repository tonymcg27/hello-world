import sys
# import os
print(sys.executable)
print(sys.version)


def myfunc():
    print("This is my function")


def newfunc():
    print("This is my new function")


print('\n'.join(sys.path))


myfunc()

for x in [1, 2, 3, 4]:
    print(x)


newfunc()

for y in range(1,10):
    print "The value of Y = {}".format(y)