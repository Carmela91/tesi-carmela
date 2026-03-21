# analyze_dataset.py
# Script minimo per caricare, verificare e anonimizzare il CSV
import os
import re

CSV_PATH = "test.csv"


try:
    import pandas as pd
except ImportError:  # pragma: no cover
    pd = None

def try_read_csv(path):
    if pd is None:
        print("pandas non è installato. Installa con: python -m pip install pandas")
        return None, None, None

    # Il file CSV usa un separatore ';' e potrebbe non essere in UTF-8.
    # Provo le combinazioni più comuni di separatore + encoding.
    for sep in [";", ",", "\t"]:
        for enc in ["utf-8", "utf-8-sig", "cp1252", "latin-1"]:
            try:
                df = pd.read_csv(path, sep=sep, encoding=enc, engine="python")
                if df.shape[1] > 1:
                    print(f"Letto con separatore={sep!r} e encoding={enc!r}")
                    return df, sep, enc
            except Exception:
                continue

    # Ultimo tentativo: lascio che pandas usi i propri valori predefiniti.
    try:
        df = pd.read_csv(path)
        print("Letto con i valori predefiniti di pandas (separatore/encoding non specificati)")
        return df, None, None
    except Exception as e:
        print("Errore leggendo il CSV:", e)
        return None, None, None

def anonymize_text(s):
    if not isinstance(s, str):
        return s
    s = re.sub(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)+\b', '[REDACTED_NAME]', s)
    s = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '[REDACTED_EMAIL]', s)
    s = re.sub(r'\b\d{6,}\b', '[REDACTED_NUMBER]', s)
    return s

def main():
    if not os.path.exists(CSV_PATH):
        print(f"File non trovato: {CSV_PATH}")
        return

    df, used_sep, used_enc = try_read_csv(CSV_PATH)
    if df is None:
        print("Impossibile leggere il CSV con pandas. Controlla il file o il formato.")
        return

    if used_sep is not None and used_enc is not None:
        print(f"(Usato separatore: {used_sep!r}, encoding: {used_enc!r})")

    # Mi assicuro che le colonne si chiamino 'text' e 'label'
    cols = [c.lower() for c in df.columns]
    if 'text' not in cols or 'label' not in cols:
        # provo a rinominare colonne comuni
        mapping = {}
        if 'column1' in cols:
            mapping[df.columns[cols.index('column1')]] = 'text'
        if 'column2' in cols:
            mapping[df.columns[cols.index('column2')]] = 'label'
        if mapping:
            df = df.rename(columns=mapping)

    print("Shape:", df.shape)
    print("Label counts:\n", df['label'].value_counts(dropna=False))
    print("Missing text:", df['text'].isna().sum())
    print("Duplicati text:", df.duplicated(subset=['text']).sum())

    # Anonimizza e salva
    df['text_anonymized'] = df['text'].astype(str).apply(anonymize_text)
    out = "test_anonymized.csv"
    df[['text_anonymized','label']].to_csv(out, index=False, encoding="utf-8")
    print("File anonimizzato salvato come:", out)

if __name__ == "__main__":
    main()
