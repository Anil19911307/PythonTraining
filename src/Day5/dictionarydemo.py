#Example 1:how to create dictionary
# mydic={101:"X",102:"Y",103:"Z"}
# print(mydic)


#Example 2:access items from dictionary

# mydic={"brand":"hyundai","Model":"i10","Year":2021}
# print(mydic["brand"])
# print(mydic["Model"])
# print(mydic["Year"])

#using get function
# print(mydic.get("Model"))

#example 3: chnage values in dictionary

# mydic={"brand":"hyundai","Model":"i10","Year":2021}
# print(mydic)
# mydic["Year"]=2022
# print(mydic)

#Example 4;Reading items from dictionary using loop

# mydic={"brand":"hyundai","Model":"i10","Year":2021}
# for key,value in mydic.items():
#     print(key,value)

#Example 5:check key exist in dictionary or not

mydic={"brand":"hyundai","Model":"i10","Year":2021}
# if "brand" in mydic:
#     print(mydic["brand"])
# else:
#     print("not exist")

# print("Model" in mydic) # key exist or not

#Example 6: find number of items in dictonary

# mydic={"brand":"hyundai","Model":"i10","Year":2021}
# print(len(mydic)) #3 print the number of items in dictionary

#Example 7: add items to dictionary

# mydic={"brand":"hyundai","Model":"i10","Year":2021}
# mydic['color']="Blue"
# print(mydic)

#Example 8: remove item from dictionary

# mydic={"brand":"hyundai","Model":"i10","Year":2021}
# mydic.pop("Model")
# print(mydic)

# mydic={"brand":"hyundai","Model":"i10","Year":2021}
# del mydic["Model"]
# print(mydic)

# del mydic # delete complete dictionary
# print(mydic)

# mydic={"brand":"hyundai","Model":"i10","Year":2021}
# mydic.clear() # clear dictionary
# print(mydic)

#Example 9; copy dictionary from one dict to another

# mydic1={"brand":"hyundai","Model":"i10","Year":2021}
# mydic2=mydic1 # wihout using copy function
# print(mydic2)

mydic1={"brand":"hyundai","Model":"i10","Year":2021}
mydic2=mydic1.copy() # using copy funcion
print(mydic2)











