# Doc-Gen

## Einleitung

Die Liste aus der technischen Wiki-Seite für Doc-Gen umfasst verschiedene Aspekte und Schritte im Zusammenhang mit der Anwendung Doc-Gen. Hier ist eine Zusammenfassung der Liste in gut lesbarer Form:

Die Dokumentation von Doc-Gen beginnt mit einem **Vorwort**, gefolgt von Informationen über den **Ansprechpartner Fachlich IT Extern**. Es gibt auch Hinweise auf die **Dokumentenablage**, die in verschiedenen Systemen wie ORGA Dateisystem, Doc-Gen Wiki und GIT Anleitungen zu finden ist.

Ein wichtiger Teil der Dokumentation ist die Beschreibung der **Systemarchitektur von Doc-Gen Ver. 1.8**, die die verschiedenen Bestandteile der Anwendung wie das Testsystem, den Operator/Converter und den Integration Server (EIS) umfasst. Es gibt auch Informationen über die **Verarbeiteten Daten**, die in fachliche Daten und personenbezogene Daten unterteilt sind.

Die Liste enthält auch eine **Schrittfolge** für die Installation und Konfiguration von Doc-Gen:
1. **Installation von JBoss** am 01.12.2022
2. **Installation von Doc-Gen Operator, Converter und teilweise EIS** auf schwubs374 am 07.12.2022
3. **Plan-B-Migration in RZ Bundesallee** am 09.10.2023

Weitere wichtige Punkte sind die **Abhängigkeit von anderen Anwendungen** und die **Termine**, die einen zeitlichen Verlauf der Aktivitäten um Doc-Gen darstellen. Einige wichtige Termine sind:
- **21.09.2022**: Start für das Update auf Version 1.8
- **08.12.2022**: Installation von Doc-Gen auf schwubs374
- **09.10.2023**: Plan-B-Migration in RZ Bundesallee

Insgesamt bietet die Liste eine umfassende Übersicht über die Anwendung Doc-Gen, ihre Systemarchitektur, die verarbeiteten Daten und die wichtigsten Schritte und Termine im Zusammenhang mit der Anwendung.

## Vorwort Bearbeiten

Generierung von Dokumenten für die Zulassung von Pflanzenschutzmitteln auf Basis von Faktendatenbanken (Bsp. Abt. 2 INFOZUPF) Die Dokumente werden in das VBS übertragen und von dort aus an den Antragsteller übermittelt

## Ansprechpartner Bearbeiten

## Fachlich Bearbeiten

Britta Busch

## IT Bearbeiten

Die Liste aus dem Abschnitt "IT" des Dokuments "Doc-Gen" enthält eine Aufzählung von Personen, die offensichtlich mit IT-bezogenen Aufgaben oder Projekten in Verbindung stehen. Die Liste umfasst folgende Personen:

Die Liste enthält eine Reihe von Namen von Personen, die anscheinend für IT-bezogene Aufgaben oder Projekte verantwortlich sind. Diese Personen sind:
- @Diana Stölzel
- @Vladislav Konov
- @Hans Labod
- @Alexandra Freytag
- @Andreas Stengl

Zusammengefasst handelt es sich um eine Liste von fünf Personen, die möglicherweise an IT-Projekten oder -Aufgaben beteiligt sind. Es gibt keine spezifischen Schritte oder Anweisungen, sondern lediglich eine Auflistung der Namen.

## Extern Bearbeiten

Die Liste enthält Kontaktdaten und Ressourcen für die externe Bearbeitung von Doc-Gen. Zusammengefasst bietet sie Informationen über die Ansprechpartner und Unterstützungsangebote, die für die Arbeit mit Doc-Gen zur Verfügung stehen.

Für Fragen oder Anliegen können Sie sich an folgende Personen oder Ressourcen wenden:
- Der Account Manager Claudia Theobald ist unter Claudia.Theobald@doc-gen.de erreichbar.
- Für technische Koordination steht Lars Decker unter Lars.Decker@doc-gen.de zur Verfügung.
- Bei Bedarf können Sie sich auch an Frederik Zimmer (Frederik.Zimmer@doc-gen.de) für Doc-Gen EIS wenden.
- Für weitere Unterstützung oder technische Probleme können Sie das Support-Portal unter https://service.doc-gen-software.de besuchen.

