#!/usr/bin/env python3
"""
Script de génération du fichier dependencies_global.json
Analyse tous les jeux et leurs dépendances
"""

import json
import os
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def analyze_dependencies(borne_root):
    """Analyse toutes les dépendances du projet"""

    data = {
        "metadata": {
            "generated_at": datetime.now().isoformat(),
            "project": "borne_arcade",
            "total_games": 0
        },
        "system_packages": {
            "debian_apt": ["git", "xdotool", "xkb-data", "unclutter", "curl", "wget", "love"]
        },
        "languages": {
            "java": {
                "versions_required": ["8", "17", "21"],
                "min_version": "8",
                "recommended_version": "17",
                "max_version": "21",
                "classpath": ["MG2D.jar"],
                "install_method": "openjdk-17-jdk or openjdk-8-jdk"
            },
            "python": {
                "versions_required": [],
                "min_version": None,
                "max_version": None,
                "packages": {},
                "install_method": "python3 python3-pip"
            },
            "lua": {
                "versions_required": ["5.1"],
                "love_version": "11.0+",
                "install_method": "love"
            }
        },
        "games": {}
    }

    # Analyser le requirements.txt racine pour les outils de développement
    root_req_file = Path(borne_root) / "requirements.txt"
    if root_req_file.exists():
        print("Analyse: requirements.txt racine")
        with open(root_req_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    match = re.match(r'([a-zA-Z0-9_-]+)(>=|==|~=|<=|>|<)(.+)', line)
                    if match:
                        pkg_name, operator, version = match.groups()
                        version = version.strip()

                        if pkg_name not in data["languages"]["python"]["packages"]:
                            data["languages"]["python"]["packages"][pkg_name] = {
                                "versions": [],
                                "min_version": None,
                                "max_version": None,
                                "used_by": []
                            }

                        pkg_data = data["languages"]["python"]["packages"][pkg_name]
                        pkg_data["versions"].append({
                            "operator": operator,
                            "version": version,
                            "game": "dev-tools"
                        })
                        if "dev-tools" not in pkg_data["used_by"]:
                            pkg_data["used_by"].append("dev-tools")
                        print(f"  OK {pkg_name} {operator} {version}")

    projet_dir = Path(borne_root) / "projet"

    for game_dir in sorted(projet_dir.iterdir()):
        if not game_dir.is_dir():
            continue

        game_name = game_dir.name
        print(f"Analyse: {game_name}")

        game_info = {
            "type": None,
            "dependencies": {},
            "python_version": None,
            "java_version": None,
            "lua_version": None,
            "has_requirements": False
        }

        # Détecter le type de jeu
        java_files = list(game_dir.glob("*.java")) + list(game_dir.glob("*/*.java"))
        py_files = list(game_dir.glob("*.py")) + list(game_dir.rglob("*.py"))
        lua_files = list(game_dir.glob("*.lua"))

        if java_files:
            game_info["type"] = "java"
            game_info["java_version"] = "8+"  # Par défaut

        elif py_files:
            game_info["type"] = "python"

            # Lire requirements.txt
            req_file = game_dir / "requirements.txt"
            if req_file.exists():
                game_info["has_requirements"] = True
                print(f"  OK requirements.txt trouvé")

                with open(req_file, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            # Parser: package>=version ou package==version
                            match = re.match(r'([a-zA-Z0-9_-]+)(>=|==|~=|<=|>|<)(.+)', line)
                            if match:
                                pkg_name, operator, version = match.groups()
                                version = version.strip()

                                game_info["dependencies"][pkg_name] = {
                                    "operator": operator,
                                    "version": version
                                }

                                # Ajouter au registre global
                                if pkg_name not in data["languages"]["python"]["packages"]:
                                    data["languages"]["python"]["packages"][pkg_name] = {
                                        "versions": [],
                                        "min_version": None,
                                        "max_version": None,
                                        "used_by": []
                                    }

                                pkg_data = data["languages"]["python"]["packages"][pkg_name]
                                pkg_data["versions"].append({
                                    "operator": operator,
                                    "version": version,
                                    "game": game_name
                                })
                                if game_name not in pkg_data["used_by"]:
                                    pkg_data["used_by"].append(game_name)

                print(f"  Packages {len(game_info['dependencies'])} dépendances")
            else:
                print(f"  WARNING  Pas de requirements.txt")

            # Analyser shebang pour version Python
            for py_file in py_files[:5]:  # Limiter à 5 fichiers
                try:
                    with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
                        first_line = f.readline()
                        if match := re.search(r'python([0-9]+\.[0-9]+)', first_line):
                            game_info["python_version"] = match.group(1)
                            print(f"  Python {match.group(1)} (détecté)")
                            break
                except:
                    pass

            # Par défaut Python 3.5+
            if not game_info["python_version"]:
                game_info["python_version"] = "3.5+"

        elif lua_files or (game_dir / "main.lua").exists() or (game_dir / "conf.lua").exists():
            game_info["type"] = "lua"
            game_info["lua_version"] = "5.1"
            print(f"  Lua 5.1 (LÖVE)")

        else:
            print(f"  UNKNOWN Type inconnu")

        data["games"][game_name] = game_info
        data["metadata"]["total_games"] += 1

    # Post-traitement: calculer min/max pour les packages Python
    for pkg_name, pkg_data in data["languages"]["python"]["packages"].items():
        versions_nums = []
        for v in pkg_data["versions"]:
            try:
                # Extraire le numéro de version
                version_num = re.findall(r'[0-9]+\.[0-9]+(?:\.[0-9]+)?', v["version"])
                if version_num:
                    versions_nums.append(version_num[0])
            except:
                pass

        if versions_nums:
            pkg_data["min_version"] = min(versions_nums)
            pkg_data["max_version"] = max(versions_nums)

    # Calculer versions Python globales
    python_versions = set()
    for game_name, game_info in data["games"].items():
        if game_info.get("python_version"):
            version = game_info["python_version"].replace("+", "")
            try:
                float(version)  # Vérifier que c'est un nombre
                python_versions.add(version)
            except:
                pass

    if python_versions:
        python_nums = [float(v) for v in python_versions]
        data["languages"]["python"]["min_version"] = f"{min(python_nums)}"
        data["languages"]["python"]["max_version"] = f"{max(python_nums)}"
        data["languages"]["python"]["versions_required"] = sorted(list(python_versions))
    else:
        # Valeurs par défaut
        data["languages"]["python"]["min_version"] = "3.5"
        data["languages"]["python"]["max_version"] = "3.14"
        data["languages"]["python"]["versions_required"] = ["3.5+", "3.14"]

    return data


def main():
    script_dir = Path(__file__).parent
    borne_root = os.environ.get('BORNE_ROOT', str(script_dir.parent))
    output_file = Path(borne_root) / 'data' / 'dependencies_global.json'

    print("=== ANALYSE DES DÉPENDANCES ===\n")
    data = analyze_dependencies(borne_root)

    # Sauvegarder le JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nOK Fichier généré: {output_file}")
    print(f"   Total jeux: {data['metadata']['total_games']}")
    print(f"   Python packages: {len(data['languages']['python']['packages'])}")

    # Afficher le résumé
    print("\n=== RÉSUMÉ ===\n")

    print("Packages PAQUETS PYTHON:")
    for pkg, info in sorted(data["languages"]["python"]["packages"].items()):
        print(f"  {pkg}:")
        if info["min_version"]:
            print(f"    Version: {info['min_version']} → {info['max_version']}")
        print(f"    Utilisé par: {', '.join(info['used_by'])}")

    print("\nPython PYTHON:")
    print(f"  Versions requises: {', '.join(data['languages']['python']['versions_required'])}")
    print(f"  Min: {data['languages']['python']['min_version']}")
    print(f"  Max: {data['languages']['python']['max_version']}")

    print("\nJava JAVA:")
    print(f"  Versions supportées: {', '.join(data['languages']['java']['versions_required'])}")
    print(f"  Min: {data['languages']['java']['min_version']}")
    print(f"  Recommandée: {data['languages']['java']['recommended_version']}")
    print(f"  Max: {data['languages']['java']['max_version']}")

    print("\nLua LUA:")
    print(f"  Version: {', '.join(data['languages']['lua']['versions_required'])}")
    print(f"  LÖVE: {data['languages']['lua']['love_version']}")

    print("\nGames JEUX PAR TYPE:")
    games_by_type = defaultdict(list)
    for game, info in data["games"].items():
        game_type = info["type"] or "unknown"
        games_by_type[game_type].append(game)

    for game_type, games in sorted(games_by_type.items()):
        print(f"  {game_type.upper()}: {len(games)} jeux")

    print("\nOK Analyse terminée !")


if __name__ == "__main__":
    main()
