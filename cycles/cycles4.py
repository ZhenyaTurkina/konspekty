number = input()

if number == '':
    print('введи быстро я сказал')
    
else:
    number = int(number)
    
    for i in range(number):
        word = str(input())
        if word == '':
            print('введи быстро я сказал')
        elif word == 'программирование':
            break

'''
Спрашивает у пользователя число N, а затем N раз спрашивает у пользователя слово и выводит его на экран.
Если пользователь ввел слово "программирование", программа должна завершить работу.
'''