Es handelt sich hier nicht um eine Schrittfolge, sondern um eine Sammlung von Kontaktdaten und Ressourcen, die für die externe Bearbeitung von Doc-Gen nützlich sein können.

## Dokumentenablage Bearbeiten

## ORGA Dateisystem Bearbeiten

Die Liste enthält Informationen über den Speicherort von Dateien im Zusammenhang mit dem Dokumenttitel "Doc-Gen" im Abschnitt "ORGA Dateisystem Bearbeiten". Zusammengefasst handelt es sich um zwei verschiedene Pfade, an denen relevante Dateien oder Dokumente abgelegt sind.

Die beiden Speicherorte sind:
1. **\\dateiablage1-bs\Projekte\DokGen**: Dieser Pfad bezieht sich auf den allgemeinen Speicherort für Projekte im Zusammenhang mit "DokGen".
2. **\\dateiablage1-bs\Projekte\IT-Anwendungen-Abt2\04_DOC-GEN\04_Dokumentation\DOC-GEN**: Dieser Pfad ist spezifischer und führt zu einem bestimmten Unterordner innerhalb des Projekts, der sich auf die Dokumentation von "DOC-GEN" konzentriert.

Diese Informationen können helfen, Dateien und Dokumente im ORGA-Dateisystem effizient zu finden und zu bearbeiten.

## Doc-Gen Wiki Bearbeiten

Die Liste bezieht sich auf den Zugriff auf die DOC-GEN Wiki-Seite. Hier finden Sie eine Zusammenfassung der Informationen:

Die DOC-GEN Wiki-Seite ist ein zentrales Informationsportal, auf dem Sie Handbücher und Hilfestellung zur Installation und Wartung finden können. Um auf diese Ressourcen zuzugreifen, müssen Sie die folgenden Schritte befolgen:

1. Öffnen Sie den Webbrowser und navigieren Sie zu der URL: www.doc-gen-wiki.de
2. Melden Sie sich an, indem Sie den Benutzernamen "doc-gen-help" und das entsprechende Passwort verwenden. 
3. Um das Passwort zu finden, öffnen Sie die Datei "S0FTW4RE-Kennwoerter.kdbx" mit dem Tool Keepass.

Nachdem Sie diese Schritte befolgt haben, sollten Sie Zugriff auf die DOC-GEN Wiki-Seite haben und können die verfügbaren Ressourcen nutzen, um Ihre Fragen zu beantworten oder Probleme zu lösen.

## GIT Bearbeiten

https://devops.cloud.orga.in.bund.de/scm/repo/A2/2012-DokGen/code/sources/master/

```
git clone https://devops.cloud.orga.in.bund.de/scm/repo/A2/2012-DokGen
```

## Anleitungen Bearbeiten

Die Liste aus der technischen Wiki-Seite enthält eine Zusammenstellung von Dokumenten und Schritten, die für die Implementierung und den Betrieb eines Systems relevant sind. Hier ist eine Zusammenfassung der Liste in gut lesbarer Form:

Die Dokumentation umfasst verschiedene Handbücher und Schritte, die für die erfolgreiche Implementierung und den Betrieb eines Systems erforderlich sind. Dazu gehören:

1. **Installationshandbuch**: Dieses Handbuch befindet sich im Verzeichnis `\\dateiablage1-bs\Abteilung_Z\Grp_A4_Allgemein\Dokumentation\Installationshandbücher` und enthält Anleitungen für die Installation des Systems.
2. **Betriebshandbuch**: Dieses Handbuch befindet sich im Verzeichnis `\\dateiablage1-bs\Abteilung_Z\Grp_A4_Allgemein\Dokumentation\Betriebshandbücher` und enthält Anleitungen für den Betrieb des Systems.
3. **Übernahme von Änderungen**: Um Änderungen aus dem Entwicklungssystem in das Produktivsystem zu übernehmen, müssen die Domänen transportiert werden. Dieser Schritt ist wichtig, um sicherzustellen, dass die Änderungen korrekt implementiert werden.

