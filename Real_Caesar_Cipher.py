alpha = '  абвгдеёжзийклмнопрстуфхцчшщъыьэюяа'

word = input().strip()

a = len(word)

res = ''

for i in word:
    res = res + alpha[(alpha.index(i) + 1)] 
        
print(res)
