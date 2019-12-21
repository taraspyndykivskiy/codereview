"""
Вивести суми парних і непарних чисел списку.
"""

array=[1, 2, 3, 4]
parni=neparni=0
for i in array:
    if(array[i]%2==0):
        parni+=array[i]
    elif(array[i]%2==1):
        neparni+=array[i]
print("sum of parni = "+str(parni))
print("sum of neparni = "+str(neparni))