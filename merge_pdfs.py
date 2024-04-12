# https://www.ilovepdf.com/merge_pdf

import sys, requests, time
from pathlib import Path
from tqdm import tqdm
from _driver import *
from pypdf import PdfWriter, PdfReader


def merge_pdfs(dir_path: Path, out_fp: Path):
    pdf_fps = sorted(dir_path.glob("**/*.pdf"))

    if len(pdf_fps) == 0:
        raise RuntimeError(f"No PDFs found at '{dir_path}'")

    pdf_fps = sorted(dir_path.glob("**/*.pdf"))

    writer = PdfWriter()

    for pdf_fp in tqdm(pdf_fps):
        for page in PdfReader(pdf_fp).pages:
            writer.add_page(page)

    writer.write(out_fp)
    writer.close()
    return out_fp


if __name__ == "__main__":
    merge_pdfs(Path(sys.argv[1]), Path(sys.argv[2]))
