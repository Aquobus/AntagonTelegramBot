import os
import yaml

class YamlFile:
    def __init__(self):
        self.base_dir = os.path.abspath(__file__)
        self.file = self.get_file(self.base_dir)
        self.body = yaml.load(self.file)

    def get_file(self, path: str):
        for file in os.listdir(path):
            if file.endswith(".yml"):
                return file
            else:
                self.create_file()

    def create_file(self, path: str):
        yaml.dump(
            {
                "token": "7513113461:AAFMBqJ4HxNbMvOny3NUuArFX2BPhB2jsdM"
            }
        )