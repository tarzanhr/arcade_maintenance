# Scripts et automatisation

Ce document décrit les scripts disponibles pour gérer la borne arcade et automatiser certaines tâches.

## Scripts principaux

### generate_docs.py

Script de génération automatique de la documentation MkDocs à partir des commentaires Javadoc.

```bash
# Utilisation
python3 generate_docs.py

# Description
# - Analyse tous les fichiers .java dans src/
# - Génère la documentation dans docs/src/
# - Met à jour mkdocs.yml automatiquement
```

### create_mg2d_jar.sh

Script pour créer le fichier JAR de MG2D à partir des sources.

```bash
#!/bin/bash
# Création du JAR MG2D

echo "Création du JAR MG2D..."

# Compilation des sources
javac -d build src/mg2d/*.java

# Création du JAR
jar cf lib/mg2d.jar -C build/ .

echo "JAR MG2D créé dans lib/mg2d.jar"
```

### build.xml

Fichier de configuration Ant pour la compilation du projet.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project name="BorneArcade" default="compile" basedir=".">
    
    <property name="src.dir" value="src"/>
    <property name="build.dir" value="build"/>
    <property name="lib.dir" value="lib"/>
    <property name="jeux.dir" value="jeux"/>
    
    <path id="classpath">
        <fileset dir="${lib.dir}" includes="*.jar"/>
        <pathelement location="${src.dir}"/>
        <pathelement location="${jeux.dir}"/>
    </path>
    
    <target name="init">
        <mkdir dir="${build.dir}"/>
        <mkdir dir="${lib.dir}"/>
    </target>
    
    <target name="compile" depends="init">
        <javac srcdir="${src.dir}" destdir="${build.dir}" classpathref="classpath"/>
        <javac srcdir="${jeux.dir}" destdir="${build.dir}" classpathref="classpath"/>
    </target>
    
    <target name="run" depends="compile">
        <java classname="Main" classpathref="classpath">
            <classpath path="${build.dir}"/>
        </java>
    </target>
    
    <target name="clean">
        <delete dir="${build.dir}"/>
    </target>
    
    <target name="jar" depends="compile">
        <jar destfile="BorneArcade.jar" basedir="${build.dir}">
            <manifest>
                <attribute name="Main-Class" value="Main"/>
                <attribute name="Class-Path" value="lib/mg2d.jar"/>
            </manifest>
        </jar>
    </target>
    
</project>
```

## Scripts de déploiement

### install.sh

Script d'installation complète de la borne arcade.

```bash
#!/bin/bash
# Script d'installation de la Borne Arcade

echo "Installation de la Borne Arcade..."

# Mise à jour du système
sudo apt-get update

# Installation de Java 8
sudo apt-get install -y openjdk-8-jdk

# Installation de Git
sudo apt-get install -y git

# Installation de Maven (pour la documentation)
sudo apt-get install -y maven

# Installation de MkDocs
sudo pip3 install mkdocs

# Création des répertoires
mkdir -p /home/pi/git
cd /home/pi/git

# Clonage du projet (si pas déjà fait)
if [ ! -d "borne_arcade" ]; then
    git clone <URL_DU_REPOSITORY> borne_arcade
fi

cd borne_arcade

# Création des répertoires nécessaires
mkdir -p lib
mkdir -p jeux
mkdir -p build

# Téléchargement de MG2D
if [ ! -f "lib/mg2d.jar" ]; then
    echo "Téléchargement de MG2D..."
    wget -O lib/mg2d.jar http://www.iut-calais.info/mg2d/mg2d.jar
fi

# Compilation du projet
echo "Compilation du projet..."
ant compile

# Génération de la documentation
echo "Génération de la documentation..."
python3 generate_docs.py

# Configuration du démarrage automatique
echo "Configuration du démarrage automatique..."
# Création du service systemd
sudo tee /etc/systemd/system/borne-arcade.service > /dev/null <<EOF
[Unit]
Description=Borne Arcade Service
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/git/borne_arcade
ExecStart=/usr/bin/java -cp lib/mg2d.jar:src Main
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Activation du service
sudo systemctl daemon-reload
sudo systemctl enable borne-arcade.service

echo "Installation terminée !"
echo "Redémarrez le système pour lancer la borne automatiquement."
```

### update.sh

Script de mise à jour du projet.

```bash
#!/bin/bash
# Script de mise à jour de la Borne Arcade

echo "Mise à jour de la Borne Arcade..."

cd /home/pi/git/borne_arcade

# Sauvegarde de la configuration actuelle
cp data/noms_jeux.txt data/noms_jeux.txt.bak

# Mise à jour du code
git pull origin main

# Re-compilation
ant clean
ant compile

# Génération de la documentation
python3 generate_docs.py

# Restauration de la configuration si nécessaire
if [ ! -f "data/noms_jeux.txt" ]; then
    cp data/noms_jeux.txt.bak data/noms_jeux.txt
fi

echo "Mise à jour terminée !"
```

## Scripts de maintenance

### backup.sh

Script de sauvegarde du projet.

```bash
#!/bin/bash
# Script de sauvegarde de la Borne Arcade

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/home/pi/backups"
BACKUP_FILE="borne_arcade_backup_${DATE}.tar.gz"

echo "Création de la sauvegarde..."

# Création du répertoire de sauvegarde
mkdir -p ${BACKUP_DIR}

# Arrêt du service
sudo systemctl stop borne-arcade.service

