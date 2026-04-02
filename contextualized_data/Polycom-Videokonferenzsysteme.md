# Polycom-Videokonferenzsysteme

## Einleitung

Die Liste beschreibt die verschiedenen Komponenten und Aspekte eines Polycom-Videokonferenzsystems. Sie umfasst eine Vielzahl von Elementen, die für die Einrichtung und den Betrieb eines solchen Systems erforderlich sind.

Zunächst ist es wichtig, den richtigen Ansprechpartner zu haben, um Fragen und Probleme schnell und effizient lösen zu können. Darüber hinaus besteht die Polycom-Infrastruktur aus verschiedenen Komponenten wie IP-Netzen, Servern und Netzwerkbasisdiensten wie DHCP und DNS. Diese Komponenten sind notwendig, um die Polycom-Endgeräte zu aktualisieren und die CMS-Bund-Plattform (BDBOS) zu unterstützen.

Die Liste erwähnt auch Polycom-Clientsysteme, die für die Teilnahme an Videokonferenzen erforderlich sind. Darüber hinaus gibt es Standardkonfigurationen für bestimmte Modelle wie x50, x52 und G7500. Die Poly Clariti App ist ein weiteres wichtiges Element, das für die Nutzung des Videokonferenzsystems erforderlich ist.

Um ein Polycom-Videokonferenzsystem einzurichten und zu betreiben, können die folgenden Schritte befolgt werden:

1. **Ansprechpartner**: Stellen Sie sicher, dass Sie den richtigen Ansprechpartner haben, um Fragen und Probleme schnell und effizient lösen zu können.
2. **Infrastruktur**: Stellen Sie sicher, dass die notwendige Infrastruktur wie IP-Netze, Server und Netzwerkbasisdienste vorhanden ist.
3. **Endgeräte-Aktualisierung**: Aktualisieren Sie die Polycom-Endgeräte, um sicherzustellen, dass sie mit der CMS-Bund-Plattform (BDBOS) kompatibel sind.
4. **Clientsysteme**: Stellen Sie sicher, dass die notwendigen Polycom-Clientsysteme für die Teilnahme an Videokonferenzen vorhanden sind.
5. **Standardkonfiguration**: Verwenden Sie die Standardkonfigurationen für bestimmte Modelle wie x50, x52 und G7500, um die Einrichtung zu vereinfachen.
6. **Poly Clariti App**: Installieren Sie die Poly Clariti App, um die Nutzung des Videokonferenzsystems zu ermöglichen.

Zusammenfassend umfasst die Liste die verschiedenen Komponenten und Aspekte eines Polycom-Videokonferenzsystems, einschließlich der Infrastruktur, der Endgeräte, der Clientsysteme und der notwendigen Software. Durch die Befolgung der oben genannten Schritte kann ein Polycom-Videokonferenzsystem erfolgreich eingerichtet und betrieben werden.

## Ansprechpartner Bearbeiten

## Poly VK-Infrastruktur Bearbeiten

## IP-Netze Bearbeiten

### Tabelle: IP-Adressbereiche für Polycom-Videokonferenzsysteme
Die Tabelle stellt eine Übersicht über verschiedene IP-Adressbereiche und ihre Beschreibungen für Polycom-Videokonferenzsysteme dar. Sie enthält Informationen über die Netzwerkkonfiguration und die Zuweisung von IP-Adressen für verschiedene Standorte und Dienste.

### Spaltenbeschreibung
* Die erste Spalte enthält den IP-Adressbereich.
* Die zweite Spalte enthält eine Beschreibung des jeweiligen IP-Adressbereichs.

