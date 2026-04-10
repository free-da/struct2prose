# struct2prose

**struct2prose** ist eine Python-basierte Vorverarbeitungspipeline zur semantischen Kontextualisierung strukturierter und semistrukturierter Wiki-Inhalte für den Einsatz in Retrieval-Augmented-Generation-(RAG)-Systemen.

Das Projekt entstand im Rahmen einer Masterarbeit mit dem Ziel, die Nutzbarkeit strukturierter technischer Dokumentationen für Large Language Models systematisch zu verbessern.

---

## Zielsetzung

Technische Wiki-Systeme enthalten häufig einen hohen Anteil an strukturierten und semistrukturierten Inhalten, insbesondere Tabellen, Listen und Konfigurationsfragmente. Diese sind für RAG-Systeme nur eingeschränkt nutzbar, da ihre Bedeutung stark vom Kontext abhängt und in fragmentierter Form vorliegt.

**struct2prose** verfolgt daher das Ziel, solche Inhalte in eine **semantisch explizite, prosebasierte Wissensrepräsentation** zu überführen.

Dabei stehen folgende Prinzipien im Vordergrund:

* **Explizite Strukturierung** statt impliziter HTML-Repräsentation
* **Semantische Kontextualisierung** statt rein syntaktischer Transformation
* **Nachvollziehbarkeit und Reproduzierbarkeit** der Verarbeitungsschritte
* **Trennung deterministischer und LLM-basierter Verarbeitung**

---

## Architekturüberblick

Die Pipeline ist als **mehrstufiges Transformationsmodell** konzipiert, bei dem ein Dokument schrittweise in unterschiedliche semantische Zustände überführt wird.

### Dokumentzustände

Ein Dokument durchläuft folgende logisch getrennte Zustände:

1. **SourceDocument** – Rohdaten (HTML)
2. **CleanDocument** – extrahierter Inhaltsbereich
3. **StrippedDocument** – bereinigter Content ohne UI-/Navigationsanteile
4. **ParsedDocument** – strukturierte Repräsentation (Abschnitte, Blöcke)
5. **ContextualizedDocument** – semantisch angereicherte Inhalte in Prosaform

Diese Zustände werden durch explizite Datenstrukturen modelliert und bilden die Grundlage für alle Transformationen innerhalb der Pipeline.

---

## Verarbeitungsschritte

Die Transformation erfolgt in vier logisch getrennten Schritten:

1. **Extraktion des Inhaltsbereichs**
   Identifikation und Isolation des fachlich relevanten HTML-Bereichs.

2. **Entfernung von UI-Elementen**
   Regelbasierte Bereinigung von Navigations- und Präsentationsartefakten.

3. **Strukturelles Parsing**
   Überführung des bereinigten HTML in ein explizites Objektmodell bestehend aus:

   * Dokumenten
   * Abschnitten
   * typisierten Inhaltsblöcken (z. B. Paragraphen, Listen, Tabellen, Code)

4. **Semantische Kontextualisierung (LLM)**
   Selektive Transformation strukturierter Inhalte (insbesondere Tabellen und Listen) in beschreibenden Fließtext.

---

## Verarbeitungsprinzip

Die Pipeline folgt einem **hybriden Ansatz**:

### Deterministische Verarbeitung

* DOM-Extraktion
* UI-Bereinigung
* strukturelles Parsing

Diese Schritte sind vollständig regelbasiert und reproduzierbar.

### Probabilistische Verarbeitung

* semantische Kontextualisierung mittels LLM

Dieser Schritt erzeugt kontextabhängige, sprachliche Repräsentationen strukturierter Inhalte.

---

## Datenmodell

Die Pipeline basiert auf einem expliziten internen Datenmodell, das die Transformation strukturiert unterstützt.

Zentrale Konzepte sind:

* **DocumentMetadata** – Kontext- und Herkunftsinformationen
* **ContentBlock** – kleinste semantische Einheit (z. B. Tabelle, Liste)
* **Section** – hierarchische Gliederung des Dokuments
* **ContextualizedBlock** – durch LLM erzeugte Prosaeinheiten

Das Datenmodell dient als zentrale Schnittstelle zwischen den Verarbeitungsschritten und ermöglicht eine gezielte, blockweise Transformation.

---

## Persistenz und Nachvollziehbarkeit

Zur Sicherstellung von Reproduzierbarkeit und Nachvollziehbarkeit werden Pipeline-Ausführungen und Artefakte persistiert.

Hierfür wird eine relationale Datenbank verwendet, in der u. a. folgende Aspekte gespeichert werden:

