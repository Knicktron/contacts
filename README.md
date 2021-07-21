#! python3
import mariadb

mydb = mariadb.connect(
    host="hgp18.duckdns.org",
    user="test",
    password="test",
    database="test"
)
cursor = mydb.cursor()

print("++++++++++++++++++++++++++++++++++++++++")
print("Welcome to the Contact Management Fox")
print("++++++++++++++++++++++++++++++++++++++++")
print(" ")
print(" ")

exit_loop = False
while not exit_loop:

    print("Please select what you want to do:")
    print("----------------------------------------")
    print("[1] view Contacts")
    print("[2] search for Contacts")
    print("[3] add Contact")
    print("[0] end programm")
    print("----------------------------------------")
    print(" ")
    action = int(input("[?]: "))

    if action == 1:
        cursor.execute("SELECT * FROM test.contacts")
        contacts = cursor.fetchall()
        for x in contacts:
            print(contacts[0])
    elif action == 2:
        pass
    elif action == 3:
        another = True
        while another:
            firstname = input("First Name: ")
            secondname = input("Second Name: ")
            sirname = input("Sirname: ")
            landline = str(input("Landline number: "))
            mobile = str(input("Mobile number: "))
            mail1 = input("Email address: ")
            mail2 = input("Email address 2: ")
            print(" ")
            print("existing Groups:")
            cursor.execute("SELECT * FROM test.groups")
            groups = cursor.fetchall()
            y = 0
            for x in groups:
                print("[" + str(x[0]) + "] " + x[1].capitalize())
                y = + 1
            print("Please select a Groupe [] or [0] to create a new Groupe")

            selection = input("[?]: ")
            if 1 <= int(selection) <= y and int:
                group = int(selection)
            else:
                cursor.execute("INSERT INTO groups (group) VALUES (?)", (selection.lower()))
                cursor.execute("SELECT ID FROM groups WHERE groupe = (?)", (selection.lower()))
                group = cursor.fetchall()

            cursor.execute("INSERT INTO contacts (first_name, second_name, sirname, landline, mobile, mail1, "
                           "mail2, group_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                           (firstname, secondname, sirname, landline, mobile, mail1, mail2, str(group)))

            print(" ")
            print("do you want to add another Contact?")
            another_contact = input("[Y]es/[N]o: ")
            if another_contact == "Y" or "y" or "Yes" or "yes":
                another = True
            else:
                another = False

    elif action == 0:
        print(" ")
        print("Have a nice Day!")
        exit_loop = True

mydb.commit()
mydb.close()
