class slidemd_parser(object):
    def __init__(self, filename):
        self.filename = filename
        self.parse()

    def parse(self):
        with open(self.filename, 'r') as f:
            for line in f:
                
