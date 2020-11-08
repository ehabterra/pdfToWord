# PDF To Word
This tool converts PDF of text images to: 
- Multiple text files (text file for each image/page) 
- Word file (not implemented yet)

## Requirements:
This tool depends on the following programs, please install them before using it:
- Ghost Script. https://www.ghostscript.com/download/gsdnld.html
- Tesseract. https://tesseract-ocr.github.io/tessdoc/Downloads.html

## Example:

- Create new environment:
```bash
conda create -n pdfToWordEnv python=3.8
```

- Make sure the environment exists:
```bash
conda list
```

- Activate the environment:
```bash
conda activate pdfToWordEnv
```

- Install packages:
```bash
pip install -r requirements.txt
```

- Run the test file:
```bash
python ./pdftoword.py -pdf scansmpl.pdf -c True -l eng
```

- When finishing using the tool don't forget to deactivate the environment:
```bash
conda deactivate
```

- To totally remove the environment:
```bash
conda remove --name pdfToWordEnv -all
```
