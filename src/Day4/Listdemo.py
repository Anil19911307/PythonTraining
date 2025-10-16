# How to create list:Example 1

# mylist1=[10,20,30,40,50]
# mylist2=["Apple","Banana","cherry"]
# mylist3=[10,"apple",30,"banana"]
# mylist4=list()

# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist4)

# How to access items from the list:Example 2:
# mylist=["Apple","Banana","cherry"]
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[-2])
# print(mylist[-3])

# Range of indexes:Example 3
# mylist=["Apple","Banana","Cherry","orange","Kiwi","melon","mango"]
# print(mylist[2:5])
# print(mylist[-4:-1])

# Change item value:Example 4:
# mylist=["Apple","Banana","cherry"]
# print(mylist)
# mylist[0]="orange" # this will chnage values based on index
# print(mylist)

# Example5:read the itmes using loop statement
# mylist=["Apple","Banana","Cherry"]
# for i in mylist:
#     print(i)


# example6: check if the item exist in the list
# mylist = ['Apple', 'Banana', 'Cherry']

# if 'Apple' in mylist:
#     print("'Yes',Apple is present")
# else:
#     print('No')

#Example 7;List length; counting the number of items in list
# mylist=['Apple', 'Banana', 'Cherry']
# print(len(mylist))

# Example 8:Add new item to the list
# mylist=['Apple', 'Banana', 'Cherry']
# # mylist.append('orange') #New item will be added at the end of list
# mylist.insert(1,'orange')
# print(mylist)

#Example 9:Remove item from the list:pop()
# mylist=['Apple', 'Banana', 'Cherry']
# mylist.pop(2)
# print(mylist)

# mylist=['Apple', 'Banana', 'Cherry']
# del mylist[2]
# print(mylist)

# mylist=['Apple', 'Banana', 'Cherry']
# mylist.clear()
# print(mylist)

# Example10:copy list:list()

# mylist1=['Apple', 'Banana', 'Cherry']
# mylist2=list(mylist1)
# print(mylist1)
# print(mylist2)

#copy
# mylist1=['Apple', 'Banana', 'Cherry']
# mylist2=mylist1.copy()
# print(mylist1)
# print(mylist2)

#example11:join 2 lists

# mylist1=['Apple', 'Banana', 'Cherry']
# mylist2=['orange', 'kiwi', 'mango']
# mylist3=mylist1+mylist2
# print(mylist3)

#using looping statement

# mylist1=['Apple', 'Banana', 'Cherry']
# mylist2=['orange', 'kiwi', 'mango']
#
# for i in mylist2:
#     mylist1.append(i)
# print(mylist1)

#Extend funciton

# mylist1=['Apple', 'Banana', 'Cherry']
# mylist2=['orange', 'kiwi', 'mango']
# mylist1.extend(mylist2)
# print(mylist1)
# print(mylist2)

#Example 12:List comparision

mylist1=[1,2,3]
mylist2=[1,2,3]
if mylist1 == mylist2:
    print("mylist1 is equal to mylist2")
else:
    print("mylist1 is not equal to mylist2")











