import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    def load(cls, string):
        fm, _, content = __regex.split(string, 2)
        load(fm, Loader = FullLoader)
        cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"]
        if self.data.has_key("type")
        else return None

    @type.setter
    def type(self, value):
        self.data["type"] = value

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return self.data.__iter__()

    def __len__(self):
        return self.data.__len__()

    def __repr__(self):
        data = directory()
        return str(data)
