# Doc-Gen

## Einleitung

Die Liste aus der technischen Wiki-Seite für Doc-Gen umfasst verschiedene Aspekte und Schritte im Zusammenhang mit der Anwendung Doc-Gen. Sie kann wie folgt zusammengefasst werden:

Die Dokumentation von Doc-Gen beginnt mit einem **Vorwort**, gefolgt von Informationen über den **Ansprechpartner Fachlich IT Extern**, der für Fragen und Probleme zur Verfügung steht. Die **Dokumentenablage** ist in verschiedenen Systemen wie ORGA Dateisystem, Doc-Gen Wiki und GIT Anleitungen zu finden.

Ein wichtiger Teil der Dokumentation ist die **Systemarchitektur von Doc-Gen**, speziell in der Version 1.8. Diese umfasst verschiedene **Bestandteile der Anwendung**, wie das Testsystem, den Operator/Converter, den Integration Server (EIS) und die Konfigurationseiten. Sowohl für das Testsystem als auch für das Produktivsystem sind spezifische Konfigurationen und Servereinstellungen erforderlich.

Die Anwendung **abhängt von anderen Anwendungen** und es gibt bestimmte **Termine** und einen **zeitlichen Verlauf**, der wichtige Ereignisse und Aktualisierungen dokumentiert. Diese Ereignisse können wie folgt aufgelistet werden:

1. **09.10.2023**: Plan-B-Migration in RZ Bundesallee
2. **08.12.2022**: Installation von Doc-Gen Operator, Converter und teilweise EIS auf schwubs374
3. **07.12.2022**: Installation von JBoss
4. **01.12.2022**: Neuer Doc-Gen Server schwubs374
5. **21.09.2022**: Start für das Update auf Version 1.8
6. **19.01.2017**: OTRS: Ticket#10021325
7. **27.10.2016**: Aktualisierung der Testdatenbank
8. **11.01.2017**: Vorbereitung für die Aktualisierung der Produktion
9. **27.08.2018**: Untersuchung der Ghostscript-Schwachstelle

Zusammenfassend kann gesagt werden, dass die Liste eine umfassende Übersicht über die Doc-Gen-Anwendung bietet, einschließlich ihrer Systemarchitektur, Bestandteile, Abhängigkeiten und wichtigen Ereignisse im zeitlichen Verlauf.

## Vorwort

Generierung von Dokumenten für die Zulassung von Pflanzenschutzmitteln auf Basis von Faktendatenbanken (Bsp. Abt. 2 INFOZUPF) Die Dokumente werden in das VBS übertragen und von dort aus an den Antragsteller übermittelt

## Ansprechpartner

## Fachlich

Britta Busch

## IT

Die Liste aus dem Dokument "Doc-Gen" im Abschnitt "IT" enthält eine Aufzählung von Personen, die offensichtlich in einem bestimmten Kontext oder Projekt involviert sind. Da es sich nicht um Schritte handelt, kann die Liste wie folgt zusammengefasst werden:

Die Liste umfasst eine Gruppe von Personen, die möglicherweise an einem IT-Projekt oder einer IT-Initiative beteiligt sind. Zu dieser Gruppe gehören:

- @Diana Stölzel
- @Vladislav Konov
- @Hans Labod
- @Alexandra Freytag
- @Andreas Stengl

Diese Personen könnten als Teammitglieder, Experten oder Verantwortliche in einem bestimmten IT-Projekt oder einer IT-Abteilung fungieren. Ohne weitere Kontextinformationen ist es jedoch schwierig, ihre genaue Rolle oder Funktion zu bestimmen.

## Extern

Die Liste enthält Kontaktdaten und Ressourcen für die technische Unterstützung und Koordination bei Doc-Gen. Zusammengefasst bietet sie Informationen über die Ansprechpartner und Plattformen, die für eine effiziente Kommunikation und Problemlösung zur Verfügung stehen.

Die Liste umfasst folgende Punkte:

* Für Fragen und Anliegen bezüglich des Account-Managements kann man sich an Claudia Theobald unter der E-Mail-Adresse Claudia.Theobald@doc-gen.de wenden.
* Bei technischen Anliegen oder für die Koordination technischer Aspekte ist Lars Decker der richtige Ansprechpartner, erreichbar unter Lars.Decker@doc-gen.de.
* Für spezifische Fragen oder Anliegen im Zusammenhang mit Doc-Gen EIS kann man sich an Frederik Zimmer unter Frederik.Zimmer@doc-gen.de wenden.
* Für allgemeine Support-Anfragen und um Hilfe bei technischen Problemen zu erhalten, kann das Support-Portal unter https://service.doc-gen-software.de besucht werden.

