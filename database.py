import json

class DB:
    def __init__(self, path):
        self.path = path

    def normalize_name(self, name):
        return name.replace("/", "-")

    def save(self, name, data):
        filename = self.path + "/" + self.normalize_name(name)
        #logger.debug(filename)
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(data, fp)

    def load(self, name):
        filename = self.path + "/" + self.normalize_name(name)
        #logger.debug(filename)
        with open(filename, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
        return data
