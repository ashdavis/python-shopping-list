# Python Shopping List

![Image of Python Shopping List Help Menu](https://ashley.one/img/python-shopping-list-1.png)

A command-line shopping list application written in Python.

## Summary

This small command-line application helps the user create a shopping list.

Alongside entering items to add to their list, the user can enter commands to:

* Display a help menu
* Show the current list contents
* Remove an item from the current list
* Delete the list
* Save the current list to a text file
* Exit without saving

## Usage

1. Download and install [Python 3] (https://www.python.org)

2. Run the script from the command-line:

    `python3 shopping_list.py`

3. Add items to your shopping list.

4. Enter the following commands when needed:

    `HELP` displays the help menu

    `SHOW` displays the current list contents

    `REMOVE` allows an item to be removed from the current list

    `CLEAR` will delete the current list and the saved list file

    `SAVE` saves the current list to a text file

    `QUIT` exits the program without saving

## Saving and Loading Shopping Lists

* If you save your list before quitting the application, the list will be saved to shopping_list.txt (in the same location as shopping_list.py).
* The application looks for a saved file when it first runs. If this file is found, it's contents are loaded into the current shopping list.
* To manually add items to the shopping_list.txt file, simply add one item per line.
