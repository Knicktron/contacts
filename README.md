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

# Main Loop
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
        print("----------------------------------------")
        for x in contacts:
            print(contacts[0])
        print("----------------------------------------")
    elif action == 2:
        pass
    elif action == 3:
        another = True
        while another:
            firstname = input("First Name: ").lower()
            secondname = input("Second Name: ").lower()
            sirname = input("Sirname: ").lower()
            landline = str(input("Landline number: "))
            mobile = str(input("Mobile number: "))
            mail1 = input("Email address: ").lower()
            mail2 = input("Email address 2: ").lower()
            print(" ")
            print("existing Groups:")
            cursor.execute("SELECT * FROM test.groups")
            groups = cursor.fetchall()
            y = 0
            print("----------------------------------------")
            for x in groups:
                print("[" + str(x[0]) + "] " + x[1].capitalize())
                y = + 1
            print("----------------------------------------")
            print(" ")

            group_type_selection = True
            while group_type_selection:
                print("Please select a Groupe [] or [(name)] to create a new Groupe")
                selection = input("[?]: ")

                try:
                    selection = int(selection)
                except ValueError:
                    if selection == "" or " ":
                        group = None
                        group_type_selection = False

                    else:
                        group = selection
                        group_type_selection = False
                except:
                    print("invalid entry. Please select again!")
                    group = None
                    group_type_selection = True


                else:
                    cursor.execute("INSERT INTO groups (groupe) VALUES (?)",
                                   (str(selection)))
                    cursor.execute("SELECT ID FROM groups WHERE groupe = '(?)'",
                                   (str(selection)))
                    group = cursor.fetchall()
                    group_type_selection = False

            cursor.execute("INSERT INTO contacts (first_name, second_name, sirname, landline, mobile, mail1, "
                           "mail2, group_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                           (firstname, secondname, sirname, landline, mobile, mail1, mail2, group))
            
            # while another_contact_choise doesn't work as it should yet
            print(" ")
            print("do you want to add another Contact?")
            another_contact = input("[Y]/[N]: ")
            another_contact_choise = True
            while another_contact_choise:
                if another_contact == "Y" or "y" or "Yes" or "yes":
                    another = True
                    another_contact_choise = False
                elif another_contact == "N" or "n" or "No" or "no":
                    another = False
                    another_contact_choise = False
                else:
                    print("invalid Input. Please try again.")

    elif action == 0:
        print(" ")
        print("Have a nice Day!")
        exit_loop = True

mydb.commit()
mydb.close()
