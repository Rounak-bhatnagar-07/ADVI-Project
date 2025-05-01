#passing keyyword as argument   

def display(id,name,marks):
    print("ID:",id)
    print("Name:",name)
    print("Marks:",marks)
display(101,"saas",456) #positional argument

display(name="soni",marks=67,id=107) #keyword argument



#func calls
def hai():
    hello()
    print("hi..")
def hello():
    bye()
    print("hello..")
def bye():
    print("bye bye")
hai()