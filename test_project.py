import pytest
import os
import sys
import csv

from project import validate_name,validate_pnum,validate_email,Contactbook


@pytest.fixture
def contactbook_instance(tmp_path):
    csv_file = tmp_path / "test_contacts.csv"
    with open(csv_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "pnum", "email"])
        writer.writeheader()
    sys.argv = ['program_name', str(csv_file)]
    return Contactbook()

def test_add_contact(contactbook_instance):
    contactbook_instance.add_contact("John Doe", "1234567890", "johndoe@example.com")
    assert len(contactbook_instance.contacts) == 1

def test_check_input(contactbook_instance):
    assert contactbook_instance.check_input("John Doe", "1234567890", "johndoe@example.com") == True
    contactbook_instance.add_contact("John Doe", "1234567890", "johndoe@example.com")
    assert contactbook_instance.check_input("John Doe", "1234567890", "johndoe@example.com") == False


def test_validate_name():
    assert validate_name("Mohamed ElMaghraby") == True
    assert validate_name("person 15") == True
    assert validate_name("Mohamed_ElMaghraby") == True
    assert validate_name("Mohamed_ElMaghraby$%^") == True

def test_validate_pnum():
    assert validate_pnum("01098434040") == True
    assert validate_pnum("0119843404") == False
    assert validate_pnum("01298434040") == True
    assert validate_pnum("01$984am040") == False
def test_validate_email():
    assert validate_email("mohamed@gmail.com") == True
    assert validate_email("mohamed@gmail") == False
    assert validate_email("@gmail.com") == False


