word = (input ("Введите слово: "))

a = len(word)

print (word)

if a == 0:
    print ("Ваша строка пуста")
else:
    for i in range (1, a+1):
        print (word[-i:])
        
'''
последний 1, последний 2.....
'''
