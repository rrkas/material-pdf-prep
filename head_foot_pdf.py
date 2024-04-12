# https://tools.pdf24.org/en/add-page-numbers

import sys, requests, time
from pathlib import Path
from tqdm import tqdm
from _driver import *


def add_page_numbers(pdf_fp: Path, out_fp: Path):
    if not pdf_fp.exists():
        raise RuntimeError(f"File at path '{pdf_fp}' doesn't exist!")


def add_text(pdf_fp: Path, out_fp: Path, position: str, text: str):
    pass


if __name__ == "__name__":
    args = sys.argv[2:]

    if sys.argv[1] == "pgnum":
        add_page_numbers(*args)

    elif sys.argv[1] == "text":
        add_text(*args)
