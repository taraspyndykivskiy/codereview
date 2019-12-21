"""
Із введеного користувачем речення 
потрібно вивести слова, що містять 
хоча б одну букву у верхньому регістрі.
"""

text=str(input("Введіть речення : "))
words=text.split()
big_words=[None]*len(words)
i=0
for word in words:
    for letter in word:
        if letter.isupper()==True:
            big_words[i]=str(word)
            i+=1
            break
print(big_words)