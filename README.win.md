# clipboard-text-correction

Program that improves text writing.

![logo](https://raw.githubusercontent.com/trucomanx/ClipboardTextCorrection/main/src/clipboard_text_correction/icons/logo.png)

## 1. Dependencies on windows

### Install Meld
This program requires `meld` to be installed on your system to function correctly. `meld` is a graphical tool for comparing files and directories. 

You can download the Meld installer at [https://meldmerge.org](https://meldmerge.org).

### Install Python

- **Open Microsoft Store:**	Press `Win + R` to open therun dialog box and type `ms-windows-store:` and press Enter. 

- **Search for Python:** In the Microsoft Store, use the search bar at the top right. Type "Python" and press Enter. 

- **Install Python:** Click the "Get" or "Install" button. **During installation, ensure you check the box to "Add Python to PATH"** (this is crucial for running Python from the command line). Wait for the download and installation to complete.

## 2. Installing from PyPI

To install the package from `PyPI`, follow the instructions below:


```bash
python -m pip install --upgrade pip
python -m pip install --upgrade supertools
pip install --upgrade clipboard-text-correction
```

Execute `pip show clipboard-text-correction` to see where it was installed, probably in `C:\Users\[USERNAME]\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.[VERSION]\local-packages\Python3[VERSION]\site-packages`.

### Using

If the program was not added to the windows start session, then to start, use the command below:

```bash
clipboard-text-correction-indicator
```

### Adding to the Startup Folder

- Press `Win + R` to open the Run dialog box. 
- Type `shell:startup` and press Enter. This will open the Startup folder in File Explorer.
- In the Startup folder, create a shortcut to the program `clipboard-text-correction-indicator` you want to start automatically.

## 3. LLM
The program needs an `API_KEY` to be used. This can be obtained from
https://deepinfra.com/dash/api_keys

Place the obtained `API_KEY` in the `clipboard-text-correction-indicator` program under menu `Program usage information >> Open config file`.

![open-config-file](https://raw.githubusercontent.com/trucomanx/ClipboardTextCorrection/main/images/open-config-file.win.png)

## 4. Buy me a coffee

If you find this tool useful and would like to support its development, you can buy me a coffee!  
Your donations help keep the project running and improve future updates.  

[☕ Buy me a coffee](https://ko-fi.com/trucomanx) 

## 5. License

This project is licensed under the GPL license. See the `LICENSE` file for more details.
