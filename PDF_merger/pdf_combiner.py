import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('output.pdf')

pdf_combiner(inputs)

# During executing this from terminal, make sure to add the input pdf filename next to python file 
# Eg: ~ python pdf_merger.py file1.pdf file2.pdf
