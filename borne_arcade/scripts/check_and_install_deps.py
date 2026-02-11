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
        # Show real-time output during installation
        # Use --only-binary=:all: to force precompiled wheels and avoid compilation
        process = subprocess.Popen(['pip3', 'install', '--only-binary=:all:', package_spec], 
                                  stdout=subprocess.PIPE, 
                                  stderr=subprocess.STDOUT, 
                                  text=True, 
                                  universal_newlines=True)
        
        for line in iter(process.stdout.readline, ''):
            if line.strip():
                print(f"  {line.strip()}")
        
        process.wait()
        
        if process.returncode == 0:
            print(f"  [OK] {package_name} installe avec succes")
            return True
        else:
            print(f"  [ERREUR] Echec installation {package_name}")
            return False
    except Exception as e:
        print(f"  [ERREUR] {e}")
        return False

def check_system_dependencies():
    """Check and install system dependencies needed for Python packages"""
    print("\n[DEPENDANCES SYSTEME]")
    
    required_packages = {
        'gfortran': 'sudo apt install gfortran',
        'python3-dev': 'sudo apt install python3-dev',
        'build-essential': 'sudo apt install build-essential'
    }
    
    missing_packages = []
    
    for package, install_cmd in required_packages.items():
        try:
            if package == 'gfortran':
                # Check with which for executables
                result = subprocess.run(['which', package], capture_output=True, text=True)
            else:
                # Check with dpkg for development packages
                result = subprocess.run(['dpkg', '-l', package], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"  [OK] {package} est installe")
            else:
                print(f"  [MANQUANT] {package} non installe")
                missing_packages.append((package, install_cmd))
        except:
            print(f"  [MANQUANT] {package} non installe")
            missing_packages.append((package, install_cmd))
    
    if missing_packages:
        print("\n=== Installation des dependances systeme manquantes ===")
        print("Les packages suivants sont necessaires pour compiler scipy et autres packages:")
        for package, install_cmd in missing_packages:
            print(f"  {package}: {install_cmd}")
        print("\nExecutez ces commandes manuellement, puis relancez ce script.")
        return False
    else:
        print("  [OK] Toutes les dependances systeme sont presentes")
        return True

def main():
    # Load dependencies file
    borne_root = Path(__file__).parent.parent
    deps_file = borne_root / 'data' / 'dependencies_global.json'

    with open(deps_file) as f:
        deps = json.load(f)

    print("=== Verification des dependances ===\n")

    # Check system dependencies first
    if not check_system_dependencies():
        print("\nInstallation des dependances systeme requise avant de continuer.")
        return

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
