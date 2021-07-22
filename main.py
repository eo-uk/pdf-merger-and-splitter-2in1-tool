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

def split_pdf(path):
    '''
    split_pdf(path)

    Splits a PDF file into separate pages.
    path: Path to the PDF file.
    '''
    #Read the PDF
    pdf = PdfFileReader(path)
    #Number of digits in the total number of pages
    total_digits = len(str(pdf.getNumPages()))

    for i in range(pdf.getNumPages()):
        #Page number with leading zeroes
        page_no = str(i+1)
        page_digits = len(page_no)
        lead_zeros = '0' * (total_digits - page_digits)
        #Add page to the writer and write to file
        writer = PdfFileWriter()
        writer.addPage(pdf.getPage(i))
        with open(
            os.path.basename(path) + " - Page" + lead_zeros + page_no + ".pdf",
            mode="wb"
        ) as output:
            writer.write(output)
            
def get_paths():
    ''' Prompts the user for PDF paths. Type 'done' to finish. '''
    paths = []
    while True:
        answer = input('Please enter a path. Type "done" when you are done.').strip()
        if answer:
            if answer in ('done', 'DONE', 'Done'):
                break
            paths.append(answer)
    return paths

def main():
    try:
        #Get paths as system arguments if any given
        paths = sys.argv[1:]
        #If no system argument was given
        if not paths:
            paths = get_paths()

        if paths:
            #If multiple PDF files are passed, merge them
            if len(paths) > 1:
                paths = sorted(paths) #All PDF paths sorted alphabetically
                merge_pdf(paths)
            #If a single PDF file is passed, split it
            else:
                path = paths[0]
                split_pdf(path)
            print('\nOperation Successful!')
        else:
            print('\nNo action taken as no path was provided.')
            
    except (PdfReadError, FileNotFoundError) as e:
        print('\nError: ', e)
        
    finally:
        input('\nPress any key to exit.')

        
if __name__ == "__main__":
    main()
