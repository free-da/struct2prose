# Doc-Gen

## Einleitung

Die Liste aus der technischen Wiki-Seite für Doc-Gen umfasst verschiedene Aspekte und Schritte im Zusammenhang mit der Anwendung und ihrer Entwicklung. Hier ist eine Zusammenfassung der Liste in gut lesbarer Form:

Die Dokumentation von Doc-Gen beginnt mit einem **Vorwort**, gefolgt von Informationen über den **Ansprechpartner Fachlich IT Extern**, der für Fragen und Anliegen zur Verfügung steht. Die **Dokumentenablage** ist in verschiedenen Systemen wie ORGA Dateisystem, Doc-Gen Wiki und GIT Anleitungen zu finden.

Ein wichtiger Teil der Dokumentation sind die **Server**, die für die Anwendung notwendig sind, einschließlich Anwendungsserver, Datenbank-Server und nützliche Server-Befehle. Darüber hinaus werden **verarbeitete Daten** wie fachliche Daten und personenbezogene Daten behandelt.

Die **Systemarchitektur** von Doc-Gen Version 1.8 wird detailliert beschrieben, einschließlich der **Bestandteile der Anwendung**, wie dem Testsystem, dem Operator/Converter und dem Integration Server (EIS). Es gibt auch Informationen über die **Konfigurationseiten** und die **Client-Gruppen** in der Active Directory (AD).

Die Anwendung ist von anderen Anwendungen **abhängig**, und es gibt einen **zeitlichen Verlauf** wichtiger Ereignisse, wie die Plan-B-Migration, die Installation von Doc-Gen-Komponenten und die Untersuchung von Sicherheitsschwachstellen.

Hier sind die wichtigsten Schritte im zeitlichen Verlauf:

1. **09.10.2023**: Plan-B-Migration in RZ Bundesallee
2. **08.12.2022**: Installation von Doc-Gen Operator, Converter und teilweise EIS auf schwubs374
3. **07.12.2022**: Installation von JBoss
4. **01.12.2022**: Neuer Doc-Gen-Server schwubs374
5. **21.09.2022**: Start für das Update auf Version 1.8
6. **19.01.2017**: OTRS-Ticket #10021325
7. **27.10.2016**: Aktualisierung der Testdatenbank
8. **11.01.2017**: Vorbereitung der Aktualisierung der Produktion
9. **27.08.2018**: Untersuchung der Ghostscript-Schwachstelle

Insgesamt bietet die Liste eine umfassende Übersicht über die Anwendung Doc-Gen, ihre Komponenten, ihre Abhängigkeiten und ihre Entwicklungsgeschichte.

## Vorwort Bearbeiten

Generierung von Dokumenten für die Zulassung von Pflanzenschutzmitteln auf Basis von Faktendatenbanken (Bsp. Abt. 2 INFOZUPF) Die Dokumente werden in das VBS übertragen und von dort aus an den Antragsteller übermittelt

## Ansprechpartner Bearbeiten

## Fachlich Bearbeiten

Britta Busch

## IT Bearbeiten

Die Liste aus dem Abschnitt "IT" des Dokuments "Doc-Gen" enthält eine Aufzählung von Personen, die offensichtlich mit IT-bezogenen Aufgaben oder Projekten in Verbindung stehen. Die Liste umfasst insgesamt fünf Personen:

Die folgenden Personen sind in der Liste aufgeführt: @Diana Stölzel, @Vladislav Konov, @Hans Labod, @Alexandra Freytag und @Andreas Stengl. Diese Liste scheint eine Zusammenstellung von Teammitgliedern oder Verantwortlichen für bestimmte IT-Aufgaben zu sein, ohne dass spezifische Schritte oder Anweisungen genannt werden. Es handelt sich daher um eine einfache Auflistung von Namen, die möglicherweise für Kommunikations- oder Koordinationszwecke verwendet wird.

## Extern Bearbeiten

Die Liste enthält Kontaktdaten und Ressourcen für die externe Bearbeitung von Doc-Gen. Zusammengefasst bietet sie Informationen über die Ansprechpartner und Unterstützungsangebote für Benutzer. Hier sind die Details:

Für Fragen oder Anliegen stehen verschiedene Ansprechpartner zur Verfügung:
- Der Account Manager ist Claudia Theobald, die unter der E-Mail-Adresse Claudia.Theobald@doc-gen.de erreichbar ist.
- Für technische Koordination ist Lars Decker zuständig, der unter der E-Mail-Adresse Lars.Decker@doc-gen.de kontaktiert werden kann.
- Für spezifische Anfragen zu Doc-Gen EIS kann man sich an Frederik Zimmer unter der E-Mail-Adresse Frederik.Zimmer@doc-gen.de wenden.
- Für weitere Unterstützung und Hilfe bietet Doc-Gen ein Support-Portal unter der Adresse https://service.doc-gen-software.de an.

