import sys, traceback
from pathlib import Path
import fitz


def get_text_xy(
    page: fitz.Page,
    pos: tuple,
    margin: float,
    text: str,
    font_size: float,
):
    v_pos, h_pos = pos

    page_w, page_h = page.rect[2], page.rect[3]

    text_x, text_y = None, None
    if v_pos == "top":
        text_y = margin * 2
    elif v_pos == "center":
        text_y = page_h / 2 - margin
    else:
        text_y = page_h - 2 * margin

    if h_pos == "left":
        text_x = margin
    elif h_pos == "center":
        text_x = (page_w - len(text)) / 2
    else:
        text_x = page_w - margin - (len(text) + 5) * 5 * (font_size / 10)
        # print(text, len(text), text_x, page_w)

    return text_x, text_y


def add_page_numbers(
    pdf_fp: Path,
    out_fp: Path,
    position: str = "bottom-right",
    margin: float = 10,
    font_size: float = 10,
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

        pdf_document: fitz.Document = fitz.open(str(pdf_fp))

        for page_num in range(len(pdf_document)):
            page: fitz.Page = pdf_document[page_num]
            text = f"{page_num + 1} / {len(pdf_document)}"

            text_x, text_y = get_text_xy(page, (v_pos, h_pos), margin, text, font_size)

            page.insert_text(
                (text_x, text_y),
                text,
                fontsize=font_size,
                color=(0, 0, 0),
            )

        # Save the modified PDF to the output file
        pdf_document.save(str(out_fp))
        pdf_document.close()

        return out_fp

    except Exception as e:
        print(e)
        traceback.print_exc()


def add_head_foot_text(
    pdf_fp: Path,
    out_fp: Path,
    position: str = "bottom-right",
    text: str = "",
    margin: float = 10,
    font_size: float = 10,
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

        pdf_document: fitz.Document = fitz.open(str(pdf_fp))

        for page_num in range(len(pdf_document)):
            page: fitz.Page = pdf_document[page_num]

            text_x, text_y = get_text_xy(page, (v_pos, h_pos), margin, text, font_size)

            page.insert_text(
                (text_x, text_y),
                text,
                fontsize=font_size,
                color=(0, 0, 0),
            )

        # Save the modified PDF to the output file
        pdf_document.save(str(out_fp))
        pdf_document.close()

        return out_fp
    except Exception as e:
        print(e)
        traceback.print_exc()


if __name__ == "__main__":
    args = sys.argv[2:]

    if sys.argv[1] == "pgnum":
        add_page_numbers(*args)

    elif sys.argv[1] == "text":
        add_head_foot_text(*args)
