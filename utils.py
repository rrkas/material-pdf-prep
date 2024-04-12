import requests
from pathlib import Path


def download(url: str, fp: Path):
    resp = requests.get(url)
    content = resp.content

    if resp.status_code == 200:
        with open(fp, "wb") as f:
            f.write(content)

        return fp
    else:
        raise RuntimeError(
            f"resp.status_code: {resp.status_code} | resp.text: {resp.text}"
        )