### Tabelleninhalte
Der IP-Adressbereich 123:213:80a:5800::/64 ::444 (vc.domain.de) wird über DFN über BRAIN verwendet. 
Der IP-Adressbereich 123.23.231.39/32 (vc.domain.de) wird über DFN verwendet und soll später an BRAIN announciert werden. 
Die IP-Adressbereiche 172.[17|19|23].8.0/24 werden durch 188.999.147.160 /28 (DDW) und 188.999.147.128/27 (Standort1) abgelöst und dienen internen Videonetzen. 
Der IP-Adressbereich 188.999.147.0/25 wird für die Standortkopplung des Videodienstes in der Hausstraße 49 verwendet. 
Der IP-Adressbereich 188.999.147.128/27 wird für die Standortkopplung und den Adressbereich für Endgeräte des Videodienstes in der Bundesallee 51 verwendet. 
Der IP-Adressbereich 188.999.147.160/28 wird für die Standortkopplung und den Adressbereich für Endgeräte des Videodienstes im Diedersdorfer Weg 1 verwendet. 
Der IP-Adressbereich 192.168.75.0/29 wird für den Transfer zwischen NdB-SBC und ORGA-SBC verwendet, wobei .2 NdB-SBC, .3 ORGA-SBC und .4 ORGA-SBC (für Redundanz geblockt, nicht vorhanden) sind.

## Server Bearbeiten

### Überschrift
Der Titel der Tabelle ist nicht explizit angegeben, daher kann sie als "Polycom-Videokonferenzsysteme-Server" bezeichnet werden.

### Beschreibung
Diese Tabelle stellt eine Übersicht über verschiedene Server in einem Polycom-Videokonferenzsystem dar. Sie enthält Informationen über die Verwendung, IP-Adresse, Seriennummer, Betriebssystem und Standort jedes Servers.

### Spaltenbeschreibung
* Name: Der Name des Servers
* Verwendung: Die Funktion oder der Zweck des Servers
* IP: Die IP-Adresse des Servers
* SN: Die Seriennummer des Servers
* OS: Das Betriebssystem des Servers
* Standort: Der physische Standort des Servers

### Tabelleninhalte
Der Server server70 wird für Netzwerkbasisdienste, Software-Deploy, DNS, DHCP verwendet und hat die IP-Adresse 188.340.8.2, keine Seriennummer, läuft unter RHEL 9 und befindet sich im VK-Cluster Standort2.
Der Server server71 dient als Clariti Manager und hat die IP-Adresse 188.340.8.21, keine Seriennummer, läuft unter OL 8 und befindet sich im VK-Cluster Standort2.
Der Server server72 dient als Clariti Core und hat die IP-Adresse 188.340.8.22, keine Seriennummer, läuft unter OL 8 und befindet sich im VK-Cluster Standort2.
Der Server server73 dient als RealPresence Collaboration Server und hat die IP-Adresse 188.340.8.23, keine Seriennummer, läuft unter OL 8 und befindet sich im VK-Cluster Standort2.
Der Server server74 dient als Clariti Media-Relay und hat die IP-Adresse 188.340.8.24, keine Seriennummer, läuft unter OL 8 und befindet sich im VK-Cluster Standort2.
Der Server server75 dient als Clariti Edge NdB-ID und hat die IP-Adresse 188.340.8.25, keine Seriennummer, läuft unter OL 8 und befindet sich im VK-Cluster Standort2.
Der Server server76 dient als Clariti Edge Internet und hat die IP-Adresse 188.340.8.26, keine Seriennummer, läuft unter OL 8 und befindet sich im VK-Cluster Standort2.
Der Server server77 dient als Clariti Edge Client und hat die IP-Adresse 188.340.8.27, keine Seriennummer, läuft unter OL 8 und befindet sich im VK-Cluster Standort2.
Der Server sbc001 dient als Secunet SBC Internet, hat keine IP-Adresse, keine Seriennummer und befindet sich im RZ Standort2, wo er aktuell ausgebaut wird.
Der Server sbc002 dient als Secunet SBC Internet, hat keine IP-Adresse, keine Seriennummer und befindet sich im RZ Standort2, wo er aktuell ausgebaut wird.
Der Server sbcmgt dient als Secunet SBC Manager, hat keine IP-Adresse, keine Seriennummer und befindet sich im RZ Standort2, wo er aktuell ausgebaut wird.

