checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    if index_check(index):
      return checklist[index]
    else:
      print("Invalid index")

# UPDATE
def update(index, item):
    if index_check(index):
      checklist[index] = item
    else:
      print("Invalid index")


# DESTROY
def destroy(index):
    if index_check(index):
      checklist.pop(index)
    else:
      print("Invalid index")

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{}: {}".format(index, list_item))
        index += 1

def mark_completed(index):
    update(index, f"√{checklist[index]}")

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input


def select(function_code):
    function_code = function_code.upper()
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = int(user_input("Index Number?"))

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "U":
        item_index = int(user_input("Index Number?"))
        new_item = user_input("Item? ")
        # Remember that item_index must actually exist or our program will crash.
        update(item_index, new_item)

    elif function_code == "D":
        item_index = int(user_input("Index Number?"))

        # Remember that item_index must actually exist or our program will crash.
        destroy(item_index)

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True

def index_check(index):
    if isinstance(index, int) and index <= (len(checklist) - 1):
        return True
    else:
        return False

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    list_all_items()

    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()

test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, U to update an item from list and Q to quit"
    )
    running = select(selection)
