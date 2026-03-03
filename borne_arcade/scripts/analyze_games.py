#!/usr/bin/env python3
"""
Analyseur batch de jeux utilisant le script d'analyse individuelle.
Parcourt tous les jeux dans projet/ et génère des présentations individuelles.
"""

import os
import sys
import time
from pathlib import Path
from datetime import datetime
from typing import List, Dict

# Importer l'analyseur individuel
from analyze_single_game import SingleGameAnalyzer


class BatchGameAnalyzer:
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.analyzer = SingleGameAnalyzer(project_root)
        
    def list_available_games(self) -> List[str]:
        """Liste les jeux disponibles."""
        return self.analyzer.list_available_games()
    
    def analyze_all_games(self, model="gemma2:latest", delay=2) -> Dict:
        """Analyse tous les jeux avec l'IA en utilisant l'analyseur individuel."""
        print("🎮" + "="*59)
        print("🎮  ANALYSE BATCH DE JEUX")
        print("🎮" + "="*59)
        
        # Récupérer la liste des jeux
        games = self.list_available_games()
        
        if not games:
            print("❌ Aucun jeu trouvé dans le dossier projet/")
            return {"success": 0, "errors": 0, "total": 0, "games": []}
        
        print(f"📊 {len(games)} jeux détectés pour l'analyse")
        print(f"🤖 Modèle IA utilisé: {model}")
        print(f"⏱️ Délai entre chaque analyse: {delay}s")
        print(f"📁 Dossier de sortie: game_presentations/")
        
        # Analyser chaque jeu
        results = []
        success_count = 0
        error_count = 0
        
        for i, game_name in enumerate(games, 1):
            print(f"\n{'='*59}")
            print(f"[{i}/{len(games)}] 🕹 Analyse du jeu: {game_name}")
            print(f"{'='*59}")
            
            try:
                # Utiliser l'analyseur individuel
                result = self.analyzer.analyze_single_game(game_name, model)
                
                if "erreur" in result.get("jeu", {}):
                    error_count += 1
                    results.append({
                        "game": game_name,
                        "status": "error",
                        "message": result["jeu"]["erreur"]
                    })
                    print(f"❌ Erreur d'extraction: {result['jeu']['erreur']}")
                else:
                    success_count += 1
                    results.append({
                        "game": game_name,
                        "status": "success",
                        "duration": result.get("duration", "N/A"),
                        "files_analyzed": result["jeu"]["nombre_fichiers_total"]
                    })
                    print(f"✅ Analyse réussie")
                
            except Exception as e:
                error_count += 1
                error_msg = str(e)
                results.append({
                    "game": game_name,
                    "status": "error", 
                    "message": error_msg
                })
                print(f"❌ Erreur lors de l'analyse: {error_msg}")
            
            # Délai entre chaque jeu (sauf pour le dernier)
            if i < len(games):
                print(f"⏱️ Pause de {delay}s avant le jeu suivant...")
                time.sleep(delay)
        
        # Résultats finaux
        print(f"\n{'='*59}")
        print(f"🎯 RÉSULTATS DE L'ANALYSE BATCH")
        print(f"{'='*59}")
        print(f"📊 Total de jeux: {len(games)}")
        print(f"✅ Succès: {success_count}")
        print(f"❌ Erreurs: {error_count}")
        print(f"📈 Taux de réussite: {success_count/len(games)*100:.1f}%")
        
        # Détail des résultats
        print(f"\n📋 DÉTAIL PAR JEU:")
        for result in results:
            status_icon = "✅" if result["status"] == "success" else "❌"
            if result["status"] == "success":
                print(f"   {status_icon} {result['game']} ({result['duration']})")
            else:
                print(f"   {status_icon} {result['game']}: {result['message']}")
        
        return {
            "success": success_count,
            "errors": error_count, 
            "total": len(games),
            "games": results
        }
    
    def generate_summary_report(self, results: Dict, output_file: Path = None):
        """Génère un rapport récapitulatif de l'analyse batch."""
        if output_file is None:
            output_file = Path("batch_analysis_summary.md")
        
        content = f"# Rapport d'analyse batch des jeux\n\n"
        content += f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        content += f"**Total de jeux:** {results['total']}\n"
        content += f"**Succès:** {results['success']}\n"
        content += f"**Erreurs:** {results['errors']}\n"
        content += f"**Taux de réussite:** {results['success']/results['total']*100:.1f}%\n\n"
        
        content += "## Détail par jeu\n\n"
        
        for result in results['games']:
            if result['status'] == 'success':
                content += f"- ✅ **{result['game']}** - Succès ({result['duration']})\n"
            else:
                content += f"- ❌ **{result['game']}** - Erreur: {result['message']}\n"
        
        content += f"\n## Fichiers générés\n\n"
        content += "Les présentations individuelles ont été générées dans:\n\n"
        content += "- Dossier `game_presentations/` (compatibilité)\n"
        content += "- Dossier `ArcadeDocs/docs/jeux/` (documentation MkDocs)\n\n"
        
        content += "### Présentations dans la documentation:\n\n"
        
        for result in results['games']:
            if result['status'] == 'success':
                filename = f"{result['game'].lower().replace(' ', '_')}.md"
                content += f"- `{filename}`\n"
        
        content += f"\n## Navigation mise à jour\n\n"
        content += "Les jeux ont été automatiquement ajoutés à la navigation MkDocs dans la section \"Développement\".\n"
        content += "Vous pouvez maintenant consulter les présentations directement sur le site de documentation.\n"
        
        output_file.write_text(content, encoding='utf-8')
        print(f"\n📄 Rapport récapitulatif généré: {output_file}")
        
        # Ajouter à la documentation aussi
        docs_summary = self.project_root / "ArcadeDocs" / "docs" / "batch_analysis_summary.md"
        docs_summary.write_text(content, encoding='utf-8')
        print(f"📚 Rapport ajouté à la documentation: {docs_summary}")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="🎮 Analyseur batch de jeux")
    parser.add_argument('--model', default='gemma2:latest', help='🤖 Modèle Ollama à utiliser')
    parser.add_argument('--delay', type=int, default=2, help='⏱️ Délai entre chaque analyse (secondes)')
    parser.add_argument('--project-root', default='.', help='📂 Racine du projet')
    parser.add_argument('--list', action='store_true', help='📋 Lister les jeux disponibles')
    parser.add_argument('--summary-only', action='store_true', help='📊 Générer uniquement le récapitulatif')
    
    args = parser.parse_args()
    
    project_root = Path(args.project_root).resolve()
    batch_analyzer = BatchGameAnalyzer(project_root)
    
    if args.list:
        print("🎮" + "="*59)
        print("🎮  JEUX DISPONIBLES POUR L'ANALYSE BATCH")
        print("🎮" + "="*59)
        
        games = batch_analyzer.list_available_games()
        if not games:
            print("❌ Aucun jeu trouvé")
            return
        
        for i, game in enumerate(games, 1):
            print(f"   {i:2d}. 🕹 {game}")
        
        print(f"\n📊 Total: {len(games)} jeux")
        print(f"🚀 Usage: python3.14 scripts/analyze_games.py")
        return
    
    if args.summary_only:
        print("📊 Mode récapitulatif uniquement - utilisez les présentations existantes")
        # Ici on pourrait scanner les fichiers existants et générer un récapitulatif
        return
    
    # Analyse batch complète
    print(f"🚀 DÉMARRAGE DE L'ANALYSE BATCH COMPLÈTE")
    print(f"⏰ Début: {datetime.now().strftime('%H:%M:%S')}")
    
    start_time = time.time()
    results = batch_analyzer.analyze_all_games(args.model, args.delay)
    end_time = time.time()
    
    # Générer le rapport récapitulatif
    batch_analyzer.generate_summary_report(results)
    
    # Durée totale
    total_duration = end_time - start_time
    print(f"\n⏱️ Durée totale: {total_duration//60}min {total_duration%60:.1f}s")
    
    print(f"\n🎮" + "="*59)
    print(f"🎮  ANALYSE BATCH TERMINÉE")
    print(f"🎮" + "="*59)
    
    if results['success'] > 0:
        print(f"📁 Consultez les présentations dans: game_presentations/")
        print(f"📊 Récapitulatif dans: batch_analysis_summary.md")
    
    print(f"🎉 {results['success']} présentations générées avec succès!")


if __name__ == '__main__':
    main()