Es gibt keine spezifischen Schritte, die in einer bestimmten Reihenfolge ausgeführt werden müssen, da die Liste hauptsächlich als Informationsquelle dient. Sie bietet eine Übersicht über die verfügbaren Ressourcen und Ansprechpartner, um Benutzern bei der Nutzung von Doc-Gen zu helfen.

## Dokumentenablage

## ORGA Dateisystem

Die Liste bezieht sich auf die Speicherorte von Dateien im ORGA-Dateisystem, insbesondere im Zusammenhang mit dem Dokumenttitel "Doc-Gen". Zusammengefasst handelt es sich um zwei verschiedene Pfade, an denen relevante Dateien oder Dokumentationen für das Projekt "Doc-Gen" abgelegt sind.

Die beiden Speicherorte sind:
1. **Hauptprojektordner**: Die Dateien sind unter `\dateiablage1-bs\Projekte\DokGen` zu finden. Dieser Pfad scheint den Hauptordner für das Projekt "DokGen" zu sein.
2. **Spezifischer Dokumentationsordner**: Weitere Dokumente oder spezifische Dateien für "Doc-Gen" sind unter `\dateiablage1-bs\Projekte\IT-Anwendungen-Abt2\04_DOC-GEN\04_Dokumentation\DOC-GEN` abgelegt. Dieser Pfad ist spezifischer und könnte sich auf eine bestimmte Abteilung oder ein bestimmtes Teilprojekt innerhalb von "Doc-Gen" beziehen.

Diese Informationen sollten es ermöglichen, schnell und effizient die benötigten Dateien und Dokumentationen für das Projekt "Doc-Gen" im ORGA-Dateisystem zu finden.

## Doc-Gen Wiki

Der Doc-Gen Wiki ist eine umfassende Ressource für alle Fragen rund um die Dokumentenerstellung und -verwaltung. Hier findet man Handbücher, Hilfestellung zur Installation und Wartung.

Um auf den Doc-Gen Wiki zuzugreifen, müssen Sie folgende Schritte befolgen:

1. Öffnen Sie Ihren Webbrowser und navigieren Sie zu der URL: www.doc-gen-wiki.de
2. Melden Sie sich an, indem Sie den Benutzernamen "doc-gen-help" und das entsprechende Passwort verwenden. 
3. Um das Passwort zu finden, öffnen Sie die Datei "S0FTW4RE-Kennwoerter.kdbx" mit dem Tool Keepass.

Nachdem Sie diese Schritte befolgt haben, haben Sie Zugriff auf die umfassenden Ressourcen des Doc-Gen Wiki und können alle benötigten Informationen finden, um Ihre Dokumente effizient zu erstellen und zu verwalten.

## GIT

https://devops.cloud.orga.in.bund.de/scm/repo/A2/2012-DokGen/code/sources/master/

```
git clone https://devops.cloud.orga.in.bund.de/scm/repo/A2/2012-DokGen
```

## Anleitungen

Die Liste aus dem Abschnitt "Anleitungen" des Dokuments "Doc-Gen" enthält wichtige Informationen zu Handbüchern und Prozessen. Zusammengefasst bietet sie Zugriff auf verschiedene Handbücher und erklärt den Prozess der Übernahme von Änderungen aus dem Entwicklungssystem in das Produktivsystem.

Die Liste umfasst folgende Punkte:
1. **Installationshandbuch**: Dieses Handbuch kann unter dem Pfad `\\dateiablage1-bs\Abteilung_Z\Grp_A4_Allgemein\Dokumentation\Installationshandbücher` gefunden werden und bietet Anleitungen zur Installation.
2. **Betriebshandbuch**: Ähnlich wie das Installationshandbuch, befindet sich das Betriebshandbuch unter `\\dateiablage1-bs\Abteilung_Z\Grp_A4_Allgemein\Dokumentation\Betriebshandbücher` und enthält Informationen zum Betrieb.
3. **Übernahme der Änderungen**: Der Prozess der Übernahme von Änderungen aus dem Entwicklungssystem in das Produktivsystem wird als "Domänen_transportieren" bezeichnet. Dieser Schritt ist entscheidend für die Implementierung von Änderungen und Aktualisierungen in der Produktivumgebung.

Um diese Schritte auszuführen, können Sie folgende Schrittfolge befolgen:
1. **Zugriff auf Handbücher**: Öffnen Sie die entsprechenden Pfade, um auf das Installationshandbuch und das Betriebshandbuch zuzugreifen.
2. **Übernahme von Änderungen**: Führen Sie den Prozess "Domänen_transportieren" aus, um Änderungen aus dem Entwicklungssystem in das Produktivsystem zu übernehmen.

