#!/usr/bin/env python3

import json
import subprocess
import sys
import re
from pathlib import Path

def get_python_version():
    """Get installed Python version"""
    try:
        result = subprocess.run(['python3', '--version'], capture_output=True, text=True)
        version = result.stdout.strip().split()[1]
        return version
    except:
        return None

def get_java_version():
    """Get installed Java version"""
    try:
        result = subprocess.run(['java', '-version'], capture_output=True, text=True, stderr=subprocess.STDOUT)
        output = result.stderr if result.stderr else result.stdout
        match = re.search(r'version "(\d+)', output)
        if match:
            return match.group(1)
    except:
        return None

def get_love_version():
    """Get installed LÖVE version"""
    try:
        result = subprocess.run(['love', '--version'], capture_output=True, text=True)
        match = re.search(r'(\d+\.\d+)', result.stdout)
        if match:
            return match.group(1)
    except:
        return None

def check_pip_package(package_name):
    """Check if a pip package is installed and return its version"""
    try:
        result = subprocess.run(['pip3', 'show', package_name], capture_output=True, text=True)
        if result.returncode == 0:
            for line in result.stdout.split('\n'):
                if line.startswith('Version:'):
                    return line.split(':')[1].strip()
        return None
    except:
        return None

def compare_versions(installed, required, operator):
    """Compare version numbers"""
    def version_tuple(v):
        return tuple(map(int, v.split('.')))

    try:
        inst = version_tuple(installed)
        req = version_tuple(required)

        if operator == '>=':
            return inst >= req
        elif operator == '==':
            return inst == req
        elif operator == '>':
            return inst > req
        elif operator == '<=':
            return inst <= req
        elif operator == '<':
            return inst < req
        return False
    except:
        return False

def install_pip_package(package_name, version_spec):
    """Install a pip package with version specification"""
    package_spec = f"{package_name}{version_spec}"
    print(f"Installation de {package_spec}...")
    try:
        result = subprocess.run(['pip3', 'install', package_spec], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  [OK] {package_name} installe avec succes")
            return True
        else:
            print(f"  [ERREUR] Echec installation {package_name}: {result.stderr}")
            return False
    except Exception as e:
        print(f"  [ERREUR] {e}")
        return False

def main():
    # Load dependencies file
    borne_root = Path(__file__).parent.parent
    deps_file = borne_root / 'data' / 'dependencies_global.json'

    with open(deps_file) as f:
        deps = json.load(f)

    print("=== Verification des dependances ===\n")

    # Check Python
    print("[PYTHON]")
    python_version = get_python_version()
    if python_version:
        print(f"  Version installee: {python_version}")
        min_version = deps['languages']['python']['min_version']
        if compare_versions(python_version, min_version, '>='):
            print(f"  [OK] Version >= {min_version}")
        else:
            print(f"  [AVERTISSEMENT] Version requise >= {min_version}")
    else:
        print("  [ERREUR] Python3 non installe")

    # Check Java
    print("\n[JAVA]")
    java_version = get_java_version()
    if java_version:
        print(f"  Version installee: {java_version}")
        min_version = deps['languages']['java']['min_version']
        if int(java_version) >= int(min_version):
            print(f"  [OK] Version >= {min_version}")
        else:
            print(f"  [AVERTISSEMENT] Version requise >= {min_version}")
    else:
        print("  [ERREUR] Java non installe")
        print(f"  Installer avec: sudo apt install {deps['languages']['java']['install_method']}")

    # Check LÖVE
    print("\n[LUA/LOVE]")
    love_version = get_love_version()
    if love_version:
        print(f"  LOVE version installee: {love_version}")
        print(f"  [OK] LOVE {deps['languages']['lua']['love_version']} present")
    else:
        print("  [ERREUR] LOVE non installe")
        print(f"  Installer avec: sudo apt install {deps['languages']['lua']['install_method']}")

    # Check and install Python packages
    print("\n[PACKAGES PYTHON]")
    packages = deps['languages']['python']['packages']

    packages_to_install = []

    for package_name, package_info in packages.items():
        print(f"\n  Verification de {package_name}:")
        installed_version = check_pip_package(package_name)

        if installed_version:
            print(f"    Version installee: {installed_version}")

            # Check if it meets all requirements
            all_ok = True
            for req in package_info['versions']:
                operator = req['operator']
                required = req['version']
                game = req['game']

                if compare_versions(installed_version, required, operator):
                    print(f"    [OK] {operator} {required} pour {game}")
                else:
                    print(f"    [MANQUANT] {operator} {required} pour {game}")
                    all_ok = False

            if not all_ok:
                # Find highest version requirement
                max_req = package_info['max_version']
                packages_to_install.append((package_name, f">={max_req}"))
        else:
            print(f"    [MANQUANT] Non installe")
            max_req = package_info['max_version']
            packages_to_install.append((package_name, f">={max_req}"))

    # Install missing packages
    if packages_to_install:
        print("\n=== Installation des packages manquants ===\n")
        for package_name, version_spec in packages_to_install:
            install_pip_package(package_name, version_spec)
    else:
        print("\n[OK] Tous les packages Python sont installes")

    print("\n=== Verification terminee ===")

if __name__ == '__main__':
    main()
