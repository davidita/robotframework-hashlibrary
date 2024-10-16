import base64

class HashLibrary:
    """This is a Robot Framework library to create base64 hashes from strings. This library may be updated in the future in order to provide more hashes and more input types."""

    def get_base64_hash_from_string(self, string):
        """Returns the base64 hash of the string that is supplied. 
        
        Example:
        
        | ${hash} | Get Base64 Hash From String | david |
        """
        string_in_bytes = string.encode('utf-8')
        base64_bytes = base64.b64encode(string_in_bytes)
        base64_string = base64_bytes.decode('utf-8')
        print(base64_string)
        return  base64_string
