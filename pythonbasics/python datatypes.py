# list data type that allows multiple values and with different data types

values =[1,3.5,"atharv"]

print(values[0])
print(values[2])
print(values[1:2])
print(values[-1])  #
values.insert(2,"p") #[1, 3.5, 'p', 'atharv']
print(values)
values.append('end') #[1, 3.5, 'p', 'atharv', 'end']
print(values)
values[2] = "ATHARV" #update
del values[0]  #delete the value in index 0
print(values)  #[3.5, 'ATHARV', 'atharv', 'end']

#tuple declaration

values =(1, 3.5, 'p' ,'atharv')
print(values[3])   #update "TypeError: 'tuple' object does not support item assignment"
#values[3] = "ATHARV"
print(values)

# dictionary
dic = {"a": 2, 4:"string", "c":"hello"}
print(dic[4])
print(dic["c"])

# empty dictionary
dict = {}
dict ["firstname"] = "Atharv"
dict ["lastname"] = "P"
dict ["gender"] = "Male"
print(dict)
print(dict["lastname"])