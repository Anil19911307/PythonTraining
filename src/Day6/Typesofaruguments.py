# def func(i,j):
#     print(i,j)
# func(1, 2) # position argumnets
# func(j=2,i=1) # keyword argumnets


#defaut values assigned to postional arugumnets:
# def func(i,j=10):
#      print(i,j)
#
# func(100,200)
# func(100)


#Example3:key word arugumnets
#
# def greetings(name,greetmsg):
#     print(greetmsg+ "   "+name)
# greetings(name="John",greetmsg="Hello") #Keyword arguments
# greetings(greetmsg="Hello",name="John") #keyword arugments


#Example 4;
#
# def fun(a,b,c):
#     print(a,b,c)
# fun(1,2,3)
# fun(a=1,b=2,c=3)
# fun(b=2,a=1,c=3)
# fun(1,2,c=3)
# fun(1,b=2,c=3)
# # fun(1, b=2,3) # this is wrong because postional arugument must appear before key word arugument

#Example 5: how function can return mulitple values

# def func(a,b):
#     if a > b:
#         return (a,b)
#     else:
#         return (b,a)
# res=func(20,10)
# print(res)
# print(type(res))