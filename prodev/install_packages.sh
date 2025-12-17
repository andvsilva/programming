#!/usr/bin/env bash

set -e

PACKAGE_LIST="packages_installed.txt"

if [[ ! -f "$PACKAGE_LIST" ]]; then
    echo "❌ Package list '$PACKAGE_LIST' not found."
    exit 1
fi

echo "📦 Updating package index..."
sudo apt update

echo "📦 Installing packages from $PACKAGE_LIST"
while read -r package; do
    if dpkg -s "$package" &> /dev/null; then
        echo "✔ $package already installed"
    else
        echo "➕ Installing $package"
        sudo apt install -y "$package" || echo "⚠ Failed to install $package"
    fi
done < "$PACKAGE_LIST"

echo "✅ Installation process finished"
