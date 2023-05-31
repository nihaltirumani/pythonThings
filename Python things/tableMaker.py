table_number=int(input("What table do you want to be generated? "))
table_times=int(input("How many times? "))
index=0

while not index==table_times:
    print(table_number,"*",index+1,"=",table_number*(index+1))
    index+=1

#No modules used. While loop is used.