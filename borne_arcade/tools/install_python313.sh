#!/bin/bash

# Script d'installation de Python 3.13 sur la borne arcade
# Auteur: Assistant IA
# Date: $(date +%Y-%m-%d)

set -e  # Arrêter le script en cas d'erreur

echo "🐍 Installation de Python 3.13 sur la borne arcade"
echo "=================================================="

# Vérifier si on est bien sur un système Raspberry Pi/ARM
ARCH=$(uname -m)
echo "🖥️ Architecture détectée: $ARCH"

# Mettre à jour les paquets
echo "📦 Mise à jour des paquets..."
sudo apt update

# Installer les dépendances nécessaires
echo "🔧 Installation des dépendances..."
sudo apt install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libbz2-dev \
    liblzma-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    git

# Télécharger Python 3.13
echo "⬇️ Téléchargement de Python 3.13..."
cd /tmp
PYTHON_VERSION="3.13.0"
PYTHON_FILE="Python-${PYTHON_VERSION}.tgz"

if [ ! -f "$PYTHON_FILE" ]; then
    wget "https://www.python.org/ftp/python/3.13.0/${PYTHON_FILE}"
fi

# Extraire Python
echo "📂 Extraction de Python..."
tar -xzf "$PYTHON_FILE"

# Compiler Python
echo "🔨 Compilation de Python (cela peut prendre du temps)..."
cd "Python-${PYTHON_VERSION}"

./configure \
    --enable-optimizations \
    --enable-loadable-sqlite-extensions \
    --with-ensurepip=install \
    --prefix=/usr/local

make -j$(nproc)
sudo make altinstall

# Créer les liens symboliques
echo "🔗 Création des liens symboliques..."
sudo ln -sf /usr/local/bin/python3.13 /usr/local/bin/python3
sudo ln -sf /usr/local/bin/pip3.13 /usr/local/bin/pip3

# Vérifier l'installation
echo "✅ Vérification de l'installation..."
/usr/local/bin/python3.13 --version

# Mettre à jour pip
echo "📦 Mise à jour de pip..."
/usr/local/bin/python3.13 -m pip install --upgrade pip

# Mettre à jour les alternatives Python (rendre 3.13 par défaut)
echo "⚙️ Configuration des alternatives Python..."
sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.13 1
sudo update-alternatives --install /usr/bin/pip3 pip3 /usr/local/bin/pip3.13 1

# Rendre Python 3.13 le choix par défaut
echo "🎯 Python 3.13 défini par défaut"
sudo update-alternatives --set python3 /usr/local/bin/python3.13
sudo update-alternatives --set pip3 /usr/local/bin/pip3.13

echo ""
echo "🎉 Installation Python 3.13 terminée avec succès !"
echo "=================================================="
echo "Python 3.13 est maintenant disponible et configuré par défaut:"
echo "  - Commande: python3.13 ou python3 (par défaut)"
echo "  - Version: $(/usr/local/bin/python3.13 --version)"
echo ""
echo "✨ Python 3.13 est maintenant la version par défaut du système !"
echo ""
echo "📦 Pour installer les dépendances des jeux, utilisez:"
echo "  python3 scripts/check_and_install_deps.py"
echo ""
echo "🚀 Redémarrez votre terminal pour utiliser Python 3.13 par défaut !"
