from convert_to_pdf import *
from head_foot_pdf import *
from merge_pdfs import *
from many2one_page import *

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--dir", "-d", dest="dir_path", default="./files")
parser.add_argument("--fname-pos", "-fnp", dest="fname_pos", default="top-center")
parser.add_argument("--pgnum-pos", "-pnp", dest="pgnum_pos", default="bottom-center")
parser.add_argument("--output", "-o", dest="output_fp", default="./outputs/file.pdf")
