word = (input ("Введите слово: "))

a = len(word)

print (word)

if a == 0:
    print ("Ваша строка пуста")
else:
    for m in range (0, a):
        print (word[:-1])
        word = word[:-1]
        
'''
по возрастанию
'''
