import pytest
import sys
import os

# Voeg het pad van de bovenliggende map toe aan sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#from HashLibrary.HashLibrary import HashLibrary
from HashLibrary import HashLibrary

string_letters = "david"
string_numbers = "12345"
string_combined = "david12345"
string_diacritic = "dävid"

hash_lib = HashLibrary()

def test_string_letters():
    hash_letters = hash_lib.get_base64_hash_from_string(string_letters)
    hash_letters == "ZGF2aWQ="

def test_string_numbers():
    hash_letters = hash_lib.get_base64_hash_from_string(string_numbers)
    hash_letters == "MTIzNDU=="

def test_string_combined():
    hash_letters = hash_lib.get_base64_hash_from_string(string_combined)
    hash_letters == "ZGF2aWQxMjM0NQ=="

def test_string_diacritic():
    hash_letters = hash_lib.get_base64_hash_from_string(string_diacritic)
    hash_letters == "ZMOkdmlk"
