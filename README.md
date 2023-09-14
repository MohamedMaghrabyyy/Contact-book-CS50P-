
---

# Contact Book

## Description:

1. This project is a console app with a simple command line interface that allows the user to store and fetch his contacts' information to/from a csv file.
2. I utilized various topics and paradigms that I studied in CS50P, including OOP, regular expressions, file I/O, looping, and exceptions.
3. The biggest challenge I faced was that most of the output is written and fetched from .csv files, so not all of the functions are testable with pytest.

## Installation:

Libraries that require installations are Validators, pytest, and tabulate. Validators are utilized to ensure that the email entered by the user is in a valid email format; pytest is used in testing, and tabulate is used to fetch the required contacts in a table to be more readable.

Commands required:

```bash
pip install validators
pip install pytest
pip install tabulate
```

## How to Use the Project:

1. User should pass the name of a csv file to be read from; a new file with the same name is created if it doesn't exist.
2. Then, the user is prompted to select the required functionality.
3. Then the user proceeds with the functionality until it finishes then they're reprompted until `(quit)` is selected or EOF is entered.

Functions:

- `choices()`: Forms the main body of the implementation, such that; all the options and exceptions are included in this function.
- `validate_name()`: Utilizes a custom-made regular expression that verifies that a user entered a valid name. If `False` is returned, the main loop in `choice()` is continued.
- `validate_pnum()`: Utilizes a custom-made regular expression that verifies that a user entered a valid phone number according to Egypt's telephone systems (it will need to be changed in other cases). If `False` is returned, the main loop in `choice()` is continued.
- `validate_email()`: Utilizes the function `email` from the validators library and returns `True` if the format is valid.
- `class Contact`: Has attributes name, phone number, and email which the user will enter the contact's information in. It has setters, getters, and `to_dict()`: which converts the attributes of a contact object to a dictionary, which will then be used to make a list of dictionaries including all the contacts.
- `class Contactbook`: This class's main objective is to collect the contact objects in a single list of dictionaries on which the classes' functions will be carried out. In the constructor, the entered file in command line will be checked if it exists. If it does then all the contacts will read from it and appended to the list of contact objects using `update_list()`, else, keys/headers will first be printed in the first line of the CSV file before any contact is added to make the fields more obvious.
- `add_contact()`: In this function, the input is first checked that it doesn't already exist in a contact using `check_input()`; then, a new contact object is created using the data entered, and that object is appended to the contact list and written into the CSV file.
- `update_contact()`: The user is prompted for the contact's name then if it's found, the user is prompted again for that contact's new name, phone number, and email. Then, the new updated list of contacts overwrites the old entries in the CSV file.
- `search_contact()`: The user is prompted to enter a contact's name, phone number, or email; then, the function searches for this contact and prints it in a table using the tabulate library.
- `delete_contact()`: The user is prompted to enter a contact's name; then, this contact is searched for then removed from the contact list. Next, the new updated list of contacts overwrites the old entries in the CSV file.