Diese Schritte sollten sorgfältig durchgeführt werden, um sicherzustellen, dass alle Änderungen korrekt implementiert und die Systeme ordnungsgemäß betrieben werden.

## Server

## Anwendungsserver

Produktiv: s-0214m.srv.domain.de

Test: s-0224m.srv.domain.de

## Datenbank Server

Datenbank Server Produktiv: s-0941.db.domain.de:1521/doc-gen19

Datenbank Server Test: s-0941.db.domain.de:1521/tbv19

## Nützliche Server Befehle

Im Abschnitt "Nützliche Server Befehle" des Dokuments "Doc-Gen" finden Sie wichtige Informationen, um Ihren Server effizient zu verwalten. Die Liste umfasst einen wichtigen Schritt, der für den Betrieb Ihres Servers unerlässlich ist:

Um Ihren Server in Betrieb zu nehmen, müssen Sie folgenden Schritt ausführen:
1. Starten Sie den Server als root-Benutzer. Dieser Schritt ist entscheidend, da er Ihnen die notwendigen Rechte und Zugriffsrechte gewährt, um Ihren Server ordnungsgemäß zu konfigurieren und zu verwalten.

Durch die Ausführung dieses Schritts können Sie sicherstellen, dass Ihr Server korrekt startet und bereit ist für weitere Konfigurationen und Anpassungen. Es ist wichtig, dass Sie als root-Benutzer agieren, um alle notwendigen Berechtigungen zu haben, um Ihren Server effektiv zu verwalten.

```
systemctl start jboss-eap-rhel
systemctl start tomcat
```

Der Abschnitt "Nützliche Server Befehle" im Dokument "Doc-Gen" bietet eine Übersicht über wichtige Befehle, die für die Verwaltung eines Servers benötigt werden. Eine der wichtigsten Aktionen, die auf einem Server durchgeführt werden kann, ist das Stoppen des Servers. Dieser Vorgang sollte jedoch mit Vorsicht und unter den richtigen Umständen durchgeführt werden.

Um den Server zu stoppen, sollten Sie folgende Schritte befolgen:
1. Stellen Sie sicher, dass Sie als root-Benutzer angemeldet sind, da nur dieser Benutzer die notwendigen Rechte besitzt, um den Server zu stoppen.
2. Führen Sie den entsprechenden Befehl aus, um den Server zu stoppen. Der genaue Befehl kann je nach Betriebssystem und Server-Software variieren, daher sollten Sie sich an die spezifischen Anweisungen für Ihr System halten.

Es ist wichtig, dass Sie vor dem Stoppen des Servers alle notwendigen Vorbereitungen treffen, um Datenverluste oder andere unerwünschte Konsequenzen zu vermeiden. Durch das Befolgen dieser Schritte können Sie den Server sicher und kontrolliert stoppen.

```
systemctl stop jboss-eap-rhel
systemctl stop tomcat
```

## Verarbeitete Daten

## Fachliche Daten

Zulassungsdaten der Abteilung 2

## Personenbezogene Daten

Antragstellerdaten

## Systemarchitektur Doc-Gen Ver. 1.8

https://devops.cloud.orga.in.bund.de/scm/repo/A2/2012-DokGen/code/sources/master/Doc-Gen1.8/Systemarchitektur_Doc-Gen.png/

## Bestandteile der Anwendung

## Doc-Gen Ver. 1.8 Testsystem

Beispielaufruf Webcomposer:

Die Liste enthält eine URL, die auf eine bestimmte Seite im Doc-Gen-Testsystem verweist. Diese Seite scheint eine Liste von Vorlagen für einen bestimmten Antrag zu enthalten.

Die URL lautet: https://doc-gen-test.domain.de:6228/generator-launcher/ui/orga/template-list?antragsnummer=00Z001-00/00&vorgang=27596

Um diese Seite zu erreichen, können Sie folgende Schritte ausführen:

1. Öffnen Sie einen Webbrowser und geben Sie die oben genannte URL ein.
2. Drücken Sie die Enter-Taste, um die Seite zu laden.
3. Die Seite sollte eine Liste von Vorlagen für den Antrag mit der Nummer 00Z001-00/00 und dem Vorgang 27596 anzeigen.

Die URL enthält zwei Parameter: "antragsnummer" und "vorgang". Diese Parameter bestimmen, welche Vorlagen auf der Seite angezeigt werden. In diesem Fall werden Vorlagen für den Antrag mit der Nummer 00Z001-00/00 und dem Vorgang 27596 angezeigt.

