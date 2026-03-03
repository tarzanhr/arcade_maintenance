#!/usr/bin/env python3
"""
Verifie la couverture de documentation du projet.
Analyse les fichiers Java et Python pour detecter les fonctions/methodes sans documentation.
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple

class DocCoverageChecker:
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.src_dir = project_root / "src"
        self.scripts_dir = project_root / "scripts"

        # Statistiques
        self.total_functions = 0
        self.documented_functions = 0
        self.missing_doc = []

    def check_java_file(self, file_path: Path) -> List[Tuple[str, int]]:
        """Verifie la documentation Java (Javadoc) dans un fichier."""
        content = file_path.read_text(encoding='utf-8')
        lines = content.split('\n')
        missing = []

        # Pattern pour trouver les methodes/classes publiques
        for i, line in enumerate(lines, 1):
            # Ignorer les lignes de commentaires et imports
            if line.strip().startswith('//') or line.strip().startswith('import'):
                continue

            # Chercher les declarations publiques
            if re.search(r'\bpublic\s+(static\s+)?(\w+\s+)?\w+\s*\(', line):
                self.total_functions += 1

                # Verifier si il y a un /** */ dans les 10 lignes precedentes
                has_javadoc = False
                for j in range(max(0, i-10), i):
                    if '/**' in lines[j-1]:
                        has_javadoc = True
                        break

                if has_javadoc:
                    self.documented_functions += 1
                else:
                    # Extraire le nom de la methode
                    match = re.search(r'\b(\w+)\s*\(', line)
                    if match:
                        method_name = match.group(1)
                        missing.append((method_name, i))

        return missing

    def check_python_file(self, file_path: Path) -> List[Tuple[str, int]]:
        """Verifie la documentation Python (docstrings) dans un fichier."""
        content = file_path.read_text(encoding='utf-8')
        lines = content.split('\n')
        missing = []

        for i, line in enumerate(lines, 1):
            # Chercher les definitions de fonctions
            match = re.match(r'\s*def\s+(\w+)\s*\(', line)
            if match:
                func_name = match.group(1)

                # Ignorer les fonctions privees (commencent par _)
                if func_name.startswith('_') and not func_name.startswith('__'):
                    continue

                self.total_functions += 1

                # Verifier si la ligne suivante contient une docstring
                has_docstring = False
                if i < len(lines):
                    next_line = lines[i].strip()
                    if next_line.startswith('"""') or next_line.startswith("'''"):
                        has_docstring = True

                if has_docstring:
                    self.documented_functions += 1
                else:
                    missing.append((func_name, i))

        return missing

    def run(self, min_coverage: float = 100.0) -> int:
        """Execute la verification de couverture."""
        print("=== Verification de la couverture documentation ===\n")

        # Verifier les fichiers Java dans src/
        if self.src_dir.exists():
            print("[JAVA] Analyse des fichiers source...")
            for java_file in self.src_dir.glob("*.java"):
                missing = self.check_java_file(java_file)
                if missing:
                    print(f"\n  {java_file.name}:")
                    for func_name, line_num in missing:
                        print(f"    Ligne {line_num}: {func_name}() - Javadoc manquant")
                        self.missing_doc.append((str(java_file), func_name, line_num))

        # Verifier les fichiers Python dans scripts/
        if self.scripts_dir.exists():
            print("\n[PYTHON] Analyse des scripts...")
            for py_file in self.scripts_dir.glob("*.py"):
                # Ignorer ce script lui-meme et __init__.py
                if py_file.name in ['check_doc_coverage.py', '__init__.py']:
                    continue

                missing = self.check_python_file(py_file)
                if missing:
                    print(f"\n  {py_file.name}:")
                    for func_name, line_num in missing:
                        print(f"    Ligne {line_num}: {func_name}() - docstring manquante")
                        self.missing_doc.append((str(py_file), func_name, line_num))

        # Calculer la couverture
        if self.total_functions > 0:
            coverage = (self.documented_functions / self.total_functions) * 100
        else:
            coverage = 100.0

        print("\n=== Resultat ===\n")
        print(f"Fonctions totales: {self.total_functions}")
        print(f"Fonctions documentees: {self.documented_functions}")
        print(f"Fonctions sans doc: {len(self.missing_doc)}")
        print(f"Couverture: {coverage:.1f}%")

        if coverage < min_coverage:
            print(f"\nERREUR: Couverture insuffisante (minimum {min_coverage}%)")
            return 1
        else:
            print(f"\nOK: Couverture suffisante (>= {min_coverage}%)")
            return 0

def main():
    project_root = Path(__file__).parent.parent
    checker = DocCoverageChecker(project_root)

    # Seuil de couverture minimum: 80%
    exit_code = checker.run(min_coverage=80.0)
    sys.exit(exit_code)

if __name__ == '__main__':
    main()
