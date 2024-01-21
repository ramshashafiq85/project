import PyPDF2
pdffiles = ["1.pdf","2.pdf","sample.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdffiles:
    pdffiles = open(filename, 'rb')
    pdfReader =PyPDF2.PdfReader(pdffiles)
    merger.append(pdfReader)
pdffiles.close()
merger.write('merged.pdf')





