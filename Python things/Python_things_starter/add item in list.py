my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def add_item(type, item):
    global my_list
    if type == "int":
        item = int(item)
        print("int")
    if type == "str":
        item = str(item)
        print("str")
    if type == "float":
        item = float(item)
        print("float")
    print(item)
    my_list.append(item)
type_ = input("What type? ")
item_ = input("What item? ")
add_item(type_, item_)
print(my_list)
