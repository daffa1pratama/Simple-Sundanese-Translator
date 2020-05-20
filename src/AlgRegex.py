# Import Library
import re

# Regular Expression String Matching Algorithm
class AlgRegex :
    # Constructor
    def __init__(self) :
        pass

    # Match Function
    # Match pattern with text with Regex algorithm
    def match(self, text, pattern) :
        x = re.search(pattern, text)
        if (x != None) :
            return x.start()
        return -1