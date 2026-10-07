"""
Unk's python library installer
"""

import os

from libs.customerrors import doraise, BadRange

def action_handler(action):
    pass

def main(error=None):
    _, termh = os.get_terminal_size()
    print("\n"*(termh-9))
    print(
        "What would you like to do ?\n\n"
        "1) Install a library\n"
        "2) Remove a library\n"
        "3) Update a library\n"
        )
    print(error + "\n" if error else "\n")
    
    try:
        action = int(input(">> "))
        if not (action <= 3 and action >= 1):
            doraise("BaddRange")
        action_handler(action)
    except ValueError:
        main(error="Bad Value")
    except BadRange:
        main(error="Value should be between 1 and 3")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...\nHave a nice day!")