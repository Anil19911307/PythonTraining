# Example1
# mytuple=("apple", "banana", "cherry")
# print(mytuple)
# mytuple=()
# print(mytuple)

# #Example 2:To access tuples
# mytuple=("apple", "banana", "cherry")
# print(mytuple[1])
# print(mytuple[-1])

# example3:range of indexes
# mytuple=("apple", "banana", "cherry","Kiwi","Melon","orange","mango")
# print(mytuple[2:5])
# print(mytuple[-4:-1])

# Example4:chnging tuple items

# mytuple=("apple", "banana", "cherry")
# mylist=list(mytuple)
# mylist[0]="orange"
# print(mylist)
# mytuple=tuple(mylist)
# print(mytuple)

# Example 5;reading tumple items using loop

# mytuple=("apple", "banana", "cherry")
#
# for i in mytuple:
#     print(i)

# Example6:searching of item in tuple

# mytuple=("apple", "banana", "cherry")
# if "apple" in mytuple:
#     print("yes,apple is present")
# else:
#     print("no,apple is not present")

# Example 7:counting items in tuple

# mytuple=("apple", "banana", "cherry")
# print(len(mytuple))

# Example 8:Add items to tumple is possible-becuase its imuutable

# Example9;copy tuple

# mytuple1=("apple", "banana", "cherry")
# mytuple2=mytuple1
# print(mytuple2)

# Example10;removing item from tuple is not possible because its immutbale
mytuple1 = ("apple", "banana", "cherry")
# mytuple1.remove(("banana", "cherry")) #not possible invalid
# del mytuple1
# print(mytuple1)

# Example 11:join tuples

# mytuple1=("apple", "banana", "cherry")
# mytuple2=("kiwi", "melon", "orange")
# mytuple3=mytuple1+mytuple2
# print(mytuple3)

# Example12:tumple compariison
mytuple1 = ("kiwi", "melon", "orange")
mytuple2 = ("kiwi", "melon", "orange")
if mytuple1 == mytuple2:
    print("tuples are equal")
else:
    print("tuples are not equal")
