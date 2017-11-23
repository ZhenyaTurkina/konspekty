sent = "Доброе утро страна информация для пользователей"
words = sent.split()

#lines = []

#for w in words:
    #lines.append(w+'\n')
    
with open ("C:\\Users\\student\\Desktop\\pot.txt","w",encoding='utf-8')as f:
    for i,w in enumerate(words):
    #print(i,w)
    #for line in lines:
    #for i in range (len(words)):
    if i%2!=0:
        f.write(str[i]+' ' + w.upper() + '\n')
    else:
        f.write(str[i]+' ' + w + '\n')
        

#for i,w in enumerate(words):
    #print(i,w)
    
            
       
