import sys
import csv
import validators
import re
from tabulate import tabulate
import os.path

class Contact:
    def __init__(self, name, pnum, email):
        self._name = name
        self._pnum = pnum
        self._email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def pnum(self):
        return self._pnum

    @pnum.setter
    def pnum(self, pnum):
        self._pnum = pnum

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def to_dict(self):
        entry = {"name": self.name, "pnum": self.pnum, "email": self.email}
        return entry


class Contactbook:
    def __init__(self):
        self.contacts = []
        if os.path.isfile(sys.argv[1]) == True:
            self.update_list()
        else:
            with open(sys.argv[1], "a") as file:
                writer = csv.DictWriter(file, fieldnames=["name", "pnum", "email"])
                writer.writeheader()

    def update_list(self):
        self.contacts.clear()
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                contact = Contact(row["name"], row["pnum"], row["email"])
                self.contacts.append(contact)

    def write_to_file(self):
        with open(sys.argv[1], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "pnum", "email"])
            writer.writeheader()
            for c in self.contacts:
                writer.writerow(c.to_dict())

    def add_contact(self, name, pnum, email):
        if self.check_input(name, pnum, email):
            contact = Contact(name, pnum, email)
            self.contacts.append(contact)
            with open(sys.argv[1], "a") as file:
                writer = csv.DictWriter(file, fieldnames=["name", "pnum", "email"])
                writer.writerow(contact.to_dict())
        else:
            print("Name, phone number, or email is already used")

    def check_input(self, name, pnum, email):
        for c in self.contacts:
            if c.name == name or c.pnum == pnum or c.email == email:
                return False
            else:
                return True
        return True

    def update_contact(self):
        change = input("Name: ")
        for c in self.contacts:
            if c.name == change:
                c.name = input("Enter new name: ")
                c.pnum = input("Enter new Phone number: ")
                c.email = input("Enter new Email: ")
        self.write_to_file()

    def search_contact(self):
        search = input("Enter name or email or phone number of the contact: ").strip()
        for c in self.contacts:
            if c.name == search or c.pnum == search or c.email == search:
                return {"name": c.name, "pnum": c.pnum, "email": c.email}
        return "Contact not found"

    def delete_contact(self):
        search = input("Enter the name of a contact to delete: ").strip()
        if search == "name" or search == "pnum" or search == "email":
            print("Invalid input")
            return
        for c in self.contacts:
            if c.name == search or c.pnum == search or c.email == search:
                self.contacts.remove(c)
        self.write_to_file()


def main():
    if len(sys.argv) != 2:
        sys.exit("Invalid number of arguments")
    if sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a CSV file")

    else:
        choices()


def choices():
    contactbook = Contactbook()
    while True:
        try:
            print(
                "1. Add a Contact\n2. Search for a Contact\n3. Update a Contact\n4. Delete a Contact\n5. Display All Contacts\n6. Quit"
            )
            try:
                choice = int(input("Select an option: "))
                match choice:
                    case 1:
                        name = input("Name: ").strip()
                        pnum = input("Phone number: ").strip()
                        email = input("Email: ").strip()
                        if (
                            validate_email(email) == False
                            or validate_pnum(pnum) == False
                            or validate_name(name) == False
                        ):
                            print("\nInvalid input entered. Try again!\n")
                            continue
                        contactbook.add_contact(name, pnum, email)
                    case 2:
                        table = []
                        result = contactbook.search_contact()
                        table.append(result)
                        print(tabulate(table, headers="keys", tablefmt="grid"))

                    case 3:
                        contactbook.update_contact()

                    case 4:
                        contactbook.delete_contact()

                    case 5:
                        table = []
                        with open(sys.argv[1]) as file:
                            reader = csv.DictReader(file)
                            for row in reader:
                                table.append(row)
                        print(tabulate(table, headers="keys", tablefmt="grid"))
                    case 6:
                        sys.exit("Exiting..")

                    case _:
                        print("\nInvalid option entered, try again\n")
                        continue
            except ValueError:
                sys.exit("\nInvalid input: Please enter an integer\n")
        except EOFError:
            sys.exit("Exiting...")


def validate_name(name):
    if re.search(r"(\w+ ?)+", name):
        return True
    else:
        return False


def validate_pnum(pnum):
    if re.search(r"(010|011|012|015)\d{8}", pnum):
        return True
    else:
        return False


def validate_email(email):
    if validators.email(email):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
