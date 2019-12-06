def make_key(file):
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

    with open(f"key_{file}", "w") as f:
        for word in len_list:
            f.write(f"{word}|")

text = ""
with open("key_text.txt") as f:
    for word in f:
        text += word

text = text.split("|")
print(text)