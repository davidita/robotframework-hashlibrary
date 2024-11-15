import base64
import binascii
import hashlib

class HashLibrary:
    """This is a Robot Framework library to create base64 hashes from strings.
    This library may be updated in the future in order to provide more hashes and more input types."""
    
    def get_base64_hash_from_string(self, string):
        """Returns the base64 hash of the string that is supplied.
        
        Example:
            | ${hash} | Get Base64 Hash From String | david |
        """
        string_in_bytes = string.encode('utf-8')
        base64_bytes = base64.b64encode(string_in_bytes)
        base64_string = base64_bytes.decode('utf-8')
        print(base64_string)
        return base64_string

    def get_crc32_hash_from_string(self, string):
        """Returns the crc32 hash of the string that is supplied.
        
        Example:
            | ${hash} | Get crc32 Hash From String | david |
        """
        string_in_bytes = string.encode('utf-8')
        crc32_bytes = binascii.crc32(string_in_bytes)
        return hex(crc32_bytes)

    def get_md5_hash_from_string(self, string):
        """Returns the md5 hash of the string that is supplied.
        
        Example:
            | ${hash} | Get md5 Hash From String | david |
        """
        data = string
        md5_hash = hashlib.md5()
        md5_hash.update(data.encode('utf-8'))
        hash_result = md5_hash.hexdigest()
        return(hash_result)
    
    def get_sha256_hash_from_string(self, string):
        """Returns the md5 hash of the string that is supplied.
        
        Example:
            | ${hash} | Get md5 Hash From String | david |
        """
        data = string
        sha256_hash = hashlib.sha256()
        sha256_hash.update(data.encode('utf-8'))
        hash_result = sha256_hash.hexdigest()
        return(hash_result)