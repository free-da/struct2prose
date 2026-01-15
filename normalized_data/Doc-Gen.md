# Doc-Gen

## Einleitung

Die Liste aus der technischen Wiki-Seite für Doc-Gen umfasst verschiedene Aspekte und Schritte im Zusammenhang mit der Anwendung und ihrer Entwicklung. Hier ist eine Zusammenfassung der Liste in gut lesbarer Form:

Die Dokumentation von Doc-Gen beginnt mit einem **Vorwort**, das den Kontext und den Zweck der Anwendung einführt. Für fachliche Fragen und IT-externen Ansprechpartner gibt es spezifische **Ansprechpartner**, die für Unterstützung zur Verfügung stehen.

Die **Dokumentenablage** erfolgt in verschiedenen Systemen, einschließlich ORGA-Dateisystem, Doc-Gen-Wiki und GIT-Anleitungen. Für die technische Infrastruktur sind **Server** wie Anwendungsserver, Datenbank-Server und nützliche Server-Befehle relevant. Die Anwendung verarbeitet verschiedene Arten von **Daten**, darunter fachliche Daten und personenbezogene Daten.

Ein wichtiger Aspekt ist die **Systemarchitektur** von Doc-Gen, Version 1.8, die die Struktur und die Komponenten der Anwendung beschreibt. Die Anwendung besteht aus verschiedenen **Bestandteilen**, einschließlich Testsystemen, Operator/Converter, Integration Server (EIS) und Konfigurationseiten. Diese Komponenten sind sowohl im Test- als auch im Produktivsystem vorhanden.

Für die Konfiguration und den Betrieb der Anwendung sind **Abhängigkeiten von anderen Anwendungen** zu berücksichtigen. Darüber hinaus gibt es wichtige **Termine** und einen **zeitlichen Verlauf**, der die Entwicklung und die Aktualisierungen der Anwendung dokumentiert. Hier sind die wichtigsten Schritte:

1. **09.10.2023**: Plan-B-Migration in RZ Bundesallee
2. **08.12.2022**: Installation von Doc-Gen Operator, Converter und teilweise EIS auf schwubs374
3. **07.12.2022**: Installation von JBoss
4. **01.12.2022**: Neuer Doc-Gen-Server schwubs374
5. **21.09.2022**: Start für das Update auf Version 1.8
6. **19.01.2017**: OTRS-Ticket #10021325
7. **27.10.2016**: Aktualisierung der Testdatenbank
8. **11.01.2017**: Vorbereitung der Aktualisierung der Produktion
9. **27.08.2018**: Untersuchung der Ghostscript-Schwachstelle

Zusammenfassend umfasst die Liste eine Vielzahl von Aspekten, von der Systemarchitektur und den Bestandteilen der Anwendung bis hin zu wichtigen Terminen und Schritten in der Entwicklung und Wartung von Doc-Gen.

## Vorwort Bearbeiten

Generierung von Dokumenten für die Zulassung von Pflanzenschutzmitteln auf Basis von Faktendatenbanken (Bsp. Abt. 2 INFOZUPF) Die Dokumente werden in das VBS übertragen und von dort aus an den Antragsteller übermittelt

## Ansprechpartner Bearbeiten

## Fachlich Bearbeiten

Britta Busch

## IT Bearbeiten

Die Liste aus dem Abschnitt "IT" des Dokuments "Doc-Gen" enthält eine Aufzählung von Personen, die offensichtlich mit IT-bezogenen Aufgaben oder Projekten in Verbindung stehen. Die Liste umfasst folgende Personen:

Die Liste besteht aus einer Reihe von Namen, die möglicherweise an einem IT-Projekt oder einer IT-Abteilung beteiligt sind. Die genannten Personen sind:
- Diana Stölzel
- Vladislav Konov
- Hans Labod
- Alexandra Freytag
- Andreas Stengl

Diese Personen könnten als Teammitglieder, Experten oder Verantwortliche für bestimmte IT-Aufgaben fungieren. Ohne weitere Kontextinformationen ist es schwierig, ihre genaue Rolle oder den Zweck der Liste zu bestimmen. Es könnte sich jedoch um eine Kontaktliste, eine Teamzusammensetzung oder eine Liste von Fachleuten handeln, die für bestimmte IT-bezogene Anliegen zuständig sind.

## Extern Bearbeiten

Die Liste fasst die Kontaktdaten und Ressourcen für die externe Bearbeitung von Doc-Gen zusammen. Hier sind die wichtigsten Informationen:

Für Fragen und Anliegen stehen verschiedene Ansprechpartner zur Verfügung. Der Account Manager ist Claudia Theobald, die unter der E-Mail-Adresse Claudia.Theobald@doc-gen.de erreichbar ist. Für technische Fragen und Koordination ist Lars Decker zuständig, der unter Lars.Decker@doc-gen.de kontaktiert werden kann. Darüber hinaus gibt es einen speziellen Ansprechpartner für Doc-Gen EIS, nämlich Frederik Zimmer, der unter Frederik.Zimmer@doc-gen.de erreichbar ist.

Wenn Sie technische Probleme haben oder Unterstützung benötigen, können Sie auch das Support-Portal unter https://service.doc-gen-software.de besuchen.

