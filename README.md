# clipboard-text-correction

Program that improves text writing

## Install from source
Installing clipboard-text-correction program

```bash
git clone https://github.com/trucomanx/ClipboardTextCorrection.git
cd ClipboardTextCorrection
pip install -r requirements.txt
cd src
python3 setup.py sdist
pip install dist/clipboard_text_correction-*.tar.gz
```

## Add a program to the Linux start session
Adding bar indicator to Linux start session (`~/.config/autostart/clipboard-text-correction-indicator.desktop`)

```bash
curl -fsSL https://raw.githubusercontent.com/trucomanx/ClipboardTextCorrection/main/install_linux_indicator_session.sh | sh
```

## Using


```bash
clipboard-text-correction-indicator
```

