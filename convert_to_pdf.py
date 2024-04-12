import sys, os
from pathlib import Path
from utils import *


def convert_to_pdf(in_fp: Path | str, out_fp: Path | str):
    in_fp = Path(in_fp).resolve()

    if not in_fp.exists():
        raise RuntimeError(f"File at path '{in_fp}' doesn't exist!")

    out_fp = Path(out_fp).resolve()

    os.system(
        f""" python -W ignore /usr/local/bin/unoconv -f pdf -o "{out_fp}" "{in_fp}" """
    )

    return out_fp


if __name__ == "__main__":
    convert_to_pdf(Path(sys.argv[1]), Path(sys.argv[2]))