* Pipeline-Ausführungen (Runs)
* Verarbeitungsschritte (Step Runs)
* Dokumentversionen je Verarbeitungsstufe
* Kontextualisierungsaufgaben und deren Ergebnisse

Diese Persistenzschicht ermöglicht eine detaillierte Analyse und Wiederholbarkeit der Verarbeitung.

---

## Aktueller Implementierungsstand

Die Pipeline ist konzeptionell als **objektbasierte Verarbeitungskette** ausgelegt.
Die Transformation erfolgt intern auf expliziten Dokumentobjekten.

Im aktuellen Entwicklungsstand werden Zwischenzustände zusätzlich als **serialisierte JSON-Artefakte** gespeichert und zwischen den Schritten übergeben.

Diese Dateibasierung dient derzeit:

* der **Debugbarkeit**
* der **schrittweisen Entwicklung**
* der **Reproduzierbarkeit von Zwischenergebnissen**

Langfristig ist vorgesehen, die Orchestrierung so umzubauen, dass die Übergabe zwischen den Schritten **direkt über Objekte** erfolgt und die Persistierung ausschließlich eine unterstützende Rolle einnimmt.

---

## Nutzung

Die Pipeline wird über eine modulbasierte CLI gesteuert:

```bash
python -m struct2prose <command>
```

### Einzelne Schritte

```bash
python -m struct2prose extract-root
python -m struct2prose strip-ui
python -m struct2prose parse
python -m struct2prose contextualize
```

### End-to-End-Ausführung

```bash
python -m struct2prose all
```

---
## Konfiguration (.env)

Die Pipeline wird über Environment-Variablen konfiguriert, die typischerweise in einer `.env`-Datei im Projektverzeichnis definiert werden. Diese Konfiguration steuert insbesondere die Anbindung des verwendeten Large Language Models sowie grundlegende Systemparameter.

Ein Beispiel für eine `.env`-Datei ist:

```
LLM_PROVIDER=groq

LOCAL_MODEL_NAME="qwen-2.5"
LOCAL_LLM_BASE_URL=http://10.200.200.11:8000

GROQ_API_KEY="..."
GROQ_MODEL_NAME="llama-3.3-70b-versatile"

DATA_PATH=./data
```

### LLM-Anbindung

Die Pipeline unterstützt unterschiedliche LLM-Provider, die über die Variable `LLM_PROVIDER` ausgewählt werden.

#### Groq (Cloud-basiert)

Bei Verwendung von `LLM_PROVIDER=groq` wird ein extern gehostetes Modell über die Groq-API angesprochen.

Erforderliche Parameter:

* `GROQ_API_KEY` – API-Schlüssel für den Zugriff auf den Dienst
* `GROQ_MODEL_NAME` – Name des verwendeten Modells

#### Lokales LLM

Bei Verwendung von `LLM_PROVIDER=local` erfolgt die Anbindung an ein lokal betriebenes Modell über eine HTTP-Schnittstelle.

Erforderliche Parameter:

* `LOCAL_MODEL_NAME` – Name des lokal bereitgestellten Modells
* `LOCAL_LLM_BASE_URL` – Basis-URL des lokalen Inferenzservers

Dieses Setup ermöglicht insbesondere den Einsatz der Pipeline in abgeschotteten oder datenschutzsensiblen Umgebungen.

---

### Datenpfad

* `DATA_PATH` definiert ein optionales Basisverzeichnis für Datenablagen innerhalb der Pipeline.

---

### Designprinzip

Die Konfiguration ist bewusst so gestaltet, dass die LLM-Anbindung **von der eigentlichen Pipeline-Logik entkoppelt** ist. Dadurch kann zwischen unterschiedlichen Modellen und Anbietern gewechselt werden, ohne die Verarbeitungsschritte selbst anzupassen.

Dies unterstützt insbesondere:

* flexible Experimente mit verschiedenen Modellen
* Migration von Cloud- zu lokalen LLMs
* reproduzierbare Pipeline-Ausführungen mit definierter Modellkonfiguration

---

## Kontext

Das Projekt entsteht im Rahmen einer Masterarbeit mit dem Titel:

**„Semantische Kontextualisierung für RAG-Systeme“**
*Ein Vorgehensmodell zur LLM-gestützten Vorverarbeitung strukturierter Wiki-Inhalte*

Der Fokus liegt auf der **Verbesserung der Wissensrepräsentation** für RAG-Systeme, nicht auf dem Vergleich unterschiedlicher Sprachmodelle.