Insgesamt bietet die Liste eine Übersicht über die wichtigsten Dokumente und Schritte, die für die Implementierung und den Betrieb eines Systems erforderlich sind. Durch die Verwendung dieser Dokumente und Schritte kann ein erfolgreiches System aufgebaut und betrieben werden.

## Server Bearbeiten

## Anwendungsserver Bearbeiten

Produktiv: s-0214m.srv.domain.de

Test: s-0224m.srv.domain.de

## Datenbank Server Bearbeiten

Datenbank Server Produktiv: s-0941.db.domain.de:1521/doc-gen19

Datenbank Server Test: s-0941.db.domain.de:1521/tbv19

## Nützliche Server Befehle Bearbeiten

Der Abschnitt "Nützliche Server Befehle" im Dokument "Doc-Gen" beschreibt wichtige Schritte für die Verwaltung eines Servers. Eine der wichtigsten Aktionen ist das Starten des Servers. Hier sind die Schritte, um den Server erfolgreich zu starten:

1. **Server starten (als root)**: Um den Server zu starten, muss man als root-Benutzer agieren. Dieser Schritt ist entscheidend, da er sicherstellt, dass der Server mit den notwendigen Rechten und Zugriffsberechtigungen gestartet wird.

Zusammenfassend lässt sich sagen, dass die Liste derzeit nur einen Punkt enthält, nämlich das Starten des Servers als root-Benutzer. Dieser Schritt ist jedoch von entscheidender Bedeutung für die erfolgreiche Inbetriebnahme des Servers. Durch die Ausführung dieses Schritts kann man sicherstellen, dass der Server ordnungsgemäß gestartet wird und alle notwendigen Funktionen und Dienste verfügbar sind.

```
systemctl start jboss-eap-rhel
systemctl start tomcat
```

Der Abschnitt "Nützliche Server Befehle" im Dokument "Doc-Gen" behandelt verschiedene Befehle, die für die Verwaltung eines Servers nützlich sein können. Eine der wichtigsten Aktionen, die in diesem Kontext erwähnt wird, ist das Stoppen des Servers.

Um den Server zu stoppen, müssen Sie folgende Schritte ausführen:
1. Stellen Sie sicher, dass Sie als root-Benutzer angemeldet sind, da dieser Vorgang administrative Rechte erfordert.
2. Führen Sie den entsprechenden Befehl aus, um den Server zu stoppen. Der genaue Befehl kann je nach Server-Software und Betriebssystem variieren, daher ist es wichtig, die spezifischen Anweisungen für Ihren Server zu konsultieren.

Es ist wichtig zu beachten, dass das Stoppen eines Servers Auswirkungen auf die Verfügbarkeit von Diensten und Anwendungen haben kann, die auf diesem Server gehostet werden. Daher sollten Sie diesen Schritt sorgfältig planen und nur dann ausführen, wenn es unbedingt notwendig ist.

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

Die Liste scheint eine URL-Adresse zu enthalten, die zum Zugriff auf ein bestimmtes System oder eine bestimmte Funktion innerhalb des Doc-Gen-Testsystems dient. Zusammengefasst handelt es sich um eine spezifische Adresse, die für den Zugriff auf eine Vorlagenliste innerhalb des Systems erforderlich ist.

Die Adresse lautet:
https://doc-gen-test.domain.de:6228/generator-launcher/ui/orga/template-list?antragsnummer=00Z001-00/00&vorgang=27596

Um diese Adresse zu verwenden, können Sie folgende Schritte befolgen:
1. Öffnen Sie Ihren Webbrowser.
2. Geben Sie die oben genannte URL-Adresse in die Adresszeile ein.
3. Drücken Sie die Enter-Taste, um zur angegebenen Seite zu gelangen.

Es ist wichtig zu beachten, dass die Adresse spezifische Parameter enthält, wie die Antragsnummer (00Z001-00/00) und den Vorgang (27596), die möglicherweise für den Zugriff auf bestimmte Funktionen oder Daten innerhalb des Systems erforderlich sind.

Doc-Gen Operator

Die Liste enthält zwei URLs, die auf verschiedene Testsysteme für Doc-Gen Ver. 1.8 verweisen. Zusammengefasst bieten diese URLs Zugriff auf die Operator-Oberfläche des Doc-Gen-Testsystems.

