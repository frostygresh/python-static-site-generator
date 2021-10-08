import Path from pathlab

class Site:
    __init__ (self, source, dest):
        self._source = Path(source)
        self._dest = Path(dest)