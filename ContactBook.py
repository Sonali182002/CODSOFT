import sqlite3
 # pythin has in-built SQLite module in library, so we don't need to insatll SQLite separately in PC.
def connect_db():
    # Connectung to database file 'contact' 
    conn=sqlite3.connect('contacts.db') # this code will create the file if it doesn't exist

    #cursor object to execute SQL queries
    cursor=conn.cursor()

    #Creating the table in database
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    address TEXT)''')

    # commit the transaction
    conn.commit()

    #conn is variable that represents connection to the database
    #conn is required to interact with database
    return conn,cursor

print("!!!!!!!!!!Contact Book!!!!!!!!!!")

def add():
    name=input("Enter New Contact name: ")
    phone=input("Enter the Contact Phone number: ")
    email=input("Enter the email id: ")
    address=input("Enter the address: ")
    
# applying the check to ensure user enters name and phone 
    if not name or not phone:
        print("Name and Phone no. are required fields.")
        return
    
    #calling connect_db() and it is returning conn,cursor 
    conn,cursor=connect_db()

    #fetching contacts from database
    cursor.execute("SELECT * FROM contacts WHERE name = ? OR phone = ?", (name, phone))
    existing_contact = cursor.fetchone()

    if existing_contact:
        print("A contact with this name or phone number already exists!")
        conn.close()
        return

    try:
        # sql insert statement
        cursor.execute('''
        INSERT INTO contacts (name,phone, email, address)
        VALUES (?, ?, ?, ?) ''',(name,phone,email,address))  
        conn.commit()
        print("Contact added succesfully!")

        # exception handling
    except sqlite3. Error as e:
        print(f"An error ocuured: {e}")
    finally:

        # closing database after use
        conn.close()   

def view():
    conn=sqlite3.connect('contacts.db')
    cursor=conn.cursor()

    cursor.execute('''
    SELECT name,phone FROM contacts
    ''')
# fetching all the contacts stored in the database
    contacts=cursor.fetchall()

    if not contacts:
        print("NO CONTACT FOUND!")
    else:
        print("CONTACTS LIST:\n")
        print("--------------------")
        for contact in contacts:
            print(f"Name:{contact[0]}, Phone no:{contact[1]}")

    conn.close()

def search():
    conn=sqlite3.connect('contacts.db')
    cursor=conn.cursor()

# strip() will remove whitespace from the user input 
# lower() string method will return the only lowercase letter
    search_by=input('Do you want to search by name or phone number? (name/phone no.): ').strip().lower()

    if search_by=='name':
        name=input("enter the name to search: ").strip().lower()

        cursor.execute('''
            SELECT name, phone, email, address FROM contacts WHERE name LIKE ?
            ''',('%' + name +' %',)) # using '%' allows for partial matches, so user don't have to input the exact full name or phone no.
    elif search_by=='phone':
        phone=input('enter the phone number: ').strip()

        cursor.execute('''
            SELECT name,phone,email, address FROM contacts WHERE phone LIKE ?
            ''',('%'+phone+'%',)) 
    else:
        print("invalid input, Please enter name or phone number.")
        conn.close()
        return
    #fetching all the matching contacts
    contacts=cursor.fetchall()

    if not contacts:
        print("no contact found")
    else:
        print("search result:\n")
        for contact in contacts:
            print(f"name:{contact[0]}, phone number:{contact[1]}, Email:{contact[2]}, Address: {contact[3]}")
            print("-----------------")
    conn.close()

def update():
    conn=sqlite3.connect('contacts.db')
    cursor=conn.cursor()

    # asking user to enter name or phone he wants to update
    search_by=input('Do you want to search by name or phone number? (name/phone no.): ').strip().lower()
    if search_by=='name':
        search_value=input("Enter the name of the contact to update: ").strip()
        cursor.execute("SELECT * FROM contacts WHERE name LIKE ?",('%'+search_value+'%',))
    elif search_by=='phone':
          search_value=input("Enter the phone number of the contact to update: ").strip()
          cursor.execute("SELECT * FROM contacts WHERE phone LIKE ?",('%'+search_value+'%',)) 
    else:
        print("invalid input, please enter the name or phone.")
        conn.close()
        return

    contact=cursor.fetchone()

    if not contact:
        print("no contact found with that information!")
        conn.close()
        return
    else:
        print(f" Contact found: name:{contact[1]}, phone number:{contact[2]}, Email:{contact[3]}, Address: {contact[4]}") 
        update_field=input(" What would you like to update? (name/phone no/email id/address): ").strip().lower()
        if update_field=='name':
            new_value=input("enter the new name: ").strip()
            cursor.execute("UPDATE contacts SET name = ? WHERE id = ?",(new_value,contact[0]))
        elif update_field=='phone':
            new_value=input("enter the new phone number: ").strip()
            cursor.execute("UPDATE contacts SET phone = ? WHERE id = ?",(new_value,contact[0]))
        elif update_field=='email':
            new_value=input("enter the new email id: ").strip()
            cursor.execute("UPDATE contacts SET email = ? WHERE id = ?",(new_value,contact[0]))
        elif update_field=='address':
            new_value=input("enter the new address: ").strip()
            cursor.execute("UPDATE contacts SET address = ? WHERE id = ?",(new_value,contact[0]))
        else:
            print("invalid field choice!")
            conn.close()
            return
    conn.commit()
    conn.close()

def delete():
    conn=sqlite3.connect('contacts.db')
    cursor=conn.cursor()

    #asking user to enter name or phone no. to delete the contact
    search_by=input('Do you want to search by name or phone number? (name/phone no.): ').strip().lower()
    if search_by=='name':
        search_value=input("Enter the name of the contact to delete: ").strip()
        cursor.execute("SELECT * FROM contacts WHERE name LIKE ?",('%'+search_value+'%',))
    elif search_by=='phone':
          search_value=input("Enter the phone number of the contact to delete: ").strip()
          cursor.execute("SELECT * FROM contacts WHERE phone LIKE ?",('%'+search_value+'%',)) 
    else:
        print("invalid input, please enter the name or phone.")
        conn.close()
        return
                
    contact=cursor.fetchone()

    if not contact:
        print("no contact found with that information!")
        conn.close()
        return
    else:
        print(f"Contact found: name:{contact[1]}, phone number:{contact[2]}, Email:{contact[3]}, Address: {contact[4]}")
        confirmation=input("Are you sure you want ot dleete this contact? (yes/no): ").strip().lower()
        if confirmation=='yes':
            cursor.execute("DELETE FROM contacts WHERE id = ?",(contact[0],))
            conn.commit()
            print(" Contact Successfully Deleted!")
        else:
            print(" Deletion cancelled!")
    conn.close()

def menu():
    while True:
        print("\n1. Add Contact")
        print("\n2. View Contact")
        print("\n3. Update Contact")
        print("\n4. Search Contact")
        print("\n5. Delete Contact")
        print("\n6.  Exit")

        choice=input("Enter your Option: ")
        if choice=='1':
            add()
        elif choice=='2':
            view()
        elif choice=='3':
            update()
        elif choice=='4':
            search()
        elif choice=='5':
            delete()
        elif choice=='6':
            print("existing.....")
            break
        else:
            print("Invalid option")  
menu()            
