import Path from pathlib

class Site:
    def __init__(self, source, dest):
        self._source = Path(source)
        self._dest = Path(dest)

    def create_dir(self, path):
        directory = self._dest / reletive_to(self._source)
        directory.mkdir(parents = True, exsit_ok = True)

    def build(self):
        self._dest.mkdir(parents = True, exsit_ok = True)
        for path in self._source.rglob("*"):
            if path.isdir():
                create_dir(path)
