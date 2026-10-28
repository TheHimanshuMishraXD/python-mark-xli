# write a program to manipulate pdf files using pyPDF. your programs should be able
# to merge multiple pdf files into a single pdf. you are welcome with more functionalites
    

from pypdf import PdfWriter
mergr = PdfWriter()

for pdf in ("pdf 1", "pdf-2", "pdf-3"):
    mergr.append(pdf)