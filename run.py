#! python3
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
        databank.contact_view()

    elif second_menu_choise == 2:
        pass

    elif second_menu_choise == 3:
        contact_list = databank.contact_list()
        if type(contact_list[0]) == (not ('int' or 'NoneType')):
            databank.contact_insert.first_insert(contact_list[0])

        if type(contact_list[1]) == (not ('int' or 'NoneType')):
            databank.contact_insert.second_insert(contact_list[1])

        if type(contact_list[2]) == (not ('int' or 'NoneType')):
            databank.contact_insert.last_insert(contact_list[2])

        if type(contact_list[3]) == (not ('int' or 'NoneType')):
            databank.contact_insert.landl_insert(contact_list[3])

        if type(contact_list[4]) == (not ('int' or 'NoneType')):
            databank.contact_insert.mobile_insert(contact_list[4])

        if type(contact_list[5]) == (not ('int' or 'NoneType')):
            databank.contact_insert.mail1_insert(contact_list[5])

        if type(contact_list[6]) == (not ('int' or 'NoneType')):
            databank.contact_insert.mail2_insert(contact_list[6])

        if type(contact_list[7]) == (not ('int' or 'NoneType')):
            databank.contact_insert.group_insert(contact_list[7])


if __name__ == '__main__':
    main()
else:
    pass

"""
    print("[1] view Contacts")
    print("[2] search for Contacts")
    print("[3] add Contact")
    print("[0] end programm")
"""



