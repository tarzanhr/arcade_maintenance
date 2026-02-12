#!/bin/bash
# Script pour verifier la qualite de la documentation markdown

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BORNE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
DOCS_DIR="$BORNE_ROOT/ArcadeDocs/docs"

ERRORS=0

echo "=== Verification qualite documentation ==="
echo ""

# Verifier que le dossier docs existe
if [ ! -d "$DOCS_DIR" ]; then
    echo "ATTENTION: Dossier $DOCS_DIR non trouve"
    echo "Ce script necessite la branche docs avec ArcadeDocs/"
    exit 0
fi

# Fonction pour verifier les liens internes casses
check_broken_links() {
    echo "[1/3] Verification des liens internes..."

    # Trouver tous les liens markdown [text](url)
    while IFS= read -r file; do
        # Extraire les liens internes (pas http/https)
        grep -oP '\[([^\]]+)\]\(([^)]+)\)' "$file" | grep -v 'http' | while read -r link; do
            # Extraire le chemin du lien
            path=$(echo "$link" | sed -n 's/.*(\([^)]*\)).*/\1/p')

            # Ignorer les ancres (#)
            if [[ "$path" == \#* ]]; then
                continue
            fi

            # Construire le chemin complet
            link_file="$(dirname "$file")/$path"

            # Verifier que le fichier existe
            if [ ! -f "$link_file" ] && [ ! -d "$link_file" ]; then
                echo "  ERREUR: Lien casse dans $(basename $file): $path"
                ERRORS=$((ERRORS + 1))
            fi
        done
    done < <(find "$DOCS_DIR" -name "*.md")

    if [ $ERRORS -eq 0 ]; then
        echo "  OK: Aucun lien casse detecte"
    fi
}

# Fonction pour verifier la syntaxe markdown basique
check_markdown_syntax() {
    echo ""
    echo "[2/3] Verification syntaxe markdown..."

    # Verifier les titres sans espace apres #
    BAD_HEADERS=$(grep -r '^#[^# ]' "$DOCS_DIR" --include="*.md" | wc -l)
    if [ $BAD_HEADERS -gt 0 ]; then
        echo "  ATTENTION: $BAD_HEADERS titres sans espace apres # detectes"
        grep -r '^#[^# ]' "$DOCS_DIR" --include="*.md" -n | head -5
    fi

    # Verifier les lignes trop longues (>120 caracteres)
    LONG_LINES=0
    while IFS= read -r file; do
        while IFS= read -r line; do
            if [ ${#line} -gt 120 ]; then
                LONG_LINES=$((LONG_LINES + 1))
            fi
        done < "$file"
    done < <(find "$DOCS_DIR" -name "*.md")

    if [ $LONG_LINES -gt 10 ]; then
        echo "  ATTENTION: $LONG_LINES lignes de plus de 120 caracteres"
    fi

    echo "  OK: Verification syntaxe terminee"
}

# Fonction pour verifier la coherence des fichiers
check_doc_consistency() {
    echo ""
    echo "[3/3] Verification coherence..."

    # Verifier que index.md existe
    if [ ! -f "$DOCS_DIR/index.md" ]; then
        echo "  ERREUR: index.md manquant"
        ERRORS=$((ERRORS + 1))
    else
        echo "  OK: index.md present"
    fi

    # Verifier que mkdocs.yml est valide
    MKDOCS_YML="$BORNE_ROOT/ArcadeDocs/mkdocs.yml"
    if [ -f "$MKDOCS_YML" ]; then
        # Verifier syntaxe YAML basique (indentation)
        if grep -q $'\t' "$MKDOCS_YML"; then
            echo "  ERREUR: mkdocs.yml contient des tabulations (utiliser espaces)"
            ERRORS=$((ERRORS + 1))
        else
            echo "  OK: mkdocs.yml syntaxe correcte"
        fi
    fi
}

# Executer les verifications
check_broken_links
check_markdown_syntax
check_doc_consistency

echo ""
echo "=== Resultat ==="
if [ $ERRORS -eq 0 ]; then
    echo "OK: Aucune erreur detectee"
    exit 0
else
    echo "ERREUR: $ERRORS erreur(s) detectee(s)"
    exit 1
fi
