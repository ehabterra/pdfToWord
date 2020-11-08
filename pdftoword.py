import sys
import os

import ghostscript
import locale

# import the following libraries 
# will convert the image to text string 
import pytesseract    
from PIL import Image


import argparse

def pdf2jpeg(pdf_input_path, jpeg_output_path):
    args = ["gs", # actual value doesn't matter
            "-dNOPAUSE",
            "-dBATCH", 
            "-sDEVICE=png16m",
            "-r144",
            "-dPDFFitPage",
            #  "-dFirstPage=" + page, 
            #  "-dLastPage=" + page,
            "-sOutputFile=" + jpeg_output_path,
            pdf_input_path]

    encoding = locale.getpreferredencoding()
    args = [a.encode(encoding) for a in args]

    ghostscript.Ghostscript(*args)

def img2text(filename, lang = "ara"):
    baseName = os.path.basename(filename)
    print(baseName)
    imageName, _ = os.path.splitext(baseName)

    options = "-l {} --psm {}".format(lang, "6")
    text = pytesseract.image_to_string(Image.open(filename), config=options)

    file1 = open('txt/{}.txt'.format(imageName),"w") 
    
    # \n is placed to indicate EOL (End of Line) 
    file1.write(text) 
    file1.close() #to change file access modes 
    return text

def convertImages(mypath, lang = "ara"):
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    print(onlyfiles)
    for file in onlyfiles:
        img2text(os.path.join(mypath, file), lang)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-pdf', '--pdf', type=str, help='name of pdf file. pdf file to generate image files in out directory')
    parser.add_argument('-doc', '--docx', type=str, help='name of docx file. transform images to docx file')
    parser.add_argument('-c', '--convert', type=bool, help='flag to convert images. convert each page to a text file and save all text files in txt directory')
    parser.add_argument('-l', '--lang', type=str, help='language to convert')
    parser.print_help()
    args = parser.parse_args()


    if not os.path.exists("txt"):
        os.makedirs("txt") 
    if not os.path.exists("out"):
        os.makedirs("out") 

    print(args)
    
    if args.pdf != None:
        pdf2jpeg(args.pdf, 'out/file_%d.png')

    if args.docx != None:
        pass

    if args.convert == True:
        if args.lang != None:
            convertImages("out", args.lang)
        else:
            convertImages("out")            

if __name__ == "__main__":
    main()
