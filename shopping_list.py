import os
import sys

# Make a list that will hold on to the items
shopping_list = []

# Create a filename for the list
saved_file = "shopping_list.txt"

def clear_console():
    # Clear the console
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_help(list):
    clear_console()
    # Print out instructions on how to use the app
    print("What should we pick up at the shops?")
    print("""
You have {} items in your list.

Enter HELP to show this help menu again.
Enter SHOW to see your list.
Enter REMOVE to remove an item.
Enter CLEAR to delete your list.
Enter SAVE to save your list and exit.
Enter QUIT to exit without saving.""".format(len(list)))

def show_list(list):
    clear_console()
    # Print out the list
    if len(list) == 0:
        print("You have 0 items in your list.")
    else:
        print("Here's your list:\n")
        for item in list:
            print(item)

def add_to_list(new_item, list):
    clear_console()
    # Add new items to the list
    list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(list)))

def remove_from_list(list):
    clear_console()
    print("What item would you like to remove?\n")
    # prompt the user for an item to remove
    word = input("Remove an item: ")
    if word in list:
        # remove item from the shopping list
        list.remove(word)
        clear_console()
        print("{} has been removed from your list.".format(word))
    else:
        clear_console()
        print("{} is not in your list.".format(word))

def open_list(filename, list):
    try:
        # open file
        with open(filename) as file:
            # read contents of the file
            data = file.read().splitlines()
            # add each line in file (minus line breaks) to the current list
            list.extend(data)
            #for line in file:
                #list.append(line[:-1])
    except FileNotFoundError:
        pass

def save_list(filename, list):
    # Save the current list to a text file
    with open(filename, "w") as file:
        for item in list:
            file.write(item + "\n")
    print("\nYour list has been saved to {}. \n\nHappy shopping!\n".format(filename))

def delete_list(filename, list):
    clear_console()
    # clear the current list
    list.clear()
    try:
        # delete saved list file
        os.remove(filename)
        print("List deleted successfully.")
    except FileNotFoundError:
        print("List deleted successfully.")

open_list(saved_file, shopping_list)

show_help(shopping_list)

while True:
    # Ask for new items
    new_item = input("\nAdd an item: ")

    # Be able to quit the app, show help, show the list, save the list, clear the list and remove an item from the list
    if new_item == "QUIT":
        show_list(shopping_list)
        print("\nHave a nice day!\n")
        break
    elif new_item == "HELP":
        show_help(shopping_list)
        continue
    elif new_item == "SHOW":
        show_list(shopping_list)
        continue
    elif new_item == "SAVE":
        show_list(shopping_list)
        save_list(saved_file, shopping_list)
        break
    elif new_item == "CLEAR":
        delete_list(saved_file, shopping_list)
        continue
    elif new_item == "REMOVE":
        remove_from_list(shopping_list)
        continue
    else:
        add_to_list(new_item, shopping_list)
