# https://www.ilovepdf.com/powerpoint_to_pdf

import sys, requests, time
from pathlib import Path
from _driver import *
from utils import *
import platform


def convert_to_pdf(in_fp: Path | str, out_fp: Path | str):
    in_fp = Path(in_fp).resolve()

    if not in_fp.exists():
        raise RuntimeError(f"File at path '{in_fp}' doesn't exist!")

    out_fp = Path(out_fp).resolve()

    os.system(f""" unoconv -f pdf -o "{out_fp}" "{in_fp}" """)

    return out_fp


if __name__ == "__main__":
    convert_to_pdf(Path(sys.argv[1]), Path(sys.argv[2]))
