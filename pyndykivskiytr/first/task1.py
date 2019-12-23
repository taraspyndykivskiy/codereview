"""
Із введеного користувачем речення 
потрібно вивести слова, що містять 
хоча б одну букву у верхньому регістрі.
"""

words=str(input("Введіть речення : ")).split()
big_words=list()

for word in words:
    for letter in word:
        if letter.isupper():
            big_words.append(word)
            break
            
print(big_words)