## S-1870: Netzwerkbasisdienste Bearbeiten

## DHCP

Genutzt wird der KEA-DHCP-Server (Nachfolger des ISC-DHCP-Servers).

Die Konfigdateien liegen unter /etc/kea/.

Die Liste bezieht sich auf die Konfiguration von Polycom-Videokonferenzsystemen im Zusammenhang mit DHCP (Dynamic Host Configuration Protocol). Sie enthält zwei wichtige Konfigurationsdateien, die für die Einrichtung und Verwaltung von DHCP-Diensten verwendet werden.

Die Liste kann wie folgt zusammengefasst werden:

Für die Konfiguration von DHCP-Diensten in Polycom-Videokonferenzsystemen sind zwei wichtige Dateien zu beachten:
1. Die Kea-Main-Konfiguration, die in der Datei **keactrl.conf** gespeichert ist. Diese Datei enthält die Hauptkonfiguration für den Kea-DHCP-Server.
2. Die Kea-DHCP4-Konfiguration, die in der Datei **kea-dhcp4.conf** gespeichert ist. Diese Datei enthält spezifische Einstellungen für den DHCPv4-Dienst.

Diese beiden Dateien sind entscheidend für die korrekte Einrichtung und Verwaltung von DHCP-Diensten in Polycom-Videokonferenzsystemen. Durch die Bearbeitung und Konfiguration dieser Dateien können Administratoren sicherstellen, dass ihre Videokonferenzsysteme ordnungsgemäß mit IP-Adressen und anderen Netzwerkeinstellungen versorgt werden.

DHCP6 ist derzeit deaktiviert. Kann in der Kea-Main-Konfig aktiviert und in der kea-dhcp6.conf konfiguriert werden.

Der DHCP ist aktuell nur für die Berliner Endgeräte. Es gibt aktuell kein DHCP-Relay zur BU oder zum DDW.

## DNS

Der
BIND (named) DNS-Server wird für die interne DNS-Zone
vk.segment.domain.de genutzt und sorgt für die DNS-Auflösungen innerhalb
des VK-Clusters.

Die Liste bezieht sich auf die Konfiguration von DNS (Domain Name System) im Rahmen von Polycom-Videokonferenzsystemen. Hier sind die wichtigsten Punkte zusammengefasst:

Die Konfiguration von DNS für Polycom-Videokonferenzsysteme umfasst zwei wichtige Dateien:
- Die Named-Konfiguration, die in der Datei `/etc/named.conf` zu finden ist, enthält die allgemeinen Einstellungen für den DNS-Server.
- Die Named-Zonen, die in der Datei `/etc/named.rfc1912.zones` definiert sind, enthalten die spezifischen Zoneneinstellungen, die für die Namensauflösung innerhalb des Netzwerks erforderlich sind.

Es handelt sich hier nicht um eine Schrittfolge, sondern um eine Beschreibung der relevanten Dateien und ihrer Funktionen im Kontext der DNS-Konfiguration für Polycom-Videokonferenzsysteme. Diese Informationen sind wichtig für die Einrichtung und Verwaltung von DNS innerhalb eines Netzwerks, das Polycom-Videokonferenzsysteme verwendet.

Ausschnitt

```
zone "vk.segment.domain.de" IN {
type master;
file "/etc/named/vk.segment.forward.zone";
allow-update { none; };
allow-query { any; };
};
```

Die Liste bezieht sich auf die Konfiguration von DNS-Einstellungen für Polycom-Videokonferenzsysteme. Sie enthält Informationen über die Forward-Zone für die Domäne "vk.segment.domain.de".

Die Liste kann wie folgt zusammengefasst werden:

Für die Konfiguration der DNS-Einstellungen ist folgender Punkt relevant:
- Die Forward-Zone für die Domäne "vk.segment.domain.de" befindet sich in der Datei "/etc/named/vk.segment.forward.zone".

Da es sich hier nicht um eine Schrittfolge handelt, sondern um eine einzelne Konfigurationsinformation, gibt es keine nummerierte Schrittfolge. Die Liste informiert lediglich über den Speicherort der Forward-Zone für die angegebene Domäne.

