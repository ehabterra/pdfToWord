# PDF To Word
pdf to text files and word file

## Requirements:
- GS script.
- Tesseract.

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
