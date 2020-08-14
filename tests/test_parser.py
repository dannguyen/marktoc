import pytest
from pathlib import Path

from marktoc.parser import Parser

@pytest.fixture
def srcpath(tmpdir):
    xdir = Path(tmpdir)
    xdir.mkdir(exist_ok=True, parents=True)
    xpath = xdir.joinpath('index.md')
    xpath.write_text("""# Hello

<!-- marktoc -->

## Lorem ipsum

### Jane Doe

## tk qc

text text""")
    return xpath

@pytest.fixture
def parsed(srcpath):
    p = Parser(srcpath)
    p.parse()
    return p


def test_init_parser(srcpath):
    p = Parser(srcpath)
    assert str(p.src_path) == str(srcpath)
    assert '# Hello' in p.lines[0]
    assert 'text text' in p.content.splitlines()[-1]
    assert len(p.lines) == len(p.content.splitlines())

def test_parsed(parsed):
    assert parsed.toc_mark_lineno is 2

def test_header_mapping(parsed):
    assert len(parsed.headers) == 4