Doc-Gen Operator

Die Liste enthält zwei URLs, die auf die Testsysteme für Doc-Gen Ver. 1.8 verweisen. Zusammengefasst bieten diese URLs Zugriff auf die Web-Oberfläche des Doc-Gen-Testsystems für den Operator.

Um auf die Testsysteme zuzugreifen, können Sie die folgenden URLs verwenden:

1. **HTTP-Zugriff**: Öffnen Sie Ihren Webbrowser und geben Sie die URL `http://doc-gen-test.domain.de:6260/doc-gen-web/operator/` ein, um auf das Testsystem über HTTP zuzugreifen.
2. **HTTPS-Zugriff**: Alternativ können Sie auch die URL `https://doc-gen-test.domain.de:6428/doc-gen-web/operator/` verwenden, um auf das Testsystem über HTTPS zuzugreifen.

Beide URLs führen Sie zur Operator-Oberfläche des Doc-Gen-Testsystems, wobei die erste URL einen ungesicherten (HTTP) und die zweite URL einen gesicherten (HTTPS) Zugriff bietet.

## Testsystem Operator/Converter 1.8

### Tabelle: Eigenschaften von Doc-Gen
Die Tabelle stellt die Eigenschaften von Doc-Gen im Kontext des Testsystem Operator/Converter 1.8 dar. Sie enthält Informationen über verschiedene Bezeichnungen und ihre entsprechenden Werte.

### Spaltenbeschreibung
* Bezeichnung: Diese Spalte enthält die Namen oder Bezeichnungen von Eigenschaften oder Parametern.
* Wert: Diese Spalte enthält die Werte, die den jeweiligen Bezeichnungen zugeordnet sind.

### Tabelleninhalte
Da die Tabelle leer ist, gibt es keine Zeilen, die beschrieben werden können. Die Tabelle besteht nur aus den Spaltenüberschriften "Bezeichnung" und "Wert", ohne weitere Inhalte.

### Tabelle: Applikation
Die Tabelle "Applikation" stellt Informationen über eine bestimmte Applikation und deren Serverumgebung dar. Sie enthält Details über den Server und die verwendete JBoss-Version.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die erste Spalte enthält den Namen der Applikation oder eine Beschreibung davon.
* Die zweite Spalte enthält Informationen über den Server, einschließlich der IP-Adresse und des Servernamens.
* Die dritte Spalte enthält Informationen über die verwendete JBoss-Version.

Die Tabellenzeilen können wie folgt beschrieben werden:
* Die erste Zeile beschreibt die Applikation, die in diesem Fall nicht explizit genannt ist.
* Die zweite Zeile beschreibt den Server, der für die Applikation verwendet wird, mit der IP-Adresse 188.455.5.174 und dem Servernamen s-0224m.srv.domain.de.
* Die dritte Zeile beschreibt die verwendete JBoss-Version, die 7.4 ist, und bezieht sich auf die zuvor genannte Applikation.

### Tabelle: Datenbankverbindungsinformationen
Die Tabelle stellt die Verbindungsinformationen zu einer Datenbank dar, die für den Testsystem Operator/Converter 1.8 verwendet wird.

Die Tabelle enthält folgende Spalten:
* Datenbank: Enthält den Namen oder die Beschreibung der Datenbank
* Server: Enthält die Adresse des Datenbankservers
* Port: Enthält den Port, über den die Verbindung hergestellt wird
* SID: Enthält den System-Identifier der Datenbank
* User: Enthält den Benutzernamen für die Datenbankverbindung

Die Tabellenzeilen können wie folgt beschrieben werden:
* Die Datenbank ist mit dem Server 188.455.6.52 (s-0941.db.domain.de) verbunden.
* Die Datenbankverbindung verwendet den Port 1521.
* Die Datenbank hat den SID tbv19.
* Die Datenbankverbindung verwendet den Benutzernamen doc-gentest18.

## Testsystem Doc-Gen Integration Server (EIS) 1.8

### Tabelle: Konfigurationswerte
Die Tabelle "Konfigurationswerte" stellt eine Sammlung von Bezeichnungen und ihren entsprechenden Werten im Kontext des Doc-Gen Integration Servers (EIS) 1.8 dar. Diese Tabelle bietet einen Überblick über die verschiedenen Konfigurationseinstellungen und ihre aktuellen Werte.

### Spaltenbeschreibung
* Bezeichnung: Diese Spalte enthält die Namen oder Beschreibungen der verschiedenen Konfigurationseinstellungen.
* Wert: Diese Spalte enthält die aktuellen Werte der jeweiligen Konfigurationseinstellungen.

