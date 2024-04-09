# https://www.ilovepdf.com/powerpoint_to_pdf

import sys, requests, time
from pathlib import Path
from _driver import *


def convert_ppt2pdf(in_ppt_fp: Path | str, out_pdf_fp: Path | str):
    in_ppt_fp = Path(in_ppt_fp).resolve()

    if not in_ppt_fp.exists():
        raise RuntimeError(f"File at path '{in_ppt_fp}' doesn't exist!")

    out_pdf_fp = Path(out_pdf_fp).resolve()
    driver = get_driver("https://www.ilovepdf.com/powerpoint_to_pdf")

    file_input_element = driver.find_element(By.TAG_NAME, "input")
    file_input_element.send_keys(str(in_ppt_fp))

    convertToPdfBtn = driver.find_element(By.ID, "processTask")
    convertToPdfBtn.click()

    while True:
        time.sleep(2)
        downloadUrl = driver.find_element(By.ID, "pickfiles").get_attribute("href")

        if downloadUrl.startswith("http"):
            # print(downloadUrl)
            resp = requests.get(downloadUrl)
            content = resp.content

            if resp.status_code == 200:
                with open(out_pdf_fp, "wb") as f:
                    f.write(content)

                return out_pdf_fp
            else:
                raise RuntimeError(
                    f"resp.status_code: {resp.status_code} | resp.text: {resp.text}"
                )


if __name__ == "__main__":
    convert_ppt2pdf(Path(sys.argv[1]), Path(sys.argv[2]))