Um auf diese Systeme zuzugreifen, können Sie folgende Schritte befolgen:

1. Öffnen Sie einen Webbrowser und geben Sie die erste URL ein: http://doc-gen-test.domain.de:6260/doc-gen-web/operator/
2. Alternativ können Sie auch die zweite URL verwenden: https://doc-gen-test.domain.de:6428/doc-gen-web/operator/

Beide URLs ermöglichen den Zugriff auf die Operator-Oberfläche des Doc-Gen-Testsystems, wobei die erste URL über HTTP und die zweite URL über HTTPS verfügbar ist.

## Testsystem Operator/Converter 1.8

### Tabelle: Eigenschaften von Doc-Gen
Die Tabelle stellt die Eigenschaften von Doc-Gen im Abschnitt "Testsystem Operator/Converter 1.8" dar. Sie enthält Informationen über verschiedene Bezeichnungen und ihre entsprechenden Werte.

### Spaltenbeschreibung
* Bezeichnung: Diese Spalte enthält die Namen oder Beschreibungen von Eigenschaften oder Parametern.
* Wert: Diese Spalte enthält die Werte oder Einstellungen, die den jeweiligen Bezeichnungen zugeordnet sind.

### Tabelleninhalte
Da die Tabelle leer ist, gibt es keine Zeilen, die beschrieben werden können. Die Tabelle enthält keine Einträge, daher kann keine weitere Information bereitgestellt werden.

### Tabelle: Applikationseinstellungen
Die Tabelle stellt die Einstellungen für eine bestimmte Applikation dar, insbesondere in Bezug auf den Server und die verwendete Software.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die erste Spalte enthält den Namen der Applikation oder eine Kategorie, zu der die folgenden Informationen gehören.
* Die zweite Spalte enthält Informationen über den Server, einschließlich der IP-Adresse und des Servernamens.
* Die dritte Spalte enthält Informationen über die verwendete Software oder den Betriebssystem.

Die Tabellenzeilen können wie folgt beschrieben werden:
* Die erste Zeile beschreibt die Applikation, ohne weitere Details anzugeben.
* Die zweite Zeile beschreibt den Server, der für die Applikation verwendet wird, mit der IP-Adresse 188.455.5.174 und dem Servernamen s-0224m.srv.domain.de.
* Die dritte Zeile beschreibt die verwendete Software, in diesem Fall JBoss 7.4, die in Verbindung mit der Applikation und dem Server aus der vorherigen Zeile verwendet wird.

Es ist zu beachten, dass die Tabelle nur drei Zeilen enthält und die erste Spalte in den zweiten und dritten Zeilen leer ist, was bedeutet, dass die Informationen in diesen Zeilen in Verbindung mit der Applikation aus der ersten Zeile stehen.

### Tabelle: Datenbankverbindungsinformationen
Die Tabelle stellt die Verbindungsinformationen zu einer Datenbank dar, die für den Testsystem Operator/Converter 1.8 verwendet wird.

Die Tabelle enthält folgende Spalten:
* Datenbank: Enthält den Namen oder die Beschreibung der Datenbank
* Server: Enthält die Adresse des Datenbankservers
* Port: Enthält den Port, der für die Verbindung verwendet wird
* SID: Enthält die System-ID der Datenbank
* User: Enthält den Benutzernamen für die Verbindung

Die Tabellenzeilen können wie folgt beschrieben werden:
* Die Datenbank ist mit dem Server 188.455.6.52 (s-0941.db.domain.de) verbunden.
* Die Datenbank verwendet den Port 1521 für die Verbindung.
* Die Datenbank hat die System-ID tbv19.
* Die Datenbank verwendet den Benutzernamen doc-gentest18 für die Verbindung.

## Testsystem Doc-Gen Integration Server (EIS) 1.8

### Tabelle: Konfigurationswerte
Die Tabelle "Konfigurationswerte" stellt eine Sammlung von Bezeichnungen und ihren entsprechenden Werten im Rahmen des Doc-Gen Integration Servers (EIS) 1.8 dar. Diese Tabelle bietet einen Überblick über die verschiedenen Konfigurationseinstellungen und ihre jeweiligen Werte.

