# clipboard-text-correction

Program that improves text writing.

![logo](https://raw.githubusercontent.com/trucomanx/ClipboardTextCorrection/main/src/clipboard_text_correction/icons/logo.png)

## 1. Dependencies on windows

### Install Meld
This program requires `meld` to be installed on your system to function correctly. `meld` is a graphical tool for comparing files and directories. 

You can download the Meld installer at [https://meldmerge.org](https://meldmerge.org).

### Install Python
This program requires `python` to be installed on your system to function correctly.

You can download the Python installer at [https://www.python.org/downloads/windows](https://www.python.org/downloads/windows).

During installation, ensure you check the box to **"Add Python to PATH"** (this is crucial for running Python from the command line).

## 2. Installing from PyPI

### 2.1. From PyPI
To install the package from `PyPI`, follow the instructions below:


```bash
python -m pip install --upgrade pip
python -m pip install --upgrade supertools
pip install --upgrade clipboard-text-correction
```

Execute `pip show clipboard-text-correction` to see where it was installed.

### 2.2. From EXE file

Download the binary file from the [release](https://github.com/trucomanx/ClipboardTextCorrection/releases) directory, then double-click to run it.

### Using

Start the program using the command below:

```bash
clipboard-text-correction-indicator
```

or

```bash
python3 -m clipboard_text_correction.indicator
```

## 3. LLM
The program needs an `API_KEY` to be used. This can be obtained from
https://deepinfra.com/dash/api_keys

Place the obtained `API_KEY` in the `clipboard-text-correction-indicator` program under menu `Program usage information >> Open config file`.

![open-config-file](https://raw.githubusercontent.com/trucomanx/ClipboardTextCorrection/main/images/open-config-file.win.png)

## 4 Uninstall

```bash
pip uninstall clipboard-text-correction
```

## 5. Buy me a coffee

If you find this tool useful and would like to support its development, you can buy me a coffee!  
Your donations help keep the project running and improve future updates.  

[☕ Buy me a coffee](https://ko-fi.com/trucomanx) 

## 6. License

This project is licensed under the GPL license. See the `LICENSE` file for more details.
