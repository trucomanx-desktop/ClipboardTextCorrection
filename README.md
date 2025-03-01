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
## LLM
The program needs an API_KEY to be used. This can be obtained from
https://deepinfra.com/dash/api_keys

Place the obtained API_KEY in the program menu under `Open config file`.


## License
This project is licensed under the GPLv3 License.

## More information

More information can be found in [README.extras.md](README.extras.md)
