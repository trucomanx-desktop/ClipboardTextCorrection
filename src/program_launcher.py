#!/usr/bin/python3

# python3 -m venv venv-temporal
# source venv-temporal/bin/activate
# pip install --upgrade pip
# pip install pyinstaller pyinstaller-hooks-contrib
# pip install -r requirements.txt
# cd src
#
# ### windows ##
# python3 -m PyInstaller --onefile --windowed --name clipboard_text_correction --add-data "clipboard_text_correction/icons;icons" --add-data "clipboard_text_correction/data;data" --collect-all PyQt5  program_launcher.py


from clipboard_text_correction.indicator import main

if __name__ == "__main__":
    main()