Es gibt keine spezifischen Schritte, die befolgt werden müssen, da es sich hier um eine Liste von Kontaktdaten und Ressourcen handelt. Stattdessen können Sie die oben genannten Informationen verwenden, um den richtigen Ansprechpartner für Ihre Anliegen zu finden.

## Dokumentenablage Bearbeiten

## ORGA Dateisystem Bearbeiten

Die Liste bezieht sich auf die Speicherorte von Dateien im Zusammenhang mit dem Dokumenttitel "Doc-Gen" im Abschnitt "ORGA Dateisystem Bearbeiten". Zusammengefasst handelt es sich um zwei verschiedene Pfade, an denen relevante Dateien oder Dokumente abgelegt sind.

Die beiden Speicherorte sind:
1. **\\dateiablage1-bs\Projekte\DokGen**: Dieser Pfad bezieht sich auf den Hauptordner für das Projekt "DokGen" innerhalb des Dateisystems.
2. **\\dateiablage1-bs\Projekte\IT-Anwendungen-Abt2\04_DOC-GEN\04_Dokumentation\DOC-GEN**: Dieser Pfad führt zu einem spezifischen Unterordner innerhalb des Projekts, der sich auf die Dokumentation von "DOC-GEN" konzentriert.

Diese Informationen liefern eine Übersicht über die Organisation der Dateien und Dokumente im Rahmen des Doc-Gen-Projekts und können bei der Suche nach bestimmten Dateien oder bei der Navigation durch das Dateisystem hilfreich sein.

## Doc-Gen Wiki Bearbeiten

Die Liste bezieht sich auf den Zugriff auf die DOC-GEN Wiki-Seite. Hier finden Sie eine Zusammenfassung der Informationen:

Um auf die DOC-GEN Wiki zuzugreifen, müssen Sie folgende Schritte befolgen:
1. Öffnen Sie den Browser und geben Sie die URL **www.doc-gen-wiki.de** ein.
2. Melden Sie sich an, indem Sie den Benutzernamen **doc-gen-help** und das entsprechende Passwort verwenden.
3. Das Passwort finden Sie in der Datei **S0FTW4RE-Kennwoerter.kdbx**, die mit dem Tool Keepass verwaltet wird.

Die DOC-GEN Wiki-Seite bietet Handbücher und Hilfestellung zur Installation und Wartung von Doc-Gen. Durch die Anmeldung auf dieser Seite können Sie auf diese Ressourcen zugreifen und weitere Informationen erhalten.

## GIT Bearbeiten

https://devops.cloud.orga.in.bund.de/scm/repo/A2/2012-DokGen/code/sources/master/

```
git clone https://devops.cloud.orga.in.bund.de/scm/repo/A2/2012-DokGen
```

## Anleitungen Bearbeiten

Die Liste aus der technischen Wiki-Seite umfasst verschiedene Dokumente und Schritte, die für die Installation, den Betrieb und die Wartung von Systemen relevant sind. Zusammengefasst finden sich hier Anleitungen für verschiedene Phasen des Systemlebenszyklus.

Die Liste enthält folgende Punkte:
1. **Installationshandbuch**: Dieses Handbuch befindet sich im Verzeichnis `\\dateiablage1-bs\Abteilung_Z\Grp_A4_Allgemein\Dokumentation\Installationshandbücher` und dient als Leitfaden für die Installation des Systems.
2. **Betriebshandbuch**: Im Verzeichnis `\\dateiablage1-bs\Abteilung_Z\Grp_A4_Allgemein\Dokumentation\Betriebshandbücher` zu finden, bietet es Anleitungen für den täglichen Betrieb und die Wartung des Systems.
3. **Übernahme von Änderungen**: Der letzte Punkt bezieht sich auf den Prozess der Übernahme von Änderungen aus dem Entwicklungssystem in das Produktivsystem, wobei der Schritt "Domänen transportieren" eine spezifische Aktion innerhalb dieses Prozesses darstellt.

Diese Liste bietet somit eine Übersicht über die wichtigsten Dokumente und Schritte, die für den reibungslosen Betrieb und die Weiterentwicklung des Systems erforderlich sind.

## Server Bearbeiten

## Anwendungsserver Bearbeiten

Produktiv: s-0214m.srv.domain.de

Test: s-0224m.srv.domain.de

## Datenbank Server Bearbeiten

Datenbank Server Produktiv: s-0941.db.domain.de:1521/doc-gen19

Datenbank Server Test: s-0941.db.domain.de:1521/tbv19

## Nützliche Server Befehle Bearbeiten

Der Abschnitt "Nützliche Server Befehle" im Dokument "Doc-Gen" enthält eine Liste mit wichtigen Anweisungen für die Verwaltung von Servern. Eine der wichtigsten Aufgaben ist das Starten des Servers. Hier sind die Schritte, um den Server erfolgreich zu starten:

1. **Server starten (als root)**: Um den Server zu starten, müssen Sie als root-Benutzer angemeldet sein. Dieser Schritt ist entscheidend, da nur der root-Benutzer die notwendigen Rechte besitzt, um den Server zu starten und zu konfigurieren.

Zusammenfassend lässt sich sagen, dass die Liste im Abschnitt "Nützliche Server Befehle" vor allem Anweisungen für die grundlegende Verwaltung von Servern enthält, wobei das Starten des Servers als root-Benutzer eine der wichtigsten und grundlegendsten Aufgaben darstellt.

