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

def test_sha256_hash_letters():
    hash_sha256 = hash_lib.get_sha256_hash_from_string(string_letters)
    assert hash_sha256 == "07d046d5fac12b3f82daf5035b9aae86db5adc8275ebfbf05ec83005a4a8ba3e"
    print(hash_sha256)

def test_sha256_hash_numbers():
    hash_sha256 = hash_lib.get_sha256_hash_from_string(string_numbers)
    assert hash_sha256 == "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"
    print(hash_sha256)

def test_sha256_hash_combined():
    hash_sha256 = hash_lib.get_sha256_hash_from_string(string_combined)
    assert hash_sha256 == "a74ccf7b011ad204882b593076d070907a12b89b6251bd14fca52b346b01c8d2"
    print(hash_sha256)

def test_sha256_hash_diacritic():
    hash_sha256 = hash_lib.get_sha256_hash_from_string(string_diacritic)
    assert hash_sha256 == "8900f1db225e5f785a11b25263efb416432ef5327a467690a6b411706cbf3ee4"
    print(hash_sha256)