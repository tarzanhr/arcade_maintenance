#!/usr/bin/env python3
"""
Analyseur IA d'un seul jeu avec logs détaillés.
Usage: python3.14 scripts/analyze_single_game.py --game Pong
"""

import os
import re
import json
import sys
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, BASE_DIR)
from ollama_wrapper import OllamaWrapper


class SingleGameAnalyzer:
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.games_dir = project_root / "projet"
        
    def extract_game_info(self, game_path: Path) -> Dict:
        """Extrait les informations brutes du jeu."""
        game_name = game_path.name
        
        print(f"   📂 Extraction des données de: {game_name}")
        
        # Contenu des fichiers sources
        source_contents = {}
        readme_content = ""
        requirements_content = ""
        
        for file_path in game_path.rglob("*"):
            if file_path.is_file():
                relative_path = str(file_path.relative_to(game_path))
                suffix = file_path.suffix.lower()
                
                # Extraire le contenu des fichiers sources
                if suffix in ['.java', '.py', '.c', '.cpp', '.md', '.txt', '.sh']:
                    try:
                        content = file_path.read_text(encoding='utf-8', errors='ignore')
                        source_contents[relative_path] = content[:1000]  # Limiter à 1000 caractères
                    except:
                        source_contents[relative_path] = "[Erreur de lecture]"
                
                # Extraire le contenu README
                if 'readme' in file_path.name.lower():
                    try:
                        readme_content = file_path.read_text(encoding='utf-8', errors='ignore')
                        print(f"   📖 Fichier README trouvé: {file_path.name}")
                    except:
                        readme_content = "[Erreur de lecture du README]"
                
                # Extraire le contenu requirements
                if 'requirement' in file_path.name.lower() or 'dependenc' in file_path.name.lower():
                    try:
                        requirements_content = file_path.read_text(encoding='utf-8', errors='ignore')
                        print(f"   📋 Fichier requirements trouvé: {file_path.name}")
                    except:
                        requirements_content = "[Erreur de lecture des requirements]"
        
        # Structure des dossiers
        folder_structure = []
        for item in game_path.rglob("*"):
            if item.is_dir():
                folder_structure.append(str(item.relative_to(game_path)))
        
        # Noms de fichiers
        file_names = []
        for item in game_path.rglob("*"):
            if item.is_file():
                file_names.append(item.name)
        
        game_info = {
            "nom_jeu": game_name,
            "structure_dossiers": sorted(folder_structure),
            "noms_fichiers": sorted(set(file_names)),
            "contenus_sources": source_contents,
            "readme_content": readme_content,
            "requirements_content": requirements_content,
            "fichiers_java": [f for f in file_names if f.endswith('.java')],
            "fichiers_python": [f for f in file_names if f.endswith('.py')],
            "fichiers_shell": [f for f in file_names if f.endswith('.sh')],
            "presence_readme": bool(readme_content),
            "presence_requirements": bool(requirements_content),
            "nombre_fichiers_total": len(file_names),
            "derniere_modification": self.get_last_modified(game_path)
        }
        
        print(f"   ✅ {len(file_names)} fichiers extraits")
        print(f"   📁 {len(folder_structure)} dossiers trouvés")
        print(f"   📄 {len(game_info['fichiers_java'])} fichiers Java")
        if readme_content:
            print(f"   📖 README disponible ({len(readme_content)} caractères)")
        if requirements_content:
            print(f"   📋 Requirements disponibles ({len(requirements_content)} caractères)")
        
        return game_info
    
    def get_last_modified(self, game_path: Path) -> str:
        """Retourne la date de dernière modification."""
        try:
            mod_time = max(
                f.stat().st_mtime 
                for f in game_path.rglob("*") 
                if f.is_file()
            )
            return datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M")
        except:
            return "Inconnue"
    
    def create_game_prompt(self, game_info: Dict) -> str:
        """Crée un prompt de présentation pour un jeu spécifique."""
        print(f"   📝 Création du prompt de présentation...")
        
        prompt = f"""Tu es un créateur de présentations de jeux vidéo. En te basant sur les informations techniques fournies, crée une présentation attractive et complète du jeu "{game_info['nom_jeu']}".

INFORMATIONS TECHNIQUES:
- Nom du jeu: {game_info['nom_jeu']}
- Nombre de fichiers: {game_info['nombre_fichiers_total']}
- Langages: Java ({len(game_info['fichiers_java'])} fichiers), Python ({len(game_info['fichiers_python'])} fichiers), Shell ({len(game_info['fichiers_shell'])} fichiers)
- Dernière modification: {game_info['derniere_modification']}

"""
        
        # Ajouter le contenu README si disponible
        if game_info['readme_content']:
            prompt += f"README DU JEU:\n{game_info['readme_content'][:1000]}\n\n"
        
        # Ajouter les requirements si disponibles
        if game_info['requirements_content']:
            prompt += f"DÉPENDANCES/REQUIREMENTS:\n{game_info['requirements_content'][:500]}\n\n"
        
        # Ajouter le contenu des fichiers principaux
        prompt += "EXTRAITS DES FICHIERS SOURCES:\n"
        important_files = 0
        for filepath, content in game_info['contenus_sources'].items():
            if any(keyword in filepath.lower() for keyword in ['main', 'game', 'src', 'principal']) and important_files < 3:
                prompt += f"\n--- {filepath} ---\n{content[:800]}\n"
                important_files += 1
        
        prompt += """

PRÉSENTATION DEMANDÉE:
Rédige une présentation complète et attrayante du jeu sous ce format exact:

# {Nom du jeu}

## Description
[Décris le jeu de manière engageante : son concept, son univers, ce qui le rend unique]

## Objectif du jeu
[Explique clairement le but du jeu, ce que le joueur doit accomplir]

## Comment jouer
[Décrit les contrôles, la manière de jouer, les règles du jeu]

## Points forts
[Liste les aspects intéressants du jeu : gameplay, graphismes, originalité, etc.]

## Aspect technique
[Mentionne brièvement les technologies utilisées de manière simple pour comprendre la réalisation]

## Pour qui ?
[Décrit le type de joueurs qui apprécieraient ce jeu : débutants, experts, enfants, etc.]

## Note finale
[Une conclusion qui donne envie d'essayer le jeu]

Style recherché:
- Engageant et enthousiaste
- Accessible même pour des non-techniciens  
- Met en valeur les aspects ludiques
- Reste fidèle aux informations techniques fournies
- Évite le jargon technique trop complexe
- IMPORTANT: N'utilise AUCUN émoji dans ta réponse, ni dans les titres ni dans le contenu

Sois créatif et fais ressortir le côté amusant du jeu !"""
        
        print(f"   ✅ Prompt de présentation de {len(prompt)} caractères créé")
        return prompt
    
    def analyze_single_game(self, game_name: str, model="gemma2:latest") -> Dict:
        """Analyse un seul jeu avec l'IA."""
        print(f"🎮" + "="*59)
        print(f"🎮  ANALYSE DU JEU: {game_name}")
        print(f"🎮" + "="*59)
        
        # Vérifier que le jeu existe
        game_path = self.games_dir / game_name
        if not game_path.exists():
            print(f"❌ Erreur: Le jeu '{game_name}' n'existe pas dans {self.games_dir}")
            return {"error": f"Jeu {game_name} introuvable"}
        
        print(f"📂 Chemin du jeu: {game_path}")
        print(f"🤖 Modèle IA: {model}")
        print(f"⏰ Début: {datetime.now().strftime('%H:%M:%S')}")
        
        try:
            # Étape 1: Extraction des données
            print(f"\n[1/4] 📂 Extraction des données brutes...")
            game_info = self.extract_game_info(game_path)
            
            # Étape 2: Création du prompt
            print(f"\n[2/4] 📝 Création du prompt de présentation...")
            prompt = self.create_game_prompt(game_info)
            
            # Étape 3: Appel à l'IA
            print(f"\n[3/4] 🤖 Génération de la présentation...")
            print(f"   🔄 Connexion au serveur Ollama...")
            
            wrapper = OllamaWrapper()
            
            print(f"   📤 Envoi du prompt ({len(prompt)} caractères)...")
            start_time = time.time()
            
            result = wrapper.generate_text(model=model, prompt=prompt)
            game_presentation = result.response.strip()
            
            end_time = time.time()
            duration = end_time - start_time
            
            print(f"   ✅ Présentation générée en {duration:.1f}s")
            print(f"   📝 Taille de la présentation: {len(game_presentation)} caractères")
            
            # Étape 4: Sauvegarde
            print(f"\n[4/4] 💾 Sauvegarde de la présentation...")
            
            analysis_result = {
                "jeu": game_info,
                "presentation": game_presentation,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "duration": f"{duration:.1f}s",
                "model": model
            }
            
            # Créer le rapport
            output_dir = Path("game_presentations")
            output_dir.mkdir(exist_ok=True)
            
            # Créer le contenu pour le dossier de documentation
            docs_dir = self.project_root / "ArcadeDocs" / "docs" / "jeux"
            docs_dir.mkdir(parents=True, exist_ok=True)
            
            report_content = f"# Presentation du jeu: {game_name}\n\n"
            
            if game_info['readme_content']:
                report_content += f"**README disponible:** Oui\n"
            if game_info['requirements_content']:
                report_content += f"**Requirements disponibles:** Oui\n"
            
            report_content += "## Presentation generee par l'IA\n\n"
            report_content += game_presentation
            
            # Sauvegarder dans game_presentations (pour compatibilité)
            report_file = output_dir / f"presentation_{game_name.lower().replace(' ', '_')}.md"
            report_file.write_text(report_content, encoding='utf-8')
            
            # Sauvegarder dans la documentation MkDocs
            docs_file = docs_dir / f"{game_name.lower().replace(' ', '_')}.md"
            docs_content = f"# {game_name}\n\n"
            docs_content += f"*Présentation générée par IA le {analysis_result['timestamp']}*\n\n"
            docs_content += "---\n\n"
            docs_content += game_presentation
            docs_file.write_text(docs_content, encoding='utf-8')
            
            print(f"   ✅ Présentation sauvegardée: {report_file}")
            print(f"   📚 Ajoutée à la documentation: {docs_file}")
            
            # Mettre à jour le fichier mkdocs.yml
            self.update_mkdocs_config(game_name)
            
            print(f"   🔄 Documentation MkDocs mise à jour")
            
            print(f"\n🎯" + "="*59)
            print(f"🎯  PRÉSENTATION TERMINÉE AVEC SUCCÈS!")
            print(f"🎯" + "="*59)
            print(f"📄 Fichier: {report_file}")
            print(f"⏱️ Durée totale: {duration:.1f}s")
            
            return analysis_result
            
        except Exception as e:
            print(f"\n❌ Erreur lors de l'analyse: {str(e)}")
            return {
                "jeu": {"nom_jeu": game_name, "erreur": str(e)},
                "presentation": f"❌ Erreur: {str(e)}",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    
    def update_mkdocs_config(self, game_name: str):
        """Met à jour le fichier mkdocs.yml pour ajouter le jeu à la navigation."""
        mkdocs_file = self.project_root / "ArcadeDocs" / "mkdocs.yml"
        
        if not mkdocs_file.exists():
            print(f"   ⚠️ Fichier mkdocs.yml non trouvé, skip mise à jour")
            return
        
        try:
            content = mkdocs_file.read_text(encoding='utf-8')
            
            # Vérifier si le jeu est déjà dans la config
            if f'"{game_name}"' in content:
                print(f"   ℹ️ Jeu déjà présent dans mkdocs.yml")
                return
            
            # Trouver la section "Développement" et ajouter le jeu
            lines = content.split('\n')
            new_lines = []
            in_dev_section = False
            
            for i, line in enumerate(lines):
                new_lines.append(line)
                
                # Détecter le début de la section Développement
                if '"Développement":' in line:
                    in_dev_section = True
                    continue
                
                # Ajouter le jeu après "Ajouter un jeu"
                if in_dev_section and '"Ajouter un jeu": ajout_jeu.md' in line:
                    # Ajouter le jeu avec une indentation appropriée
                    indent = '    '
                    game_line = f'{indent}- "{game_name}": jeux/{game_name.lower().replace(" ", "_")}.md'
                    new_lines.append(game_line)
                    in_dev_section = False
            
            # Écrire le fichier mis à jour
            mkdocs_file.write_text('\n'.join(new_lines), encoding='utf-8')
            print(f"   ✅ mkdocs.yml mis à jour avec {game_name}")
            
        except Exception as e:
            print(f"   ⚠️ Erreur mise à jour mkdocs.yml: {str(e)}")
    
    def list_available_games(self) -> List[str]:
        """Liste les jeux disponibles."""
        if not self.games_dir.exists():
            return []
        
        game_dirs = [d.name for d in self.games_dir.iterdir() if d.is_dir() and not d.name.startswith('.')]
        return sorted(game_dirs)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="🎮 Générateur de présentations de jeux")
    parser.add_argument('--game', help='🕹 Nom du jeu à présenter')
    parser.add_argument('--model', default='gemma2:latest', help='🤖 Modèle Ollama à utiliser')
    parser.add_argument('--project-root', default='.', help='📂 Racine du projet')
    parser.add_argument('--list', action='store_true', help='📋 Lister les jeux disponibles')
    
    args = parser.parse_args()
    
    project_root = Path(args.project_root).resolve()
    analyzer = SingleGameAnalyzer(project_root)
    
    if args.list:
        print("🎮" + "="*59)
        print("🎮  JEUX DISPONIBLES")
        print("🎮" + "="*59)
        
        games = analyzer.list_available_games()
        if not games:
            print("❌ Aucun jeu trouvé")
            return
        
        for i, game in enumerate(games, 1):
            print(f"   {i:2d}. 🕹 {game}")
        
        print(f"\n📊 Total: {len(games)} jeux")
        print(f"🎯 Usage: python3.14 scripts/analyze_single_game.py --game <nom>")
        return
    
    # Vérifier qu'un jeu est spécifié
    if not args.game:
        print("❌ Erreur: --game <nom> est requis ou utilisez --list pour voir les jeux disponibles")
        return
    
    # Analyser le jeu spécifié
    result = analyzer.analyze_single_game(args.game, args.model)
    
    if "error" in result:
        print(f"❌ {result['error']}")
    elif "erreur" in result.get("jeu", {}):
        print(f"❌ Erreur: {result['jeu']['erreur']}")
    else:
        print(f"\n🎉 Présentation réussie du jeu: {args.game}")


if __name__ == '__main__':
    main()