### Tabelleninhalte
Leider ist die Tabelle leer, daher gibt es keine Zeilen, die beschrieben werden können. Die Tabelle besteht nur aus den beiden Spalten "Bezeichnung" und "Wert", ohne weitere Einträge.

### Tabelle: Applikationen auf dem Doc-Gen Integration Server (EIS) 1.8
Die Tabelle stellt die Applikationen und Server auf dem Doc-Gen Integration Server (EIS) 1.8 dar. Sie enthält Informationen über die verwendeten Applikationen und die zugehörigen Server.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die erste Spalte enthält den Namen der Applikation.
* Die zweite Spalte enthält die Server-Informationen, einschließlich der IP-Adresse und des Server-Namens.
* Die dritte Spalte enthält Informationen über die verwendete Tomcat-Version.

Die Tabellenzeilen können wie folgt beschrieben werden:
* Die erste Zeile beschreibt die Applikation "Applikation" ohne weitere Server-Informationen.
* Die zweite Zeile beschreibt den Server "Server" mit der IP-Adresse "188.455.5.174" und dem Server-Namen "s-0224m.srv.domain.de", der der Applikation "Applikation" zugeordnet ist.
* Die dritte Zeile beschreibt die Tomcat-Version "Tomcat 9", die auf dem Server "Server" verwendet wird, der der Applikation "Applikation" zugeordnet ist.

Es ist zu beachten, dass die Tabelle nur drei Zeilen enthält und die erste Zeile keine Server-Informationen enthält. Die zweite und dritte Zeile beziehen sich auf die Applikation "Applikation" und enthalten Informationen über den Server und die Tomcat-Version.

### Tabelle: EIS-Server-Konfiguration
Die Tabelle stellt die Konfigurationsparameter für den Doc-Gen Integration Server (EIS) 1.8 dar. Sie enthält Informationen über die Datenbankverbindung und die entsprechenden Zugangsdaten.

Die Bedeutung jeder Spalte ist wie folgt:
* Die erste Spalte enthält die Kategorien oder Instanzen, wie z.B. "Datenbank", "Server", "Port", "SID" und "User".
* Die zweite Spalte enthält die entsprechenden Werte oder Informationen zu jeder Kategorie.

Die Tabellenzeilen können wie folgt beschrieben werden:
* Die Datenbank ist auf dem Server 188.455.6.52 (s-0941.db.domain.de) konfiguriert.
* Der Port für die Datenbankverbindung ist 1521.
* Die System-ID (SID) der Datenbank ist tbv19.
* Die Benutzer für die Datenbank sind EISKARMA_dev, EISJPAStore_dev, EISLockRegistry_dev, EISTBHStore_dev und EISUserService_dev.

Es gibt keine leeren Felder oder Fortsetzungen in der Tabelle, daher können alle Zeilen direkt beschrieben werden. Die Tabelle bietet eine Übersicht über die notwendigen Konfigurationsparameter für den EIS-Server.

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

## Doc-Gen Ver. 1.8 Produktivsystem

Beispielaufruf Webcomposer:

Die Liste bezieht sich auf den Doc-Gen Ver. 1.8 Produktivsystem und enthält Anweisungen und Links zur Verwendung des Systems. Zusammengefasst kann man sagen, dass die Liste Hinweise zur Nutzung des Doc-Gen-Systems gibt, insbesondere im Zusammenhang mit der Erstellung von Dokumenten.

Die Liste enthält zwei spezifische Links zum Doc-Gen-System:
- Der erste Link (`https://doc-gen.domain.de:6228/generator-launcher/ui/orga/template-list?antragsnummer=009999-00/00&vorgang=27596`) führt zu einer spezifischen Seite innerhalb des Systems, die möglicherweise für die Erstellung von Dokumenten mit bestimmten Antragsnummern und Vorgangsnummern verwendet wird.
- Der zweite Link (`https://doc-gen.domain.de:6228/generator-launcher/ui/orga/template-list?`) scheint eine allgemeine Adresse für den Zugriff auf die Vorlagenliste innerhalb des Doc-Gen-Systems zu sein.

Es gibt auch eine wichtige Anweisung:
- Bitte keine Bescheide erstellen, weil die sonst im Infozupf landen! Dies bedeutet, dass Benutzer darauf hingewiesen werden, keine Bescheide über das Doc-Gen-System zu erstellen, da diese sonst möglicherweise an einem ungewollten Ort landen könnten.

Es gibt keine spezifischen Schritte, die in einer bestimmten Reihenfolge ausgeführt werden müssen. Die Liste dient eher als Hinweis und Anleitung für die Nutzung des Doc-Gen-Systems.

