import pytest
import sys
import os

# Voeg het pad van de bovenliggende map toe aan sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from HashLibrary.HashLibrary import HashLibrary

string_letters = "david"
string_numbers = "12345"
string_combined = "david12345"
string_diacritic = "dävid"

hash_lib = HashLibrary()

def test_string_letters():
    hash_letters = hash_lib.get_base64_hash_from_string(string_letters)
    assert hash_letters == "ZGF2aWQ="

def test_string_numbers():
    hash_letters = hash_lib.get_base64_hash_from_string(string_numbers)
    assert hash_letters == "MTIzNDU="

def test_string_combined():
    hash_letters = hash_lib.get_base64_hash_from_string(string_combined)
    assert hash_letters == "ZGF2aWQxMjM0NQ=="

def test_string_diacritic():
    hash_letters = hash_lib.get_base64_hash_from_string(string_diacritic)
    assert hash_letters == "ZMOkdmlk"

def test_crc32_hash_letters():
    hash_crc32 = hash_lib.get_crc32_hash_from_string(string_letters)
    assert hash_crc32 == "0x8796d7bb"
    print(hash_crc32)

def test_crc32_hash_numbers():
    hash_crc32 = hash_lib.get_crc32_hash_from_string(string_numbers)
    assert hash_crc32 == "0xcbf53a1c"
    print(hash_crc32)

def test_crc32_hash_combined():
    hash_crc32 = hash_lib.get_crc32_hash_from_string(string_combined)
    assert hash_crc32 == "0x9a3d48f7"
    print(hash_crc32)

def test_crc32_hash_diacritic():
    hash_crc32 = hash_lib.get_crc32_hash_from_string(string_diacritic)
    assert hash_crc32 == "0xe08791fb"
    print(hash_crc32)