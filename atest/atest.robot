*** Settings ***
Library    String
Library    HashLibrary

*** Variables ***
${string_letters}    david
${string_numbers}    12345
${string_combined}    david12345
${string_diacritic}    dävid

*** Test Cases ***
Base64 - String with only letters
    ${hash}    Get Base64 Hash From String    ${string_letters}
    Should Be Equal    ${hash}    ZGF2aWQ=

Base64 - String with only numbers
    ${hash}    Get Base64 Hash From String    ${string_numbers}
    Should Be Equal    ${hash}    MTIzNDU=

Base64 - String combined
    ${hash}    Get Base64 Hash From String    ${string_combined}
    Should Be Equal    ${hash}    ZGF2aWQxMjM0NQ==

Base64 - String diacritic
    ${hash}    Get Base64 Hash From String    ${string_diacritic}
    Should Be Equal    ${hash}    ZMOkdmlk

CRC-32 - String with only letters
    ${hash}    Get Crc32 Hash From String    ${string_letters}
    Should Be Equal    ${hash}    0x8796d7bb

CRC-32 - String with only numbers
    ${hash}    Get Crc32 Hash From String    ${string_numbers}
    Should Be Equal    ${hash}    0xcbf53a1c

CRC-32 - String combined
    ${hash}    Get Crc32 Hash From String    ${string_combined}
    Should Be Equal    ${hash}    0x9a3d48f7

CRC-32 - String diacritic
    ${hash}    Get Crc32 Hash From String    ${string_diacritic}
    Should Be Equal    ${hash}    0xe08791fb

MD5 - String with only letters
    ${hash}    Get md5 Hash From String    ${string_letters}
    Should Be Equal    ${hash}    172522ec1028ab781d9dfd17eaca4427

MD5 - String with only numbers
    ${hash}    Get md5 Hash From String    ${string_numbers}
    Should Be Equal    ${hash}    827ccb0eea8a706c4c34a16891f84e7b

MD5 - String combined
    ${hash}    Get md5 Hash From String    ${string_combined}
    Should Be Equal    ${hash}    0944987d6bbf31cf3ffcd1ee0ba828b6

MD5 - String diacritic
    ${hash}    Get md5 Hash From String    ${string_diacritic}
    Should Be Equal    ${hash}    dfaf70eb8ae4ff763918f6917eb28f2b

Base64 - File
    ${hash}    Get Base64 Hash From File    ${CURDIR}/testfile.docx
    Should Be Equal    ${hash}    DQpMb3JlbSBpcHN1bSBkb2xvciBzaXQgYW1ldC4gUXVvIHRvdGFtIHZvbHVwdGFzIHV0IHZvbHVwdGF0ZW0gcmVwdWRpYW5kYWUgaW4gZXhwbGljYWJvIHRvdGFtIHV0IHZvbHVwdGF0ZW0gdm9sdXB0YXRlbSBzaXQgYXBlcmlhbSBlbmltIGV0IHZlbGl0IGxhYm9ydW0uIEVvcyByZXBlbGxhdCBtaW5pbWEgZXN0IHJlcnVtIHZpdGFlIHV0IFF1aXMgaGFydW0gZXN0IHNhcGllbnRlIGFsaXF1YW0gYXV0IHJlaWNpZW5kaXMgbnVtcXVhbSBxdWkgbWFnbmFtIHJhdGlvbmUuIFZlbCBtYWlvcmVzIGFwZXJpYW0gYXV0IGxhYm9ydW0gcG9zc2ltdXMgcXVvIGl0YXF1ZSBjb21tb2RpLiBWZWwgdm9sdXB0YXRlbSBkb2xvcnVtIGlkIGZ1Z2lhdCBxdWFtIGV0IHZvbHVwdGF0ZW0gdm9sdXB0YXRpYnVzIGEgZW5pbSBmYWNlcmUuDQoNCkVzdCBwZXJzcGljaWF0aXMgdm9sdXB0YXMgdXQgdG90YW0gZXhwZWRpdGEgaW4gbmVtbyBkZWJpdGlzLiBFdCBwYXJpYXR1ciBlc3NlIGF1dCBhcmNoaXRlY3RvIGxpYmVybyBlc3QgZXJyb3IgZnVnYSBxdWkgZW5pbSBibGFuZGl0aWlzIHF1aSBudWxsYSBuaWhpbCBzaXQgcG9zc2ltdXMgbmVjZXNzaXRhdGlidXMuIEV0IG1vZGkgcXVhcyB1dCBzaW50IG1vbGVzdGlhZSBldCBleGVyY2l0YXRpb25lbSBhbGlhcyBpZCBxdWlhIHZlbmlhbSBldW0gZG9sb3JlbXF1ZSBuYXR1cyBldCBvZmZpY2lpcyBlaXVzIGEgbW9sZXN0aWFlIGl0YXF1ZS4NCg0KRXN0IGxpYmVybyBmYWNpbGlzIGFiIHF1aXNxdWFtIGZ1Z2lhdCBoaWMgaWxsbyBxdW9zISBFdCBhbWV0IGRvbG9yIGV0IGl1cmUgbW9sbGl0aWEgYWQgYWxpYXMgbW9kaSBhIGFyY2hpdGVjdG8gc2ludCB2ZWwgaXBzYW0gc2ltaWxpcXVlIGV0IHN1c2NpcGl0IGFjY3VzYW50aXVtLg0K

Sha256 - File
    ${hash}    Get Sha256 Hash From File    ${CURDIR}/testfile.docx
    Should Be Equal    ${hash}    8fcf7cb45c180e4390e9347af46c506668272b9eb20ece93d8ed4a445b13b0f5