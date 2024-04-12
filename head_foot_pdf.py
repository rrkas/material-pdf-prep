# https://tools.pdf24.org/en/add-page-numbers

import sys, traceback
from pathlib import Path
from _driver import *
import aspose.pdf as pdf


def add_page_numbers(
    pdf_fp: Path, out_fp: Path, position: str = "bottom-right", margin: float = 10
):
    """
    position = top/center/bottom-left/center/right
    """
    pdf_fp, out_fp = Path(pdf_fp), Path(out_fp)

    if not pdf_fp.exists():
        raise RuntimeError(f"File at path '{pdf_fp}' doesn't exist!")

    try:
        position = position.lower()
        v_pos, h_pos = position.split("-")
        assert v_pos in "top/center/bottom".split(
            "/"
        ), f"{v_pos} should be top/center/bottom"
        assert h_pos in "left/center/right".split(
            "/"
        ), f"{h_pos} should be left/center/right"

        doc = pdf.Document(str(pdf_fp))

        pages = doc.pages
        len_pages = len(pages)
        num_width = len(str(len_pages))

        for page_idx, page in enumerate(pages):
            stamp = pdf.TextStamp(
                f"{str(page_idx+1).rjust(num_width)} / {str(len_pages).rjust(num_width)}"
            )

            stamp.vertical_alignment = eval(f"pdf.VerticalAlignment.{v_pos.upper()}")
            stamp.horizontal_alignment = eval(
                f"pdf.HorizontalAlignment.{h_pos.upper()}"
            )
            if h_pos in "left,right".split(","):
                exec(f"stamp.{h_pos}_margin = {margin}")

            if v_pos in "top,bottom".split(","):
                exec(f"stamp.{v_pos}_margin = {margin}")

            page.add_stamp(stamp)

        doc.save(str(out_fp))
        return out_fp

    except Exception as e:
        print(e)
        traceback.print_exc()


def add_text(
    pdf_fp: Path,
    out_fp: Path,
    position: str = "bottom-right",
    text: str = "",
    margin: float = 10,
):
    """
    position = top/center/bottom-left/center/right
    """
    pdf_fp, out_fp = Path(pdf_fp), Path(out_fp)

    if not pdf_fp.exists():
        raise RuntimeError(f"File at path '{pdf_fp}' doesn't exist!")

    try:
        position = position.lower()
        v_pos, h_pos = position.split("-")
        assert v_pos in "top/center/bottom".split(
            "/"
        ), f"{v_pos} should be top/center/bottom"
        assert h_pos in "left/center/right".split(
            "/"
        ), f"{h_pos} should be left/center/right"

        doc = pdf.Document(str(pdf_fp))

        pages = doc.pages

        for page in pages:
            stamp = pdf.TextStamp(text)
            stamp.vertical_alignment = eval(f"pdf.VerticalAlignment.{v_pos.upper()}")
            stamp.horizontal_alignment = eval(
                f"pdf.HorizontalAlignment.{h_pos.upper()}"
            )
            if h_pos in "left,right".split(","):
                exec(f"stamp.{h_pos}_margin = {margin}")

            if v_pos in "top,bottom".split(","):
                exec(f"stamp.{v_pos}_margin = {margin}")

            page.add_stamp(stamp)

        doc.save(str(out_fp))
        return out_fp
    except Exception as e:
        print(e)
        traceback.print_exc()


if __name__ == "__main__":
    args = sys.argv[2:]

    if sys.argv[1] == "pgnum":
        add_page_numbers(*args)

    elif sys.argv[1] == "text":
        add_text(*args)
