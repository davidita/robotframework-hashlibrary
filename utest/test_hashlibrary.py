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

def test_crc32_hash_numbers():
    hash_crc32 = hash_lib.get_crc32_hash_from_string(string_numbers)
    assert hash_crc32 == "0xcbf53a1c"

def test_crc32_hash_combined():
    hash_crc32 = hash_lib.get_crc32_hash_from_string(string_combined)
    assert hash_crc32 == "0x9a3d48f7"

def test_crc32_hash_diacritic():
    hash_crc32 = hash_lib.get_crc32_hash_from_string(string_diacritic)
    assert hash_crc32 == "0xe08791fb"

def test_md5_hash_letters():
    hash_md5 = hash_lib.get_md5_hash_from_string(string_letters)
    assert hash_md5 == "172522ec1028ab781d9dfd17eaca4427"

def test_md5_hash_numbers():
    hash_md5 = hash_lib.get_md5_hash_from_string(string_numbers)
    assert hash_md5 == "827ccb0eea8a706c4c34a16891f84e7b"

def test_md5_hash_combined():
    hash_md5 = hash_lib.get_md5_hash_from_string(string_combined)
    assert hash_md5 == "0944987d6bbf31cf3ffcd1ee0ba828b6"

def test_md5_hash_diacritic():
    hash_md5 = hash_lib.get_md5_hash_from_string(string_diacritic)
    assert hash_md5 == "dfaf70eb8ae4ff763918f6917eb28f2b"

def test_base64_file():
    hash_base64 = hash_lib.get_base64_hash_from_file(current_directory / 'utest' / 'testfile.docx')
    assert hash_base64 == "CkxvcmVtIGlwc3VtIGRvbG9yIHNpdCBhbWV0LiBRdW8gdG90YW0gdm9sdXB0YXMgdXQgdm9sdXB0YXRlbSByZXB1ZGlhbmRhZSBpbiBleHBsaWNhYm8gdG90YW0gdXQgdm9sdXB0YXRlbSB2b2x1cHRhdGVtIHNpdCBhcGVyaWFtIGVuaW0gZXQgdmVsaXQgbGFib3J1bS4gRW9zIHJlcGVsbGF0IG1pbmltYSBlc3QgcmVydW0gdml0YWUgdXQgUXVpcyBoYXJ1bSBlc3Qgc2FwaWVudGUgYWxpcXVhbSBhdXQgcmVpY2llbmRpcyBudW1xdWFtIHF1aSBtYWduYW0gcmF0aW9uZS4gVmVsIG1haW9yZXMgYXBlcmlhbSBhdXQgbGFib3J1bSBwb3NzaW11cyBxdW8gaXRhcXVlIGNvbW1vZGkuIFZlbCB2b2x1cHRhdGVtIGRvbG9ydW0gaWQgZnVnaWF0IHF1YW0gZXQgdm9sdXB0YXRlbSB2b2x1cHRhdGlidXMgYSBlbmltIGZhY2VyZS4KCkVzdCBwZXJzcGljaWF0aXMgdm9sdXB0YXMgdXQgdG90YW0gZXhwZWRpdGEgaW4gbmVtbyBkZWJpdGlzLiBFdCBwYXJpYXR1ciBlc3NlIGF1dCBhcmNoaXRlY3RvIGxpYmVybyBlc3QgZXJyb3IgZnVnYSBxdWkgZW5pbSBibGFuZGl0aWlzIHF1aSBudWxsYSBuaWhpbCBzaXQgcG9zc2ltdXMgbmVjZXNzaXRhdGlidXMuIEV0IG1vZGkgcXVhcyB1dCBzaW50IG1vbGVzdGlhZSBldCBleGVyY2l0YXRpb25lbSBhbGlhcyBpZCBxdWlhIHZlbmlhbSBldW0gZG9sb3JlbXF1ZSBuYXR1cyBldCBvZmZpY2lpcyBlaXVzIGEgbW9sZXN0aWFlIGl0YXF1ZS4KCkVzdCBsaWJlcm8gZmFjaWxpcyBhYiBxdWlzcXVhbSBmdWdpYXQgaGljIGlsbG8gcXVvcyEgRXQgYW1ldCBkb2xvciBldCBpdXJlIG1vbGxpdGlhIGFkIGFsaWFzIG1vZGkgYSBhcmNoaXRlY3RvIHNpbnQgdmVsIGlwc2FtIHNpbWlsaXF1ZSBldCBzdXNjaXBpdCBhY2N1c2FudGl1bS4K"

def test_sha256_file():
    hash_sha256 = hash_lib.get_sha256_hash_from_file(current_directory / 'utest' / 'testfile.docx')
    assert hash_sha256 == "0a916e40c0f794cd7a37ec5d54118a242253415698b81de0c50e1b1a0675231a"

def test_md5_file():
    hash_md5 = hash_lib.get_md5_hash_from_file(current_directory / 'utest' / 'testfile.docx')
    assert hash_md5 == "342d948dbfbebb56b93792c359ae985f"

def test_crc32_file():
    hash_crc32 = hash_lib.get_crc32_hash_from_file(current_directory / 'utest' / 'testfile.docx')
    assert hash_crc32 == "0x63b0c776"

def test_base64_file_not_found():
    with pytest.raises(FileNotFoundError):
        hash_lib.get_base64_hash_from_file(current_directory / 'utest' / 'non_existent_file.txt')

def test_sha256_file_not_found():
    with pytest.raises(FileNotFoundError):
        hash_lib.get_sha256_hash_from_file(current_directory / 'utest' / 'non_existent_file.txt')

def test_md5_file_not_found():
    with pytest.raises(FileNotFoundError):
        hash_lib.get_md5_hash_from_file(current_directory / 'utest' / 'non_existent_file.txt')

def test_crc32_file_not_found():
    with pytest.raises(FileNotFoundError):
        hash_lib.get_crc32_hash_from_file(current_directory / 'utest' / 'non_existent_file.txt')