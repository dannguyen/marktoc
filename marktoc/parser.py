from pathlib import Path
import regex as re
from typing import List, Tuple


HEADER_PATTERN = re.compile(r'^(?P<level>#{1,6}) (?P<title>.+)$')

TOC_MARKER = '<!-- marktoc -->'

class Parser(object):
    def __init__(self, src_path:Path):
        self.src_path = Path(src_path)
        self.content = ''
        self.lines = []
        with open(self.src_path) as src:
            for line in src:
                self.content += line
                self.lines.append(line)




    def parse(self):
        self.toc_mark_lineno = parsers.find_toc_mark(self.lines)


class parsers(object):
    @staticmethod
    def find_toc_mark(lines:List[str]) -> (int, bool):
        """
        Searches for `TOC_MARKER` in `txt`, returns the line number of
            the first occurrence.

        If `TOC_MARKER` is not found, returns False

        TODO: make warning if more than one TOC is found?
        """
        for i, line in enumerate(lines):
            if TOC_MARKER in line:
                return i
        return False


    def find_headers(lines:List[str]) -> List[Tuple[int, int, str]]:
        """

        returns [(line number, heading level, title text)]
        """
        hmap = []
        for i, line in enumerate(lines):
            pass
        pass
