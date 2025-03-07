# clipboard-text-correction

Program that improves text writing.

![logo](https://raw.githubusercontent.com/trucomanx/ClipboardTextCorrection/main/src/clipboard_text_correction/icons/logo.png)


## 1. Dependencies on Linux

This program requires `meld` to be installed on your system to function correctly. `meld` is a graphical tool for comparing files and directories. How to install `meld`:

```bash
sudo apt-get install meld
```

## 2. Install from PyPI and add to Linux start session
Install `clipboard-text-correction` from `pypi` and add the program to the bar indicator on Linux startup session.

```bash
curl -fsSL https://raw.githubusercontent.com/trucomanx/ClipboardTextCorrection/main/install_linux_indicator_session.sh | sh
```

## 3. LLM
The program needs an `API_KEY` to be used. This can be obtained from
https://deepinfra.com/dash/api_keys

Place the obtained `API_KEY` in the `clipboard-text-correction-indicator` program under menu `Program usage information >> Open config file`.

![open-config-file](https://raw.githubusercontent.com/trucomanx/ClipboardTextCorrection/main/images/open-config-file.lin.png)

## 4 Uninstall

```bash
pip uninstall clipboard-text-correction
```

## 5. Buy me a coffee

If you find this tool useful and would like to support its development, you can buy me a coffee!  
Your donations help keep the project running and improve future updates.  

[☕ Buy me a coffee](https://ko-fi.com/trucomanx) 

## 6. License
This project is licensed under the GPLv3 License.