Die Spalten haben folgende Bedeutung:
* Bezeichnung: Hier werden die Namen oder Identifikatoren der Konfigurationswerte aufgeführt.
* Wert: In dieser Spalte sind die entsprechenden Werte zu den jeweiligen Bezeichnungen angegeben.

Da die Tabelle leer ist, gibt es keine Zeilen, die beschrieben werden können. Die Tabelle bleibt somit ohne Inhalt.

### Tabelle: Server-Konfiguration
Die Tabelle "Server-Konfiguration" stellt die Konfiguration eines Servers im Zusammenhang mit der Doc-Gen Integration Server (EIS) 1.8 dar. Sie enthält Informationen über die verwendete Applikation und den Server.

Die Bedeutung jeder Spalte ist wie folgt:
* Die erste Spalte enthält den Namen der Applikation.
* Die zweite Spalte enthält die Server-Adresse und den Server-Namen.
* Die dritte Spalte enthält die verwendete Tomcat-Version.

Die Tabellenzeilen können wie folgt beschrieben werden:
* Die erste Zeile beschreibt die Applikation, aber da keine weitere Information vorhanden ist, kann nicht genau gesagt werden, was diese Applikation ist.
* Die zweite Zeile beschreibt den Server mit der Adresse 188.455.5.174 und dem Namen s-0224m.srv.domain.de, der in Verbindung mit der vorherigen Applikation steht.
* Die dritte Zeile beschreibt die Verwendung von Tomcat 9, ebenfalls in Verbindung mit der vorherigen Applikation und dem Server.

### Tabelle: EIS-Server-Konfiguration
Die Tabelle hat keinen expliziten Titel, daher wird sie als "EIS-Server-Konfiguration" bezeichnet.

Diese Tabelle stellt die Konfigurationseinstellungen für den EIS-Server (Enterprise Integration Server) dar. Sie enthält Informationen über die Datenbankverbindung und die verwendeten Benutzer.

Die Bedeutung jeder Spalte ist wie folgt:
* Die erste Spalte enthält die Kategorie oder den Typ der Konfigurationseinstellung.
* Die zweite Spalte enthält den entsprechenden Wert oder die Details zu dieser Einstellung.

Die Tabellenzeilen können wie folgt beschrieben werden:
* Der Server für die Datenbank ist 188.455.6.52 (s-0941.db.domain.de).
* Der Port für die Datenbankverbindung ist 1521.
* Der SID (System Identifier) für die Datenbank ist tbv19.
* Die Benutzer für die Datenbank sind EISKARMA_dev, EISJPAStore_dev, EISLockRegistry_dev, EISTBHStore_dev und EISUserService_dev.

Es gibt keine weiteren Informationen oder leeren Felder in der Tabelle, die beschrieben werden müssten.

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

Die Liste kann wie folgt zusammengefasst werden:

Es gibt zwei Links zum Doc-Gen-System, die für die Erstellung von Dokumenten verwendet werden können. Der erste Link enthält spezifische Parameter wie eine Antragsnummer und einen Vorgang, während der zweite Link ohne diese Parameter ist. Es ist jedoch wichtig zu beachten, dass Bescheide nicht erstellt werden sollten, da sie sonst im Infozupf landen.

Es gibt keine spezifischen Schritte, die in einer bestimmten Reihenfolge ausgeführt werden müssen. Die Liste dient eher als Informationsquelle und Hinweis auf die Verwendung des Doc-Gen-Systems. Wenn Sie jedoch die Links verwenden möchten, können Sie folgende Schritte befolgen:

1. Öffnen Sie den ersten Link, wenn Sie eine Antragsnummer und einen Vorgang haben, die Sie in die URL einfügen möchten.
2. Öffnen Sie den zweiten Link, wenn Sie keine spezifischen Parameter haben.
3. Beachten Sie, dass Sie keine Bescheide erstellen sollten, um eine ungewollte Weiterleitung im Infozupf zu vermeiden.

Es ist wichtig, diese Hinweise zu beachten, um eine korrekte und effiziente Verwendung des Doc-Gen-Systems zu gewährleisten.

