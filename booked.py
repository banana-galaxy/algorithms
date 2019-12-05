text = ""

with open("text.txt", "r") as f:
    for line in f:
        text += line

#print(text.split(" "))
text = text.split(" ")

words_dict = {}
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
for alist in words_dict:
    if len(words_dict[alist]) > previous_len:
        previous_len = int(len(words_dict[alist]))
        word = alist
len_list.append(word)

print(previous_len)

while True:
    for alist in words_dict:
        if len(words_dict[alist]) == previous_len:
            len_list.append(alist)
    for alist in words_dict:
        if int(len(words_dict[alist])) < int(previous_len):
            len_list.append(alist)
            previous_len = words_dict[alist]
            break
    print(len(words_dict), len(len_list))
    if len(len_list) >= len(words_dict):
        break


print(len_list)