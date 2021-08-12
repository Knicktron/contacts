#! python3
"""
little helper functions
"""


def main_menu():
    print("Please select what you want to do:")
    print("----------------------------------------")
    print("[1] view Contacts")
    print("[2] search for Contacts")
    print("[3] add Contact")
    print("[0] end programm")
    print("----------------------------------------")
    print(" ")
    action = int(input("[?]: "))
    return action
