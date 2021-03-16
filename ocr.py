# Import libraries 
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
from pathlib import Path
import shutil

# Path of the pdf 
# PDF_file = "contestacao_GIL.pdf"

def convert_pdf_to_img(PDF_file):
	print("Converting PDF")
	pages = convert_from_path(PDF_file, 500) 
	image_counter = 1

	print("Saving Images")
	for page in pages: 

		filename = "img/page_"+str(image_counter)+".jpg"

		page.save(filename, 'JPEG') 
		image_counter = image_counter + 1
	
	return image_counter

def ocr(image_counter):
	print("Starting OCR")
	filelimit = image_counter-1

	outfile = "out_text.txt"

	f = open(outfile, "a") 
 
	for i in range(1, filelimit + 1): 
		filename = "img/page_"+str(i)+".jpg"
			
		text = str(((pytesseract.image_to_string(Image.open(filename))))) 
		text = text.replace('-\n', '')	 

		f.write(text) 

	f.close() 

def cleanup_img_folder():
	if os.path.exists("img/") and os.path.isdir("img/"):
		shutil.rmtree("img/")

def main():
	cleanup_img_folder()
	Path("img/").mkdir(parents=True, exist_ok=True)

	if len(sys.argv) < 2:
		print("Pass the file the argument!")
	else:
		image_counter = convert_pdf_to_img(sys.argv[1])
		ocr(image_counter)
		print("The output text can be found on the file: out_text.txt")

if __name__ == '__main__':
	main()