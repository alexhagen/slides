import numpy as np
import argparse
import os
import sys

parser = argparse.ArgumentParser(description='Convert specially formatted' +
                                 'markdown file to beautiful slides.')
parser.add_argument('--filename', dest='filename',
                    metavar='<filename>', type=str,
                    help='the path to the markdown file')

args = parser.parse_args()

if args.filename is not None:
    markdown_file = args.filename
if not os.path.isfile(markdown_file):
    print("The system cannot find the markdown file at the path given.")
    sys.exit(1)