```
systemctl start jboss-eap-rhel
systemctl start tomcat
```

Der Abschnitt "Nützliche Server Befehle" im Dokument "Doc-Gen" behandelt verschiedene Befehle, die für die Verwaltung eines Servers nützlich sein können. Eine der wichtigsten Aktionen, die aufgeführt ist, ist das Stoppen des Servers. Dieser Vorgang ist wichtig, um Wartungsarbeiten durchzuführen oder um den Server aus anderen Gründen zu deaktivieren.

Um den Server zu stoppen, sollten Sie folgende Schritte befolgen:
1. Stellen Sie sicher, dass Sie als root-Benutzer angemeldet sind, da dieser Vorgang administrative Rechte erfordert.
2. Führen Sie den Befehl zum Stoppen des Servers aus. Der genaue Befehl kann je nach Betriebssystem und Server-Software variieren, daher sollten Sie sich an die spezifischen Anweisungen für Ihr System halten.

Es ist wichtig, dass Sie vor dem Stoppen des Servers alle notwendigen Sicherheitsmaßnahmen treffen und sicherstellen, dass alle Benutzer und Prozesse, die vom Server abhängig sind, informiert und vorbereitet sind. Durch das Befolgen dieser Schritte können Sie den Server sicher und kontrolliert stoppen.

```
systemctl stop jboss-eap-rhel
systemctl stop tomcat
```

## Verarbeitete Daten Bearbeiten

## Fachliche Daten Bearbeiten

Zulassungsdaten der Abteilung 2

## Personenbezogene Daten Bearbeiten

Antragstellerdaten

## Systemarchitektur Doc-Gen Ver. 1.8 Bearbeiten

https://devops.cloud.orga.in.bund.de/scm/repo/A2/2012-DokGen/code/sources/master/Doc-Gen1.8/Systemarchitektur_Doc-Gen.png/

## Bestandteile der Anwendung Bearbeiten

## Doc-Gen Ver. 1.8 Testsystem Bearbeiten

Beispielaufruf Webcomposer:

Die Liste bezieht sich auf eine URL, die zum Testsystem von Doc-Gen Ver. 1.8 gehört. Zusammengefasst ermöglicht diese URL den Zugriff auf eine bestimmte Funktion innerhalb des Doc-Gen-Systems.

Um auf diese Funktion zuzugreifen, können Sie folgenden Schritt ausführen:

1. Öffnen Sie Ihren Webbrowser und geben Sie die folgende URL ein: https://doc-gen-test.domain.de:6228/generator-launcher/ui/orga/template-list?antragsnummer=00Z001-00/00&vorgang=27596

Diese URL enthält spezifische Parameter wie die Antragsnummer (00Z001-00/00) und den Vorgang (27596), die für den Zugriff auf bestimmte Funktionen oder Daten innerhalb des Testsystems erforderlich sind. Durch die Eingabe dieser URL können Sie auf die Template-Liste des Doc-Gen-Systems zugreifen und die entsprechenden Funktionen nutzen.

Doc-Gen Operator

Die Liste enthält zwei URLs, die auf das Testsystem von Doc-Gen Ver. 1.8 verweisen. Diese URLs können verwendet werden, um auf die Operator-Oberfläche des Testsystems zuzugreifen.

Zusammengefasst bieten diese URLs zwei Möglichkeiten, auf das Testsystem zuzugreifen:

1. Über die HTTP-Verbindung: http://doc-gen-test.domain.de:6260/doc-gen-web/operator/
2. Über die HTTPS-Verbindung: https://doc-gen-test.domain.de:6428/doc-gen-web/operator/

Diese beiden URLs ermöglichen es, auf die Operator-Oberfläche des Testsystems zuzugreifen, wobei die erste URL eine unverschlüsselte Verbindung (HTTP) und die zweite URL eine verschlüsselte Verbindung (HTTPS) verwendet.

## Testsystem Operator/Converter 1.8

### Tabelle: Kein Titel verfügbar
Da die Tabelle keinen expliziten Titel hat, kann sie basierend auf ihrem Inhalt und dem Kontext, in dem sie gefunden wurde, als "Testsystem-Parameter" bezeichnet werden.

Diese Tabelle stellt eine Sammlung von Parametern oder Konfigurationen für ein Testsystem dar, spezifisch im Zusammenhang mit dem Operator/Converter 1.8. Sie enthält Informationen über verschiedene Bezeichnungen und ihre entsprechenden Werte.

Die Spalten haben folgende Bedeutungen:
- Bezeichnung: Hier werden die Namen oder Identifikatoren der Parameter oder Konfigurationen aufgelistet.
- Wert: Diese Spalte enthält die jeweiligen Werte oder Einstellungen, die den Bezeichnungen zugeordnet sind.

Da die Tabelle leer ist, gibt es keine spezifischen Zeilen, die beschrieben werden können. Die Tabelle bleibt somit ohne weitere Einträge.

### Tabelle: Applikationseinstellungen
Die Tabelle stellt die Einstellungen für eine bestimmte Applikation dar, insbesondere in Bezug auf den Server und die verwendete Software.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die erste Spalte enthält den Namen der Applikation oder eine Beschreibung der Einstellung.
* Die zweite Spalte enthält die Server-Adresse oder weitere Details zur Einstellung.

