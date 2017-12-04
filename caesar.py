lines2016 = []
with open('C:\\Users\\ЕВГЕНИЯ\\Desktop\\happiness-cantril-ladder (1).csv', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        #print(line)
        cells = line.split(',')
        #print(cells)
        if cells[2] == '2016':
            lines2016.append(cells)
#print (lines2016)

user_ = input('country: ')
found_answer = False
for line in lines2016:
    if line[0] == user_:
        value = float(line[3].strip())
        print(value)
        found_answer = True
        break
if not found_answer:
        print ('здесь нет такой страны')
      

    