```
$TTL 86400
@ IN SOA ns1.vk.segment.domain.de. admin.vk.segment.domain.de. (
2020011800 ;Serial
3600 ;Refresh
1800 ;Retry
604800 ;Expire
86400 ;Minimum TTL
)
;Name Server Information
@ IN NS ns1.vk.segment.domain.de.
;IP Address for Name Server
ns1 IN A 188.340.8.2
;A Record for the following Host name
server70  IN   A   188.340.8.2
server71  IN   A   188.340.8.21
server72  IN   A   188.340.8.22
server73  IN   A   188.340.8.23
server74  IN   A   188.340.8.24
server75  IN   A   188.340.8.25
server76  IN   A   188.340.8.26
server77  IN   A   188.340.8.27
vc      IN   A   188.340.8.22
deploy  IN   A   188.340.8.2
app     IN   A   188.340.8.22
```

Die Liste bezieht sich auf die Konfiguration von Polycom-Videokonferenzsystemen im Zusammenhang mit DNS-Einstellungen. Insbesondere wird hier die Reverse-Zone für die Domäne "vk.segment.domain.de" erwähnt.

Die Liste kann wie folgt zusammengefasst werden:

Für die Konfiguration der Reverse-Zone in einem Polycom-Videokonferenzsystem ist es wichtig, die Datei `/etc/named/vk.segment.reverse.zone` zu beachten. Diese Datei ist Teil der DNS-Konfiguration und enthält die notwendigen Einträge für die Reverse-Zone der Domäne "vk.segment.domain.de".

Es gibt keine spezifischen Schritte, die in dieser Liste aufgeführt sind, sondern lediglich einen Hinweis auf die relevante Datei für die Konfiguration der Reverse-Zone. Wenn Sie jedoch die Konfiguration durchführen möchten, könnten die allgemeinen Schritte wie folgt aussehen:

1. Öffnen Sie die Datei `/etc/named/vk.segment.reverse.zone` in einem Texteditor.
2. Überprüfen Sie die Einträge in der Datei und passen Sie sie gegebenenfalls an, um sicherzustellen, dass die Reverse-Zone korrekt konfiguriert ist.
3. Speichern Sie die Änderungen und schließen Sie den Texteditor.
4. Überprüfen Sie die Funktionalität der Reverse-Zone, um sicherzustellen, dass sie korrekt funktioniert.

Bitte beachten Sie, dass diese Schritte nur eine allgemeine Anleitung darstellen und je nach spezifischer Konfiguration und Umgebung variieren können. Es ist immer ratsam, die offizielle Dokumentation und Anleitungen für Ihr spezifisches System zu konsultieren.

```
$TTL 86400
@ IN SOA ns1.vk.segment.domain.de. admin.vk.segment.domain.de. (
2020011800 ;Serial
3600 ;Refresh
1800 ;Retry
604800 ;Expire
86400 ;Minimum TTL
)
;Name Server Information
@ IN NS ns1.vk.segment.domain.de.de.
;Reverse lookup for Name Server
10 IN PTR ns1.vk.segment.orga.domain.de.
;PTR Record IP address to Hostname
50      IN      PTR     server70.vk.segment.domain.de.
```

## Software-Deployer

Der Abschnitt "Software-Deployer" im Dokument über Polycom-Videokonferenzsysteme enthält wichtige Informationen über den Zugriff und die Konfiguration des Deployers. Zusammengefasst handelt es sich um die folgenden Punkte:

Um den Software-Deployer zu nutzen, müssen Sie die folgenden Informationen beachten:
1. Die Deploy-Adresse lautet http://deploy.vk.sagmente.domain.de/. Diese Adresse ist der Zugriffspunkt für den Deployer.
2. Der Pfad auf dem Server, an dem die Deployer-Software installiert ist, ist /var/www/html. Dieser Pfad ist wichtig für die Konfiguration und Wartung des Systems.

