#! python3
import mariadb

"""
functions for the sql database integration
"""

mydb = mariadb.connect(
    host="hgp18.duckdns.org",
    port=25555,
    user="test",
    password="test",
    database="test"
    )
cursor = mydb.cursor()


def view_contacts():
    cursor.execute("SELECT * FROM test.contacts")
    contacts = cursor.fetchall()
    print("----------------------------------------")
    for x in contacts:
        print(contacts[0])
    print("----------------------------------------")

cursor.close()
mydb.commit()
mydb.close()