### Tabelle: Doc-Gen Ver. 1.8 Produktivsystem
Die Tabelle stellt die Konfiguration oder Eigenschaften des Doc-Gen Ver. 1.8 Produktivsystems dar. Sie enthält Informationen über verschiedene Bezeichnungen und ihre entsprechenden Werte.

### Spaltenbeschreibung
* Bezeichnung: Diese Spalte enthält die Namen oder Identifikatoren für verschiedene Eigenschaften oder Konfigurationen.
* Wert: Diese Spalte enthält die Werte oder Einstellungen, die zu den jeweiligen Bezeichnungen gehören.

### Tabelleninhalte
Da die Tabelle leer ist, gibt es keine Zeilen, die beschrieben werden können. Die Tabelle besteht nur aus den Spaltenüberschriften "Bezeichnung" und "Wert", ohne weitere Einträge.

### Tabelle: Applikationsserver
Die Tabelle stellt die Konfiguration von Applikationsservern dar. Sie enthält Informationen über die Server, die für die Applikation "Doc-Gen" verwendet werden.

Die Bedeutung jeder Spalte ist wie folgt:
* Die erste Spalte enthält den Namen der Applikation.
* Die zweite Spalte enthält die Server-Adresse, einschließlich der IP-Adresse und des Domain-Namens.

Die Tabellenzeilen können wie folgt beschrieben werden:
Die Applikation "Applikation" wird auf dem Server mit der Adresse "188.455.5.164 (s-0214m.srv.domain.de/doc-gen.domain.de)" gehostet.

### Tabelle: Doc-Gen Verbindungseinstellungen
Die Tabelle "Doc-Gen Verbindungseinstellungen" stellt die Konfiguration für die Verbindung zu einer Datenbank im Doc-Gen System dar. Sie enthält Informationen über den Server, den Port, die Systemkennung (SID) und den Benutzernamen für die Produktionsumgebung.

### Spaltenbeschreibung
* Datenbank: Bezeichnung der Datenbank
* Server: Adresse des Servers
* Port: Kommunikationsport für die Verbindung
* SID: Systemkennung der Datenbank
* User: Benutzername für die Verbindung

### Tabelleninhalte
Die Datenbank verwendet den Server mit der Adresse 188.455.6.52 (s-0941.db.domain.de). 
Die Datenbank verwendet den Port 1521. 
Die Datenbank verwendet die Systemkennung doc-gen19. 
Die Datenbank verwendet den Benutzernamen DOC-GEN_PROD.

## Produktivsystem Doc-Gen Intergation Server (EIS) 1.8

### Tabelle: Konfigurationswerte für Doc-Gen Intergation Server (EIS) 1.8
Die Tabelle stellt Konfigurationswerte für den Doc-Gen Intergation Server (EIS) 1.8 dar. Sie enthält Informationen über verschiedene Bezeichnungen und ihre entsprechenden Werte.

### Spaltenbeschreibung
* Bezeichnung: Diese Spalte enthält die Namen oder Beschreibungen von Konfigurationswerten.
* Wert: Diese Spalte enthält die entsprechenden Werte für die jeweiligen Bezeichnungen.

### Tabelleninhalte
Leider ist die Tabelle leer, daher gibt es keine Zeilen, die beschrieben werden können. Die Tabelle besteht nur aus den Spaltenüberschriften "Bezeichnung" und "Wert", ohne weitere Einträge.

### Tabelle: Server-Informationen
Die Tabelle stellt Server-Informationen für die Applikation dar. Sie enthält Informationen über den Server, auf dem die Applikation gehostet wird.

Die Bedeutung jeder Spalte ist wie folgt:
* Applikation: Die Name der Applikation, die auf dem Server gehostet wird.
* Server: Die Adresse des Servers, auf dem die Applikation gehostet wird.

Die Tabellenzeilen können wie folgt beschrieben werden:
Die Applikation wird auf dem Server mit der Adresse 188.455.5.164 (doc-gen.domain.de) gehostet.

Es gibt nur eine Zeile in der Tabelle, daher gibt es keine Fortsetzungen oder leeren Kategorien. Die Tabelle ist sehr einfach und enthält nur eine einzige Information über den Server, auf dem die Applikation gehostet wird.