Diese Informationen sind entscheidend für die erfolgreiche Installation, Konfiguration und Nutzung des Software-Deployers im Rahmen der Polycom-Videokonferenzsysteme. Durch die Kenntnis dieser Details können Administratoren und Benutzer den Deployer effektiv nutzen und die Videokonferenzsysteme entsprechend einrichten und warten.

Als root im root/ Verzeichnis das Skript "./Poly-Updater.sh" ausführen.

## S-1872: CMS-Bund-Plattform (BDBOS) Bearbeiten

In
den DIAL-Plan am Clariti-Core werden alle Rufnummern der
CMS-Bund-Plattform auf die Rufnummer +49 999999999 geändert. Grund sind
Tests für unser Nutzerhaus.

https://188.340.8.22:6228/cce/service-config/dial-plan/dial-plans

DIAL-Rule: Resolve to external SIP Peer NdB println("Original DIAL_STRING: " + DIAL_STRING); println("Modified by us DIAL_STRING: " + DIAL_STRING); return DIAL_STRING;

## Poly Clientsysteme Bearbeiten

### Tabelle: Polycom-Videokonferenzsysteme
Die Tabelle hat keinen expliziten Titel, daher wird sie als "Polycom-Videokonferenzsysteme" bezeichnet, basierend auf dem Dokumenttitel.

### Inhalt der Tabelle
Diese Tabelle stellt eine Übersicht über verschiedene Polycom-Videokonferenzsysteme an verschiedenen Standorten dar. Sie enthält Informationen über die Systeme, wie IP-Adressen, MAC-Adressen, Modelle und VMR-IDs.

### Bedeutung der Spalten
* Standort/Raum: Der Standort oder Raum, in dem das System installiert ist.
* Name: Der Name des Systems.
* VKA-IP: Die IP-Adresse des Videokonferenzsystems.
* VKA-MAC: Die MAC-Adresse des Videokonferenzsystems.
* SIP: Die SIP-Nummer des Systems.
* Modell: Das Modell des Videokonferenzsystems.
* TC-IP: Die IP-Adresse des TC-Systems (wahrscheinlich ein Teil des Videokonferenzsystems).
* TC-MAC: Die MAC-Adresse des TC-Systems.
* TC-SN: Die Seriennummer des TC-Systems.
* VMR-ID: Die VMR-ID des Systems.

