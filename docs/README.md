# HashLibrary for Robot Framework®

HashLibrary is a library for Robot Framework that provides methods to generate various hashes from strings and files. It supports base64, crc32, md5, and sha256 hashes.

---

## Installation

If you already have Python >= 3.8 with pip installed, you can simply run:

```sh
pip install robotframework-hashlibrary
```

---

## Getting started

Here are some examples of how to import and use the library.

### Importing the Library

```robotframework
*** Settings ***
Library            HashLibrary
```

### Variables

```robotframework
*** Variables ***
${TEST_STRING}    david
${TEST_FILE}      path/to/file.txt
```

### Test Cases

#### Generate Base64 Hash for String

```robotframework
*** Test Cases ***
Generate Base64 Hash for String
    ${hash}    Get Base64 Hash From String    ${TEST_STRING}
    Should Be Equal    ${hash}    ZGF2aWQ=
```

#### Generate CRC32 Hash for String

```robotframework
*** Test Cases ***
Generate CRC32 Hash for String
    ${hash}    Get Crc32 Hash From String    ${TEST_STRING}
    Should Be Equal    ${hash}    0x8796d7bb
```

#### Generate MD5 Hash for String

```robotframework
*** Test Cases ***
Generate MD5 Hash for String
    ${hash}    Get md5 Hash From String    ${TEST_STRING}
    Should Be Equal    ${hash}    172522ec1028ab781d9dfd17eaca4427
```

#### Generate SHA256 Hash for File

```robotframework
*** Test Cases ***
Generate SHA256 Hash for File
    ${hash}    Get Sha256 Hash From File    ${TEST_FILE}
    Should Be Equal    ${hash}    <expected_sha256_hash>
```

#### Generate Base64 Hash for File

```robotframework
*** Test Cases ***
Generate Base64 Hash for File
    ${hash}    Get Base64 Hash From File    ${TEST_FILE}
    Should Be Equal    ${hash}    <expected_base64_hash>
```

#### Generate CRC32 Hash for File

```robotframework
*** Test Cases ***
Generate CRC32 Hash for File
    ${hash}    Get Crc32 Hash From File    ${TEST_FILE}
    Should Be Equal    ${hash}    <expected_crc32_hash>
```

#### Generate MD5 Hash for File

```robotframework
*** Test Cases ***
Generate MD5 Hash for File
    ${hash}    Get md5 Hash From File    ${TEST_FILE}
    Should Be Equal    ${hash}    <expected_md5_hash>
```

---

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome all contributions!