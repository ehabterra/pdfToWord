# pdfToWord
pdf to text files and word file

## Requirements:
- GS script.
- Tesseract.

## Example:

### Create new environment:
conda create -n pdfToWordEnv python=3.8

### Make sure the environment exists:
conda list

### Activate the environment:
conda activate pdfToWordEnv

### Install packages:
pip install -r requirements.txt

### Run the test file:
python ./pdftoword.py -pdf scansmpl.pdf -c True -l eng
