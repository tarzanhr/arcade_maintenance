#!/usr/bin/env python3
"""
Ameliorateur IA de documentation.
Analyse les changements git et propose des ameliorations de documentation via Ollama.
IMPORTANT: Ce script propose uniquement, il ne modifie JAMAIS automatiquement.
"""

import argparse
import subprocess
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, '/home/thr/git')
from ollama_wrapper import OllamaWrapper


def get_git_diff(project_root):
    """Recupere le diff git des fichiers modifies."""
    result = subprocess.run(
        ['git', 'diff', '--cached'],
        cwd=project_root,
        capture_output=True,
        text=True
    )
    if result.stdout.strip():
        return result.stdout

    # Si rien en staged, diff avec HEAD
    result = subprocess.run(
        ['git', 'diff', 'HEAD'],
        cwd=project_root,
        capture_output=True,
        text=True
    )
    return result.stdout


def analyser_doc(wrapper, diff, model="llama3.2"):
    """Analyse le diff avec l'IA et genere des suggestions."""
    prompt = f"""Tu es un assistant de documentation technique.

Analyse ce diff git et propose des ameliorations de documentation:

{diff[:5000]}

INSTRUCTIONS:
1. Identifie les fonctions/classes ajoutees ou modifiees
2. Verifie si elles ont de la documentation (Javadoc ou docstring)
3. Si documentation manquante ou incomplete, propose un ajout
4. Sois concis et precise

Format de reponse:
- Liste les fichiers concernes
- Pour chaque fichier, propose la documentation manquante
"""

    result = wrapper.generate_text(model=model, prompt=prompt)
    return result.response.strip()


def main():
    parser = argparse.ArgumentParser(description="Ameliorateur IA de documentation")
    parser.add_argument('--dry-run', action='store_true', default=True, help='Mode dry-run (par defaut)')
    parser.add_argument('--model', default='llama3.2', help='Modele Ollama')
    args = parser.parse_args()

    project_root = Path(__file__).parent.parent

    print("=== Ameliorateur IA de documentation ===\n")

    # Recuperer le diff
    print("[1/2] Recuperation des changements git...")
    diff = get_git_diff(project_root)
    if not diff:
        print("Aucun changement detecte")
        return 0

    print(f"  {len(diff)} caracteres de diff trouves")

    # Analyser avec l'IA
    print(f"\n[2/2] Analyse avec IA (modele: {args.model})...")
    wrapper = OllamaWrapper()
    suggestions = analyser_doc(wrapper, diff, model=args.model)

    if not suggestions:
        print("Aucune suggestion generee")
        return 1

    # Sauvegarder les suggestions
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = project_root / f"ai_doc_suggestions_{timestamp}.txt"
    output_file.write_text(suggestions, encoding='utf-8')

    print("\n=== Resultat ===")
    print(f"Suggestions generees: {output_file.name}")
    print("\nSuggestions:")
    print(suggestions)

    return 0


if __name__ == '__main__':
    sys.exit(main())
