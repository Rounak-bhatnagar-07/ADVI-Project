class student:                                                  #single inheritance 
    def setID(self,id):
        self.id = id
    def setName(self,name):
        self.name = name
    def setAddress(self,addr):
        self.addr = addr
    def setMarks(self,marks):
        self.marks = marks
    def getID(self):
        return self.id
    def getName(self):
        return self.name
    def getAddress(self):
        return self.addr
    def getMarks(self):
        return self.marks  
        
s1=student()
s1.setID(101)
s1.setName("John")
s1.setAddress("hyderabad")
s1.setMarks(90)

print("id:",s1.getID())
print("name:",s1.getName())
print("address:",s1.getAddress())
print("marks:",s1.getMarks())

class teacher(student):
    def setsalary(self,salary):
        self.salary = salary                    #multiple inheritance 
    def getsalary(self):
        return self.salary
t1=teacher()
t1.setID(465)
t1.setName("raj")
t1.setAddress("banglore")
t1.setsalary(50000)
print("id:",t1.getID())
print("name:",t1.getName())
print("address:",t1.getAddress())
print("salary:",t1.getsalary())

#multilevel inheritance 
class A:
      def seta(self,a):
          self.a=a
      def geta(self):
          return self.a
class B(A):
      def setb(self,b):
          self.b=b
      def getb(self):
          return self.b
class C(B):
      def setc(self,c):
          self.c=c
      def getc(self):
          return self.c
      def getc(self):
            return self.c
c1=C()
c1.seta(7)
c1.setb(20)
c1.setc(c1.geta()*c1.getb())
print("a:",c1.geta())
print("b:",c1.getb())
print("c:",c1.getc())
#multilevel inheritance 
class A:
    def display(self):
        print("hi....from A")

class B:
    def display(self):
        print("hi....from B")

class C(A,B):
    def display(self):
        super().display()
        print("hi....from C")
ob=C()
ob.display()


#multiple inheritance

class A:
    def SetA(self,x):
        self.__a=x
    def getA(self):
        return self.__a
class B:
     def SetB(self,x):
        self.__b=x
     def getB(self):
        return self.__b
    
class C(A,B):
    def mult(self):
        self.c=self.getA()*self.getB()
    def display(self):
        print("a:",self.getA())
        print("b:",self.getB())
        print("c:",self.c)
ob=C()
ob.SetA(11)
ob.SetB(22)
ob.mult()
ob.display()

