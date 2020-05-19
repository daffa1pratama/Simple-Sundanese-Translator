class Parser:
    def __init__(self):
        self.delim = ['?', ',', '.', ';', '/']

    def parse(self, text):
        text_container = text.split(' ')
        new_container = []
        i = 0
        for txt in text_container:
            found = False
            for t in self.delim:
                if t in txt:
                    found = True
                    break
            if found:
                new_container.append(txt.strip(t))
                new_container.append(t)
            else:
                new_container.append(txt)
            i += 1
        return new_container
