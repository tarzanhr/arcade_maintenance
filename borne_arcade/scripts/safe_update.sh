#!/bin/bash

# Script de mise à jour SÉCURISÉ pour Raspberry Pi
# N'utilise PAS rpi-update (version bêta)

echo "=== Mise à jour sécurisée du système ==="
echo "Date: $(date)"
echo ""

# Sauvegarde des informations avant mise à jour
echo "📋 État avant mise à jour :"
echo "Version actuelle: $(cat /etc/debian_version 2>/dev/null || echo 'Inconnue')"
echo "Noyau: $(uname -r)"
echo ""

# Étape 1: Mettre à jour la liste des paquets
echo "🔄 Mise à jour de la liste des paquets..."
sudo apt update

# Étape 2: Mettre à niveau les paquets (sécurisé)
echo "🔄 Mise à niveau des paquets système..."
sudo apt upgrade -y

# Étape 3: Nettoyer les paquets inutiles
echo "🧹 Nettoyage des paquets inutiles..."
sudo apt autoremove -y
sudo apt autoclean

# Étape 4: Mettre à jour les paquets de sécurité
echo "Mise à jour des paquets de sécurité..."
sudo apt install --only-upgrade -y $(apt-get -s dist-upgrade | awk '/^Inst.*security/ {print $2}')

# Étape 5: Vérifier si redémarrage nécessaire
echo ""
echo "État après mise à jour :"
echo "Version: $(cat /etc/debian_version 2>/dev/null || echo 'Inconnue')"
echo "Noyau: $(uname -r)"

# Vérifier si redémarrage nécessaire
if [ -f /var/run/reboot-required ]; then
    echo ""
    echo "REDÉMARRAGE REQUIS"
    echo "Redémarrage automatique dans 10 secondes..."
    echo "Appuyez sur Ctrl+C pour annuler"
    sleep 10
    echo "🔄 Redémarrage du système..."
    sudo reboot
else
    echo ""
    echo "Aucun redémarrage nécessaire"
fi

echo ""
echo "=== Mise à jour terminée ==="
