s1 = input("Введите первую строку: ")
s2 = input("Введите вторую строку: ")
f1 = input("Введите первое число: ")
f2 = input("Введите второе число: ")
f1 = float(f1)
f2 = float(f2)
 
bool_s = s1 > s2
bool_f = f1 != f2
bool_or = f1 + f2 > 0 or (s1 != '' and s2 != '')
 
print('-'*10)
print("Первая строка больше второй:", bool_s)
print("Числа не равны друг другу:", bool_f)
print("Первая строка больше второй и числа не равны друг другу:", bool_s and bool_f)
print("Сумма чисел больше нуля ИЛИ ни одна из строк не пуста:", bool_or)



ПРИМЕРНЫЙ ВЫВОД:
Введите первую строку: ty
Введите вторую строку: kl;
Введите первое число: 6.8
Введите второе число: 8
----------
Первая строка больше второй: True
Числа не равны друг другу: True
Первая строка больше второй и числа не равны друг другу: True
Сумма чисел больше нуля ИЛИ ни одна из строк не пуста: True
