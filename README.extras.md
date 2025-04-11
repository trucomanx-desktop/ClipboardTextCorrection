# clipboard-text-correction

Program that improves text writing

## Testar indicator

```bash
cd src
python3 -m clipboard_text_correction.indicator
```

## Upload to PYPI

```bash
cd src
python -m build
twine upload dist/*
```

## Install from PYPI

The homepage in pipy is https://pypi.org/project/clipboard-text-correction/

```bash
pip install --upgrade clipboard-text-correction
```

Using:

```bash
clipboard-text-correction-indicator
```

## Install from source
Installing `clipboard-text-correction` program

```bash
git clone https://github.com/trucomanx/ClipboardTextCorrection.git
cd ClipboardTextCorrection
pip install -r requirements.txt
cd src
python3 setup.py sdist
pip install dist/clipboard_text_correction-*.tar.gz
```
Using:

```bash
clipboard-text-correction-indicator
```

## Uninstall

```bash
pip uninstall clipboard_text_correction
```
