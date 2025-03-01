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
### Using

```bash
clipboard-text-correction-indicator
```

## Install from PIP and add to the Linux startup session
Install `clipboard-text-correction` from pip and add the program to the bar indicator on Linux startup by creating `~/.config/autostart/clipboard-text-correction-indicator.desktop`.

```bash
curl -fsSL https://raw.githubusercontent.com/trucomanx/ClipboardTextCorrection/main/install_linux_indicator_session.sh | sh
```

## Install from PIP

```bash
pip install --upgrade clipboard-text-correction
```

### Using

```bash
clipboard-text-correction-indicator
```
