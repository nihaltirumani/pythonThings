import time

part_list = []

def add_item(type, item):
    global part_list
    if type == "int":
        item = int(item)
    if type == "str":
        item = str(item)
    if type == "float":
        item = float(item)
    part_list.insert(0, item)


def extract_time():
    global part_list
    whole_time = time.ctime()
    index = 0
    part_time = ""

    while index < len(whole_time):
        while index < len(whole_time) and not whole_time[index] == " ":
            part_time = part_time + whole_time[index]
            index += 1
        index += 1
        add_item("str", part_time)
        part_time = ""

extract_time()

answer = input("Ask about time: ")
print(part_list)
if answer == "what year is it?":
    print(part_list[0])
if answer == "what time is it?":
    print(part_list[1])
if answer == "what is the date?":
    print(part_list[2])
if answer == "what month is it?":
    print(part_list[3])
if answer == "what day is it?":
    print(part_list[4])

# modules used: time. 
