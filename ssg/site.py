from pathlib import Path

class Site:
    def __init__ (self, source, dest):
        self._source = Path(source)
        self._dest = Path(dest)

    def create_dir (self, path):
        directory = ''