### Tabelle: Doc-Gen Ver. 1.8 Produktivsystem - Konfiguration
Die Tabelle stellt die Konfiguration des Doc-Gen Ver. 1.8 Produktivsystems dar. Sie enthält Informationen über verschiedene Bezeichnungen und ihre entsprechenden Werte.

### Spaltenbeschreibung
* Bezeichnung: Diese Spalte enthält die Namen oder Beschreibungen von verschiedenen Konfigurationseinstellungen oder Parametern.
* Wert: Diese Spalte enthält die Werte oder Einstellungen, die den jeweiligen Bezeichnungen zugeordnet sind.

### Tabelleninhalte
Da die Tabelle leer ist, gibt es keine Zeilen, die beschrieben werden können. Die Tabelle besteht nur aus den Spaltenüberschriften "Bezeichnung" und "Wert", ohne weitere Einträge.

### Tabelle: Applikationsserver
Die Tabelle "Applikationsserver" stellt die Verbindung zwischen einer Applikation und ihrem entsprechenden Server dar.

Diese Tabelle enthält Informationen über die Server, auf denen bestimmte Applikationen gehostet werden. 

Die Bedeutung jeder Spalte ist wie folgt:
* Die erste Spalte enthält den Namen der Applikation.
* Die zweite Spalte enthält die Adresse des Servers, auf dem die Applikation gehostet wird.

Die Tabellenzeilen können wie folgt beschrieben werden:
Die Applikation wird auf dem Server mit der Adresse 188.455.5.164 (s-0214m.srv.domain.de/doc-gen.domain.de) gehostet.

### Tabelle: Dokumentations-Generierung (Doc-Gen) Konfiguration
Die Tabelle stellt die Konfiguration für das Dokumentations-Generierungssystem (Doc-Gen) Version 1.8 im Produktivsystem dar. Sie enthält Informationen über die Datenbankverbindung.

### Spaltenbeschreibung
* Datenbank: Enthält Informationen über die Datenbank, wie Server und SID.
* Server: Die IP-Adresse oder der Name des Servers.
* Port: Der Port, über den die Verbindung hergestellt wird.
* SID: Der System-Identifier der Datenbank.
* User: Der Benutzername für die Datenbankverbindung.

### Tabelleninhalte
Die Datenbank ist auf dem Server 188.455.6.52 (s-0941.db.domain.de) konfiguriert. 
Der Port für die Datenbankverbindung ist 1521. 
Der SID für die Datenbank ist doc-gen19. 
Der Benutzername für die Datenbankverbindung ist DOC-GEN_PROD.

## Produktivsystem Doc-Gen Intergation Server (EIS) 1.8

### Tabelle: Konfigurationswerte für Doc-Gen Intergation Server (EIS) 1.8
Die Tabelle stellt eine Sammlung von Konfigurationswerten für den Doc-Gen Intergation Server (EIS) 1.8 dar. Sie enthält Informationen über verschiedene Bezeichnungen und ihre entsprechenden Werte.

### Spaltenbeschreibung
* Bezeichnung: Diese Spalte enthält die Namen oder Beschreibungen der verschiedenen Konfigurationswerte.
* Wert: Diese Spalte enthält die entsprechenden Werte für jede Bezeichnung.

### Tabelleninhalte
Leider ist die Tabelle leer, daher gibt es keine Zeilen, die beschrieben werden können. Die Tabelle besteht nur aus den Spaltennamen "Bezeichnung" und "Wert", ohne weitere Einträge.

### Tabelle: Server-Informationen
Die Tabelle stellt Server-Informationen für die Applikation dar. Sie enthält Informationen über den Server, auf dem die Applikation gehostet wird.

Die Tabelle hat zwei Spalten:
* Applikation: Diese Spalte enthält den Namen der Applikation.
* Server: Diese Spalte enthält die Adresse des Servers, auf dem die Applikation gehostet wird.

Die Tabelle enthält folgende Informationen:
Die Applikation wird auf dem Server mit der Adresse 188.455.5.164 (doc-gen.domain.de) gehostet.

Es gibt keine weiteren Informationen in der Tabelle.

### Tabelle: EIS-Server-Konfiguration
Die Tabelle hat keinen expliziten Titel, daher wird sie als "EIS-Server-Konfiguration" bezeichnet.

Diese Tabelle stellt die Konfiguration des Doc-Gen Intergation Server (EIS) 1.8 dar und enthält Informationen über die Datenbankverbindung. Die Tabelle gibt einen Überblick über die erforderlichen Parameter für die Verbindung zum EIS-Server.

