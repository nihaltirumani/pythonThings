# varibles and lists.
index = 0
word = ""
words_list = []


# defining funtions.
def add_item(type, item):
    global words_list
    if type == "int":
        item = int(item)
    if type == "str":
        item = str(item)
    if type == "float":
        item = float(item)
    words_list.append(item)

def split_sentence(string):
    global index, word
    while index != len(string):
        while string[index] != " ":
            word = word + string[index]
            if not index == 18:
                index += 1
        if not index == 18:
            index += 1
        add_item("str", word)
        word = ""


# running test.
split_sentence("hi my name is nihal")
print(words_list)

# not working as imagined.

