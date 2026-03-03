#!/usr/bin/env python3
"""
Ameliorateur IA de documentation.
Analyse les changements git et propose des ameliorations de documentation via Ollama.
IMPORTANT: Ce script propose uniquement, il ne modifie JAMAIS automatiquement.
"""

import argparse
import subprocess
import sys
import os
import glob
from pathlib import Path
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, BASE_DIR)
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


def cleanup_old_logs(logs_dir, keep_count=10):
    """Garde seulement les keep_count derniers fichiers de log."""
    log_files = sorted(glob.glob(str(logs_dir / "ai_doc_suggestions_*.txt")), 
                     key=os.path.getmtime, reverse=True)
    
    # Supprimer les vieux logs au-delà de keep_count
    for old_log in log_files[keep_count:]:
        try:
            os.remove(old_log)
            print(f"  Supprimé: {Path(old_log).name}")
        except OSError as e:
            print(f"  Erreur suppression {old_log}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Ameliorateur IA de documentation")
    parser.add_argument('--dry-run', action='store_true', default=True, help='Mode dry-run (par defaut)')
    parser.add_argument('--model', default='gemma2:latest', help='Modele Ollama')
    args = parser.parse_args()

    project_root = Path(__file__).parent.parent
    logs_dir = project_root / "logs"
    
    # Créer le dossier logs s'il n'existe pas
    logs_dir.mkdir(exist_ok=True)
    
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

    # Sauvegarder les suggestions dans le dossier logs
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = logs_dir / f"ai_doc_suggestions_{timestamp}.txt"
    output_file.write_text(suggestions, encoding='utf-8')

    print(f"\n=== Resultat ===")
    print(f"Suggestions generees: logs/{output_file.name}")
    
    # Nettoyer les vieux logs (garder seulement les 10 derniers)
    print("\n[Nettoyage des vieux logs]...")
    cleanup_old_logs(logs_dir, keep_count=10)
    
    print(f"\nSuggestions:")
    print(suggestions)

    return 0


if __name__ == '__main__':
    sys.exit(main())
