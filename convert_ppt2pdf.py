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

        downloadBtn = driver.find_element(By.ID, "pickfiles")
        downloadUrl = downloadBtn.get_attribute("href")

        if downloadUrl.startswith("http"):
            # print(downloadUrl)
            with open(out_pdf_fp, "wb") as f:
                resp = requests.get(downloadUrl)
                content = resp.content
                if resp.status_code == 200:
                    f.write(content)
                else:
                    raise RuntimeError(
                        f"resp.status_code: {resp.status_code} | resp.text: {resp.text}"
                    )

            return out_pdf_fp


if __name__ == "__main__":
    convert_ppt2pdf(Path(sys.argv[1]), Path(sys.argv[2]))
