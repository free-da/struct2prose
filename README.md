# struct2prose

**struct2prose** ist eine Python-basierte Vorverarbeitungspipeline zur semantischen Normalisierung strukturierter und semistrukturierter Wiki-Inhalte für den Einsatz in Retrieval-Augmented-Generation-(RAG)-Systemen.

Das Projekt entstand im Rahmen einer (Mini-)Masterarbeit mit dem Fokus auf der Transformation von HTML-basierten Wiki-Seiten (insbesondere Tabellen und Listen) in prosebasierte Wissenseinheiten, um bekannte Schwächen von RAG-Systemen im Umgang mit strukturierten Daten zu adressieren.

---

## Zielsetzung

Viele technische Wikis enthalten einen hohen Anteil an Tabellen, Listen und Konfigurationsfragmenten. Diese Inhalte sind für Large Language Models und RAG-Systeme nur eingeschränkt nutzbar, da sie semantisch fragmentiert und kontextabhängig sind.

**struct2prose** verfolgt daher das Ziel,

- strukturierte Wiki-Inhalte deterministisch zu extrahieren,
- explizit zu parsen und zu typisieren,
- ausgewählte Strukturen (z. B. Tabellen) mittels LLMs in beschreibenden Fließtext zu überführen,
- und die Ergebnisse in einem RAG-freundlichen Markdown-Format bereitzustellen.

Der Fokus liegt auf **Nachvollziehbarkeit, Modularität und Reproduzierbarkeit**, nicht auf maximaler Automatisierung.

---

## Pipeline-Überblick

Die Pipeline besteht aus vier logisch getrennten Verarbeitungsschritten:

1. **Extraktion des Inhaltsbereichs**  
   Auswahl des fachlichen Hauptinhalts aus HTML-Wiki-Exporten (z. B. `#xwikicontent`).

2. **Entfernung verbliebener UI-Elemente**  
   Regelbasierte Entfernung von Navigations-, Inhaltsverzeichnis- und Editier-UI.

3. **Parsing in ein strukturiertes Zwischenformat**  
   Überführung des HTML in eine explizite JSON-Repräsentation bestehend aus Dokumenten, Abschnitten und typisierten Inhaltsblöcken.

4. **LLM-gestützte semantische Normalisierung**  
   Selektive Normalisierung strukturierter Inhalte (insb. Tabellen) mittels eines Large Language Models und Ausgabe als Markdown.

---

## Projektstruktur

```text
.
├── raw_data/           # HTML-Exporte der Wiki-Seiten
├── clean_data/         # Bereinigte HTML-Dateien
├── processed_data/     # JSON-Zwischenformat (strukturierte Repräsentation)
├── normalized_data/    # Normalisierte Markdown-Dokumente
├── src/
│   └── struct2prose/
│       ├── cli.py
│       ├── parser/
│       ├── preprocessing/
│       └── steps/
├── pyproject.toml
└── README.md
```
## Installation

### Voraussetzungen
- Python ≥ 3.10
- Ein gültiger Groq API Key (für die semantische Normalisierung)

### Installation im Projektverzeichnis

```bash
pip install -e .
```
## Konfiguration

Für die Nutzung des Groq-LLMs muss der API-Key als Environment-Variable gesetzt werden.
### Linux / macOS

```bash
export GROQ_API_KEY="sk-..."
```

### Windows (PowerShell)

```powershell
$env:GROQ_API_KEY="sk-..."
```

⚠️ **Hinweis:**  
Wenn das Projekt über das Terminal gestartet wird, muss die Variable auch **im Terminal-Kontext** gesetzt sein.  
Environment-Variablen aus PyCharm Run Configurations gelten **nicht automatisch** für manuelle Terminal-Aufrufe.

## Nutzung

Die Pipeline wird über eine modulbasierte CLI gesteuert:
```bash
python -m struct2prose <command>
```


### Einzelne Verarbeitungsschritte

```bash
python -m struct2prose extract-root
python -m struct2prose strip-ui
python -m struct2prose parse
python -m struct2prose normalize
```

### End-to-End-Ausführung (MVP)

```bash
python -m struct2prose all
```

---

## Verwendete Verzeichnisse (Standard)

| Zweck | Verzeichnis |
|-----|-----------|
| Rohdaten (HTML) | `raw_data/` |
| Bereinigtes HTML | `clean_data/` |
| Strukturierte JSON-Daten | `processed_data/` |
| Normalisierte Markdown-Dateien | `normalized_data/` |

Die Verzeichnisse können bei Bedarf über CLI-Parameter überschrieben werden.

## Semantische Normalisierung (LLM)

Die Normalisierung strukturierter Inhalte (Tabellen, Listen, Codeblöcke) erfolgt mithilfe eines Large Language Models über das **Groq-Framework**.

### Standardmodell
- `llama-3.3-70b-versatile`
- Temperatur: `0.2` (deterministische, reproduzierbare Ausgaben)

### Aufgaben des LLM
- Beschreibung der semantischen Bedeutung von Tabellen
- Umwandlung tabellarischer Konfigurationen in Fließtext
- Kontextualisierung von Code- und XML-Blöcken
- Erzeugung gut lesbarer Markdown-Dokumente

Die Ausgabe ist bewusst **prosaorientiert**, um die Nutzbarkeit der Inhalte in RAG-Systemen zu verbessern.

## Projektstatus

Dieses Repository stellt einen **Minimal Viable Prototype (MVP)** dar.  
Ziel ist es, den methodischen Ansatz der semantischen Normalisierung sichtbar und nachvollziehbar zu machen.

Geplante Erweiterungen (nicht Teil des MVP):
- Feinere UI-Bereinigung (Step 2)
- Strukturierte Tabellen-Normalisierung mit Schema-Erkennung
- Chunking-Strategien für RAG
- Evaluation der Retrieval-Qualität

## Kontext

Das Projekt entsteht im Rahmen einer (Mini-)Masterarbeit mit dem Titel:

**„Semantische Normalisierung für RAG-Systeme“**  
*Ein Vorgehensmodell zur LLM-gestützten Vorverarbeitung strukturierter Wiki-Inhalte*

Der Fokus liegt auf **Wissensmanagement** und **praktischer Nutzbarkeit**, nicht auf Modellvergleich oder Benchmarking.
