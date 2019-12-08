def make_key(file, key):
    text = ""

    with open(file, "r") as f:
        for line in f:
            text += line

    #print(text.split(" "))
    text = text.split(" ")

    words_dict = {}

    # - adding all the words to dictionary
    for word in range(len(text)):
        try:
            isinstance(words_dict[text[word]], list)
            words_dict[text[word]].append(text[word])
        except KeyError:
            words_dict[text[word]] = []
            words_dict[text[word]].append(text[word])
    #print(words_dict)
    len_list = []
    word = ""
    previous_len = 0

    # - getting the word that comes up the most in the text and how much it does
    for alist in words_dict:
        if len(words_dict[alist]) > previous_len:
            previous_len = len(words_dict[alist])
            word = alist
    len_list.append(word)

    print(len_list)

    #print(previous_len, words_dict)
    found_smaller = False

    while len(len_list) < len(words_dict):
        for blist in words_dict:
            if len(words_dict[blist]) == previous_len:
                if blist != len_list[len(len_list)-1]:
                    len_list.append(blist)
        for clist in words_dict:
            if len(words_dict[clist]) == previous_len-1:
                len_list.append(clist)
                previous_len = len(words_dict[clist])
                found_smaller = True
                break
        if not found_smaller:
            previous_len -= 1

    with open(key, "w") as f:
        for word in len_list:
            f.write(f"{word}|")


def encrypt(file, key, destination):
    
    # - retrieving text to encrypt and key associated with it     
    text = ""
    with open(key, "r") as f:
        for word in f:
            text += word

    keys = text.split("|")
    text = ""
    with open(file) as f:
        for word in f:
            text += word
    text = text.split(" ")

    # - encrypting
    encrypted = ""
    for word in text:
        encrypted += str(keys.index(word))
        encrypted += "|"
    with open(destination, "w") as f:
        f.write(encrypted)


def decrypt(encrypted, key, destination):
    encrypted_text = ""
    with open(encrypted, "r") as f:
        encrypted_text = f.read()
    encrypted_text = encrypted_text.split("|")

    text = ""
    with open(key, "r") as f:
        for word in f:
            text += word
    keys = text.split("|")

    decrypted = ""
    for number in range(len(encrypted_text)):
        if not number == len(encrypted_text)-1:
            decrypted += keys[int(encrypted_text[number])]
            decrypted += " "
    with open(destination, "w") as f:
        f.write(decrypted)
