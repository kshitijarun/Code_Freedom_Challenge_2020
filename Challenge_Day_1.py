"""
CodeForFreedom Challenge 20/04/2020

Write a program to print a list of strings in the predefined order, with the following modifications:
If the string’s length is equal to its printed position, convert string to UPPERCASE
	- Else convert the string to lowercase
	- Except if the string’s position is unchanged from its original position
	- Input will be a number N, then a list of N non-repeating numbers defining the required position of the string, and finally the list of N non-repeating strings. Output will be a list of N strings at the required location, with the required changes.

- Input:
5
5
4
3
1
2
Dog
Goat
Cat
Horse
Elephant

- Output:
horse
elephant
Cat
GOAT
dog
"""


n=int(input("Enter the range:: "))
arr1=[]                  #Created to store index values
for i in range(0,n):
    arr1.append(int(input("Enter index value:: "))-1)
arr2=[]                    #Created to store String values
for j in range(0,n):
    arr2.append(input("Enter String value:: "))

arr3=[]                 #Created to store result
for k in range(0,n):
    arr3.append(1)      #default temporary values
#print(arr3)
for i in range(0,n):
    #arr3.insert(arr1[i],arr2[i])
    #arr3.pop(arr1[i]+1)
    arr3[arr1[i]]=arr2[i]
    
for i in range(0,n):
    if(arr2.index(arr2[i])==arr3.index(arr2[i])):
        print(arr3[i])
    elif(len(arr3[i])==i+1):
        print(arr3[i].upper())
    elif(len(arr3[i])!=i+1):
        print(arr3[i].lower())
    
#print(arr3)
"""
arr4={}
#arr3.remove(arr1[2]-1)
arr3.insert(arr1[2],arr2[2])
print(arr3)
arr3.pop(arr1[2]+1)
print(arr3)
arr3.insert(arr1[0],arr2[0])
print(arr3)
arr3.pop(arr1[0]+1)
print(arr3)
arr3.insert(arr1[1],arr2[1])
print(arr3)
arr3.pop(arr1[1]+1)

print(arr3)
"""