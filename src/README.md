# clipboard-text-correction

Program that improves text writing.

## Dependencies

This program requires **Meld** to be installed on your system to function correctly. The **Meld** is a graphical tool for comparing files and directories.

How to install or **Meld**

- **Ubuntu/Debian**:

```bash
sudo apt-get install meld
```
- **Windows**: You can download the Meld installer at [meldmerge.org](meldmerge.org).


## 1. Installing

### 1.1. Install the package pip

To install the package from `pypi`, follow the instructions below:


```bash
pip install clipboard-text-correction
```

Execute `which clipboard-text-correction` to see where it was installed, probably in `/home/USERNAME/.local/bin/clipboard-text-correction`.


### 1.2. Add clipboard-text-correction to the Linux start session

Adding bar indicator to Linux start session (`~/.config/autostart/clipboard-text-correction-indicator.desktop`)

```bash
curl -fsSL https://raw.githubusercontent.com/trucomanx/ClipboardTextCorrection/main/install_linux_indicator_session.sh | sh
```

## 2. Using

If the program was not added to the Linux start session, then to start use the command below:

```bash
clipboard-text-correction-indicator
```

## 3. License

This project is licensed under the GPL license. See the `LICENSE` file for more details.
