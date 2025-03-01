# clipboard-text-correction

Program that improves text writing

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

## Install from PYPI and add to the Linux startup session
Install `clipboard-text-correction` from `pypi` and add the program to the bar indicator on Linux startup by creating `~/.config/autostart/clipboard-text-correction-indicator.desktop`.

```bash
curl -fsSL https://raw.githubusercontent.com/trucomanx/ClipboardTextCorrection/main/install_linux_indicator_session.sh | sh
```

## Install from PYPI

```bash
pip install --upgrade clipboard-text-correction
```

Using:

```bash
clipboard-text-correction-indicator
```

## More information

More information can be found in [README.extras.md](README.extras.md)
