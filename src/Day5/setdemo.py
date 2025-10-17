#Example1:How to cretae a set:
#
# myset={"apple","banana","cherry"}
# print(myset)

#Example 2: Accesing items from set:
# myset={"apple","banana","cherry"}
# for i in myset:
#     print(i)

#Example3:value exist in set or not:
# myset={"apple","banana","cherry"}
# print("banana" in myset)
# print("banana" not in myset)

#Example4;Adding items to set
# add()-single item, and update()-multiple items

# myset={"apple","banana","cherry"}
# myset.add("melon") #add
# myset.update({"kiwi","orange","melon"})  #update
# print(myset)


#Example5;How to find the number of items in set

# myset={"apple","banana","cherry"}
# print(len(myset)) #3

#Exmaple6:Remove items from set:remove(),discard()
# myset={"apple","banana","cherry"}
# myset.remove("banana")
# print(myset)
# myset.remove("Xyz") #key error
# myset.discard("banana")
# print(myset)
# myset.discard("XYZ") #No error
# print(myset)

#Example 7:clear all items from the set

# myset={"apple","banana","cherry"}
# myset.clear() #clear the values
# print(myset)
#
#
# del myset #complete set variable with data
# print(myset)

#Example 8: join 2 sets:union

# myset1={"apple","banana","cherry"}
# myset2={"melon","orange","kiwi"}
# myset3=myset1.union(myset2)
# print(myset3)
#
# myset1.update(myset2)
# print(myset1)

