#!/bin/bash

echo "======================================"
echo "   Installing Python environment      "
echo "======================================"

# Check if Homebrew is installed
if ! command -v brew &> /dev/null
then
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    # Add Homebrew to PATH (Apple Silicon)
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
else
    echo "Homebrew already installed."
fi

echo "Updating Homebrew..."
brew update

echo ""
echo "======================================"
echo " Installing Git                       "
echo "======================================"
brew install git

echo "Git version:"
git --version


echo ""
echo "======================================"
echo " Installing Python                    "
echo "======================================"
brew install python

echo "Python version:"
python3 --version
pip3 --version


echo ""
echo "======================================"
echo " Installing Python libraries          "
echo "======================================"

pip3 install --upgrade pip setuptools wheel

pip3 install numpy pandas matplotlib scipy scikit-learn \
             jupyterlab ipykernel \
             requests flask fastapi uvicorn \
             black pylint pytest

echo "Python libraries installed."


echo ""
echo "======================================"
echo " Installing VS Code                   "
echo "======================================"
brew install --cask visual-studio-code


echo ""
echo "======================================"
echo "              DONE                    "
echo "======================================"
echo "✔ Git installed"
echo "✔ Python installed"
echo "✔ Python libraries installed"
echo "✔ Visual Studio Code installed"