Es handelt sich nicht um eine Schrittfolge, sondern um eine Auflistung von Kontaktdaten und Ressourcen. Diese Informationen ermöglichen es Benutzern, schnell und einfach die richtigen Ansprechpartner zu finden oder Unterstützung zu erhalten, wenn sie mit Doc-Gen arbeiten.

## Dokumentenablage Bearbeiten

## ORGA Dateisystem Bearbeiten

Die Liste enthält Pfadangaben für die Dateiablage im Rahmen des Dokumenttitels "Doc-Gen" im Abschnitt "ORGA Dateisystem Bearbeiten". Zusammengefasst handelt es sich um zwei verschiedene Speicherorte für Dokumente und Projekte im Dateisystem.

Die Liste kann wie folgt zusammengefasst werden:

Es gibt zwei wichtige Speicherorte im Dateisystem:
1. Der erste Speicherort ist `\dateiablage1-bs\Projekte\DokGen`, der möglicherweise als Hauptspeicherort für das Projekt "DokGen" dient.
2. Der zweite Speicherort ist `\dateiablage1-bs\Projekte\IT-Anwendungen-Abt2\04_DOC-GEN\04_Dokumentation\DOC-GEN`, der spezifischer für die Dokumentation innerhalb des Projekts "DokGen" oder der IT-Anwendungen der Abteilung 2 sein könnte.

Diese beiden Speicherorte bieten eine klare Struktur für die Organisation von Dokumenten und Projekten im Dateisystem.

## Doc-Gen Wiki Bearbeiten

Die Liste bezieht sich auf den Zugriff auf die DOC-GEN Wiki-Seite. Hier finden Sie eine Zusammenfassung der Informationen:

Die DOC-GEN Wiki-Seite ist ein zentrales Informationsportal, auf dem Sie Handbücher und Hilfestellungen zur Installation und Wartung finden können. Um auf diese Ressourcen zuzugreifen, müssen Sie die folgenden Schritte befolgen:

1. Öffnen Sie den Browser und navigieren Sie zur URL: www.doc-gen-wiki.de
2. Melden Sie sich an, indem Sie den Benutzernamen "doc-gen-help" und das entsprechende Passwort verwenden. 
3. Um das Passwort zu finden, öffnen Sie die Datei "S0FTW4RE-Kennwoerter.kdbx" mit dem Tool Keepass.

Nachdem Sie diese Schritte befolgt haben, sollten Sie Zugriff auf die DOC-GEN Wiki-Seite haben und die verfügbaren Ressourcen nutzen können.

## GIT Bearbeiten

https://devops.cloud.orga.in.bund.de/scm/repo/A2/2012-DokGen/code/sources/master/

```
git clone https://devops.cloud.orga.in.bund.de/scm/repo/A2/2012-DokGen
```

## Anleitungen Bearbeiten

Die Liste aus der technischen Wiki-Seite enthält wichtige Dokumente und Schritte für die Implementierung und den Betrieb eines Systems. Zusammengefasst umfasst sie die folgenden Punkte:

Um das System erfolgreich zu implementieren und zu betreiben, müssen einige wichtige Schritte und Dokumente berücksichtigt werden. Dazu gehören:

1. **Installationshandbuch**: Dieses Handbuch befindet sich unter \\dateiablage1-bs\Abteilung_Z\Grp_A4_Allgemein\Dokumentation\Installationshandbücher und enthält alle notwendigen Anweisungen für die Installation des Systems.
2. **Betriebshandbuch**: Nach der Installation ist das Betriebshandbuch unter \\dateiablage1-bs\Abteilung_Z\Grp_A4_Allgemein\Dokumentation\Betriebshandbücher zu finden. Es bietet Anleitungen für den täglichen Betrieb und die Wartung des Systems.
3. **Übernahme von Änderungen**: Schließlich ist es wichtig, Änderungen aus dem Entwicklungssystem in das Produktivsystem zu übernehmen. Dieser Prozess wird als "Domänen_transportieren" bezeichnet und ist ein entscheidender Schritt, um sicherzustellen, dass das System auf dem neuesten Stand bleibt und alle notwendigen Funktionen und Updates enthält.

Diese Schritte und Dokumente sind entscheidend für eine erfolgreiche Implementierung und den reibungslosen Betrieb des Systems. Durch die Befolgung dieser Anleitungen kann man sicherstellen, dass das System korrekt installiert, betrieben und aktualisiert wird.

