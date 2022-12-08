from typing import List
from pathlib import Path
import shutil

class Parser:
    def __init__(self):
        #'extensions' is a list of strings
        self.extensions : List[str] = []    #type: List[str]

    def valid_extension(self, extension):
        return extension in  self.extensions

    def parse(self, path, source, dest):
        #'path' is a Path
        #'source' is a Path
        #'dest' is a Path
        raise NotImplementedError

    def read(self, path):
        with open(path) as file:
            return file.read()

    def write(self, path, dest, content, ext = ".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))

class ResourceParser(Parser):
    def __init__(self):
        self.extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path, source, dest):
        self.copy(path, source, dest)
