# if- else code and should follow the proper intendation in python.
greet = "Hi"
a=5
#if greet == "Hello":
if a > 4:
    print("it satisfies the condition")
    print("second line")
else:
    print("It does not satisfy the condition")
print("if else code is completed")

#for loop
obj= [2, 3, 5, 7, 9]
for i in obj:
    #print(i)
    print(i*2) #multiples of 2
# sum of first 5 natural number 1+2+3+4+5=15
summation = 0
for j in range (1,6):  #range (i,j) ->i to j-1
    summation =summation + j
print(summation)

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
# in java (i=0,i>1,i++) similarly in python
# we will be having the increment +1 by default if we need to shift we need to specify like below
for k in range (1 ,10 ,2): #here we are shifting by 2
    print(k)
for l in range (1 ,15 ,5): #here we are shifting by 5
    print (l)
print("*********skipping first index**************")
for m in range(10):
    print(m)

