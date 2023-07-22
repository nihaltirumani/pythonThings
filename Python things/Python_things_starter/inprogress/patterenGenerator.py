def pattern_generator():
    # Importing modules.
    import random

    # Variables.
    outerIndex = 1
    middleIndex = 1
    innerIndex = 1
    bundle = ""
    pattern_type = ""
    rows = 0
    columns = 0
    random_picker = 0

    # Function to ask for rows and columns.
    def rows_and_columns():
        nonlocal random_picker
        nonlocal rows
        nonlocal columns
        try:
            if random_picker == 0:
                print("If you enter 0 for rows and columns, it will go into random mode.")
                rows = int(input("How many rows? "))
                columns = int(input("How many columns? "))
            if rows == 0 and columns == 0 :
                rows = random.randint(10,50)
                columns = random.randint(10,50)
        except ValueError:
            pass
            print("Enter only numeric values.")
            exit()

    # Function to check pattern types and print patterns.
    def check_pattern_types():
        nonlocal rows
        nonlocal columns
        nonlocal pattern_type
        nonlocal outerIndex
        nonlocal middleIndex
        nonlocal innerIndex
        nonlocal bundle
        nonlocal random_picker

        if pattern_type == "stars":
            rows_and_columns()
            while outerIndex < rows + 1:
                print("*"*columns)
                outerIndex += 1
            outerIndex = 1
        elif pattern_type == "1and0":
            rows_and_columns()
            while outerIndex < rows + 1:
                while middleIndex < (columns * outerIndex) + 1:
                    bundle = bundle + str(random.randint(0,1))
                    middleIndex += 1
                print(bundle)
                outerIndex += 1
                bundle = ""
        elif pattern_type == "X":
            print("X")
        elif pattern_type == "random":
            random_picker = random.randint(1,3)
            if random_picker == 1:
                pattern_type = "stars"
            elif random_picker == 2:
                pattern_type = "1and0"
            elif random_picker == 3:
                pattern_type = "X"
                
            rows = 0
            columns = 0
            check_pattern_types()
            print("This pattren was", pattern_type + ".")
            print("The rows are", str(rows) + ".", "And the columns are", str(columns) + ".")
            random_picker = 0

    # Asking the user what pattern type they want.
    pattern_type = input("What pattern type do you want? \nType \"help\" for more. ")

    # prints the types of patterns are there.
    if pattern_type == "help":
        print("Pattern types: stars, 1and0, random")
        print("Note: Type the command exactly.")
        pattern_type = input("What pattern type do you want? ")
        check_pattern_types()

    check_pattern_types()

pattern_generator()