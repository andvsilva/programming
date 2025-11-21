#!/bin/bash

echo "==============================="
echo "   Installing Python on macOS  "
echo "==============================="

# Check if Homebrew is installed
if ! command -v brew &> /dev/null
then
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    # Add Homebrew to PATH (required for Apple Silicon)
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
else
    echo "Homebrew already installed."
fi

echo "Updating Homebrew..."
brew update

echo "Installing Python..."
brew install python

echo "==============================="
echo "   Python Installation Done!   "
echo "==============================="

# Show version
python3 --version
pip3 --version

echo "✔ Python and pip installed successfully!"
