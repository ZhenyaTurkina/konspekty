word = (input ("Введите слово: "))

a = len(word)

print (word)

if a == 0:
    print ("Ваша строка пуста")
else:
    for m in range (1, a):
        k = word[-1] + word[:-1]
        print (k)
        word = k
        
        
        
 '''
 обратно 3-ему
 '''
