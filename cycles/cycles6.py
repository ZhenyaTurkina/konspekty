number = input()

if number == '':
    print('введи быстро я сказал') 
else:
    number = int(number)
    for i in range(10):
        print (i,'*', number,'=', i*number)
        
'''
Спрашивает у пользователя число и выводит на экран таблицу умножения на это число (т. е., например, если введено число 5,
то выводятся строчки вида "1 * 5 = 5"; "2 * 5 = 10", и так далее -- всего десять строчек).
'''
