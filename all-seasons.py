
def get_word(filename):
    # эта функция прочитывает файл и сплитит текст по возожным знакам прtпинания
    with open (filename,encoding = 'utf-8') as f:
        text = f.readlines()
    return text

def character_text(raw_text):
    character_all_texts = {}
    for line in raw_text[1:]:
        splitted = line.split(',')
        if len(splitted) > 3:
            name = splitted[2]
            text = ','.join(splitted[3:])
            text = text[1:]
            if name in character_all_texts:
                character_all_texts[name] = character_all_texts[name] + '\n' + text
            else:
                character_all_texts[name] = text
                
    return character_all_texts


def freq_d(person, character_texts):
    top_words = {}
    freq_d = {}
    no_punct = character_texts.replace('.',' ')
    no_punct = no_punct.replace(',',' ')
    tokens = no_punct.split()
    
    return top_words

def main():
    raw_data = get_word('C:\\Users\\student\\Desktop\\all-seasons.csv')
    all_texts = character_text(raw_data)
    #for character in all_texts:
        #print(character, len(all_texts[character]))
    texts_length = {}
    for character in all_texts:
        if character not in texts_length:
            texts_length[character] = len(all_texts[character])
    main_characters_pre = texts_length.items()
    main_characters = []
    for name,length in main_characters_pre:
        main_characters.append([length, name])
    main_characters = sorted(main_characters, reverse = True)[:20]
    main_names = []
    for length,name in main_characters:
        main_names.append(name)
    print(main_names)
    for character in main_names:
        freq_d(character, all_texts(character))
        print(character)
        print(top)

if __name__ == '__main__':
    main()