Die Tabellenzeilen können wie folgt beschrieben werden:
* Die Applikation verwendet den Server mit der Adresse 188.455.5.174, der auch als s-0224m.srv.domain.de bekannt ist.
* Die Applikation verwendet JBoss 7.4, was auf den zuvor genannten Server bezogen ist.

Es ist zu beachten, dass die Tabelle sehr knapp gehalten ist und nur wenige Informationen enthält. Es gibt keine explizite Überschrift oder Unterschrift, die den Titel der Tabelle angibt, daher wurde der Titel "Applikationseinstellungen" gewählt, um den Inhalt der Tabelle zu beschreiben.

### Tabelle: Datenbankverbindungsinformationen
Die Tabelle stellt die Verbindungsinformationen zu einer Datenbank dar, die für den Testsystem Operator/Converter 1.8 verwendet wird.

Die Tabelle enthält folgende Spalten:
* Datenbank: Enthält die Informationen zur Datenbank
* Wert: Enthält die entsprechenden Werte zu den Datenbankinformationen

Die Tabellenzeilen können wie folgt beschrieben werden:
* Die Datenbankverbindung verwendet den Server 188.455.6.52 (s-0941.db.domain.de).
* Die Datenbankverbindung verwendet den Port 1521.
* Die Datenbankverbindung verwendet die SID tbv19.
* Die Datenbankverbindung verwendet den User doc-gentest18.

Es ist zu beachten, dass die Tabelle keine explizite Überschrift enthält, daher wurde der Titel "Datenbankverbindungsinformationen" vergeben, um den Inhalt der Tabelle zu beschreiben.

## Testsystem Doc-Gen Integration Server (EIS) 1.8

### Tabelle: Eigenschaften von Doc-Gen
Die Tabelle "Eigenschaften von Doc-Gen" stellt die verschiedenen Eigenschaften und Werte des Doc-Gen-Systems dar, insbesondere im Kontext der Integration mit dem EIS 1.8. Diese Tabelle bietet einen Überblick über die wichtigsten Parameter und Konfigurationen des Systems.

### Spaltenbeschreibung
* Bezeichnung: Diese Spalte enthält die Namen oder Bezeichnungen der verschiedenen Eigenschaften oder Parameter des Doc-Gen-Systems.
* Wert: Hier sind die entsprechenden Werte oder Einstellungen für jede der aufgelisteten Eigenschaften angegeben.

### Tabelleninhalte
Da die Tabelle leer ist, gibt es keine spezifischen Zeilen, die beschrieben werden können. Die Tabelle besteht lediglich aus den beiden Spalten "Bezeichnung" und "Wert", ohne weitere Einträge.

### Tabelle: Server-Konfiguration
Die Tabelle hat keinen expliziten Titel, daher wird sie als "Server-Konfiguration" bezeichnet.

Diese Tabelle stellt die Konfiguration eines Servers im Zusammenhang mit der Doc-Gen Integration Server (EIS) 1.8 dar. Sie enthält Informationen über die Applikation und den Server.

Die Bedeutung jeder Spalte ist wie folgt:
* Die erste Spalte enthält den Namen der Applikation.
* Die zweite Spalte enthält die Server-Adresse.
* Die dritte Spalte enthält die Version des Tomcat-Servers.

Die Tabellenzeilen können wie folgt beschrieben werden:
* Die erste Zeile beschreibt die Applikation.
* Die zweite Zeile beschreibt den Server, der der Applikation zugeordnet ist, mit der Adresse 188.455.5.174 (s-0224m.srv.domain.de).
* Die dritte Zeile beschreibt den Tomcat-Server, der mit der Version 9 verwendet wird, in Bezug auf die zuvor genannte Applikation.

### Tabelle: EIS-Server-Konfiguration
Die Tabelle "EIS-Server-Konfiguration" stellt die Konfigurationsdetails für den Doc-Gen Integration Server (EIS) 1.8 dar. Sie enthält Informationen über die Datenbankverbindung, die für den Betrieb des Servers erforderlich sind.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die erste Spalte enthält die Kategorie oder den Typ der Konfigurationseinstellung (z.B. Datenbank, Server, Port, SID, User).
* Die zweite Spalte enthält den entsprechenden Wert oder die Details zu jeder Kategorie.

Die Tabellenzeilen können wie folgt beschrieben werden:
* Der Server für die Datenbank ist 188.455.6.52 (s-0941.db.domain.de).
* Der Port für die Datenbankverbindung ist 1521.
* Der SID (System Identifier) für die Datenbank ist tbv19.
* Die Benutzer für die Datenbank sind EISKARMA_dev, EISJPAStore_dev, EISLockRegistry_dev, EISTBHStore_dev und EISUserService_dev.

Es ist zu beachten, dass die Tabelle keine explizite Überschrift enthält, daher wurde der Titel "EIS-Server-Konfiguration" basierend auf dem Inhalt gewählt.

## Konfigurationseiten

Konfigurationfiles liegen im GIT: https://devops.cloud.orga.in.bund.de/scm/repo/A2/2012-DokGen/code/sources/master/Doc-Gen1.8/Prod/