## Server Bearbeiten

## Anwendungsserver Bearbeiten

Produktiv: s-0214m.srv.domain.de

Test: s-0224m.srv.domain.de

## Datenbank Server Bearbeiten

Datenbank Server Produktiv: s-0941.db.domain.de:1521/doc-gen19

Datenbank Server Test: s-0941.db.domain.de:1521/tbv19

## Nützliche Server Befehle Bearbeiten

Der Abschnitt "Nützliche Server Befehle" im Dokument "Doc-Gen" bietet eine Übersicht über wichtige Befehle für die Verwaltung von Servern. Eine der wichtigsten Aktionen ist das Starten des Servers. Dieser Vorgang sollte sorgfältig durchgeführt werden, um sicherzustellen, dass der Server ordnungsgemäß funktioniert.

Um den Server zu starten, sollten Sie folgende Schritte befolgen:
1. Stellen Sie sicher, dass Sie als root-Benutzer angemeldet sind, da das Starten des Servers administrative Rechte erfordert.
2. Führen Sie den entsprechenden Befehl zum Starten des Servers aus. Der genaue Befehl kann je nach Server-Software und Betriebssystem variieren, daher sollten Sie sich an die spezifischen Anweisungen für Ihr System halten.

Es ist wichtig, dass Sie diese Schritte sorgfältig befolgen, um sicherzustellen, dass der Server korrekt gestartet wird und keine Probleme oder Sicherheitsrisiken verursacht.

```
systemctl start jboss-eap-rhel
systemctl start tomcat
```

Der Abschnitt "Nützliche Server Befehle" im Dokument "Doc-Gen" enthält eine Liste mit wichtigen Befehlen für die Verwaltung von Servern. Eine der wichtigsten Aktionen, die in dieser Liste erwähnt wird, ist das Stoppen des Servers.

Um den Server zu stoppen, sollten Sie folgende Schritte befolgen:
1. Stellen Sie sicher, dass Sie als root-Benutzer angemeldet sind, da dieser Vorgang administrative Rechte erfordert.
2. Führen Sie den entsprechenden Befehl aus, um den Server zu stoppen. Der genaue Befehl kann je nach Server-Software und Betriebssystem variieren, daher sollten Sie sich an die spezifischen Anweisungen für Ihr System halten.

Es ist wichtig, dass Sie diese Schritte sorgfältig befolgen, um sicherzustellen, dass der Server ordnungsgemäß heruntergefahren wird und keine Daten verloren gehen. Wenn Sie weitere Informationen oder spezifische Anweisungen benötigen, sollten Sie sich an die offizielle Dokumentation oder den Support Ihres Servers wenden.

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

Die Liste scheint eine URL zu enthalten, die zum Testsystem von Doc-Gen Ver. 1.8 gehört. Zusammengefasst handelt es sich um eine spezifische Webadresse, die für den Zugriff auf das Testsystem benötigt wird.

Um auf das Testsystem zuzugreifen, können Sie folgende Schritte befolgen:

1. Öffnen Sie Ihren Webbrowser und geben Sie die folgende URL ein: https://doc-gen-test.domain.de:6228/generator-launcher/ui/orga/template-list
2. Fügen Sie die erforderlichen Parameter an die URL an, um auf die gewünschte Ressource zuzugreifen. Die Parameter sind:
 * antragsnummer: 00Z001-00/00
 * vorgang: 27596
3. Die vollständige URL sollte dann wie folgt aussehen: https://doc-gen-test.domain.de:6228/generator-launcher/ui/orga/template-list?antragsnummer=00Z001-00/00&vorgang=27596

Wenn Sie diese Schritte befolgen, sollten Sie in der Lage sein, auf das Testsystem von Doc-Gen Ver. 1.8 zuzugreifen und die gewünschten Funktionen zu nutzen.

Doc-Gen Operator

Die Liste enthält zwei URLs, die auf verschiedene Testsysteme für Doc-Gen Ver. 1.8 hinweisen. Zusammengefasst bieten diese URLs Zugriff auf Testumgebungen für das Doc-Gen-System, die über unterschiedliche Protokolle und Ports erreichbar sind.

Um auf diese Testsysteme zuzugreifen, können Sie die folgenden Schritte befolgen:

1. Öffnen Sie Ihren bevorzugten Webbrowser.
2. Geben Sie eine der folgenden URLs in die Adresszeile ein:
   - Für den ersten Testsystem-Zugriff: http://doc-gen-test.domain.de:6260/doc-gen-web/operator/
   - Für den zweiten Testsystem-Zugriff: https://doc-gen-test.domain.de:6428/doc-gen-web/operator/
