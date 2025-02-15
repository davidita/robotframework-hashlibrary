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
    Should Be Equal    ${hash}    CkxvcmVtIGlwc3VtIGRvbG9yIHNpdCBhbWV0LiBRdW8gdG90YW0gdm9sdXB0YXMgdXQgdm9sdXB0YXRlbSByZXB1ZGlhbmRhZSBpbiBleHBsaWNhYm8gdG90YW0gdXQgdm9sdXB0YXRlbSB2b2x1cHRhdGVtIHNpdCBhcGVyaWFtIGVuaW0gZXQgdmVsaXQgbGFib3J1bS4gRW9zIHJlcGVsbGF0IG1pbmltYSBlc3QgcmVydW0gdml0YWUgdXQgUXVpcyBoYXJ1bSBlc3Qgc2FwaWVudGUgYWxpcXVhbSBhdXQgcmVpY2llbmRpcyBudW1xdWFtIHF1aSBtYWduYW0gcmF0aW9uZS4gVmVsIG1haW9yZXMgYXBlcmlhbSBhdXQgbGFib3J1bSBwb3NzaW11cyBxdW8gaXRhcXVlIGNvbW1vZGkuIFZlbCB2b2x1cHRhdGVtIGRvbG9ydW0gaWQgZnVnaWF0IHF1YW0gZXQgdm9sdXB0YXRlbSB2b2x1cHRhdGlidXMgYSBlbmltIGZhY2VyZS4KCkVzdCBwZXJzcGljaWF0aXMgdm9sdXB0YXMgdXQgdG90YW0gZXhwZWRpdGEgaW4gbmVtbyBkZWJpdGlzLiBFdCBwYXJpYXR1ciBlc3NlIGF1dCBhcmNoaXRlY3RvIGxpYmVybyBlc3QgZXJyb3IgZnVnYSBxdWkgZW5pbSBibGFuZGl0aWlzIHF1aSBudWxsYSBuaWhpbCBzaXQgcG9zc2ltdXMgbmVjZXNzaXRhdGlidXMuIEV0IG1vZGkgcXVhcyB1dCBzaW50IG1vbGVzdGlhZSBldCBleGVyY2l0YXRpb25lbSBhbGlhcyBpZCBxdWlhIHZlbmlhbSBldW0gZG9sb3JlbXF1ZSBuYXR1cyBldCBvZmZpY2lpcyBlaXVzIGEgbW9sZXN0aWFlIGl0YXF1ZS4KCkVzdCBsaWJlcm8gZmFjaWxpcyBhYiBxdWlzcXVhbSBmdWdpYXQgaGljIGlsbG8gcXVvcyEgRXQgYW1ldCBkb2xvciBldCBpdXJlIG1vbGxpdGlhIGFkIGFsaWFzIG1vZGkgYSBhcmNoaXRlY3RvIHNpbnQgdmVsIGlwc2FtIHNpbWlsaXF1ZSBldCBzdXNjaXBpdCBhY2N1c2FudGl1bS4K

Sha256 - File
    ${hash}    Get Sha256 Hash From File    ${CURDIR}/testfile.docx
    Should Be Equal    ${hash}    0a916e40c0f794cd7a37ec5d54118a242253415698b81de0c50e1b1a0675231a

MD5 - File
    ${hash}    Get md5 Hash From File    ${CURDIR}/testfile.docx
    Should Be Equal    ${hash}    342d948dbfbebb56b93792c359ae985f

CRC-32 - File
    ${hash}    Get Crc32 Hash From File    ${CURDIR}/testfile.docx
    Should Be Equal    ${hash}    0x63b0c776

Base64 - File Not Found
    [Documentation]    Test for FileNotFoundError when file is not found
    Run Keyword And Expect Error    FileNotFoundError: File not found: ${CURDIR}/non_existent_file.txt    Get Base64 Hash From File    ${CURDIR}/non_existent_file.txt

Sha256 - File Not Found
    [Documentation]    Test for FileNotFoundError when file is not found
    Run Keyword And Expect Error    FileNotFoundError: File not found: ${CURDIR}/non_existent_file.txt    Get Sha256 Hash From File    ${CURDIR}/non_existent_file.txt

MD5 - File Not Found
    [Documentation]    Test for FileNotFoundError when file is not found
    Run Keyword And Expect Error    FileNotFoundError: File not found: ${CURDIR}/non_existent_file.txt    Get md5 Hash From File    ${CURDIR}/non_existent_file.txt

CRC-32 - File Not Found
    [Documentation]    Test for FileNotFoundError when file is not found
    Run Keyword And Expect Error    FileNotFoundError: File not found: ${CURDIR}/non_existent_file.txt    Get Crc32 Hash From File    ${CURDIR}/non_existent_file.txt