*** Settings ***
Library    String
Library    HashLibrary

*** Variables ***
${string_letters}    david
${string_numbers}    12345
${string_combined}    david12345
${string_diacritic}    dävid

*** Test Cases ***
String with only letters
    ${hash}    Get Base64 Hash From String    ${string_letters}
    Should Be Equal    ${hash}    ZGF2aWQ=

String with only numbers
    ${hash}    Get Base64 Hash From String    ${string_numbers}
    Should Be Equal    ${hash}    MTIzNDU=

String combined
    ${hash}    Get Base64 Hash From String    ${string_combined}
    Should Be Equal    ${hash}    ZGF2aWQxMjM0NQ==

String diacritic
    ${hash}    Get Base64 Hash From String    ${string_diacritic}
    Should Be Equal    ${hash}    ZMOkdmlk
