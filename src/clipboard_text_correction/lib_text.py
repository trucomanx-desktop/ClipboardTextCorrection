import unicodedata

REPLACEMENTS = {
    "∈": " in ",
    "ℝ": " R ",
    "ℕ": " N ",
    "≤": "<=",
    "≥": ">=",
    "≠": "!=",
}

def sanitize_string(s: str) -> str:
    # normaliza Unicode — seguro, não altera texto bom
    s = unicodedata.normalize("NFKC", s)

    # só aplica substituições se houver algum caractere que precisa mudar
    if any(char in s for char in REPLACEMENTS):
        for k, v in REPLACEMENTS.items():
            s = s.replace(k, v)

    # garante UTF-8 válido
    s = s.encode("utf-8", errors="ignore").decode("utf-8")
    
    return s

