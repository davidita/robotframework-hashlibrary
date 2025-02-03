import pytest
import sys
import os
import pathlib

# Voeg het pad van de bovenliggende map toe aan sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
current_directory = pathlib.Path.cwd()

from HashLibrary.HashLibrary import HashLibrary

string_letters = "david"
string_numbers = "12345"
string_combined = "david12345"
string_diacritic = "dävid"


hash_lib = HashLibrary()

def test_base64_letters():
    hash_letters = hash_lib.get_base64_hash_from_string(string_letters)
    assert hash_letters == "ZGF2aWQ="

def test_base64_numbers():
    hash_letters = hash_lib.get_base64_hash_from_string(string_numbers)
    assert hash_letters == "MTIzNDU="

def test_base64_combined():
    hash_letters = hash_lib.get_base64_hash_from_string(string_combined)
    assert hash_letters == "ZGF2aWQxMjM0NQ=="

def test_base64_diacritic():
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

def test_md5_hash_letters():
    hash_md5 = hash_lib.get_md5_hash_from_string(string_letters)
    assert hash_md5 == "172522ec1028ab781d9dfd17eaca4427"
    print(hash_md5)

def test_md5_hash_numbers():
    hash_md5 = hash_lib.get_md5_hash_from_string(string_numbers)
    assert hash_md5 == "827ccb0eea8a706c4c34a16891f84e7b"
    print(hash_md5)

def test_md5_hash_combined():
    hash_md5 = hash_lib.get_md5_hash_from_string(string_combined)
    assert hash_md5 == "0944987d6bbf31cf3ffcd1ee0ba828b6"
    print(hash_md5)

def test_md5_hash_diacritic():
    hash_md5 = hash_lib.get_md5_hash_from_string(string_diacritic)
    assert hash_md5 == "dfaf70eb8ae4ff763918f6917eb28f2b"
    print(hash_md5)

def test_base64_file():
    hash_base64 = hash_lib.get_base64_hash_from_file(current_directory / 'utest'/ 'testfile.docx')
    print(hash_base64) 
    assert hash_base64  == "DQpMb3JlbSBpcHN1bSBkb2xvciBzaXQgYW1ldC4gUXVvIHRvdGFtIHZvbHVwdGFzIHV0IHZvbHVwdGF0ZW0gcmVwdWRpYW5kYWUgaW4gZXhwbGljYWJvIHRvdGFtIHV0IHZvbHVwdGF0ZW0gdm9sdXB0YXRlbSBzaXQgYXBlcmlhbSBlbmltIGV0IHZlbGl0IGxhYm9ydW0uIEVvcyByZXBlbGxhdCBtaW5pbWEgZXN0IHJlcnVtIHZpdGFlIHV0IFF1aXMgaGFydW0gZXN0IHNhcGllbnRlIGFsaXF1YW0gYXV0IHJlaWNpZW5kaXMgbnVtcXVhbSBxdWkgbWFnbmFtIHJhdGlvbmUuIFZlbCBtYWlvcmVzIGFwZXJpYW0gYXV0IGxhYm9ydW0gcG9zc2ltdXMgcXVvIGl0YXF1ZSBjb21tb2RpLiBWZWwgdm9sdXB0YXRlbSBkb2xvcnVtIGlkIGZ1Z2lhdCBxdWFtIGV0IHZvbHVwdGF0ZW0gdm9sdXB0YXRpYnVzIGEgZW5pbSBmYWNlcmUuDQoNCkVzdCBwZXJzcGljaWF0aXMgdm9sdXB0YXMgdXQgdG90YW0gZXhwZWRpdGEgaW4gbmVtbyBkZWJpdGlzLiBFdCBwYXJpYXR1ciBlc3NlIGF1dCBhcmNoaXRlY3RvIGxpYmVybyBlc3QgZXJyb3IgZnVnYSBxdWkgZW5pbSBibGFuZGl0aWlzIHF1aSBudWxsYSBuaWhpbCBzaXQgcG9zc2ltdXMgbmVjZXNzaXRhdGlidXMuIEV0IG1vZGkgcXVhcyB1dCBzaW50IG1vbGVzdGlhZSBldCBleGVyY2l0YXRpb25lbSBhbGlhcyBpZCBxdWlhIHZlbmlhbSBldW0gZG9sb3JlbXF1ZSBuYXR1cyBldCBvZmZpY2lpcyBlaXVzIGEgbW9sZXN0aWFlIGl0YXF1ZS4NCg0KRXN0IGxpYmVybyBmYWNpbGlzIGFiIHF1aXNxdWFtIGZ1Z2lhdCBoaWMgaWxsbyBxdW9zISBFdCBhbWV0IGRvbG9yIGV0IGl1cmUgbW9sbGl0aWEgYWQgYWxpYXMgbW9kaSBhIGFyY2hpdGVjdG8gc2ludCB2ZWwgaXBzYW0gc2ltaWxpcXVlIGV0IHN1c2NpcGl0IGFjY3VzYW50aXVtLg0K"
    print(hash_base64)

def test_sha256_file():
    hash_sha256 = hash_lib.get_sha256_hash_from_file(current_directory / 'utest'/ 'testfile.docx')
    print(hash_sha256)
    assert hash_sha256 == "8fcf7cb45c180e4390e9347af46c506668272b9eb20ece93d8ed4a445b13b0f5"
    print(hash_sha256)