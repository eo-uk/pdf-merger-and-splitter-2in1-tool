from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from PyPDF2.utils import PdfReadError
import os
import sys


def merge_pdf(paths):
    merger = PdfFileMerger()
    for path in paths:
        merger.append(path)
    merger.write(os.path.basename(path) + " - merged.pdf")
    merger.close()