Die Bedeutung jeder Spalte ist wie folgt:
* Die erste Spalte enthält die Kategorie oder den Parameter der Datenbankverbindung.
* Die zweite Spalte enthält den entsprechenden Wert oder die Einstellung für den jeweiligen Parameter.

Die Tabellenzeilen können wie folgt beschrieben werden:
* Der Server für die Datenbankverbindung ist 188.455.6.52 (s-0941.db.domain.de).
* Der Port für die Datenbankverbindung ist 1521.
* Der SID (System Identifier) für die Datenbankverbindung ist doc-gen19.
* Der User für die Datenbankverbindung umfasst mehrere Benutzer, darunter EISKARMA, EISJPAStore, EISLockRegistry, EISTBHStore und EISUserService.

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

## Client

Der Abschnitt "Client" im Dokument "Doc-Gen" beschreibt die verschiedenen Komponenten, die für die Nutzung von Doc-Gen erforderlich sind. Hierbei werden zwei wichtige Aspekte hervorgehoben:

Zum einen gibt es den **Webbrowser für Endanwender**, der als "doc-gen19" bezeichnet wird. Dieser ermöglicht es Endanwendern, auf die Doc-Gen-Funktionen zuzugreifen und ihre Dokumente zu erstellen und zu verwalten.

Zum anderen steht der **Doc-Gen-Designer für Administratoren** zur Verfügung. Dieser ermöglicht es Administratoren, die Doc-Gen-Systeme zu konfigurieren und zu verwalten, um sicherzustellen, dass die Dokumentenerstellung und -verwaltung reibungslos und effizient durchgeführt wird.

Insgesamt bietet Doc-Gen also zwei wichtige Komponenten, die sowohl für Endanwender als auch für Administratoren konzipiert sind, um die Dokumentenerstellung und -verwaltung zu erleichtern. Es gibt keine spezifischen Schritte, die in einer bestimmten Reihenfolge ausgeführt werden müssen, sondern vielmehr eine Beschreibung der verfügbaren Tools und Funktionen.

## Gruppen in der AD

Die Liste bezieht sich auf Gruppen in der Active Directory (AD) im Zusammenhang mit dem Dokumenttitel "Doc-Gen". Sie enthält verschiedene Gruppen, die offensichtlich mit der Verwaltung und dem Zugriff auf bestimmte Dokumente oder Funktionen innerhalb des Systems "Doc-Gen" zu tun haben.

Die Liste umfasst folgende Gruppen:
- Doc-Gen_Zwimis_PSM
- Doc-Gen_Bescheide_PSM
- Doc-Gen_Zulassungsberichte_PSM
- WebAuthor_PSM

Diese Gruppen können wie folgt zusammengefasst werden: Es handelt sich um spezifische Gruppen innerhalb des Doc-Gen-Systems, die jeweils Zugriff auf bestimmte Arten von Dokumenten oder Funktionen haben. Die Gruppen sind in verschiedene Kategorien unterteilt, wie zum Beispiel Zwischenmitteilungen (Zwimis), Bescheide und Zulassungsberichte, alle mit dem Zusatz "_PSM", was möglicherweise auf eine spezifische Abteilung oder ein bestimmtes System hinweist. Darüber hinaus gibt es die Gruppe "WebAuthor_PSM", die möglicherweise für die Verwaltung oder Erstellung von Web-Inhalten innerhalb des Doc-Gen-Systems verantwortlich ist.

Es gibt keine expliziten Schritte in dieser Liste, sondern vielmehr eine Auflistung von Gruppen, die im Doc-Gen-System eine Rolle spielen.

## Abhängigkeit von anderen Anwendungen

Infozupf

## Termine

## zeitlicher Verlauf

## 09.10.2023 Plan-B-Migration in RZ Bundesallee

neuer Server Doc-Gen TEST: s-0224m.srv.domain.de, PROD: s-0214.srv.domain.de

## 08.12.2022 Installation Doc-Gen Operator, Converter, tw. EIS auf schwubs374

## 07.12.2022 Installation JBoss

## 01.12.2022 neuer Doc-Gen Server schwubs374

Robert hat den neuen Server gestern zur Verfügung gestellt. Java 1.8 und JBoss 7.4 müssen noch installiert werden

## 21.09.2022 Start für das Update auf Version 1.8

## 19.01.2017 OTRS: Ticket#10021325

## 27.10.2016 (Aktualisierung Testdatenbank)

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

## 11.01.2017 (Vorbereitung Aktualisierung Produktion)

Geplant ist die Umstellung für den 19.01. 15.00 Uhr. ist das richtig?

Für erledigte Aufgaben ✔ verwenden.

Test:

