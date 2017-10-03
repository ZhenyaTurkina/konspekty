'''
for i in range (5):
    word=(input('введите слово: '))
    a=len(word)
    print  (a)

'''
'''
kol=int(input('kolichestvo'))

for i in range (kol):
    num=int(input('vvedite chislo: '))
    if num>0:
        print('bolshe')
    elif num<0:
        print('menshe')
    else:
        print (0)

'''
'''
a=0

for i in word: #letter, i - просто переменные
    #print(letter)
    #print('---')
    #print (letter*3)
    print (i,a)
    a+=1

print(a)
print ('--'*10)
#print(word[1])

#print (word[0])
print(len(word))
print(word[len(word)-1])
print (word[-4])

'''

'''
a=0

for i in word: #letter, i - просто переменные
    #print(letter)
    #print('---')
    #print (letter*3)
    if a%2!=0:
        print(i)
    a+=1
'''
#print(word[2:4]) #обращение к 2-м переменным, не включая второе
#print(word[3:]) с третье буквы до конца
#print(word[3:-1])

#print(word[-2:2])
#print(word[::2]) с шагом два
#print(word[-5:-1])

#part=word[3:6]
#print(word[:3]+'!'+part+'!'+word[6:])
#a=0

#for i in range(3,20,2):
    #if i>10 and i%2!=0:
        #print (i**2)
'''
a=0
for k in range (word+1):
    a+=k
    print (a)
print(a)
'''
'''
for i in range(10):
    print()
    print(i, end='  ') #выводит на той же строке
    if i == 8:
        continue
    print (i**2)
print('end')
'''
'''
i=2
while i**2<=100:
    print(i, i**2)
    i+=1
print (i)
'''
