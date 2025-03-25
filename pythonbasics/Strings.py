# strings in Python are arrays of bytes representing unicode characters.
str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str2 = "RahulShetty"

print(str[1])   #1
print(str[0:5]) # if you want substring "Rahul"
print(str+str1)  #concatinate
print(str2 in str) #substring check

var =str.split(".")
print(var)
print(var[0])
str3 = "Great"
print(str3.strip()) #it wil be used like trim in java to remove spaces
print(str3.lstrip()) #to remove  left space
print(str3.rstrip())  #to remove right space