3. Drücken Sie die Enter-Taste, um die entsprechende Testumgebung aufzurufen.

Diese URLs ermöglichen es Ihnen, die Funktionalität und Leistung des Doc-Gen-Systems in verschiedenen Testumgebungen zu überprüfen und zu testen. Beachten Sie dabei die Unterschiede in den Protokollen (http vs. https) und den Ports (6260 vs. 6428), die für den Zugriff auf die jeweiligen Testsysteme erforderlich sind.

## Testsystem Operator/Converter 1.8

Die Tabelle stellt eine Sammlung von Bezeichnungen und ihren entsprechenden Werten im Kontext des Testsystem Operator/Converter 1.8 dar. Sie bietet eine Übersicht über verschiedene Konfigurationen oder Einstellungen, die für das System relevant sind.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die Spalte "Bezeichnung" enthält die Namen oder Identifikatoren für verschiedene Einstellungen oder Konfigurationen.
* Die Spalte "Wert" enthält die spezifischen Werte, die jeder Bezeichnung zugeordnet sind.

Leider ist die Tabelle leer, daher kann ich keine beschreibenden Sätze für die Tabellenzeilen formulieren. Wenn die Tabelle gefüllt wäre, würde ich jeden Eintrag in einen Satz umwandeln, um die Beziehung zwischen Bezeichnung und Wert zu beschreiben. Zum Beispiel: "Die Bezeichnung X hat den Wert Y." Wenn eine Zeile eine leere Bezeichnung enthält, würde ich mich auf die letzte nicht-leere Bezeichnung beziehen und den entsprechenden Wert dazu beschreiben.

Diese Tabelle stellt Informationen über eine bestimmte Applikation und ihre Umgebung im Kontext des Testsystems Operator/Converter 1.8 dar. Sie enthält Details über den Server und die verwendete Software.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die erste Spalte gibt den Typ oder die Kategorie der Information an, wie z.B. "Applikation" oder "Server".
* Die zweite Spalte enthält spezifische Details zu der in der ersten Spalte genannten Kategorie, wie z.B. die Server-Adresse oder die Software-Version.

Die Tabellenzeilen können wie folgt beschrieben werden:
Die Applikation wird auf einem Server mit der Adresse 188.455.5.174 (s-0224m.srv.domain.de) gehostet. 
Die Applikation verwendet JBoss 7.4. 

Es ist zu beachten, dass die zweite und dritte Zeile der Tabelle auf die "Applikation" Bezug nehmen, da die erste Spalte leer ist und somit als Fortsetzung der vorherigen Kategorie interpretiert wird.

Diese Tabelle stellt eine Zusammenstellung von Konfigurationsparametern für eine Datenbankverbindung dar. Sie enthält Informationen, die für den Zugriff auf eine bestimmte Datenbank erforderlich sind.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die erste Spalte enthält die Kategorie oder den Typ der Konfiguration, wie z.B. "Datenbank", "Server", "Port", "SID" und "User".
* Die zweite Spalte enthält den entsprechenden Wert oder die spezifische Einstellung für jede Kategorie.

Die Tabellenzeilen können wie folgt beschrieben werden:
Die Datenbank verwendet den Server 188.455.6.52, der auch als s-0941.db.domain.de bekannt ist. 
Der Port, der für die Datenbankverbindung verwendet wird, ist 1521. 
Die System-ID (SID) der Datenbank ist tbv19. 
Der Benutzername für den Zugriff auf die Datenbank ist doc-gentest18.

## Testsystem Doc-Gen Integration Server (EIS) 1.8

Die Tabelle stellt eine Sammlung von Bezeichnungen und ihren entsprechenden Werten im Kontext des Doc-Gen Integration Servers (EIS) 1.8 dar. Sie bietet eine Übersicht über verschiedene Konfigurationen oder Eigenschaften des Systems.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Bezeichnung: Diese Spalte enthält die Namen oder Identifikatoren von verschiedenen Komponenten, Eigenschaften oder Konfigurationen innerhalb des Doc-Gen Integration Servers.
* Wert: Diese Spalte enthält die entsprechenden Werte oder Einstellungen, die jeder Bezeichnung zugeordnet sind.

Leider ist die Tabelle leer, daher kann ich keine spezifischen Tabellenzeilen als beschreibende Sätze formulieren. Wenn die Tabelle jedoch gefüllt wäre, würde ich jede Zeile in einen Satz übersetzen, der die Bezeichnung und ihren entsprechenden Wert beschreibt. Zum Beispiel, wenn eine Zeile "Bezeichnung1,Wert1" enthielte, würde der entsprechende Satz lauten: "Die Bezeichnung1 hat den Wert Wert1." Für Zeilen, die als Fortsetzung einer vorherigen Bezeichnung dienen, würde ich mich auf die letzte nicht-leere Kategorie beziehen und den Satz entsprechend anpassen.