### Tabelle: EIS-Verbindungsdetails
Die Tabelle "EIS-Verbindungsdetails" stellt die Verbindungseinstellungen für den Doc-Gen Intergation Server (EIS) 1.8 dar. Sie enthält Informationen über die Datenbankverbindung, die zum Betrieb des Servers erforderlich sind.

Die Bedeutung jeder Spalte ist wie folgt:
* Die erste Spalte enthält die Kategorie oder den Typ der Verbindungseinstellung.
* Die zweite Spalte enthält den entsprechenden Wert oder die Details zu dieser Einstellung.

Die Tabellenzeilen können wie folgt beschrieben werden:
* Die Datenbankverbindung erfolgt über den Server mit der Adresse 188.455.6.52 (s-0941.db.domain.de).
* Der Port für die Datenbankverbindung ist 1521.
* Die System-ID (SID) für die Datenbankverbindung ist doc-gen19.
* Der Benutzer für die Datenbankverbindung umfasst mehrere Rollen, darunter EISKARMA, EISJPAStore, EISLockRegistry, EISTBHStore und EISUserService.

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

Der Abschnitt "Client Bearbeiten" im Dokument "Doc-Gen" behandelt verschiedene Aspekte der Client-Konfiguration und -Verwaltung. Die Liste gibt einen Überblick über die wichtigsten Komponenten, die für die Arbeit mit Doc-Gen relevant sind.

Zusammengefasst umfasst die Liste zwei wichtige Elemente:
- Der Webbrowser für Endanwender ist ein wichtiger Bestandteil von Doc-Gen, da er es Endanwendern ermöglicht, auf die Plattform zuzugreifen und Dokumente zu generieren.
- Der Doc-Gen-Designer ist speziell für Administratoren konzipiert und bietet ihnen die Möglichkeit, die Plattform anzupassen und zu verwalten.

Es handelt sich hier nicht um eine Schrittfolge, sondern um eine Auflistung der wichtigsten Komponenten, die für die Arbeit mit Doc-Gen relevant sind. Durch die Kombination aus Webbrowser für Endanwender und Doc-Gen-Designer für Administratoren bietet Doc-Gen eine umfassende Lösung für die Dokumentenerstellung und -verwaltung.

## Gruppen in der AD Bearbeiten

Die Liste bezieht sich auf Gruppen in der Active Directory (AD) im Kontext des Dokumenttitels "Doc-Gen". Sie enthält verschiedene Gruppen, die offensichtlich mit der Verwaltung von Dokumenten und Berichten in Zusammenhang stehen. Hier ist eine Zusammenfassung der Liste in gut lesbarer Form:

Die Gruppen in der AD umfassen verschiedene Bereiche der Dokumentengenerierung und -verwaltung. Dazu gehören:
- Gruppen, die für die Verwaltung von Zwischeninformationen (Doc-Gen_Zwimis_PSM) zuständig sind,
- solche, die sich mit der Bearbeitung von Bescheiden (Doc-Gen_Bescheide_PSM) beschäftigen,
- Gruppen, die für die Erstellung und Verwaltung von Zulassungsberichten (Doc-Gen_Zulassungsberichte_PSM) verantwortlich sind,
- sowie die Gruppe WebAuthor_PSM, die möglicherweise für die Autoren von Webinhalten oder die Verwaltung von Webinhalten im Rahmen von Doc-Gen zuständig ist.

Es handelt sich hier nicht um eine Schrittfolge, sondern um eine Auflistung von Gruppen, die jeweils unterschiedliche Aufgabenbereiche innerhalb der Dokumentengenerierung und -verwaltung abdecken.

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

Die Liste beschreibt eine Reihe von Schritten und Aufgaben, die im Rahmen der Vorbereitung der Aktualisierung der Produktion durchgeführt wurden. Hier ist eine Zusammenfassung der Liste als gut lesbarer Fließtext:

