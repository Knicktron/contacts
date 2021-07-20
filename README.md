#! python3
import mariadb

mydb = mariadb.connect(
    host="hgp18.duckdns.org",
    user="test",
    password="test",
    database="test"
)
cursor = mydb.cursor()


def show_contacts():
    cursor.execute("SELECT * FROM test.contacts")
    contacts = cursor.fetchall()
    for x in contacts:
        print(contacts)


def search_contact():
    pass


def add_contact(first, second, last, land, mobile, mail1, mail2, group):
    cursor.execute(
        "INSERT INTO test.contacts(first_name, second_name, sirname, landline, mobile, mail1, mail2, "
        "group) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (first, second, last, land, mobile, mail1, mail2, group))


exit = False
while not exit:
    print("++++++++++++++++++++++++++++++++++++++++")
    print("Welcome to the Contact Management Fox")
    print("Please select the ")
    print("----------------------------------------")
    print("[1] view Contacts")
    print("[2] search for Contacts")
    print("[3] add Contact")
    print("----------------------------------------")
    action = int(input("[?]: "))

    if action == 1:
        show_contacts()
    elif action == 2:
        pass
    elif action == 3:
        another = True
        while another == True:
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
                y =+ 1
            print("Please select a Groupe [] or [N]ew to create a new Groupe")
            selection = input("[?]: ")

            group_ok = False

            while group_ok = False:
                if selection == str():
                    cursor.execute("INSERT INTO test.genres (genre) VALUES (?)", (selection.lower()))
                    cursor.execute("SELECT ID FROM test.groups WHERE groupe = (?)", (selection.lower()))
                    group = cursor.fetchall()
                    group_ok = True
                elif selection == int() and 1 <= y:
                    group = selection
                    group_ok = True
                else:
                    print("please try again")
                    group_ok = False

            add_contact(firstname, secondname, sirname, landline, mobile, mail1, mail2, group)

            print(" ")
            print("do you want to add another Contact?")
            another_contact = input("[Y]es/[N]o: ")
            if another_contact == "Y" or "y" or "Yes" or "yes":
                another == True
            else:
                another == False
"""




y = 0
for x in groups:
    print(x[1].capitalize())
    y += 1
print("to add a new Groupe just type in the name :)")
# group = input("Group: ")
existing = False

for x in groups:
    if group.lower() == groups[1]:
        existing = True



def add_contact(fistname, secondname, sirname, landline, moblie, mailaddress1, mailadress2, group):
    genredb = mariadb.connect(
        user="test",
        password="test",
        host="localhost",
        port=3306,
    )
    #curser.execute("INSERT INTO test.contacts()")


cursor = genredb.cursor()

cursor.execute("SELECT ID, Name, Kategorie_ID FROM genre.genre")
sgenre1 = random.choice(cursor.fetchall())
cursor.execute("SELECT ID, Name, Kategorie_ID FROM genre.genre")
sgenre2 = random.choice(cursor.fetchall())
cursor.execute("SELECT Genre_ID_1, Genre_ID_2 FROM genre.history ORDER BY ID DESC LIMIT 1")
hist_ID1, hist_ID2 = cursor.fetchall()[0]


while sgenre2[2] == sgenre1[2]:
    cursor.execute("SELECT ID, Name, Kategorie_ID FROM genre.genre")
    sgenre2 = random.choice(cursor.fetchall())





"""
mydb.commit()
mydb.close()
