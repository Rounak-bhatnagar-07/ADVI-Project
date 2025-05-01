#variable length args

def display(*args):
    print(len(args))
display(10)
display(10,20)
display(10,20,30,33,44)


def display(*args):
    for i in range (len(args)):
        print(args[i])
    print("____________")
display(10)
display(10,20)
display(10,20,30,33,44)

def display(*args):
    for i in args:
        print(i)
    print("____________")
display(10)
display(10,20)
display(10,20,30,33,44)