Die Vorbereitung der Aktualisierung der Produktion umfasste mehrere Schritte. Zunächst wurde ein Template in der neuen Entwicklung angelegt und getestet. Anschließend wurde die Gen-Admin-Konfigurationsdatei angepasst, um bestimmte Testvorlagenschlüssel zu entfernen. Ein Zulassungsbericht wurde erstellt und die Berechtigungen wurden überprüft.

Die folgenden Schritte wurden durchgeführt:

1. Ein Template in der neuen Entwicklung anlegen und testen.
2. Die Gen-Admin-Konfigurationsdatei anpassen, um bestimmte Testvorlagenschlüssel zu entfernen.
3. Ein Zulassungsbericht erstellen.
4. Die Berechtigungen überprüfen.
5. Die Bescheiddaten kontrollieren.
6. Fehler in der Formatierung im Testsystem untersuchen und beheben.

Es gab auch einige spezifische Aufgaben, wie die Einrichtung von Apache auf bestimmten Servern und die Erstellung von Weiterleitungen. Einige dieser Aufgaben konnten abgeschlossen werden, wie die Einrichtung von Apache auf schwubs174.old.domain.de und die Erstellung einer index.html, die auf schwubs174.old.domain.de:4040/secure/webauthor/ weiterleitet. Andere Aufgaben, wie die Untersuchung, warum bestimmte Umleitungen erfolgen, konnten ebenfalls abgeschlossen werden.

Es gibt jedoch noch einige offene Aufgaben, wie die Überprüfung des Testaufbaus Apache auf schwubs172.old.domain.de, die aufgrund von technischen Problemen noch nicht abgeschlossen werden konnte. Insgesamt zeigt die Liste, dass eine Vielzahl von Schritten und Aufgaben durchgeführt wurden, um die Aktualisierung der Produktion vorzubereiten.

Am Tag der Umstellung :

Die Liste beschreibt die Schritte und Aufgaben, die im Rahmen der Vorbereitung der Aktualisierung der Produktion am 11.01.2017 durchgeführt wurden. Hier sind die wichtigsten Punkte in einer klaren und lesbaren Form zusammengefasst:

Die Vorbereitung der Aktualisierung der Produktion umfasste mehrere Schritte, die wie folgt aussehen:
1. **Export und Import von TBV**: Zunächst wurde die alte Produktion von `srvlnx170.old.domain.de` exportiert und in die neue Produktion auf `Subs169.old.domain.de` importiert. Dieser Schritt wurde von Amir durchgeführt.
2. **Aktualisierung des Jackrabbit Repository**: Anschließend wurde das Jackrabbit Repository von `Subs031.old.domain.de` auf `Subs174.old.domain.de` aktualisiert.
3. **DNS-Umstellung**: Es folgten zwei DNS-Umstellungen: 
   - Die erste Umstellung betraf `doc-gen.old.domain.de`, die von `schwubs031.old.domain.de` auf `schwubs174.old.domain.de` umgestellt wurde. 
   - Die zweite Umstellung betraf `webauthor.old.domain.de`, die ebenfalls von `schwubs031.old.domain.de` auf `schwubs174.old.domain.de` umgestellt wurde. Beide Schritte wurden von Gabel und Lux durchgeführt und mit Dennis per E-Mail abgestimmt.
4. **Fachliche Freigabe**: Nach den technischen Schritten wurde die fachliche Freigabe durch Britta Busch erteilt.
5. **Abschaltung Altsysteme**: Anschließend wurden die Altsysteme `Subs028.old.domain.de` bis `Subs031.old.domain.de` abgeschaltet.
6. **Anpassung Nagios Überwachung**: Es wurde eine Anpassung der Nagios Überwachung beantragt.
7. **Aktualisierung der Dokumentation**: Zum Abschluss wurde die Dokumentation (Wiki, Installation/Betriebshandbuch) aktualisiert.

Diese Schritte zusammenfassen die Vorbereitung und Durchführung der Aktualisierung der Produktion am 11.01.2017.

## 2018-08-27 (Untersuchung Ghostscript Schwachstelle) Bearbeiten

Ein Ticket im Supportportal geöffnet ( DOC-GEN Support ESP-5481 )

Ergebnis:

Ghostskript wird nicht verwendet.

... Nein. Ghostscript wird von Doc-Gen nicht verwendet. ... {{/7box}} {{/box}}