Anpassungen
können auf den entsprechenden Komponenten in den o.g.
Konfigurationsdateien (env.xml und main.xml) vorgenommen werden und dann
auf den dazugehörigen Seiten (s.u.) mit dem user doc-gen_admin_dev
hochgeladen werden.

Bei Änderungen an Datenfeldern oder sonstigen
DB-relevanten Einstellungen ist möglicherweise eine Synchronisierung im
Doc-Gen Operator (s.o.) nötig.

https://doc-gen-test.domain.de:6228/authorization-server/admin/ui/services/orga

https://doc-gen-test.domain.de:6228/eis-runtime/admin/ui/services/orga

https://doc-gen-test.domain.de:6228/eis-runtime/admin/ui/services/orga-adapter

https://doc-gen-test.domain.de:6228/eis-user-manager/admin/ui/services/orga

https://doc-gen-test.domain.de:6228/eis-sql-adapter/admin/ui/services/orga

https://doc-gen-test.domain.de:6228/generator-launcher/admin/ui/services/orga

https://doc-gen-test.domain.de:6228/s0ftw4re-persistence/admin/ui/services/orga

https://doc-gen-test.domain.de:6228/eis-user-manager/ui/orga/usermanagement/login - Benutzer und Rollenadmin

User: doc-gen_admin_dev

Password: S0ftw4re Kennwortdatenbank

## Doc-Gen Ver. 1.8 Produktivsystem Bearbeiten

Beispielaufruf Webcomposer:

Die Liste bezieht sich auf den Abschnitt "Doc-Gen Ver. 1.8 Produktivsystem" und enthält Informationen über die Verwendung des Doc-Gen-Systems. Zusammengefasst handelt es sich um Hinweise und Links zur Nutzung des Systems.

Die Liste enthält zwei spezifische URLs, die zum Doc-Gen-System führen. Die erste URL enthält spezifische Parameter wie eine Antragsnummer und einen Vorgang, während die zweite URL ohne diese Parameter ist. Es gibt auch einen Hinweis darauf, dass keine Bescheide erstellt werden sollten, da diese sonst im Infozupf landen würden.

Um die Liste besser zu verstehen, kann man folgende Schritte befolgen:

1. **Zugriff auf das Doc-Gen-System**: Man kann auf das Doc-Gen-System über die bereitgestellten URLs zugreifen. Die erste URL (`https://doc-gen.domain.de:6228/generator-launcher/ui/orga/template-list?antragsnummer=009999-00/00&vorgang=27596`) enthält spezifische Parameter, die für bestimmte Anträge oder Vorgänge relevant sind.
2. **Verwendung der zweiten URL**: Die zweite URL (`https://doc-gen.domain.de:6228/generator-launcher/ui/orga/template-list?`) kann ohne spezifische Parameter verwendet werden, um allgemeine Informationen oder Listen im Doc-Gen-System abzurufen.
3. **Wichtiger Hinweis**: Es ist wichtig zu beachten, dass keine Bescheide im Doc-Gen-System erstellt werden sollten, da diese sonst im Infozupf landen könnten. Dieser Hinweis dient dazu, eine ungewollte Weiterleitung von Dokumenten zu vermeiden.

Insgesamt bietet die Liste eine kurze Anleitung und wichtige Hinweise zur Nutzung des Doc-Gen-Systems, um sicherzustellen, dass die Benutzer die Plattform effektiv und korrekt verwenden können.

### Tabelle: Doc-Gen Ver. 1.8 Produktivsystem
Die Tabelle stellt die Konfiguration oder Eigenschaften des Doc-Gen Ver. 1.8 Produktivsystems dar. Sie enthält Informationen über verschiedene Bezeichnungen und ihre entsprechenden Werte.

### Spaltenbeschreibung
* Bezeichnung: Diese Spalte enthält die Namen oder Identifikatoren für verschiedene Eigenschaften oder Konfigurationen.
* Wert: Diese Spalte enthält die Werte, die jeder Bezeichnung zugeordnet sind.

### Tabelleninhalte
Leider ist die Tabelle leer, es gibt keine Zeilen mit Inhalten. Daher kann keine detaillierte Beschreibung der Tabellenzeilen erfolgen. Die Tabelle bleibt ohne Inhalt.

### Tabelle: Applikationsserver
Die Tabelle "Applikationsserver" stellt die Verbindung zwischen einer Applikation und ihrem entsprechenden Server dar. Sie enthält Informationen über die Applikation und die zugehörige Server-Adresse.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die erste Spalte enthält den Namen der Applikation.
* Die zweite Spalte enthält die Adresse des Servers, auf dem die Applikation gehostet wird.

Die Tabellenzeile kann wie folgt beschrieben werden:
Die Applikation wird auf dem Server mit der Adresse 188.455.5.164 (s-0214m.srv.domain.de/doc-gen.domain.de) gehostet.

Es gibt keine weiteren Informationen in der Tabelle, da nur eine Zeile vorhanden ist.

### Tabelle: Doc-Gen Ver. 1.8 Produktivsystem-Konfiguration
Die Tabelle stellt die Konfiguration des Doc-Gen Ver. 1.8 Produktivsystems dar und enthält Informationen über die Datenbankverbindung.

