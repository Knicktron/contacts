#! python3
import mariadb
import helpers
import databank

"""
'Contact Management Fox' by Niclas Fuchs, 2021-02-11
This Program is for managing Contacts with use of a sql-database
This is one of my fist programs. So please be gentle.
"""




def main():

    print(" ")
    print("++++++++++++++++++++++++++++++++++++++++")
    print("Welcome to the Contact Management Fox")
    print("++++++++++++++++++++++++++++++++++++++++")
    print(" ")
    print(" ")

    second_menu_choise = helpers.main_menu()
    print(second_menu_choise)

    if second_menu_choise == 1:
        databank.view_contacts()


if __name__ == '__main__':
    main()
else:
    pass
