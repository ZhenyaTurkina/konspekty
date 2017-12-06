word = (input ("Введите слово: "))

a = len(word)

if a == 0:
    print ("Ваша строка пуста")
else:
    for i in range (0,a//2 + a % 2):
        print (word[i:+a-i])
        
'''
с обеих сторон по одной букве
'''