# Création de l'archive
tar -czf ${BACKUP_DIR}/${BACKUP_FILE} \
    --exclude='build' \
    --exclude='*.class' \
    --exclude='.git' \
    /home/pi/git/borne_arcade

# Redémarrage du service
sudo systemctl start borne-arcade.service

echo "Sauvegarde créée : ${BACKUP_DIR}/${BACKUP_FILE}"

# Nettoyage des anciennes sauvegardes (garde les 5 dernières)
cd ${BACKUP_DIR}
ls -t borne_arcade_backup_*.tar.gz | tail -n +6 | xargs -r rm

echo "Nettoyage terminé."
```

### monitor.sh

Script de surveillance de la borne arcade.

```bash
#!/bin/bash
# Script de surveillance de la Borne Arcade

LOG_FILE="/var/log/borne-arcade.log"
MAX_LOG_SIZE=10485760  # 10MB

# Fonction de logging
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> ${LOG_FILE}
}

# Vérification de l'état du service
check_service() {
    if systemctl is-active --quiet borne-arcade.service; then
        log_message "Service Borne Arcade: ACTIF"
    else
        log_message "Service Borne Arcade: INACTIF - Redémarrage..."
        sudo systemctl restart borne-arcade.service
    fi
}

# Vérification de l'espace disque
check_disk_space() {
    USAGE=$(df /home/pi | awk 'NR==2 {print $5}' | sed 's/%//')
    if [ ${USAGE} -gt 90 ]; then
        log_message "ATTENTION: Espace disque à ${USAGE}%"
    fi
}

# Rotation des logs
rotate_logs() {
    if [ -f ${LOG_FILE} ] && [ $(stat -c%s ${LOG_FILE}) -gt ${MAX_LOG_SIZE} ]; then
        mv ${LOG_FILE} ${LOG_FILE}.old
        log_message "Rotation des logs effectuée"
    fi
}

# Exécution des vérifications
check_service
check_disk_space
rotate_logs

log_message "Vérification de surveillance terminée"
```

## Scripts de développement

### dev_server.sh

Script pour lancer un serveur de développement avec rechargement automatique.

```bash
#!/bin/bash
# Serveur de développement pour la Borne Arcade

echo "Lancement du serveur de développement..."

# Surveillance des fichiers Java et recompilation automatique
while true; do
    # Recherche des fichiers modifiés
    CHANGED=$(find src jeux -name "*.java" -newer /tmp/last_build 2>/dev/null | wc -l)
    
    if [ ${CHANGED} -gt 0 ]; then
        echo "Détection de modifications - Recompilation..."
        ant compile
        
        # Mise à jour du timestamp
        touch /tmp/last_build
        
        # Si le service tourne, le redémarrer
        if systemctl is-active --quiet borne-arcade.service; then
            sudo systemctl restart borne-arcade.service
            echo "Service redémarré"
        fi
    fi
    
    sleep 2
done
```

### test_games.sh

Script pour tester tous les jeux rapidement.

```bash
#!/bin/bash
# Script de test des jeux

echo "Test des jeux de la Borne Arcade..."

# Lecture de la liste des jeux
if [ -f "data/noms_jeux.txt" ]; then
    while IFS= read -r jeu; do
        echo "Test du jeu: ${jeu}"
        
        # Compilation du jeu si nécessaire
        if [ -d "jeux/${jeu}" ]; then
            javac -cp lib/mg2d.jar:src jeux/${jeu}/*.java
            echo "  -> Compilation OK"
        else
            echo "  -> ATTENTION: Répertoire du jeu non trouvé"
        fi
        
    done < data/noms_jeux.txt
else
    echo "Fichier data/noms_jeux.txt non trouvé"
fi

echo "Test terminé"
```

## Utilisation des scripts

### Permissions

Rendez les scripts exécutables :

```bash
chmod +x scripts/*.sh
```

### Exécution

```bash
# Installation
./scripts/install.sh

# Mise à jour
./scripts/update.sh

# Sauvegarde
./scripts/backup.sh

# Surveillance
./scripts/monitor.sh
```

### Automatisation avec cron

Pour automatiser certaines tâches, ajoutez des entrées dans crontab :

```bash
# Éditer crontab
crontab -e

# Ajouter les lignes suivantes :
# Sauvegarde quotidienne à 2h du matin
0 2 * * * /home/pi/git/borne_arcade/scripts/backup.sh

# Surveillance toutes les 5 minutes
*/5 * * * * /home/pi/git/borne_arcade/scripts/monitor.sh

# Mise à jour hebdomadaire le dimanche à 3h du matin
0 3 * * 0 /home/pi/git/borne_arcade/scripts/update.sh
```

## Dépannage des scripts

### Problèmes courants

1. **Permission denied**
   - Vérifiez les permissions avec `chmod +x script.sh`
   - Exécutez avec `sudo` si nécessaire

2. **Command not found**
   - Vérifiez que les dépendances sont installées
   - Utilisez les chemins absolus

3. **Service ne démarre pas**
   - Vérifiez les logs avec `journalctl -u borne-arcade.service`
   - Testez manuellement avec la commande du service

### Logs

Consultez les logs pour diagnostiquer les problèmes :

```bash
# Logs du service
journalctl -u borne-arcade.service -f

# Logs de surveillance
tail -f /var/log/borne-arcade.log

# Logs de compilation
ant compile 2>&1 | tee build.log
```
