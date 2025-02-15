import base64
import binascii
import hashlib

class HashLibrary:
    """This is a Robot Framework library to create various hashes from strings and files.
    This library provides methods to generate base64, crc32, md5, and sha256 hashes.
    """

    def get_base64_hash_from_string(self, string):
        """Returns the base64 hash of the string that is supplied.
        
        The input string is encoded to bytes using UTF-8 encoding, then it is
        base64 encoded and returned as a string.
        
        Example:
            | ${hash} | Get Base64 Hash From String | david |
            | Should Be Equal | ${hash} | ZGF2aWQ= |
        
        Arguments:
            - string: The input string to be hashed.
        
        Returns:
            - The base64 encoded hash of the input string.
        """
        string_in_bytes = string.encode('utf-8')
        base64_bytes = base64.b64encode(string_in_bytes)
        base64_string = base64_bytes.decode('utf-8')
        return base64_string

    def get_crc32_hash_from_string(self, string):
        """Returns the crc32 hash of the string that is supplied.
        
        The input string is encoded to bytes using UTF-8 encoding, then it is
        hashed using the crc32 algorithm and returned as a hexadecimal string.
        
        Example:
            | ${hash} | Get Crc32 Hash From String | david |
            | Should Be Equal | ${hash} | 0x8796d7bb |
        
        Arguments:
            - string: The input string to be hashed.
        
        Returns:
            - The crc32 hash of the input string as a hexadecimal string.
        """
        string_in_bytes = string.encode('utf-8')
        crc32_bytes = binascii.crc32(string_in_bytes)
        return hex(crc32_bytes)

    def get_md5_hash_from_string(self, string):
        """Returns the md5 hash of the string that is supplied. 
        
        The input string is encoded to bytes using UTF-8 encoding, then it is
        hashed using the md5 algorithm and returned as a hexadecimal string.
        
        Example:
            | ${hash} | Get md5 Hash From String | david |
            | Should Be Equal | ${hash} | 172522ec1028ab781d9dfd17eaca4427 |
        
        Arguments:
            - string: The input string to be hashed.
        
        Returns:
            - The md5 hash of the input string as a hexadecimal string.
        """
        data = string
        md5_hash = hashlib.md5()
        md5_hash.update(data.encode('utf-8'))
        hash_result = md5_hash.hexdigest()
        return hash_result
    
    def get_base64_hash_from_file(self, file_path):
        """Returns the base64 hash of the file that is supplied.
        
        The file is read in binary mode in chunks of 8KB, then its contents are
        base64 encoded and returned as a string.
        
        Example:
            | ${hash} | Get Base64 Hash From File | path/to/file.txt |
            | Should Be Equal | ${hash} | <expected_base64_hash> |
        
        Arguments:
            - file_path: The path to the file to be hashed.
        
        Returns:
            - The base64 encoded hash of the file contents.
        
        Raises:
            - FileNotFoundError: If the file at the specified path does not exist.
            - Exception: If any other error occurs while reading the file.
        """
        try:
            base64_encoded = base64.b64encode(b'')
            with open(file_path, 'rb') as file:
                while chunk := file.read(8192):
                    base64_encoded += base64.b64encode(chunk)
            return base64_encoded.decode('utf-8')
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")
        
    def get_sha256_hash_from_file(self, file_path):
        """Returns the sha256 hash of the file that is supplied.
        
        The file is read in binary mode in chunks of 8KB, then its contents are
        hashed using the sha256 algorithm and returned as a hexadecimal string.
        
        Example:
            | ${hash} | Get sha256 Hash From File | path/to/file.txt |
            | Should Be Equal | ${hash} | <expected_sha256_hash> |
        
        Arguments:
            - file_path: The path to the file to be hashed.
        
        Returns:
            - The sha256 hash of the file contents as a hexadecimal string.
        
        Raises:
            - FileNotFoundError: If the file at the specified path does not exist.
            - Exception: If any other error occurs while reading the file.
        """
        sha256 = hashlib.sha256()
    
        try:
            with open(file_path, "rb") as f:
                while chunk := f.read(8192):  # Read file in chunks of 8kb
                    sha256.update(chunk)
            return sha256.hexdigest()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")
    
    def get_md5_hash_from_file(self, file_path):
        """Returns the md5 hash of the file that is supplied.
        
        The file is read in binary mode in chunks of 8KB, then its contents are
        hashed using the md5 algorithm and returned as a hexadecimal string.
        
        Example:
            | ${hash} | Get md5 Hash From File | path/to/file.txt |
            | Should Be Equal | ${hash} | <expected_md5_hash> |
        
        Arguments:
            - file_path: The path to the file to be hashed.
        
        Returns:
            - The md5 hash of the file contents as a hexadecimal string.
        
        Raises:
            - FileNotFoundError: If the file at the specified path does not exist.
            - Exception: If any other error occurs while reading the file.
        """
        md5 = hashlib.md5()
    
        try:
            with open(file_path, "rb") as f:
                while chunk := f.read(8192):  # Read file in chunks of 8kb
                    md5.update(chunk)
            return md5.hexdigest()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")
    
    def get_crc32_hash_from_file(self, file_path):
        """Returns the crc32 hash of the file that is supplied.
        
        The file is read in binary mode in chunks of 8KB, then its contents are
        hashed using the crc32 algorithm and returned as a hexadecimal string.
        
        Example:
            | ${hash} | Get Crc32 Hash From File | path/to/file.txt |
            | Should Be Equal | ${hash} | <expected_crc32_hash> |
        
        Arguments:
            - file_path: The path to the file to be hashed.
        
        Returns:
            - The crc32 hash of the file contents as a hexadecimal string.
        
        Raises:
            - FileNotFoundError: If the file at the specified path does not exist.
            - Exception: If any other error occurs while reading the file.
        """
        crc32 = 0
    
        try:
            with open(file_path, "rb") as f:
                while chunk := f.read(8192):  # Read file in chunks of 8kb
                    crc32 = binascii.crc32(chunk, crc32)
            return hex(crc32 & 0xFFFFFFFF)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")