### Beschreibung der Spalten
* Die erste Spalte enthält die Kategorien der Konfiguration, wie z.B. "Datenbank", "Server", "Port", "SID" und "User".
* Die zweite Spalte enthält die entsprechenden Werte für jede Kategorie.

### Beschreibung der Tabellenzeilen
Die Datenbank des Doc-Gen Ver. 1.8 Produktivsystems ist konfiguriert mit dem Server 188.455.6.52 (s-0941.db.domain.de). 
Der Port für die Datenbankverbindung ist 1521. 
Der SID für die Datenbankverbindung ist doc-gen19. 
Der User für die Datenbankverbindung ist DOC-GEN_PROD. 

### Zusammenfassung
Insgesamt enthält die Tabelle die notwendigen Informationen für die Konfiguration der Datenbankverbindung des Doc-Gen Ver. 1.8 Produktivsystems.

## Produktivsystem Doc-Gen Intergation Server (EIS) 1.8

### Tabelle: Konfigurationswerte für Doc-Gen Intergation Server (EIS) 1.8
Die Tabelle stellt Konfigurationswerte für den Doc-Gen Intergation Server (EIS) 1.8 dar und enthält Informationen über verschiedene Bezeichnungen und ihre entsprechenden Werte.

### Spaltenbeschreibung
* Bezeichnung: Enthält die Namen oder Beschreibungen von Konfigurationseinstellungen.
* Wert: Enthält die Werte oder Einstellungen, die den jeweiligen Bezeichnungen zugeordnet sind.

### Tabelleninhalte
Da die Tabelle leer ist, gibt es keine Zeilen, die beschrieben werden können. Die Tabelle enthält keine Einträge.

### Tabelle: Server-Informationen
Die Tabelle "Server-Informationen" stellt die Konfiguration des Doc-Gen Intergation Server (EIS) 1.8 dar. Sie enthält Informationen über die Applikation und den Server.

Die Bedeutung jeder Spalte ist wie folgt:
* Applikation: Die Art der Applikation oder Anwendung, die auf dem Server läuft.
* Server: Die Adresse oder der Name des Servers, auf dem die Applikation gehostet wird.

Die Tabellenzeile kann wie folgt beschrieben werden:
Die Applikation wird auf dem Server mit der Adresse 188.455.5.164 (doc-gen.domain.de) gehostet.

Es ist zu beachten, dass die Tabelle nur eine Zeile enthält und daher nicht viel Information bietet. Es fehlen weitere Details über die Applikation und den Server.

### Tabelle: EIS-Verbindungseinstellungen
Die Tabelle "EIS-Verbindungseinstellungen" stellt die Konfigurationseinstellungen für die Verbindung zum Doc-Gen Intergation Server (EIS) 1.8 dar. Diese Tabelle enthält Informationen über die Datenbankverbindung, die zum Betrieb des EIS erforderlich sind.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die erste Spalte enthält die Kategorie oder den Typ der Einstellung (z.B. Datenbank, Server, Port, SID, User).
* Die zweite Spalte enthält den entsprechenden Wert oder die Details zu jeder Kategorie.

Die Tabellenzeilen können wie folgt beschrieben werden:
* Die Datenbank ist auf dem Server 188.455.6.52 (s-0941.db.domain.de) konfiguriert.
* Der Port für die Datenbankverbindung ist 1521.
* Der SID (System Identifier) für die Datenbank ist doc-gen19.
* Der Benutzer für die Datenbankverbindung umfasst mehrere Rollen, darunter EISKARMA, EISJPAStore, EISLockRegistry, EISTBHStore und EISUserService.

Insgesamt bietet diese Tabelle eine Übersicht über die notwendigen Einstellungen, um eine erfolgreiche Verbindung zum EIS herzustellen.

## Konfigurationseiten Bearbeiten

Konfigurationfiles liegen im GIT: https://devops.cloud.orga.in.bund.de/scm/repo/A2/2012-DokGen/code/sources/master/Doc-Gen1.8/Prod/

Anpassungen
können auf den entsprechenden Komponenten in den o.g.
Konfigurationsdateien (env.xml und main.xml) vorgenommen werden und dann
auf den dazugehörigen Seiten (s.u.) mit dem user doc-gen_admin_dev
hochgeladen werden.

Bei Änderungen an Datenfeldern oder sonstigen
DB-relevanten Einstellungen ist möglicherweise eine Synchronisierung im
Doc-Gen Operator (s.o.) nötig.

https://doc-gen.domain.de:6228/authorization-server/admin/ui/services/orga

https://doc-gen.domain.de:6228/eis-runtime/admin/ui/services/orga

https://doc-gen.domain.de:6228/eis-runtime/admin/ui/services/orga-adapter

https://doc-gen.domain.de:6228/eis-user-manager/admin/ui/services/orga

https://doc-gen.domain.de:6228/eis-sql-adapter/admin/ui/services/orga

https://doc-gen.domain.de:6228/generator-launcher/admin/ui/services/orga

https://doc-gen.domain.de:6228/s0ftw4re-persistence/admin/ui/services/orga

https://doc-gen.domain.de:6228/eis-user-manager/ui/orga/usermanagement/login - Benutzer und Rollenadmin

User: doc-gen_admin

Password: S0ftw4re Kennwortdatenbank

## Client Bearbeiten