Diese Tabelle stellt Informationen über eine bestimmte Applikation und deren Server- und Software-Konfiguration dar. Sie bietet einen Überblick über die technischen Details einer bestimmten Umgebung, in diesem Fall des Doc-Gen Integration Servers.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die erste Spalte enthält den Namen oder die Kategorie der Applikation oder des Servers.
* Die zweite Spalte enthält spezifische Details oder Konfigurationen, wie z.B. die IP-Adresse oder den Server-Namen.
* Die dritte Spalte enthält Informationen über die verwendete Software oder den Server-Typ.

Die Tabellenzeilen können wie folgt beschrieben werden:
Die Applikation wird auf einem Server mit der IP-Adresse 188.455.5.174 (s-0224m.srv.domain.de) gehostet. 
Die Applikation verwendet Tomcat 9 als Server-Software. 

Insgesamt bietet diese Tabelle einen schnellen Überblick über die technischen Details der Doc-Gen Integration Server-Umgebung.

Diese Tabelle stellt die Konfigurationsdetails für die Verbindung zu einer Datenbank im Rahmen des Doc-Gen Integration Servers (EIS) 1.8 dar. Sie enthält Informationen über den Server, den Port, die System-ID (SID) und die Benutzer, die für die Verbindung verwendet werden.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
- Die erste Spalte enthält die Kategorie oder den Typ der Konfiguration, wie z.B. "Datenbank", "Server", "Port", "SID" und "User".
- Die zweite Spalte enthält die entsprechenden Werte oder Details zu jeder Kategorie.

Die Tabellenzeilen können wie folgt beschrieben werden:
- Die Datenbank ist auf dem Server mit der Adresse 188.455.6.52 (s-0941.db.domain.de) konfiguriert.
- Der Port, der für die Verbindung zur Datenbank verwendet wird, ist 1521.
- Die System-ID (SID) der Datenbank ist tbv19.
- Die Benutzer, die für die Verbindung zur Datenbank verwendet werden, sind EISKARMA_dev, EISJPAStore_dev, EISLockRegistry_dev, EISTBHStore_dev und EISUserService_dev.

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

Die Liste bezieht sich auf den Abschnitt "Doc-Gen Ver. 1.8 Produktivsystem" in der technischen Wiki-Seite. Sie enthält zwei URLs und eine wichtige Anmerkung. Hier ist eine Zusammenfassung der Liste als gut lesbarer Fließtext:

Die Liste enthält zwei URLs, die zum Doc-Gen-System gehören. Die erste URL ist spezifisch für eine bestimmte Antragsnummer und einen Vorgang:
https://doc-gen.domain.de:6228/generator-launcher/ui/orga/template-list?antragsnummer=009999-00/00&vorgang=27596

Die zweite URL ist eine allgemeine URL für den Template-List-Bereich:
https://doc-gen.domain.de:6228/generator-launcher/ui/orga/template-list

Es ist wichtig zu beachten, dass Bescheide nicht erstellt werden sollten, da sie sonst im Infozupf landen. Dies ist eine wichtige Anweisung, um sicherzustellen, dass die Dokumente korrekt verarbeitet werden.

Es gibt keine spezifischen Schritte, die in dieser Liste beschrieben werden, sondern eher eine Sammlung von Informationen und einer wichtigen Anmerkung. Wenn Sie jedoch die URLs verwenden möchten, können Sie folgende Schritte befolgen:

1. Öffnen Sie die erste URL, um auf die spezifische Antragsnummer und den Vorgang zuzugreifen.
2. Öffnen Sie die zweite URL, um auf den allgemeinen Template-List-Bereich zuzugreifen.
3. Beachten Sie die Anweisung, keine Bescheide zu erstellen, um sicherzustellen, dass die Dokumente korrekt verarbeitet werden.

Die Tabelle stellt die Konfiguration oder Eigenschaften des Doc-Gen Ver. 1.8 Produktivsystems dar. Sie enthält Informationen über verschiedene Aspekte des Systems, die in zwei Spalten aufgelistet sind.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die erste Spalte "Bezeichnung" enthält die Namen oder Kategorien der Eigenschaften oder Konfigurationen.
* Die zweite Spalte "Wert" enthält die entsprechenden Werte oder Einstellungen für jede Bezeichnung.

