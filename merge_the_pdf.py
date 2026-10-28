# # write a program to manipulate pdf files using pyPDF. your programs should be able
# # to merge multiple pdf files into a single pdf. you are welcome with more functionalites
    

# # from pypdf import PdfWriter
# # mergr = PdfWriter()
# # )
# # for pdf in ["pdf", "pdf-2", "pdf-3"]:
# #     mergr.append(pdf)

# # mergr.write("out-basic-pdf"


# from pypdf import PdfWriter
# import os

# merger = PdfWriter()
# files = [file for file in os.listdir() if file.endswith(".pdf")]

# for pdf in files:
#     merger.append(pdf)

# merger.write("merger-pdf.pdf")
# merger.close()


from pypdf import PdfWriter
import os

merger = PdfWriter()

files = [
    file for file in os.listdir()
    if file.endswith(".pdf") and file != "merger-pdf.pdf"
]

for pdf in files:
    merger.append(pdf)

merger.write("merger-pdf.pdf")
merger.close()

print("PDFs merged successfully!")

from pypdf import PdfWriter
import os

merger = PdfWriter()

files = [for file in file in os.listdir()]