### Beschreibung der Tabellenzeilen
Es gibt eine leere Zeile am Anfang, die keinen Inhalt hat. 
Der Standort "Garten" hat keine weiteren Informationen. 
Der Standort "Standort1 A103" hat ein System namens "Standort1-A103" mit der IP-Adresse "188.455.8.50" und dem Modell "StudioX50, TC8". 
Der Standort "Standort1 A107" hat ein System namens "Standort1-A107" mit der IP-Adresse "188.455.8.52" und dem Modell "StudioX50, TC8". 
Der Standort "Standort1 B001" hat ein System namens "Standort1-B001" mit der IP-Adresse "188.455.8.54" und dem Modell "HDX8000HD". 
Der Standort "Standort1 B003" hat ein System namens "Standort1-B003" mit der IP-Adresse "188.455.8.56" und dem Modell "StudioX52, TC10". 
Der Standort "Standort1 B003 Mobil" hat ein System namens "Standort1-B003-Mobil" mit der IP-Adresse "188.455.8.58" und dem Modell "StudioX50, TC8". 
Der Standort "Standort1 B008 Mobil 2" hat ein System namens "Standort1-B008-Mobil" mit der IP-Adresse "188.455.8.60" und dem Modell "StudioX52, TC10". 
Der Standort "Standort1 B206" hat ein System namens "Standort1-B206" mit der IP-Adresse "188.455.8.62" und dem Modell "StudioX52, TC10". 
Der Standort "Standort1 C125" hat ein System namens "Standort1-C125" mit der IP-Adresse "188.455.8.64" und dem Modell "StudioX52, TC10". 
Der Standort "Standort1 C202 Mobil 1" hat ein System namens "Standort1-C202-Mobil" mit der IP-Adresse "188.455.8.66" und dem Modell "StudioX52, TC10". 
Der Standort "Hof" hat keine weiteren Informationen. 
Der Standort "Standort3 0.19" hat ein System namens "Standort3-0.19" mit der IP-Adresse "188.888.8.13" und dem Modell "StudioX50, TC8". 
Der Standort "Hausstraße" hat keine weiteren Informationen. 
Der Standort "Standort2 A.1.1" hat ein System namens "Standort2-A.1.1" mit der IP-Adresse "188.340.8.92" und dem Modell "G7500, TC8". 
Der Standort "Standort2 B.0.2.2" hat ein System namens "Standort2-B.0.2.2" mit der IP-Adresse "188.340.8.83" und dem Modell "StudioX50, TC8". 
Der Standort "Standort2 B.0.2.3" hat ein System namens "Standort2-B.0.2.3" mit der IP-Adresse "188.340.8.84" und dem Modell "StudioX50, TC8". 
Der Standort "Standort2 B.1.1" hat ein System namens "Standort2-B.1.1" mit der IP-Adresse "188.340.8.70" und dem Modell "G7500, TC8". 
Der Standort "Standort2 B.2.22" hat ein System namens "Standort2-B.2.22" mit der IP-Adresse "188.340.8.94" und dem Modell "StudioX50, TC8". 
Der Standort "Standort2 B.4.10" hat ein System namens "Standort2-B.4.10" mit der IP-Adresse "188.340.8.96" und dem Modell "StudioX50, TC8". 
Der Standort "Standort2 B.5.1" hat ein System namens "Standort2-B.5.1" mit der IP-Adresse "188.340.8.79" und dem Modell "StudioX50, TC8". 
Der Standort "Standort2 B.5.20" hat ein System namens "Standort2-B.5.20" mit der IP-Adresse "188.340.8.80" und dem Modell "StudioX50, TC8". 
Der Standort "Standort2 B.6.17" hat ein System namens "Standort2-B.6.17" mit der IP-Adresse "188.340.8.63" und dem Modell "G7500, TC8". 
Der Standort "Standort2 D.1.2" hat ein System namens "Standort2-D.1.2" mit der IP-Adresse "188.340.8.71" und dem Modell "StudioX50, TC8". 
Der Standort "Standort2 D.1.10" hat ein System namens "Standort2-D.1.10" mit der IP-Adresse "188.340.8.86" und dem Modell "StudioX50, TC8". 
Der Standort "Standort2 D.2.2" hat ein System namens "Standort2-D.2.2" mit der IP-Adresse "188.340.8.57" und dem Modell "StudioX50, TC8". 
Der Standort "Standort2 D.2.11" hat ein System namens "Standort2-D.2.11" mit der IP-Adresse "188.340.8.90" und dem Modell "StudioX50, TC8". 
Der Standort "Standort2 D.3.3" hat ein System namens "Standort2-D.3.3" mit der IP-Adresse "188.340.8.64" und dem Modell "StudioX50, TC8". 
Der Standort "Standort2 D.4.3" hat ein System namens "Standort2-D.4.3" mit der IP-Adresse "188.340.8.62" und dem Modell "StudioX50, TC8". 
Der Standort "Standort2 D.5.2" hat ein System namens "Standort2-D.5.2" mit der IP-Adresse "188.340.8.55" und dem Modell "StudioX50, TC8". 
Der Standort "Standort2 E.6.15" hat ein System namens "Standort2-E.6.15" mit der IP-Adresse "188.340.8.81" und dem Modell "StudioX50, TC8".

## Poly Standardkonfig (x50/x52/G7500) Bearbeiten

### Tabelle: Polycom-Videokonferenzsysteme - Standardkonfiguration
Die Tabelle stellt die Standardkonfiguration für Polycom-Videokonferenzsysteme dar, insbesondere für die Modelle x50, x52 und G7500. Sie enthält verschiedene Einstellungen und Konfigurationen für die Systeme.