Leider ist die Tabelle leer, daher gibt es keine Zeilen, die beschrieben werden können. Wenn die Tabelle gefüllt wäre, würde jede Zeile als beschreibender Satz formuliert werden, der die Bezeichnung und den entsprechenden Wert enthält. Zum Beispiel: 
- Wenn eine Zeile die Bezeichnung "Systemversion" und den Wert "1.8" enthält, würde der Satz lauten: Die Systemversion ist 1.8.
- Wenn eine Zeile eine leere Bezeichnung und einen Wert enthält, würde sich der Satz auf die letzte nicht-leere Bezeichnung beziehen.

Diese Tabelle stellt eine Übersicht über die Applikationen und deren zugehörigen Server dar. Sie enthält Informationen über die Verbindung zwischen bestimmten Anwendungen und den Servern, auf denen sie gehostet werden.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die erste Spalte enthält den Namen der Applikation.
* Die zweite Spalte enthält die Informationen über den Server, einschließlich der IP-Adresse und des Domain-Namens.

Die Tabellenzeile kann wie folgt beschrieben werden: Die Applikation wird auf dem Server mit der IP-Adresse 188.455.5.164 und dem Domain-Namen s-0214m.srv.domain.de/doc-gen.domain.de gehostet.

Diese Tabelle stellt die Konfigurationsdetails für die Datenbank des Doc-Gen Ver. 1.8 Produktivsystems dar. Sie enthält Informationen über den Zugriff auf die Datenbank, wie Serveradresse, Port, SID und Benutzername.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die erste Spalte enthält die Kategorie oder den Typ der Konfiguration, wie z.B. Datenbank, Server, Port, SID und User.
* Die zweite Spalte enthält den entsprechenden Wert oder die Details zu jeder Kategorie.

Die Tabellenzeilen können wie folgt beschrieben werden:
Die Datenbank ist auf dem Server mit der Adresse 188.455.6.52 (s-0941.db.domain.de) konfiguriert. 
Der Port für die Datenbank ist 1521. 
Der SID für die Datenbank ist doc-gen19. 
Der User für die Datenbank ist DOC-GEN_PROD.

## Produktivsystem Doc-Gen Intergation Server (EIS) 1.8

Die Tabelle stellt eine Sammlung von Informationen über den Doc-Gen Intergation Server (EIS) 1.8 dar, der Teil des Produktivsystems Doc-Gen ist. Diese Informationen sind in einer strukturierten Form präsentiert, um eine einfache Übersicht über die verschiedenen Aspekte des Servers zu ermöglichen.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die Spalte "Bezeichnung" enthält die Namen oder Kategorien, unter denen die verschiedenen Werte oder Einstellungen des Doc-Gen Intergation Servers (EIS) 1.8 aufgelistet sind.
* Die Spalte "Wert" enthält die spezifischen Werte oder Einstellungen, die zu jeder Bezeichnung gehören.

Leider ist die Tabelle leer, daher kann ich keine spezifischen Tabellenzeilen als beschreibende Sätze formulieren. Wenn die Tabelle gefüllt wäre, würde ich jede Zeile in einen Satz übersetzen, der die Bezeichnung und den entsprechenden Wert beschreibt. Zum Beispiel: "Die Bezeichnung XYZ hat den Wert ABC." Wenn eine Zeile eine leere Bezeichnung enthält, würde ich mich auf die letzte nicht-leere Kategorie beziehen und den Satz entsprechend anpassen.

Diese Tabelle stellt eine Übersicht über die Konfiguration des Produktivsystems Doc-Gen Intergation Server (EIS) 1.8 dar. Sie enthält Informationen über die Applikation und den Server, auf dem sie ausgeführt wird.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die erste Spalte enthält den Namen der Applikation.
* Die zweite Spalte enthält die Server-Informationen, einschließlich der IP-Adresse und des Domains.

Die Tabellenzeile kann wie folgt beschrieben werden: Die Applikation wird auf dem Server mit der IP-Adresse 188.455.5.164 und dem Domain doc-gen.domain.de ausgeführt. 

Es gibt nur eine Zeile in der Tabelle, daher ist dies auch die einzige Beschreibung.

Diese Tabelle stellt die Konfigurationsdetails für die Datenbankverbindung des Doc-Gen Intergation Server (EIS) 1.8 dar. Sie enthält Informationen über den Server, den Port, die Systemkennung (SID) und die autorisierten Benutzer.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Datenbank: Bezeichnet die Art der Datenbank oder den Kontext, in dem die folgenden Informationen gelten.
* Server: Gibt den Server an, der für die Datenbankverbindung verwendet wird.
* Port: Definiert den Port, über den die Verbindung hergestellt wird.
* SID: Stellt die Systemkennung der Datenbank dar, die für die Verbindung benötigt wird.
* User: Listet die autorisierten Benutzer auf, die Zugriff auf die Datenbank haben.

