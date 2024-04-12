import warnings

warnings.filterwarnings("ignore")

import sys, requests, time
from pathlib import Path
from tqdm import tqdm
import fitz


def merge_pdfs(dir_path: Path, out_fp: Path):
    pdf_fps = sorted(dir_path.glob("**/*.pdf"))

    if len(pdf_fps) == 0:
        raise RuntimeError(f"No PDFs found at '{dir_path}'")

    pdf_fps = sorted(dir_path.glob("**/*.pdf"))

    pdf_writer = fitz.open()

    for pdf_fp in tqdm(pdf_fps):
        pdf_reader = fitz.open(pdf_fp)
        pdf_writer.insert_pdf(pdf_reader)
        pdf_reader.close()

    pdf_writer.save(out_fp)
    pdf_writer.close()

    return out_fp


if __name__ == "__main__":
    merge_pdfs(Path(sys.argv[1]), Path(sys.argv[2]))
