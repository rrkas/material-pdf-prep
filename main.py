import warnings

warnings.filterwarnings("ignore")

from convert_to_pdf import *
from head_foot_pdf import *
from merge_pdfs import *
from many2one_page import *

import argparse, uuid, shutil, datetime


parser = argparse.ArgumentParser()
parser.add_argument("--dir", "-d", dest="dir_path", required=True)
parser.add_argument("--fname-pos", "-fnp", dest="fname_pos", default="top-right")
parser.add_argument("--pgnum-pos", "-pnp", dest="pgnum_pos", default="bottom-center")
parser.add_argument("--output", "-o", dest="output_fp", required=True)
args = parser.parse_args()

dir_path: Path = Path(args.dir_path)
fname_pos: str = args.fname_pos
pgnum_pos: str = args.pgnum_pos
output_fp: Path = Path(args.output_fp)

TEMP_DIR = Path("./temp")
os.makedirs(TEMP_DIR, exist_ok=True)

# JOB_DIR = TEMP_DIR / str(uuid.uuid4())
JOB_DIR = TEMP_DIR / "testing"

###############################################
#     stage 1 - convert files to PDF
###############################################

print("Stage 1 started =============", flush=True)
s1_start = datetime.datetime.now()

STAGE1_DIR = JOB_DIR / "all_pdfs"
os.makedirs(STAGE1_DIR, exist_ok=True)

files = sorted(dir_path.glob("**/*.*"))
f_w = len(str(len(files)))
for fp_idx, fp in tqdm(enumerate(files), total=len(files)):
    fname = ".".join(fp.name.split(".")[:-1])

    if any([fp.name.endswith(e) for e in [".pdf", ".PDF"]]):
        shutil.copy(fp, STAGE1_DIR / f"{str(fp_idx+1).zfill(f_w)}__{fp.name}")
    else:
        print(
            f""" "{fp}" ==> """.lstrip()
            + f""" "{STAGE1_DIR / f"{str(fp_idx+1).zfill(f_w)}__{fname}.pdf"}" """.strip()
        )
        convert_to_pdf(fp, STAGE1_DIR / f"{str(fp_idx+1).zfill(f_w)}__{fname}.pdf")

s1_end = datetime.datetime.now()
print("Stage 1 ended =============", (s1_end - s1_start).total_seconds(), flush=True)

###############################################
#     stage 2 - header filenames in files
###############################################

print("Stage 2 started =============", flush=True)
s2_start = datetime.datetime.now()

STAGE2_DIR = JOB_DIR / "headed_pdfs"
os.makedirs(STAGE2_DIR, exist_ok=True)

for fp in tqdm(sorted(STAGE1_DIR.glob("**/*.*"))):
    fname = "_".join(fp.name.split(".")[:-1])
    add_head_foot_text(fp, STAGE2_DIR / fp.name, fname_pos, fname, font_size=12)

s2_end = datetime.datetime.now()
print("Stage 2 ended =============", (s2_end - s2_start).total_seconds(), flush=True)

###############################################
#     stage 3 - merge all pdfs
###############################################

print("Stage 3 started =============", flush=True)
s3_start = datetime.datetime.now()

STAGE3_FP = JOB_DIR / "combined.pdf"
merge_pdfs(STAGE2_DIR, STAGE3_FP)

s3_end = datetime.datetime.now()
print("Stage 3 ended =============", (s3_end - s3_start).total_seconds(), flush=True)

###############################################
#     stage 4 - page num merged pdf
###############################################

print("Stage 4 started =============", flush=True)
s4_start = datetime.datetime.now()

STAGE4_FP = JOB_DIR / "combined.pgnum.pdf"
add_page_numbers(STAGE3_FP, STAGE4_FP, pgnum_pos, 5)

s4_end = datetime.datetime.now()
print("Stage 4 ended =============", (s4_end - s4_start).total_seconds(), flush=True)

##############################################
#                CLEANUP
##############################################

print("Processing done!", flush=True)
