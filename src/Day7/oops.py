#Example 1
#
# class MyClass:
#     def myfun(self):
#         pass
#     def display(self,name):
#         print(name)
# myobj = MyClass()
# myobj.myfun()
# myobj.display("scott")

# #Example 2:
# class MyClass:
#     def m1(self):
#         print("This is insatnce menthod")
#
#     @staticmethod
#     def m2(self,num):
#         print(self,num)
# myobj = MyClass()
# myobj.m1()
#  myobj.m2(100,200)
#
# MyClass.m2(100,200) #calling through class ot object

# #Example 3
# class MyClass:
#     a,b=100,200
#     def add(self):
#         print(self.a+self.b)
#     def sub(self):
#         print(self.a-self.b)
# mc=MyClass()
# mc.add()
# mc.sub()

# #Example 4:
# i,j=100,200
# class MyClass:
#     a,b=300,600
#     def add(self,x,y):
#         print(x+y) # local variable
#         print(self.a+self.b) # class variable
#         print(i+j) # Global variable
#
# mc=MyClass()
# mc.add(150,250)

# #Example 5:
# a,b=100,200
# class MyClass:
#     a,b=300,600
#     def add(self,a,b):
#         print(a+b) # local variable
#         print(self.a+self.b) # class variable
#         print(globals()['a']+globals()['b'])
#
# mc=MyClass()
# mc.add(150,250)

#Exmaple 6:from one class we can create multiple objects
#
# class MyClass:
#     def display(self,name):
#         print("This is display method")
#         print(name)
#
# obj1 = MyClass()
# obj1.display("John")
# obj2 = MyClass()
# obj2.display("scott")

#Example 7:Constrcutors:

# class MyClass:
#     def __init__(self):
#         print("MyClass constructor")
#     def func1(self):
#         print("Hello World")
#     def func2(self,a,b):
#         return(a+b)
# myobj = MyClass() #at the time of object creation,constructor will be called
# myobj.func1()
# res=myobj.func2(10,20)
# print(res)

#
# class Myclass():
#     name="David"
#     def __init__(self,name):
#         print(name)
#         print(self.name)
# obj=Myclass("Scott")  #passing parameter to constructor

#
# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#     def display(self):
#         print(self.name, self.age, self.salary)
# mc1=Employee('Michael', 25, 10000)
# mc1.display()
#
# mc2=Employee('scott', 25, 20000)
# mc2.display()


# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#     def __str__(self):
#         return(self.name)
#
# mc1=Employee("Michael", 25, 10000)
# print(mc1)
















