# clipboard-text-correction

Program that improves text writing

## Dependencies

This program requires **Meld** to be installed on your system to function correctly. The **Meld** is a graphical tool for comparing files and directories.

How to install or **Meld**

- **Ubuntu/Debian**:

```bash
sudo apt-get install meld
```
- **Windows**: You can download the Meld installer at [meldmerge.org](meldmerge.org).

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

## License
This project is licensed under the GPLv3 License.

## More information

More information can be found in [README.extras.md](README.extras.md)