### Spaltenbeschreibung
* Menüpunkt: Die Kategorie oder der Menüpunkt, zu dem die Einstellung gehört.
* Thema: Das spezifische Thema oder die Einstellung, die konfiguriert wird.
* Wert: Der Wert oder die Einstellung, die für das Thema verwendet wird.
* Bemerkung: Optional, zusätzliche Informationen oder Bemerkungen zur Einstellung.

### Tabelleninhalte
Die Allgemeine Einstellung "Anbieter" ist auf "Poly" gesetzt. 
Die Allgemeine Einstellung "Startseite" hat den Hintergrund "Standort2/BU/DDW" mit Bildern, die unter "Share Z33/VK" abgelegt sind. 
Bei den Allgemeinen Einstellungen auf der Startseite sind die Elemente "Favoriten, Kontrollkästen nicht ankreuzen" aktiviert. 
Die Adressleiste ist auf "Primär: H.323, Sekundär: SIP-Adresse" eingestellt, wobei aktuell H.323 ein ist. 
Bei den Informationen zu Poly Control sind die Kontrollkästen nicht ankreuzen (aus). 
Die Allgemeine Einstellung "Systemsprache" ist auf "Deutsch" gesetzt. 
Die Allgemeine Einstellung "Datum und Uhrzeit" verwendet die Adresse des primären Zeit-Servers "188.340.8.1". 
Bei den Allgemeinen Einstellungen zur Geräteverwaltung sind die Aktualisierungen auf einen benutzerdefinierten Server-URL "http://deploy.vk.segment.domain.de" gesetzt, wobei die Kontrollkästen nicht ankreuzen (aus) sind. 
Die Allgemeine Einstellung "Systemeinstellungen" verwendet den Geräte- und Raumnamen "[Standort]-[RAUM]" wie z.B. "Standort2-D.1.10". 
Der Schlafmodus ist auf "Kein Signal, 15 Minuten, Kontrollkästen ankreuzen" eingestellt. 
Die Digitale Beschilderung ist auf "Kontrollkästen nicht ankreuzen (aus)" gesetzt. 
Der Zeitraum außerhalb Bürozeiten ist auf "Kontrollkästen nicht ankreuzen (aus)" gesetzt. 
Die System-LED ist auf "100%" eingestellt. 
Die Zusammenarbeitswerkzeuge sind auf "Kontrollkästen ankreuzen, Timeout 2 Minuten" gesetzt. 
Poly Connect ist auf "Kontrollkästen nicht ankreuzen (aus)" gesetzt, aktuell jedoch aktiv. 
Die Fernbedienung und Zahlentastatur sind auf "Kontrollkästen ankreuzen, Voreinstellung #, dann @ und . dann *" gesetzt. 
Die Umgebung ist auf "Kontrollkästen nicht ankreuzen (aus)" gesetzt. 
Der Geplante automatische Neustart ist auf "Kontrollkästen ankreuzen, Wöchentlich, Samstag, 12:00 AM" gesetzt. 
Die Allgemeine Einstellung "Fernbedienung" ist auf "Keine" gesetzt. 
Das LAN-Netzwerk verwendet IP-Adressen, die auf "2: DHCP (188.340.8.0/24) : Statisch (188.455.19.8.0/24)" gesetzt sind, wobei kein IPv6 verwendet wird. 
Die LAN-Optionen sind auf "Hostname [Standort]-[RAUM] Domänenname: vk.segment.domain.de" gesetzt, wobei alle Checkboxen aktiv sind, außer auf Broad/Multicast-Echoanforderungen, EAP, 802.1p/Q. 
Die Netzwerkqualität ist auf "6144 Bandbreite" gesetzt. 
Das WLAN ist auf "kein WLAN" gesetzt. 
Der DNS-Server ist auf "188.340.8.2" gesetzt. 
Die Anrufeinstellungen sind auf "8 Stunden, Alle Checkboxen aktiv, Anzeige des Systemnamens statt SIP-Adresse, Zahlentastatur, AES-Verschlüsselung: wenn verfügbar" gesetzt. 
Die Anwahloptionen sind auf "Alle Checkboxen aktiv, Videoanrufreihenfolge: 1. SIP, 2. H323" gesetzt. 
Die bevorzugten Anrufgeschwindigkeiten sind auf "abgehende: 3840, eingehende: 6144" gesetzt. 
Die Letzten Anrufe sind auf "Alle Checkboxen aktiv, maximal 100" gesetzt. 
Die H.323-Einstellungen sind auf "Name: <ID>@vc.domain.de, Nebenstelle: <ID>, Gatekeeper (manuell), IP: 188.340.8.22" gesetzt. 
Die SIP-Einstellungen sind auf "SIP-Server: Manuell, Transportprotokoll: TCP, BFCP: UDP, Anmeldeadresse: <ID>@vc.domain.de, Benutzername: <ID>@vc.domain.de, Registrar-Server: 188.340.8.22, Proxy-Server: 188.340.8.22, Registrar-Typ: Standard-PIP" gesetzt, wobei die Kontrollkästen nicht ankreuzen (aus) sind und das Transportprotokoll auf TLS umgestellt werden soll, sobald der CMS-Bund klappt. 
Die Monitoreinstellungen sind auf "Automatisch, Vollbild, Ein Monitor" gesetzt. 
Die Audioeinstellungen sind auf "Pro Raum anpassen" gesetzt, wobei bei G7500 ggf. andere Optionen verwendet werden. 
Die Video-Eingänge sind auf "Pro Raum anpassen" gesetzt. 
Die Zugriffseinstellungen sind auf "Netzwerk-IDS-System aktivieren: (deaktiviert), Web-Zugriff aktivieren: (aktiviert), Telnet-Zugriff aktivieren: (deaktiviert), Lgacy-API über SSH aktivieren: (deaktiviert), SNMP-Zugriff aktivieren: (aktiviert)" gesetzt, wobei die Portsperrung nach fehlerhaften Anmeldeversuchen auf 10 gesetzt ist und die Dauer der Portsperre auf 1 Minute gesetzt ist. 
Die Zertifikatseinstellungen sind auf "Standard-Einstellungen" gesetzt, wobei aktuell keine eigenen Zertifikate verwendet werden und somit selbstsigniert ist. 
Die Lokalen Konten sind auf "Standard-Einstellungen" gesetzt, wobei das Kennwort nach der Einrichtung geändert werden sollte. 
Die Globale Sicherheit ist auf "erweitert" gesetzt. 
Die Kennwortanforderungen sind auf "Standard-Einstellungen" gesetzt. 
Der Sicherheitscode ist aktiviert. 
Das Sicherheitsbanner ist deaktiviert. 
Die Content-Einstellungen sind auf "Benutzer dürfen Content aus primärem Netzwerk speichern: (Aktiviert), Benutzer dürfen Content aus dem WLAN speichern: (Deaktiviert)" gesetzt. 
Die WLAN- und Bildschirmspiegelungseinstellungen sind auf "WLAN-Funktionen aktivieren: (Deaktiviert), Bluetooth aktivieren: (Aktiviert), Bildschirmspiegelung: (deaktiviert), Miracast: (deaktiviert)" gesetzt, wobei geprüft werden sollte, ob Bluetooth abgeschaltet werden kann. 
Der Kalenderdienst ist deaktiviert. 
Der Verzeichnisserver ist auf "Servertyp: Polycom GDS, Serveradresse: 188.340.8.21" gesetzt. 
Der Bereitstellungsserver ist deaktiviert. 
Der SNMP-Server ist aktiviert, wobei die Version 3 verwendet wird und die Community mit Leseberechtigung deaktiviert ist. 
Die Cloud-Einstellungen sind deaktiviert.

## Poly Clariti App Bearbeiten

aktuell nicht in der produktiven Verwendung ( https://188.340.8.22:6228/client/)
