#! python3
import mariadb

"""
functions for the sql database integration
"""


def view_contacts():
    cursor.execute("SELECT * FROM test.contacts")
    contacts = cursor.fetchall()
    print("----------------------------------------")
    for x in contacts:
        print(contacts[0])
    print("----------------------------------------")
