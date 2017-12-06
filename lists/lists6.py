word = (input ("Введите слово: "))

a = len(word)

print (word)

if a == 0:
    print ("Ваша строка пуста")
else:
    for i in range (a-1, -1, -1):
        print (word[-i:])
        
 '''
 без 1-го, без двух первых, без трех первых....
 '''
