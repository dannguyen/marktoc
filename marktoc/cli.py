#!/usr/bin/env python3
import click
from pathlib import Path
import regex as re
from typing import NoReturn, List

from marktoc.mylog import mylogger
from marktok.parser import Parser




@click.group()
def main():
    """
    Welcome to marktoc
    """
    pass

@main.command()
def foo():
    """
    foo this is for foos!
    """
    mylogger.info("Welcome to writhub – a test")
    mylogger.debug("A debug message")
    mylogger.info("Info for you")
    mylogger.warning("Warning for this")
    mylogger.critical("Critical oops")
    mylogger.error("An error appears!")

    def _fubar(txt:str) -> int:
        val = len(str(txt))
        print("You gave me", txt, 'but i give you', val)
        return val

    _fubar(9)


@main.command()
@click.argument("src-path", nargs=1, type=click.Path(exists=True, dir_okay=False))
# @click.option("--output-path", "-o", type=click.Path(file_okay=True, dir_okay=True), default=None)
def go(src_path:click.Path):
    """
    Reads `src_path`, ostensibly a Markdown file, and re-generates the Markdown content
        with a TOC and hyperlinks
    """

    src_path = Path(src_path)
    mylogger.debug(f"Processing {src_path}")

    soup = Parser(src_path)





if __name__ == '__main__':
    main()
