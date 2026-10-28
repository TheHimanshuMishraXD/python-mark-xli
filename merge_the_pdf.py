# write a program to manipulate pdf files using pyPDF. your programs should be able
# to merge multiple pdf files into a single pdf. you are welcome with more functionalites
    

# from pypdf import PdfWriter
# mergr = PdfWriter()
# )
# for pdf in ["pdf", "pdf-2", "pdf-3"]:
#     mergr.append(pdf)

# mergr.write("out-basic-pdf"


from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["example.pdf", "hello-world.pdf", "jpeg.pdf"]:
    merger.append(pdf)

merger.write("out-basic.pdf")