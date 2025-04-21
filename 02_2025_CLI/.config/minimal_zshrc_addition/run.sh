#!/bin/bash

# Verzeichnis mit ASCII-Bildern
PIXELART_DIR="$HOME/.config/minimal_zshrc_addition/pixelart"

# Alle Dateien mit dem Muster "01_pixelart" bis "04_pixelart" finden
ASCII_FILES=("$PIXELART_DIR"/*_pixelart)

# Prüfen, ob Dateien existieren
if [ ${#ASCII_FILES[@]} -eq 0 ]; then
    echo "Keine ASCII-Bilder gefunden im Verzeichnis $PIXELART_DIR"
    exit 1
fi

# Zufälliges ASCII-Bild auswählen
RANDOM_INDEX=$((RANDOM % ${#ASCII_FILES[@]}))
SELECTED_FILE="${ASCII_FILES[$RANDOM_INDEX]}"

# ASCII-Bild anzeigen
cat "$SELECTED_FILE