Der Abschnitt "Client Bearbeiten" im Dokument "Doc-Gen" behandelt die verschiedenen Tools und Anwendungen, die für die Bearbeitung und Verwaltung von Dokumenten verwendet werden können. Hier sind die wichtigsten Punkte zusammengefasst:

Für die Arbeit mit Doc-Gen stehen zwei Hauptkomponenten zur Verfügung: 
1. Der Webbrowser für Endanwender, der als "doc-gen19" bezeichnet wird, ermöglicht es Benutzern, auf eine einfache Weise mit den Dokumenten zu interagieren.
2. Der "Doc-Gen_Designer" ist speziell für Administratoren konzipiert und bietet umfassende Funktionen zur Gestaltung und Verwaltung von Dokumenten.

Diese beiden Komponenten ermöglichen es, die Dokumente sowohl für Endanwender als auch für Administratoren auf eine effiziente und benutzerfreundliche Weise zu bearbeiten und zu verwalten.

## Gruppen in der AD Bearbeiten

Die Liste bezieht sich auf verschiedene Gruppen in der Active Directory (AD) im Zusammenhang mit dem Dokumenttitel "Doc-Gen". Diese Gruppen scheinen in der Verwaltung von Dokumenten und Berichten eine Rolle zu spielen. Hier ist eine Zusammenfassung der Liste in gut lesbarer Form:

Die Gruppen in der AD umfassen verschiedene Bereiche, wie zum Beispiel:
- Die Verwaltung von Zwischeninformationen (Doc-Gen_Zwimis_PSM)
- Die Bearbeitung von Bescheiden (Doc-Gen_Bescheide_PSM)
- Die Erstellung von Zulassungsberichten (Doc-Gen_Zulassungsberichte_PSM)
- Die Nutzung von WebAuthor (WebAuthor_PSM)

Diese Gruppen sind möglicherweise für die Verwaltung und Bearbeitung von Dokumenten und Berichten innerhalb der Organisation verantwortlich. Es handelt sich nicht um eine Schrittfolge, sondern um eine Auflistung von Gruppen, die jeweils für bestimmte Aufgaben zuständig sind.

## Abhängigkeit von anderen Anwendungen Bearbeiten

Infozupf

## Termine Bearbeiten

## zeitlicher Verlauf Bearbeiten

## 09.10.2023 Plan-B-Migration in RZ Bundesallee Bearbeiten

neuer Server Doc-Gen TEST: s-0224m.srv.domain.de, PROD: s-0214.srv.domain.de

## 08.12.2022 Installation Doc-Gen Operator, Converter, tw. EIS auf schwubs374 Bearbeiten

## 07.12.2022 Installation JBoss Bearbeiten

## 01.12.2022 neuer Doc-Gen Server schwubs374 Bearbeiten

Robert hat den neuen Server gestern zur Verfügung gestellt. Java 1.8 und JBoss 7.4 müssen noch installiert werden

## 21.09.2022 Start für das Update auf Version 1.8 Bearbeiten

## 19.01.2017 OTRS: Ticket#10021325 Bearbeiten

## 27.10.2016 (Aktualisierung Testdatenbank) Bearbeiten

Für
die finalen Tests wurden die beiden alten Testdatenbanken
(schwubs098.old.domain.de, SID enzo, Benutzernamen db_doc-gen &
db_tbv) noch einmal in die beiden neuen Testdatenbanken
(schwubs169.old.domain.de, SID tbv, Benutzernamen doc-gentest &
tbvtest) kopiert.

In der Doc-Gen Datenbank wurde die Tabelle Property wie im Betriebshandbuch beschrieben angepasst.

Weiterhin wurde vom bisherigen Testsystem Jackrabbit Subs029.old.domain.de das Repository auf den neuen Testserver Jackrabbit Subs172.old.domain.de kopiert.

Folgende Dateien werden im Vorfeld gesichert.

```
/opt/jackrabbit/repository/conf/repository.xml
/opt/jackrabbit/repository/repository/workspaces/default/workspace.xml
/opt/jackrabbit/repository/repository/workspaces/security/workspace.xml
/opt/jackrabbit/repository/workspaces/default/workspace.xml
/opt/jackrabbit/repository/workspaces/security/workspace.xml
```

SSH Schlüssel auf schwubs172.old.domain.de als tomcat erzeugen

```
ssh-keygen -b 2048 -t rsa
```

Inhalt
von /opt/apache-tomcat-6.0.32/.ssh/id_rsa.pub auf den Server
schwubs029.old.domain.de (/opt/apache-tomcat-6.0.32/.ssh/authorized_keys)
anhängen

Test des Zugriffs

```
ssh -l tomcat6 schwubs029.old.domain.de
```

Anschließend den Ordner /opt/jackrabbit verschieben (sichern).

Anschließend über scp den Ordner /opt/jackrabbit vom schwubs029.old.domain.de auf den schwubs172.old.domain.de kopieren

```
scp -r tomcat6@schwubs029.old.domain.de:/opt/jackrabbit/ /opt/
```

## 11.01.2017 (Vorbereitung Aktualisierung Produktion) Bearbeiten

Geplant ist die Umstellung für den 19.01. 15.00 Uhr. ist das richtig?

Für erledigte Aufgaben ✔ verwenden.

Test:

Die Liste beschreibt eine Reihe von Schritten und Aufgaben, die im Rahmen der Vorbereitung einer Aktualisierung der Produktion durchgeführt wurden. Hier ist eine Zusammenfassung der Liste als gut lesbarer Fließtext:

Im Rahmen der Vorbereitung der Aktualisierung der Produktion wurden verschiedene Schritte durchgeführt. Die wichtigsten Schritte sind:

1. **Ein Template in der neuen Entwicklung anlegen**: Dieser Schritt wurde von H. Busch durchgeführt und erfolgreich abgeschlossen.
2. **Den Domänentransport testen**: H. Busch und Stölzel haben den Domänentransport mit dem neuen Template getestet und bestätigt, dass es funktioniert.
3. **Gen-Admin Konfigurationsdatei anpassen**: Die Konfigurationsdatei wurde von H. Stölzel und Busch angepasst, um die beiden Testvorlagenschlüssel zu entfernen.
4. **Zulassungsbericht erstellen**: H. Stölzel hat einen Zulassungsbericht erstellt.
5. **Berechtigungen überprüfen**: H. Stölzel hat die Berechtigungen mit Frau Bolten oder Stevens überprüft.
6. **Testaufbau Apache einrichten**: Der Testaufbau Apache sollte auf schwubs172.old.domain.de für die Weiterleitung auf schwubs174.old.domain.de:4040/secure/webauthor/ eingerichtet werden, aber dieser Schritt ist noch nicht abgeschlossen, da auf die Rückkehr von Henrik gewartet wird.
7. **Untersuchung der Umleitung**: Es wurde festgestellt, dass beim Aufruf von http://webauthor.old.domain.de:4040/secure/webauthor/ auf http://schwubs031.old.domain.de:4040/secure/webauthor/ umgeleitet wird. Dies liegt wahrscheinlich an einer Softwareanpassung.
8. **Bescheiddaten kontrollieren**: H. Busch und Stölzel haben die Bescheiddaten kontrolliert.
9. **Fehler in Formatierung beheben**: H. Gabel hat einen Fehler in der Formatierung im Testsystem Subs172.old.domain.de untersucht und behoben.
10. **Einrichtung Apache auf schwubs174.old.domain.de**: H. Gabel hat die Einrichtung Apache auf schwubs174.old.domain.de durchgeführt und eine index.html erstellt, die beim Aufruf von http://webauthor.old.domain.de auf schwubs174.old.domain.de:4040/secure/webauthor/ weiterleitet.

Insgesamt wurden die meisten Schritte erfolgreich abgeschlossen, aber einige Aufgaben wie der Testaufbau Apache auf schwubs172.old.domain.de sind noch nicht abgeschlossen.

Am Tag der Umstellung :

Die Liste beschreibt die Vorbereitung und Durchführung einer Aktualisierung der Produktion am 11.01.2017. Hier sind die wichtigsten Schritte und Punkte zusammengefasst:

Die Aktualisierung umfasst mehrere Schritte, die wie folgt durchgeführt wurden:

1. **Export und Import von TBV**: Zunächst wurde die alte Produktion von `srvlnx170.old.domain.de` exportiert und in die neue Produktion auf `Subs169.old.domain.de` importiert. Dieser Schritt wurde von Amir durchgeführt.
2. **Aktualisierung des Jackrabbit Repository**: Anschließend wurde das Jackrabbit Repository von `Subs031.old.domain.de` auf `Subs174.old.domain.de` aktualisiert.
3. **DNS-Umstellung**: Es folgten zwei DNS-Umstellungen: 
   - Die erste Umstellung betraf `doc-gen.old.domain.de`, die von `schwubs031.old.domain.de` auf `schwubs174.old.domain.de` umgestellt wurde. 
   - Die zweite Umstellung betraf `webauthor.old.domain.de`, die ebenfalls von `schwubs031.old.domain.de` auf `schwubs174.old.domain.de` umgestellt wurde. Beide Schritte wurden von Gabel und Lux durchgeführt und mit Dennis per E-Mail abgestimmt.
4. **Fachliche Freigabe**: Nach den technischen Schritten erfolgte die fachliche Freigabe durch Britta Busch.
5. **Abschaltung Altsysteme**: Anschließend wurden die Altsysteme `Subs028.old.domain.de` bis `Subs031.old.domain.de` abgeschaltet.
6. **Anpassung Nagios Überwachung**: Es wurde eine Anpassung der Nagios Überwachung beantragt.
7. **Aktualisierung der Dokumentation**: Zum Abschluss wurde die Dokumentation (Wiki, Installation/Betriebshandbuch) aktualisiert.

Insgesamt umfasst die Liste eine Reihe von Schritten, die zur Vorbereitung und Durchführung einer Aktualisierung der Produktion erforderlich waren. Diese Schritte wurden von verschiedenen Personen durchgeführt und umfassen sowohl technische als auch fachliche Aspekte.

## 2018-08-27 (Untersuchung Ghostscript Schwachstelle) Bearbeiten

Ein Ticket im Supportportal geöffnet ( DOC-GEN Support ESP-5481 )

Ergebnis:

Ghostskript wird nicht verwendet.

... Nein. Ghostscript wird von Doc-Gen nicht verwendet. ... {{/7box}} {{/box}}
