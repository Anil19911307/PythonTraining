

#Example 1
#
# class A:
#     def m1(self):
#         print("this is m1 method from class A")
#
#
# class B(A):
#     def m2(self):
#         print("this is m2 method from class B")
#
#
# obj = B()
# obj.m1()
# obj.m2()


#Example 2:single inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b,=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# obj=B()
# obj.m1()
# obj.m2()

#Example 3: multilevel inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b,=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(B):
#     i,j=10,20
#     def m3(self):
#         print(self.i*self.j)
#
# obj=C()
# obj.m1()
# obj.m2()
# obj.m3()

#Exmaple 3:Hierachy inheritance


# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b,=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A):
#     i,j=10,20
#     def m3(self):
#         print(self.i*self.j)
#
# obj1=C()
# obj1.m1()
# obj1.m3()
#
#
# obj2=B()
# obj2.m2()
# obj2.m1()

#Example 5:Multiple inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B:
#     a,b,=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A,B):
#     i,j=10,20
#     def m3(self):
#         print(self.i*self.j)
#
# obj=C()
# obj.m1()
# obj.m2()
# obj.m3()

#Example 6:calling parent class method using child class super()

# class A:
#     def m1(self):
#         print('this is m1 method from class A')
# class B(A):
#     def m1(self):
#         print('this is m2 method from class B')
#         super().m1()
#
# obj = B()
# obj.m1()

#Example 7:

# class A:
#     a,b=10,20
# class B(A):
#     i,j=20,30
#     def m1(self,x,y):
#         print(x+y)
#         print(self.i+self.j)
#         print(self.a+self.b)
#
# obj=B()
# obj.m1(10,20)


#Example 8:overriding variables

# class parent:
#     name=("scott")
# class child(parent):
#     name=("john")
#     def func(self):
#         print(super().name)
#
# obj=child()
# print(obj.name)
# obj.func()

# #example 9;method over riding
# class Bank:
#     def rateofinterst(self):
#         return 0
# class XBank(Bank):
#     def rateofinterst(self):
#         return 10
# class YBank(Bank):
#     def rateofinterst(self):
#         return 20
# obj = XBank()
# print(obj.rateofinterst())
# obj=YBank()
# print(obj.rateofinterst())

#Method over loading,polyporphism
# class Human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print("Hello" +name)
#         else:
#             print("Hello ")
# obj = Human()
# obj.sayhello("scott")
# obj.sayhello()

#example 11;Overloading,polyporphism

# class calculator:
#     def add(self,a=0,b=0,c=0):
#         print(a+b+c)
#
# obj = calculator()
# obj.add(1,2)
# obj.add(3,4,10)
# obj.add()
# obj.add(1)