Die Liste beschreibt eine Reihe von Schritten und Aufgaben, die im Rahmen der Vorbereitung der Aktualisierung der Produktion am 11.01.2017 durchgeführt wurden. Hier ist eine Zusammenfassung der Liste als gut lesbarer Fließtext:

Im Rahmen der Vorbereitung der Aktualisierung der Produktion wurden verschiedene Schritte durchgeführt. Zunächst wurde ein Template in der neuen Entwicklung angelegt und getestet. Anschließend wurde die Gen-Admin-Konfigurationsdatei angepasst, um bestimmte Testvorlagenschlüssel zu entfernen. Ein Zulassungsbericht wurde erstellt und die Berechtigungen mit Frau Bolten oder Stevens überprüft.

Es gab jedoch auch einige Aufgaben, die noch nicht abgeschlossen werden konnten. So musste der Testaufbau Apache auf schwubs172.old.domain.de aufgrund von technischen Problemen verschoben werden. Eine Untersuchung ergab, dass die Anwendung den HTTP-Header "location:SERVERNAME" setzt, was möglicherweise nur durch eine Softwareanpassung geändert werden kann.

Die folgenden Schritte wurden erfolgreich abgeschlossen:

1. Ein Template in der neuen Entwicklung anlegen und testen.
2. Die Gen-Admin-Konfigurationsdatei anpassen, um bestimmte Testvorlagenschlüssel zu entfernen.
3. Ein Zulassungsbericht erstellen.
4. Die Berechtigungen mit Frau Bolten oder Stevens überprüfen.
5. Die Bescheiddaten kontrollieren.
6. Fehler in der Formatierung im Testsystem Subs172.old.domain.de untersuchen und beheben.
7. Die Einrichtung Apache auf schwubs174.old.domain.de und die Erstellung einer index.html, die beim Aufruf von http://webauthor.old.domain.de auf schwubs174.old.domain.de:4040/secure/webauthor/ weiterleitet.

Insgesamt zeigt die Liste, dass eine Reihe von Schritten und Aufgaben durchgeführt wurden, um die Vorbereitung der Aktualisierung der Produktion voranzutreiben. Es gibt jedoch noch einige offene Punkte, die bearbeitet werden müssen, um den Prozess abzuschließen.

Am Tag der Umstellung :

Die Liste beschreibt die Vorbereitung für die Aktualisierung der Produktion am 11.01.2017. Hier sind die wichtigsten Schritte und Punkte zusammengefasst:

Zur Vorbereitung der Aktualisierung der Produktion wurden verschiedene Schritte durchgeführt. Hier sind die wichtigsten Punkte:

1. **Export und Import von TBV**: Zunächst wurde die alte Produktion von `srvlnx170.old.domain.de` exportiert und in die neue Produktion auf `Subs169.old.domain.de` importiert. Dieser Schritt wurde von Amir durchgeführt.
2. **Aktualisierung des Jackrabbit Repository**: Anschließend wurde das Jackrabbit Repository von `Subs031.old.domain.de` auf `Subs174.old.domain.de` aktualisiert.
3. **DNS-Umstellung**: Es folgten zwei DNS-Umstellungen:
 * Die erste Umstellung betraf `doc-gen.old.domain.de`, die von `schwubs031.old.domain.de` auf `schwubs174.old.domain.de` umgestellt wurde.
 * Die zweite Umstellung betraf `webauthor.old.domain.de`, die ebenfalls von `schwubs031.old.domain.de` auf `schwubs174.old.domain.de` umgestellt wurde.
4. **Fachliche Freigabe**: Nach diesen technischen Schritten wurde die fachliche Freigabe durch Britta Busch erteilt.
5. **Abschaltung Altsysteme**: Anschließend wurden die Altsysteme `Subs028.old.domain.de` bis `Subs031.old.domain.de` abgeschaltet.
6. **Anpassung Nagios Überwachung**: Es wurde eine Anpassung der Nagios Überwachung beantragt.
7. **Aktualisierung der Dokumentation**: Schließlich wurde die Dokumentation (Wiki, Installation/Betriebshandbuch) aktualisiert.

Insgesamt wurden diese Schritte durchgeführt, um die Produktion auf den neuesten Stand zu bringen und die notwendigen Anpassungen vorzunehmen.

## 2018-08-27 (Untersuchung Ghostscript Schwachstelle)

Ein Ticket im Supportportal geöffnet ( DOC-GEN Support ESP-5481 )

Ergebnis:

Ghostskript wird nicht verwendet.

... Nein. Ghostscript wird von Doc-Gen nicht verwendet. ... {{/7box}} {{/box}}
