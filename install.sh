#!/bin/bash

pip3 install colorama
PYTHON_FILE="$HOME/Installer/main.py"
DESKTOP_FILE="$HOME/.local/share/applications/PiPack.desktop"
LOGO_PATH="$HOME/Installer/Icon/Logo.png"

cat > "$DESKTOP_FILE" <<EOL
[Desktop Entry]
Name=PiPack
Exec=gnome-terminal --title="PiPack" -- python3 "$PYTHON_FILE" 
Icon=$LOGO_PATH
Type=Application
Categories=Development;
Terminal=>True
EOL

python3 install_text.py


