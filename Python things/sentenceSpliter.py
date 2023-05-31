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
    words_list.insert(0, item)

def split_sentence(string):
    global index, word
    while index != len(string):
        while not string[index] != " ":
            word = word + string[index]
            index += 1
        index += 1
        add_item("str", word)
        word = ""


# running test
split_sentence("hi my name is nihal")
print(words_list)
 