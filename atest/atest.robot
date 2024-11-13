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