"""
Вивести кількість пустих списків.
"""

array=[1, [], 2, [], 9, []]
k=0
for i in array:
    if i==[]:
        k+=1
print("У списку є "+str(k)+" пустих множин")