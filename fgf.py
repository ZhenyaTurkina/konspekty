'''
def hello (user1,age):
    print('Hello, ' + user1 + '!')
    #print (user2.title())
    #print (user3.title())
    if age > 10:
        print ('Older than 10')
    else:
        print ('age')

hello('Anna',15)
'''

'''
def hello (user1,age):
    
    print('Hello, ' + user1 + '!')
    #print (user2.title())
    #print (user3.title())
    if age > 10:
        print ('Older than 10')
    else:
        print (age)
    new_name = user1.title()
    return new_name

user_title = hello('ann', 10)

print (user_title)

#hello('Anna',15)

'''
'''
def elements (word):
    #a = len(word)
    for i in word:
        print(i)
    print (len(word))
    #print (user2.title())
    #print (user3.title())

#elements('word')

def tokenize (sentence):
    words = sentence.split()
    return words

sent = 'functions are useful'

tok_result = tokenize(sent)
print(tok_result)

for w in tok_result:
    print(w.upper())
#els = sent.split()
#elements (els)
    

#hello(word)
'''
def lines_div (uk):
    #a = len(word)
    with open (uk, encoding = 'utf-8') as f:
        lines_raw = f.readlines()
    lines_length = []
    for line in lines_raw:
        clear_line = line.strip()
        if clear_line:
            print(len(clear_line), clear_line)
            lines_length.append(len(clear_line))
            
    return min(lines_length)

min_1 = lines_div('uk.txt')

print (min_1)



