#!/bin/bash

pip install --upgrade clipboard-text-correction

# Defina as variáveis que você deseja substituir
USER=$(whoami)  # Nome do usuário atual
GROUP=$(id -gn) # Nome do grupo principal do usuário atual
HOME_DIR=$HOME  # Diretório home do usuário
USERID=$(id -u $USER)
PROGRAM_PATH=$(which clipboard-text-correction-indicator)
PYTHON_NAME=$(python3 --version | awk '{print "python" $2}' | sed 's/\.[0-9]*$//')

# Caminho para o arquivo de serviço
SERVICE_FILE="$HOME_DIR/.config/autostart/clipboard-text-correction-indicator.desktop"

# Conteúdo do arquivo de serviço (substitua os placeholders)
SERVICE_CONTENT="[Desktop Entry]
Type=Application
Name=Clipboard Text Correction Indicator
Exec=$PROGRAM_PATH
X-GNOME-Autostart-enabled=true
Icon=$HOME_DIR/.local/lib/$PYTHON_NAME/site-packages/clipboard_text_correction/icons/logo.png
Comment=Converts clipboard text writing
Terminal=false
Path=$HOME_DIR
Categories=Utility;AudioVideo;
StartupNotify=true
"

# Cria o arquivo de serviço temporário e escreve o conteúdo nele
echo "$SERVICE_CONTENT" | tee $SERVICE_FILE > /dev/null

