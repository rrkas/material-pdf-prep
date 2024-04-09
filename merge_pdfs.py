# https://www.ilovepdf.com/merge_pdf

import sys, requests, time
from pathlib import Path
from tqdm import tqdm
from _driver import *


def merge_pdfs(dir_path: Path, out_fp: Path):
    pdf_fps = sorted(dir_path.glob("**/*.pdf"))

    if len(pdf_fps) == 0:
        raise RuntimeError(f"No PDFs found at '{dir_path}'")

    driver = get_driver("https://www.ilovepdf.com/merge_pdf")

    for fp in tqdm(pdf_fps):
        file_input_element = driver.find_element(By.TAG_NAME, "input")
        file_input_element.send_keys(str(fp))

    driver.find_element(By.ID, "orderByName").click()
    driver.find_element(By.ID, "processTask").click()

    while True:
        time.sleep(2)
        downloadURL = driver.find_element(By.ID, "pickfiles").get_attribute("href")

        if downloadURL.startswith("http"):
            print(downloadURL)
            resp = requests.get(downloadURL)
            content = resp.content

            if resp.status_code == 200:
                with open(out_fp, "wb") as f:
                    f.write(content)

                return out_fp
            else:
                raise RuntimeError(
                    f"resp.status_code: {resp.status_code} | resp.text: {resp.text}"
                )


if __name__ == "__main__":
    merge_pdfs(Path(sys.argv[1]), Path(sys.argv[2]))
