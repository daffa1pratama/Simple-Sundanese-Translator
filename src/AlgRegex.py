import re

class AlgRegex :
    def __init__(self) :
        pass

    def match(self, text, pattern) :
        x = re.search(pattern, text)
        if (x != None) :
            return x.start()
        return -1