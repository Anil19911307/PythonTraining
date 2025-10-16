# s="welcome"
# s='welcome'
# s=str('welcome')
# s=str("welcome")
#
# #creating empty string
# name=str()
# name=''
# name=""

# srings are immutable

# str1="welcome"
# print(id(str1))
# str1=str1+" to python"
# print(str1)
# print(id(str1))

# + and * in string

# str1="welcome"
# str1=str1+(" to python")
# print(str1)
# print(str1*3)

# slicing

# str=("welcome")
# print(str[1:3])
# print(str[:6])
# print(str[2:])
# print(str[1:-1])
# print(str[1:-2])
# print(str[1:-3])

# ord() and chr() function

# print(ord('A'))
# print(chr(65))

# max(),min(),len() functions in strings
# print(max("Anil"))
# print(min("Anil"))
# print(len("Anil"))
# print(max("zebra"))
# print(min("zebra"))

# in and not in

# s1="welcome"
# print("come" in s1)
# print("hello" in s1)
# print("come" not in s1)
# print("lome" not in s1)


# string comparision
# print("tim" == "tie")  # False
# print("free" != "freedom")  # True
# print("arrow" > "aron")  # True
# print("right" >= "left")  # True
# print("teeth" < "tee")  # False
# print("yellow" <= "fellow")  # False
# print("abc" > "")  # True

# s="welcome to python"
# print(s.isalnum())
# print("welcome".isalpha())
# print('2012'.isdigit())
# print("first number".isidentifier())
# print(s.islower())
# print(s.isupper())
# print("WELCOME".isupper())
# print(" ".isspace())

# searhing sunstrings

# s="welcome to python"
# print(s.endswith("thon"))
# print(s.find("thon"))
# print(s.startswith("thon"))
# print(s.find("become"))
# print(s.count("t"))
# print(s.rfind("p"))

# converting strings

# s = "String in PYTHON"
# s1 = s.capitalize()
# print(s1)  # String in python
# s2 = s.title()
# print(s2)  # String In Python
# s3 = s.lower()
# print(s3)  # string in python
# s4 = s.upper()
# print(s4)  # STRING IN PYTHON
# s5 = s.swapcase()
# print(s5)  # sTRING IN python
# s6 = s.replace("in", "on")
# print(s6)  # Strong on PYTHON
# print(s)  # String in PYTHON

# s="welcome"
# rev_str=""
# for i in s:
#     rev_str=i+rev_str
# print("Reversed string is:",rev_str)

# s='welcome'
# for i in s:
#     print(i,end=' ')

# s='welcome'
# rev_str=s[::-1]
# print(s)
# print(rev_str)