Die Tabellenzeilen können wie folgt beschrieben werden:
Die Datenbank verwendet den Server 188.455.6.52, der auch als s-0941.db.domain.de bezeichnet wird.
Der Port, der für die Datenbankverbindung verwendet wird, ist 1521.
Die Systemkennung (SID) der Datenbank ist doc-gen19.
Die autorisierten Benutzer für die Datenbank sind EISKARMA, EISJPAStore, EISLockRegistry, EISTBHStore und EISUserService.

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

Der Abschnitt "Client Bearbeiten" im Dokument "Doc-Gen" befasst sich mit den verschiedenen Tools und Anwendungen, die für die Bearbeitung und Verwaltung von Dokumenten verwendet werden können. Die Liste umfasst zwei wichtige Komponenten:

Die erste Komponente ist der Webbrowser für Endanwender, der als "doc-gen19" bezeichnet wird. Dieser ermöglicht es Endanwendern, auf eine einfache und benutzerfreundliche Weise mit den Dokumenten zu interagieren.

Die zweite Komponente ist der "Doc-Gen_Designer" für Administratoren. Dieser bietet Administratoren eine umfassende Plattform, um Dokumente zu erstellen, zu bearbeiten und zu verwalten.

Zusammengefasst bietet die Liste eine Übersicht über die beiden Hauptkomponenten des Doc-Gen-Systems: den Webbrowser für Endanwender und den Designer für Administratoren. Diese beiden Komponenten ermöglichen es, Dokumente auf verschiedenen Ebenen zu bearbeiten und zu verwalten, um eine effiziente und benutzerfreundliche Dokumentenverwaltung zu gewährleisten. 

Es handelt sich hier nicht um Schritte, sondern um eine Beschreibung der Komponenten, daher ist keine Schrittfolge erforderlich.

## Gruppen in der AD Bearbeiten

Die Liste bezieht sich auf verschiedene Gruppen in der Active Directory (AD) im Zusammenhang mit dem Dokumenttitel "Doc-Gen". Diese Gruppen scheinen in der Verwaltung und Erstellung von Dokumenten und Berichten eine Rolle zu spielen. Hier ist eine zusammenfassende Erklärung der Liste:

Die Gruppen in der AD umfassen verschiedene Bereiche, die für die Dokumentenerstellung und -verwaltung relevant sind. Dazu gehören:
- **Doc-Gen_Zwimis_PSM**: Diese Gruppe ist möglicherweise für die Verwaltung von Zwischenmitteln oder Zwischenprodukten im Rahmen der Dokumentenerstellung zuständig.
- **Doc-Gen_Bescheide_PSM**: Hierbei handelt es sich wahrscheinlich um eine Gruppe, die sich mit der Erstellung oder Verwaltung von Bescheiden beschäftigt, was in einem bestimmten Kontext, wie zum Beispiel in der öffentlichen Verwaltung, relevant sein könnte.
- **Doc-Gen_Zulassungsberichte_PSM**: Diese Gruppe könnte für die Erstellung oder Verwaltung von Zulassungsberichten verantwortlich sein, was in Bereichen wie der Zulassung von Produkten oder Dienstleistungen eine wichtige Rolle spielt.
- **WebAuthor_PSM**: Der Name dieser Gruppe deutet darauf hin, dass sie mit der Erstellung oder Verwaltung von Web-Inhalten zu tun hat, möglicherweise im Rahmen der Dokumentenerstellung oder -veröffentlichung.

Da es sich hier nicht um eine Schrittfolge handelt, sondern um eine Auflistung von Gruppen, gibt es keine nummerierte Schrittfolge. Stattdessen bietet diese Erklärung einen Überblick über die verschiedenen Gruppen und ihre möglichen Funktionen im Rahmen der Dokumentenerstellung und -verwaltung in der AD.

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

Die Liste beschreibt eine Reihe von Schritten und Aufgaben, die im Rahmen der Vorbereitung einer Aktualisierung der Produktion durchgeführt wurden. Hier ist eine Zusammenfassung der Liste als gut lesbaren Fließtext:

Im Rahmen der Vorbereitung der Aktualisierung der Produktion wurden verschiedene Schritte durchgeführt. Die folgenden Aufgaben wurden abgeschlossen:

1. **Ein Template in der neuen Entwicklung anlegen**: Dieser Schritt wurde von H. Busch durchgeführt.
2. **Den Domänentransport testen**: H. Busch und Stölzel haben den Domänentransport getestet.
3. **Gen-Admin Konfigurationsdatei anpassen**: Die Konfigurationsdatei wurde von H. Stölzel und Busch angepasst, um die beiden Testvorlagenschlüssel zu entfernen.
4. **Zulassungsbericht erstellen**: H. Stölzel hat einen Zulassungsbericht erstellt.
5. **Berechtigungen überprüfen**: H. Stölzel hat die Berechtigungen mit Frau Bolten oder Stevens überprüft.
6. **Bescheiddaten kontrollieren**: H. Busch und Stölzel haben die Bescheiddaten kontrolliert.
7. **Fehler in Formatierung beheben**: H. Gabel hat einen Fehler in der Formatierung im Testsystem Subs172.old.domain.de untersucht und behoben.
8. **Einrichtung Apache und Erstellung einer index.html**: H. Gabel hat Apache auf schwubs174.old.domain.de eingerichtet und eine index.html erstellt, die beim Aufruf von http://webauthor.old.domain.de auf schwubs174.old.domain.de:4040/secure/webauthor/ weiterleitet.

Es gibt jedoch noch zwei offene Punkte:
- Der Testaufbau Apache auf schwubs172.old.domain.de für die Weiterleitung auf schwubs174.old.domain.de:4040/secure/webauthor/ ist noch nicht abgeschlossen, da auf die Rückkehr von Henrik gewartet wird.
- Die Untersuchung, warum beim Aufruf von http://webauthor.old.domain.de:4040/secure/webauthor/ auf http://schwubs031.old.domain.de:4040/secure/webauthor/ umgeleitet wird, hat ergeben, dass die Anwendung den HTTP-Header location:SERVERNAME setzt, was möglicherweise nur durch eine Softwareanpassung geändert werden kann.

Am Tag der Umstellung :

Die Liste beschreibt die Schritte und Aufgaben im Rahmen der Vorbereitung der Aktualisierung der Produktion am 11.01.2017 für das Dokument "Doc-Gen". Hier sind die Schritte und Aufgaben in einer klaren und lesbaren Form dargestellt:

Die Vorbereitung der Aktualisierung der Produktion umfasst mehrere Schritte, die wie folgt auszuführen sind:

1. **Exportieren und Importieren von TBV**: Zunächst müssen die alten Produktionen von `srvlnx170.old.domain.de` exportiert und in die neue Produktion auf `Subs169.old.domain.de` importiert werden. Dieser Schritt wurde bereits von "amir" durchgeführt.
2. **Aktualisierung des Jackrabbit Repository**: Als nächstes muss das Jackrabbit Repository von `Subs031.old.domain.de` auf `Subs174.old.domain.de` aktualisiert werden. Dieser Schritt wurde bereits von "H: Gabel" durchgeführt.
3. **DNS-Umstellung**: Es müssen zwei DNS-Umstellungen durchgeführt werden:
 * Die DNS-Umstellung für `doc-gen.old.domain.de` von `schwubs031.old.domain.de` auf `schwubs174.old.domain.de` wurde bereits von "Gabel" und "Lux" durchgeführt.
 * Die DNS-Umstellung für `webauthor.old.domain.de` von `schwubs031.old.domain.de` auf `schwubs174.old.domain.de` wurde ebenfalls von "Gabel" und "Lux" durchgeführt.
4. **Fachliche Freigabe**: Die fachliche Freigabe wurde bereits von "H: Britta Busch" erteilt.
5. **Abschaltung Altsysteme**: Die Altsysteme `Subs028.old.domain.de` bis `Subs031.old.domain.de` wurden bereits abgeschaltet.
6. **Beantragung Anpassung Nagios Überwachung**: Die Anpassung der Nagios Überwachung wurde bereits von "H: Gabel" beantragt.
7. **Aktualisierung Dokumentation**: Die Dokumentation (Wiki, Installation/Betriebshandbuch) muss noch aktualisiert werden. Dieser Schritt ist noch ausstehend und wurde "H: Gabel" zugewiesen.

Insgesamt umfasst die Liste eine Reihe von Schritten und Aufgaben, die im Rahmen der Vorbereitung der Aktualisierung der Produktion durchgeführt werden müssen. Die meisten Schritte wurden bereits abgeschlossen, aber einige sind noch ausstehend.

## 2018-08-27 (Untersuchung Ghostscript Schwachstelle) Bearbeiten

Ein Ticket im Supportportal geöffnet ( DOC-GEN Support ESP-5481 )

Ergebnis:

Ghostskript wird nicht verwendet.

... Nein. Ghostscript wird von Doc-Gen nicht verwendet. ... {{/7box}} {{/box}}
