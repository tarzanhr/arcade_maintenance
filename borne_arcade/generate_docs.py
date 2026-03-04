#!/usr/bin/env python3
"""
Générateur de documentation MkDocs pour le projet Borne Arcade.
Ce script analyse les fichiers Java source et génère une documentation
structurée pour MkDocs à partir des commentaires Javadoc.
"""

import os
import re
import json
import yaml
from pathlib import Path
from typing import Dict, List, Tuple

class JavaDocGenerator:
    def __init__(self, src_dir: str, docs_dir: str, mkdocs_config: str):
        self.src_dir = Path(src_dir)
        self.docs_dir = Path(docs_dir)
        self.mkdocs_config = Path(mkdocs_config)
        self.classes_info = []
        
    def parse_java_file(self, file_path: Path) -> Dict:
        """Parse un fichier Java et extrait les informations de documentation."""
        content = file_path.read_text(encoding='utf-8')
        
        # Extraire la documentation de classe
        class_match = re.search(r'/\*\*(.*?)\*/\s*public\s+class\s+(\w+)', content, re.DOTALL)
        if not class_match:
            return None
            
        class_doc = self.clean_javadoc(class_match.group(1))
        class_name = class_match.group(2)
        
        # Extraire les méthodes
        methods = []
        method_pattern = r'/\*\*(.*?)\*/\s*(?:public|private|protected)\s+(?:static\s+)?[\w<>]+\s+(\w+)\s*\([^)]*\)'
        for match in re.finditer(method_pattern, content, re.DOTALL):
            method_doc = self.clean_javadoc(match.group(1))
            method_name = match.group(2)
            methods.append({
                'name': method_name,
                'documentation': method_doc
            })
        
        # Extraire les attributs
        attributes = []
        attr_pattern = r'/\*\*(.*?)\*/\s*(?:public|private|protected)\s+(?:static\s+)?(\w+(?:<[^>]+>)?)\s+(\w+)\s*[;=]'
        for match in re.finditer(attr_pattern, content, re.DOTALL):
            attr_doc = self.clean_javadoc(match.group(1))
            attr_type = match.group(2)
            attr_name = match.group(3)
            attributes.append({
                'name': attr_name,
                'type': attr_type,
                'documentation': attr_doc
            })
        
        return {
            'name': class_name,
            'file': file_path.name,
            'class_documentation': class_doc,
            'methods': methods,
            'attributes': attributes
        }
    
    def clean_javadoc(self, javadoc: str) -> str:
        """Nettoie le texte Javadoc pour le rendre lisible en Markdown."""
        # Supprimer les étoiles et les balises HTML
        cleaned = re.sub(r'\s*\*\s?', ' ', javadoc)
        cleaned = re.sub(r'<[^>]+>', '', cleaned)
        cleaned = re.sub(r'\{@link\s+([^}]+)\}', r'`\1`', cleaned)
        cleaned = re.sub(r'\{@code\s+([^}]+)\}', r'`\1`', cleaned)
        cleaned = re.sub(r'\n\s+', '\n', cleaned)
        cleaned = cleaned.strip()
        
        # Convertir les paragraphes
        cleaned = re.sub(r'\s*<p>\s*', '\n\n', cleaned)
        cleaned = re.sub(r'\s*</p>\s*', '\n\n', cleaned)
        
        return cleaned.strip()
    
    def generate_class_doc(self, class_info: Dict) -> str:
        """Génère la documentation Markdown pour une classe."""
        doc = f"# {class_info['name']}\n\n"
        doc += f"**Fichier source:** `{class_info['file']}`\n\n"
        
        if class_info['class_documentation']:
            doc += f"## Description\n\n{class_info['class_documentation']}\n\n"
        
        if class_info['attributes']:
            doc += "## Attributs\n\n"
            for attr in class_info['attributes']:
                doc += f"### `{attr['name']}` : `{attr['type']}`\n\n"
                if attr['documentation']:
                    doc += f"{attr['documentation']}\n\n"
        
        if class_info['methods']:
            doc += "## Méthodes\n\n"
            for method in class_info['methods']:
                doc += f"### `{method['name']}()`\n\n"
                if method['documentation']:
                    doc += f"{method['documentation']}\n\n"
        
        return doc
    
    def generate_index(self) -> str:
        """Génère la page d'index de la documentation."""
        doc = "# Documentation du projet Borne Arcade\n\n"
        doc += "Bienvenue dans la documentation du projet Borne Arcade de l'IUT de Calais.\n\n"
        doc += "## Guide rapide\n\n"
        doc += "- **[Utilisation](utilisation.md)** : Comment utiliser la borne arcade\n"
        doc += "- **[Code Source](src.md)** : Architecture et documentation des classes\n"
        doc += "- **[Développement](#développement)** : Ajouter des jeux et développer\n\n"
        doc += "## Développement\n\n"
        doc += "- **[Ajouter un jeu](ajout_jeu.md)** : Guide pour intégrer de nouveaux jeux\n\n"
        doc += "## Documentation des classes\n\n"
        doc += "La documentation détaillée des classes Java est accessible depuis la page **[Code Source](src.md)**.\n"
        
        return doc
    
    def update_mkdocs_config(self):
        """Met à jour uniquement la section Code Source dans mkdocs.yml sans toucher au reste."""
        with open(self.mkdocs_config, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)

        # Reconstruire la section Code Source uniquement
        code_source_entries = [{"Vue d'ensemble": "src.md"}]
        for class_info in sorted(self.classes_info, key=lambda x: x['name']):
            code_source_entries.append({class_info['name']: f"src/{class_info['name']}.md"})

        # Mettre a jour uniquement la section "Code Source" dans la nav existante
        for i, entry in enumerate(config.get('nav', [])):
            if isinstance(entry, dict) and 'Code Source' in entry:
                config['nav'][i] = {'Code Source': code_source_entries}
                break

        with open(self.mkdocs_config, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    
    def generate_documentation(self):
        """Génère toute la documentation."""
        print("Génération de la documentation...")
        
        # Créer le répertoire docs s'il n'existe pas
        self.docs_dir.mkdir(exist_ok=True)
        
        # Créer le sous-dossier src pour la documentation du code source
        src_docs_dir = self.docs_dir / "src"
        src_docs_dir.mkdir(exist_ok=True)
        
        # Parser tous les fichiers Java
        java_files = list(self.src_dir.glob("*.java"))
        
        for java_file in java_files:
            print(f"Analyse de {java_file.name}...")
            class_info = self.parse_java_file(java_file)
            if class_info:
                self.classes_info.append(class_info)
                
                # Générer le fichier de documentation pour cette classe
                doc_content = self.generate_class_doc(class_info)
                doc_file = src_docs_dir / f"{class_info['name']}.md"
                doc_file.write_text(doc_content, encoding='utf-8')
                print(f"  -> {doc_file}")
        
        # Générer l'index
        index_content = self.generate_index()
        index_file = self.docs_dir / "index.md"
        index_file.write_text(index_content, encoding='utf-8')
        print(f"  -> {index_file}")
        
        # Mettre à jour mkdocs.yml
        self.update_mkdocs_config()
        print(f"  -> {self.mkdocs_config}")
        
        print(f"\nDocumentation générée avec succès !")
        print(f"Classes documentées: {len(self.classes_info)}")
        print(f"\nPour construire le site:")
        print(f"  cd {self.docs_dir.parent}")
        print(f"  mkdocs build")
        print(f"\nPour servir le site localement:")
        print(f"  mkdocs serve")

def main():
    """Point d'entrée principal."""
    # Chemins relatifs au script
    script_dir = Path(__file__).parent
    src_dir = script_dir / "src"
    docs_dir = script_dir / "ArcadeDocs" / "docs"
    mkdocs_config = script_dir / "ArcadeDocs" / "mkdocs.yml"

    generator = JavaDocGenerator(str(src_dir), str(docs_dir), str(mkdocs_config))
    generator.generate_documentation()

if __name__ == "__main__":
    main()
