#! python3
import mariadb

"""
functions for the sql database integration
"""
"""mydb = mariadb.connect(
    host="hgp18.duckdns.org",
    port=25555,
    user="test",
    password="test",
    database="test"
)
cursor = mydb.cursor()"""


def contact_view():
    mydb = mariadb.connect(
        host="hgp18.duckdns.org",
        port=25555,
        user="test",
        password="test",
        database="test"
    )
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM test.contacts")
    contacts = cursor.fetchall()
    print("----------------------------------------")
    for x in contacts:
        print(contacts[0])
    print("----------------------------------------")

    cursor.close()
    mydb.commit()
    mydb.close()


def contact_search(search_input):
    mydb = mariadb.connect(
        host="hgp18.duckdns.org",
        port=25555,
        user="test",
        password="test",
        database="test"
    )
    cursor = mydb.cursor()

    cursor.execute(
        "SELECT * FROM test.contacts WHERE firstname OR secondname OR sirname OR landline OR mobile OR mailaddress1 "
        "OR mailaddress2 = %s",
        search_input)
    result = cursor.fetchall()
    print(result)

    cursor.close()
    mydb.commit()
    mydb.close()


def groupe_view():
    mydb = mariadb.connect(
        host="hgp18.duckdns.org",
        port=25555,
        user="test",
        password="test",
        database="test"
    )
    cursor = mydb.cursor()
    print(" ")
    print("existing Groups:")
    cursor.execute("SELECT * FROM test.groups")
    groups = cursor.fetchall()
    y = 0
    print("----------------------------------------")
    for group in groups:
        print("[" + str(group[0]) + "] " + group[1].capitalize())
        y = + 1
    print("----------------------------------------")
    print(" ")

    cursor.close()
    mydb.commit()
    mydb.close()


def contact_list():
    first = input("First Name: ").lower()
    second = input("Second Name: ").lower()
    sir = input("Sirname: ").lower()
    landl = str(input("Landline number: "))
    mobile = str(input("Mobile number: "))
    mail1 = input("Email address: ").lower()
    mail2 = input("Email address 2: ").lower()
    groupe_view()
    print("Please insert the number of the Groupe(not the name!)")
    group = input("Groupe: ")

    cont_list = [first, second, sir, landl, mobile, mail1, mail2, group]
    return cont_list


class contact_insert:

    def __init__(self, cont_input):
        self.input = cont_input
        self.mydb = mariadb.connect(
            host="hgp18.duckdns.org",
            port=25555,
            user="test",
            password="test",
            database="test"
        )
        self.cursor = self.mydb.cursor()
        self.con_id = self.cursor.fetchall()
        self.fname = self.input
        self.input = cont_input

    def first_insert(self):
        self.cursor.execute("INSERT INTO test.contacts (firstname) VALUES (%s)",
                            self.input)

    def get_contact_id(self):
        self.cursor.execute("SELECT id FROM test.contacts where firstname = %s",
                            self.fname)

    def second_insert(self):
        self.cursor.execute("UPDATE test.contacts SET secondname = '(%s)' WHERE ID = ",
                            self.con_id)

    def last_insert(self):
        self.cursor.execute("UPDATE test.contacts SET sirname = '(%s)' WHERE ID = ",
                            self.con_id)

    def landl_insert(self):
        self.cursor.execute("UPDATE test.contacts SET landline = '(%s)' WHERE ID = ",
                            self.con_id)

    def mobile_insert(self):
        self.cursor.execute("UPDATE test.contacts SET mobile = '(%s)' WHERE ID = ",
                            self.con_id)

    def mail1_insert(self):
        self.cursor.execute("UPDATE test.contacts SET mailaddress1 = '(%s)' WHERE ID = ",
                            self.con_id)

    def mail2_insert(self):
        self.cursor.execute("UPDATE test.contacts SET mailaddress2 = '(%s)' WHERE ID = ",
                            self.con_id)

    def group_insert(self):
        self.cursor.execute("UPDATE test.contacts SET group = '(%s)' WHERE ID = ",
                            self.con_id)

    def disconnect(self):
        self.cursor.close()
        self.mydb.commit()
        self.mydb.close()



"""
cursor.close()
mydb.commit()
mydb.close()
"""
