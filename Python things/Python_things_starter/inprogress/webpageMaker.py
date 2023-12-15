# variables and lists
element_list = ["<p></p>", "<h1></h1>"]
elements = ["p","h1"]
code_list = []
found_element = False
content = ""
user_element = ""
index = 0

user_element = input("What element? ")

while not found_element:
    if elements[index] == user_element:
        found_element = True
        code_list.append(element_list[index][0:((len(element_list[index]) - 1) / 2)])
