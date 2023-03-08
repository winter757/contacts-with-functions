import json
import csv

contacts = []

def PrintContacts():
    for contact in contacts:
            print(f"{contact['name']} {contact['surname']} {contact['number']} {contact['email']}")

def AddContact():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    number = input("Enter number: ")
    email = input("Enter email:")

    contact = {
        "name": name, 
        "surname": surname, 
        "number": number,
        "email": email
        }

    contacts.append(contact)

def SaveContacts(format):
        if format == "json":
             SaveAsJson()
        elif format == "csv":
             SaveAsCsv()
        else:
             print("File not saved. File format not defined.")

def SaveAsCsv():
    with open("contacts.csv", "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=virsraksti)
            writer.writeheader()
            writer.writerows(contacts)

def SaveAsJson():
    with open("contacts.json", "w", encoding="UTF8") as file:
        contacts_dict = {'contacts_list': contacts}
        json.dump(contacts_dict, file, indent=4)

virsraksti = ["name", "surname", "number", "email"]

def DeleteContact():
    name = input('Enter name: ')    
    found = False

    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            found = True
            break

    if found:
        print(f"Contact {name} has been deleted.")
    else:
        print(f"Contact {name} not found.")

while True:
    response = input("A - add new, P - print, D - delete, C - save as csv, E - exit: ")
    if response == "A":
         AddContact()
         SaveContacts("json")
    elif response == "C":
         SaveContacts("csv")
    elif response == "P":
         PrintContacts()
    elif response == "D":
        DeleteContact()
    elif response == "E":
        break
    else:
        print("Please enter a valid response!")
