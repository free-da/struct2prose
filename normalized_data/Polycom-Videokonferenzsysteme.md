# Polycom-Videokonferenzsysteme-TEST - XWiki

## Einleitung

Die Liste beschreibt die verschiedenen Komponenten und Aspekte des Polycom-Videokonferenzsystems. Zusammengefasst umfasst sie die folgenden Punkte:

Das Polycom-Videokonferenzsystem besteht aus mehreren wichtigen Komponenten. Zunächst gibt es einen Ansprechpartner, der für Fragen und Probleme zur Verfügung steht. Die Poly VK-Infrastruktur umfasst IP-Netze und Server, wie den S-1870, der für Netzwerkbasisdienste wie DHCP und DNS sowie den Software-Deployer verantwortlich ist. Dieser Server ermöglicht es, Poly-Endgeräte zu aktualisieren. Ein weiterer wichtiger Server ist der S-1872, der als CMS-Bund-Plattform (BDBOS) dient.

Weitere wichtige Aspekte des Systems sind die Poly-Clientsysteme, die Standardkonfigurationen wie x50, x52 und G7500 sowie die Poly Clariti App. Darüber hinaus gibt es verschiedene Szenarien, in denen das System eingesetzt werden kann.

Es gibt keine spezifischen Schritte, die in einer bestimmten Reihenfolge ausgeführt werden müssen. Stattdessen bietet die Liste einen Überblick über die verschiedenen Komponenten und Aspekte des Polycom-Videokonferenzsystems.

## Ansprechpartner Bearbeiten

## Poly VK-Infrastruktur Bearbeiten

## IP-Netze Bearbeiten

### Übersicht über die Tabelle
Die Tabelle hat keinen expliziten Titel, daher kann sie als "IP-Adressbereiche und Beschreibungen" bezeichnet werden. Diese Tabelle stellt insgesamt eine Sammlung von IP-Adressbereichen und ihren entsprechenden Beschreibungen dar, die im Kontext von Polycom-Videokonferenzsystemen und deren Netzwerkkonfigurationen verwendet werden.

### Spaltenbeschreibung
Die Tabelle besteht aus zwei Spalten:
- Die erste Spalte enthält die IP-Adressbereiche.
- Die zweite Spalte enthält die Beschreibungen dieser Adressbereiche.

### Tabelleninhalte
Die Tabelle enthält folgende Informationen:
- Der IP-Adressbereich 123:213:80a:5800::/64 ::444 (vc.domain.de) wird von DFN über BRAIN verwendet.
- Der IP-Adressbereich 123.23.231.39/32 (vc.domain.de) wird von DFN verwendet und soll später an BRAIN announciert werden.
- Die IP-Adressbereiche 172.[17|19|23].8.0/24 für DDW [19] und Standort1 [23] werden durch 188.999.147.160 /28 (DDW) und 188.999.147.128/27 (Standort1) abgelöst und dienen internen Videonetzen.
- Der IP-Adressbereich 188.999.147.0/25 dient der Standortkopplung für den Videodienst in der Hausstraße 49.
- Der IP-Adressbereich 188.999.147.128/27 dient sowohl der Standortkopplung als auch als Adressbereich für Endgeräte des Videodienstes in der Bundesallee 51.
- Der IP-Adressbereich 188.999.147.160/28 dient sowohl der Standortkopplung als auch als Adressbereich für Endgeräte des Videodienstes im Diedersdorfer Weg 1.
- Der IP-Adressbereich 192.168.75.0/29 wird für den Transfer zwischen NdB-SBC und ORGA-SBC verwendet, wobei .2 für NdB-SBC, .3 für ORGA-SBC und .4 für eine redundante, aber nicht vorhandene ORGA-SBC reserviert ist.

## Server Bearbeiten

### Übersicht über die Tabelle
Der Titel der Tabelle ist nicht explizit angegeben, daher kann sie als "Übersicht über Server und ihre Konfigurationen" bezeichnet werden. Diese Tabelle stellt eine Zusammenfassung von Servern und ihren jeweiligen Konfigurationen, Verwendungen und Standorten dar.

### Beschreibung der Spalten
Die Tabelle enthält folgende Spalten:
- Name: Der Name des Servers
- Verwendung: Die Verwendung oder Funktion des Servers
- IP: Die IP-Adresse des Servers
- SN: Die Seriennummer des Servers (in diesem Fall leer)
- OS: Das Betriebssystem des Servers
- Standort: Der physische Standort des Servers

### Beschreibung der Tabellenzeilen
- Der Server "server70" wird für Netzwerkbasisdienste, Software-Deploy, DNS und DHCP verwendet und hat die IP-Adresse 188.340.8.2, läuft unter RHEL 9 und befindet sich im VK-Cluster Standort2.
- Der Server "server71" wird als Clariti Manager verwendet, hat die IP-Adresse 188.340.8.21, läuft unter OL 8 und befindet sich im VK-Cluster Standort2.
- Der Server "server72" wird als Clariti Core verwendet, hat die IP-Adresse 188.340.8.22, läuft unter OL 8 und befindet sich im VK-Cluster Standort2.
- Der Server "server73" wird als RealPresence Collaboration Server verwendet, hat die IP-Adresse 188.340.8.23, läuft unter OL 8 und befindet sich im VK-Cluster Standort2.
- Der Server "server74" wird als Clariti Media-Relay verwendet, hat die IP-Adresse 188.340.8.24, läuft unter OL 8 und befindet sich im VK-Cluster Standort2.
- Der Server "server75" wird als Clariti Edge NdB-ID verwendet, hat die IP-Adresse 188.340.8.25, läuft unter OL 8 und befindet sich im VK-Cluster Standort2.
- Der Server "server76" wird als Clariti Edge Internet verwendet, hat die IP-Adresse 188.340.8.26, läuft unter OL 8 und befindet sich im VK-Cluster Standort2.
- Der Server "server77" wird als Clariti Edge Client verwendet, hat die IP-Adresse 188.340.8.27, läuft unter OL 8 und befindet sich im VK-Cluster Standort2.
- Der Server "sbc001" wird als Secunet SBC Internet verwendet, hat keine angegebene IP-Adresse, und befindet sich im RZ Standort2, das aktuell ausgebaut wird.
- Der Server "sbc002" wird ebenfalls als Secunet SBC Internet verwendet, hat keine angegebene IP-Adresse, und befindet sich im RZ Standort2, das aktuell ausgebaut wird.
- Der Server "sbcmgt" wird als Secunet SBC Manager verwendet, hat keine angegebene IP-Adresse, und befindet sich im RZ Standort2, das aktuell ausgebaut wird.

## S-1870: Netzwerkbasisdienste Bearbeiten

## DHCP

Genutzt wird der KEA-DHCP-Server (Nachfolger des ISC-DHCP-Servers).

Die Konfigdateien liegen unter /etc/kea/.

Die Liste bezieht sich auf die Konfiguration von Polycom-Videokonferenzsystemen im Zusammenhang mit DHCP (Dynamic Host Configuration Protocol). Sie umfasst zwei wichtige Konfigurationsdateien:

Die Konfiguration für das Polycom-Videokonferenzsystem unter Verwendung von DHCP umfasst zwei Hauptkomponenten: 
1. Die Kea-Main-Konfiguration, die in der Datei `keactrl.conf` gespeichert ist. 
2. Die Kea-DHCP4-Konfiguration, die in der Datei `kea-dhcp4.conf` zu finden ist.

Diese Dateien sind entscheidend für die Einrichtung und Verwaltung der DHCP-Funktionen im Polycom-Videokonferenzsystem, da sie die notwendigen Parameter und Einstellungen enthalten, um die dynamische Zuweisung von IP-Adressen und anderen Netzwerkeinstellungen zu ermöglichen.

DHCP6 ist derzeit deaktiviert. Kann in der Kea-Main-Konfig aktiviert und in der kea-dhcp6.conf konfiguriert werden.

Der DHCP ist aktuell nur für die Berliner Endgeräte. Es gibt aktuell kein DHCP-Relay zur BU oder zum DDW.

## DNS

Der
BIND (named) DNS-Server wird für die interne DNS-Zone
vk.segment.domain.de genutzt und sorgt für die DNS-Auflösungen innerhalb
des VK-Clusters.

Die Liste bezieht sich auf die Konfiguration von DNS (Domain Name System) im Rahmen von Polycom-Videokonferenzsystemen. Hier sind die wichtigsten Punkte zusammengefasst:

Die Konfiguration von DNS für Polycom-Videokonferenzsysteme umfasst zwei wichtige Dateien:
- Die Named-Konfiguration, die in der Datei `/etc/named.conf` zu finden ist.
- Die Named-Zonen, die in der Datei `/etc/named.rfc1912.zones` definiert sind.

Um diese Konfiguration zu verstehen, können Sie folgende Schritte befolgen:
1. Öffnen Sie die Datei `/etc/named.conf`, um die Named-Konfiguration zu überprüfen und gegebenenfalls anzupassen.
2. Öffnen Sie die Datei `/etc/named.rfc1912.zones`, um die Named-Zonen zu überprüfen und gegebenenfalls anzupassen.

Diese Dateien sind entscheidend für die korrekte Funktion des DNS-Systems in Ihrem Polycom-Videokonferenzsystem. Durch die Überprüfung und Anpassung dieser Dateien können Sie sicherstellen, dass Ihre Videokonferenzsysteme ordnungsgemäß funktionieren.

Ausschnitt

```
zone "vk.segment.domain.de" IN {
type master;
file "/etc/named/vk.segment.forward.zone";
allow-update { none; };
allow-query { any; };
};
```

Die Liste bezieht sich auf die Konfiguration von Polycom-Videokonferenzsystemen im Zusammenhang mit DNS-Einstellungen. Zusammengefasst enthält die Liste Informationen über die Forward-Zone für die Domain "vk.segment.domain.de".

Die Liste kann wie folgt umformuliert werden:

Die Konfiguration der DNS-Einstellungen für Polycom-Videokonferenzsysteme umfasst die Definition einer Forward-Zone. Diese Zone ist in der Datei "/etc/named/vk.segment.forward.zone" definiert und bezieht sich auf die Domain "vk.segment.domain.de".

Es gibt keine expliziten Schritte in der Liste, sondern lediglich eine Beschreibung der Konfiguration. Wenn jedoch Schritte erforderlich wären, um diese Konfiguration vorzunehmen, könnten diese wie folgt aussehen:

1. Öffnen Sie die Datei "/etc/named/vk.segment.forward.zone" in einem Texteditor.
2. Fügen Sie die erforderlichen Einträge für die Forward-Zone hinzu, um die Domain "vk.segment.domain.de" zu konfigurieren.
3. Speichern und schließen Sie die Datei, um die Änderungen zu übernehmen.

Es ist jedoch wichtig zu beachten, dass die ursprüngliche Liste keine expliziten Schritte enthält und lediglich eine Beschreibung der Konfiguration liefert.

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

Die Liste bezieht sich auf die Konfiguration von Polycom-Videokonferenzsystemen im Zusammenhang mit DNS-Einstellungen. Zusammengefasst enthält die Liste Informationen über die Reverse-Zone für die Domain "vk.segment.domain.de".

Die Liste kann wie folgt als Fließtext formuliert werden:

Für die Konfiguration der Polycom-Videokonferenzsysteme ist es wichtig, die DNS-Einstellungen korrekt zu konfigurieren. Insbesondere für die Reverse-Zone der Domain "vk.segment.domain.de" ist die Datei "/etc/named/vk.segment.reverse.zone" relevant. Diese Datei enthält die notwendigen Einträge für die Reverse-Zone und sollte daher korrekt konfiguriert und gepflegt werden.

Es gibt keine spezifischen Schritte, die in dieser Liste aufgeführt sind, sondern lediglich eine Information über die Datei, die für die Konfiguration der Reverse-Zone verwendet wird. Wenn jedoch Schritte für die Konfiguration erforderlich wären, könnten diese beispielsweise wie folgt aussehen:

1. Öffnen Sie die Datei "/etc/named/vk.segment.reverse.zone" in einem Texteditor.
2. Überprüfen Sie die Einträge in der Datei und stellen Sie sicher, dass sie korrekt sind.
3. Speichern Sie die Änderungen und schließen Sie die Datei.

Es ist jedoch wichtig zu beachten, dass diese Schritte nicht explizit in der ursprünglichen Liste aufgeführt sind und daher nur als Beispiel dienen.

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

Die Liste bezieht sich auf die Konfiguration des Software-Deployers für Polycom-Videokonferenzsysteme. Zusammengefasst enthält sie Informationen über die Deploy-Adresse und den Pfad auf dem Server.

Um den Software-Deployer korrekt zu konfigurieren, sollten Sie folgende Punkte beachten:

1. **Deploy-Adresse**: Die Deploy-Adresse ist `http://deploy.vk.sagmente.domain.de/`. Dies ist die URL, über die der Deployer erreicht wird.
2. **Pfad auf dem Server**: Der Pfad auf dem Server, an dem die Deploy-Dateien gespeichert sind, ist `/var/www/html`. Dieser Pfad ist wichtig, um die korrekte Speicherung und Abrufbarkeit der Deploy-Dateien zu gewährleisten.

Indem Sie diese beiden Punkte berücksichtigen, können Sie den Software-Deployer für Ihre Polycom-Videokonferenzsysteme erfolgreich konfigurieren.

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
Die Tabelle trägt keinen expliziten Titel, daher wird sie hier als "Polycom-Videokonferenzsysteme" bezeichnet.

### Inhalt der Tabelle
Diese Tabelle stellt eine Übersicht über verschiedene Polycom-Videokonferenzsysteme an verschiedenen Standorten dar. Sie enthält Informationen über die Systeme, wie IP-Adressen, MAC-Adressen, Modelle und VMR-IDs.

### Bedeutung der Spalten
- **Standort/Raum**: Der Standort oder Raum, in dem das Videokonferenzsystem installiert ist.
- **Name**: Der Name des Videokonferenzsystems.
- **VKA-IP**: Die IP-Adresse des Videokonferenzsystems.
- **VKA-MAC**: Die MAC-Adresse des Videokonferenzsystems.
- **SIP**: Die SIP-Nummer des Videokonferenzsystems.
- **Modell**: Das Modell des Videokonferenzsystems.
- **TC-IP**: Die IP-Adresse des TC-Systems (Teil des Videokonferenzsystems).
- **TC-MAC**: Die MAC-Adresse des TC-Systems.
- **TC-SN**: Die Seriennummer des TC-Systems.
- **VMR-ID**: Die VMR-ID des Videokonferenzsystems.

### Beschreibung der Tabellenzeilen
- Es gibt einen leeren Eintrag ohne Standort oder Raum.
- Der Standort "Standort1 A103" hat ein Videokonferenzsystem namens "Standort1-A103" mit der IP-Adresse "188.455.8.50" und dem Modell "StudioX50, TC8".
- Der Standort "Standort1 A107" hat ein Videokonferenzsystem namens "Standort1-A107" mit der IP-Adresse "188.455.8.52" und dem Modell "StudioX50, TC8".
- Der Standort "Standort1 B001" hat ein Videokonferenzsystem namens "Standort1-B001" mit der IP-Adresse "188.455.8.54" und dem Modell "HDX8000HD".
- Der Standort "Standort1 B003" hat ein Videokonferenzsystem namens "Standort1-B003" mit der IP-Adresse "188.455.8.56" und dem Modell "StudioX52, TC10".
- Der Standort "Standort1 B003 Mobil" hat ein Videokonferenzsystem namens "Standort1-B003-Mobil" mit der IP-Adresse "188.455.8.58" und dem Modell "StudioX50, TC8".
- Der Standort "Standort1 B008 Mobil 2" hat ein Videokonferenzsystem namens "Standort1-B008-Mobil" mit der IP-Adresse "188.455.8.60" und dem Modell "StudioX52, TC10".
- Der Standort "Standort1 B206" hat ein Videokonferenzsystem namens "Standort1-B206" mit der IP-Adresse "188.455.8.62" und dem Modell "StudioX52, TC10".
- Der Standort "Standort1 C125" hat ein Videokonferenzsystem namens "Standort1-C125" mit der IP-Adresse "188.455.8.64" und dem Modell "StudioX52, TC10".
- Der Standort "Standort1 C202 Mobil 1" hat ein Videokonferenzsystem namens "Standort1-C202-Mobil" mit der IP-Adresse "188.455.8.66" und dem Modell "StudioX52, TC10".
- Es gibt einen leeren Eintrag ohne Standort oder Raum, der sich auf den letzten nicht-leeren Standort "Standort1" bezieht.
- Der Standort "Standort3 0.19" hat ein Videokonferenzsystem namens "Standort3-0.19" mit der IP-Adresse "188.888.8.13" und dem Modell "StudioX50, TC8".
- Es gibt einen leeren Eintrag ohne Standort oder Raum, der sich auf den letzten nicht-leeren Standort "Standort3" bezieht.
- Der Standort "Standort2 A.1.1" hat ein Videokonferenzsystem namens "Standort2-A.1.1" mit der IP-Adresse "188.340.8.92" und dem Modell "G7500, TC8".
- Der Standort "Standort2 B.0.2.2" hat ein Videokonferenzsystem namens "Standort2-B.0.2.2" mit der IP-Adresse "188.340.8.83" und dem Modell "StudioX50, TC8".
- Der Standort "Standort2 B.0.2.3" hat ein Videokonferenzsystem namens "Standort2-B.0.2.3" mit der IP-Adresse "188.340.8.84" und dem Modell "StudioX50, TC8".
- Der Standort "Standort2 B.1.1" hat ein Videokonferenzsystem namens "Standort2-B.1.1" mit der IP-Adresse "188.340.8.70" und dem Modell "G7500, TC8".
- Der Standort "Standort2 B.2.22" hat ein Videokonferenzsystem namens "Standort2-B.2.22" mit der IP-Adresse "188.340.8.94" und dem Modell "StudioX50, TC8".
- Der Standort "Standort2 B.4.10" hat ein Videokonferenzsystem namens "Standort2-B.4.10" mit der IP-Adresse "188.340.8.96" und dem Modell "StudioX50, TC8".
- Der Standort "Standort2 B.5.1" hat ein Videokonferenzsystem namens "Standort2-B.5.1" mit der IP-Adresse "188.340.8.79" und dem Modell "StudioX50, TC8".
- Der Standort "Standort2 B.5.20" hat ein Videokonferenzsystem namens "Standort2-B.5.20" mit der IP-Adresse "188.340.8.80" und dem Modell "StudioX50, TC8".
- Der Standort "Standort2 B.6.17" hat ein Videokonferenzsystem namens "Standort2-B.6.17" mit der IP-Adresse "188.340.8.63" und dem Modell "G7500, TC8".
- Der Standort "Standort2 D.1.2" hat ein Videokonferenzsystem namens "Standort2-D.1.2" mit der IP-Adresse "188.340.8.71" und dem Modell "StudioX50, TC8".
- Der Standort "Standort2 D.1.10" hat ein Videokonferenzsystem namens "Standort2-D.1.10" mit der IP-Adresse "188.340.8.86" und dem Modell "StudioX50, TC8".
- Der Standort "Standort2 D.2.2" hat ein Videokonferenzsystem namens "Standort2-D.2.2" mit der IP-Adresse "188.340.8.57" und dem Modell "StudioX50, TC8".
- Der Standort "Standort2 D.2.11" hat ein Videokonferenzsystem namens "Standort2-D.2.11" mit der IP-Adresse "188.340.8.90" und dem Modell "StudioX50, TC8".
- Der Standort "Standort2 D.3.3" hat ein Videokonferenzsystem namens "Standort2-D.3.3" mit der IP-Adresse "188.340.8.64" und dem Modell "StudioX50, TC8".
- Der Standort "Standort2 D.4.3" hat ein Videokonferenzsystem namens "Standort2-D.4.3" mit der IP-Adresse "188.340.8.62" und dem Modell "StudioX50, TC8".
- Der Standort "Standort2 D.5.2" hat ein Videokonferenzsystem namens "Standort2-D.5.2" mit der IP-Adresse "188.340.8.55" und dem Modell "StudioX50, TC8".
- Der Standort "Standort2 E.6.15" hat ein Videokonferenzsystem namens "Standort2-E.6.15" mit der IP-Adresse "188.340.8.81" und dem Modell "StudioX50, TC8".

## Poly Standardkonfig (x50/x52/G7500) Bearbeiten

### Tabelle: Polycom-Videokonferenzsysteme-Standardkonfiguration
Die Tabelle stellt die Standardkonfiguration für Polycom-Videokonferenzsysteme dar, insbesondere für die Modelle x50, x52 und G7500. Sie enthält verschiedene Einstellungen und Konfigurationen für die Systeme.

### Spaltenbeschreibung
* Menüpunkt: Gibt den Menüpunkt an, unter dem die Einstellung zu finden ist.
* Thema: Beschreibt das Thema oder die Kategorie der Einstellung.
* Wert: Enthält den Wert oder die Einstellung selbst.
* Bemerkung: Optional, enthält zusätzliche Informationen oder Bemerkungen zur Einstellung.

### Tabelleninhalte
Die Allgemeine Einstellung "Anbieter" ist auf "Poly" gesetzt. 
Die Allgemeine Einstellung "Startseite" hat den Hintergrund "Standort2/BU/DDW" mit Bildern, die unter "Share Z33/VK" abgelegt sind. 
Bei den Allgemeinen Einstellungen ist auf der Startseite "Favoriten" und "Kontrollkästen nicht ankreuzen" ausgewählt. 
Die Adressleiste ist auf "Primär: H.323, Sekundär: SIP-Adresse" eingestellt, wobei aktuell H.323 ein ist. 
Die Informationen zu Poly Control sind auf "Kontrollkästen nicht ankreuzen (aus)" gesetzt. 
Die Allgemeine Einstellung "Systemsprache" ist auf "Deutsch" gesetzt. 
Die Allgemeine Einstellung "Datum und Uhrzeit" hat die Adresse des primären Zeit-Servers "188.340.8.1". 
Die Allgemeine Einstellung "Geräteverwaltung" hat die Aktualisierungen auf "Benutzerdefinierte Server-URL http://deploy.vk.segment.domain.de" mit Kontrollkästen nicht ankreuzen (aus) gesetzt. 
Die Allgemeine Einstellung "Systemeinstellungen" hat den Geräte- und Raumnamen auf "[Standort]-[RAUM]" gesetzt, beispielsweise "Standort2-D.1.10". 
Der Schlafmodus ist auf "Kein Signal, 15 Minuten, Kontrollkästen ankreuzen" gesetzt. 
Die Digitale Beschilderung ist auf "Kontrollkästen nicht ankreuzen (aus)" gesetzt. 
Der Zeitraum außerhalb Bürozeiten ist auf "Kontrollkästen nicht ankreuzen (aus)" gesetzt. 
Die System-LED ist auf "100%" gesetzt. 
Die Zusammenarbeitswerkzeuge sind auf "Kontrollkästen ankreuzen, Timeout 2 Minuten" gesetzt. 
Poly Connect ist auf "Kontrollkästen nicht ankreuzen (aus)" gesetzt, aber aktuell aktiv. 
Die Fernbedienung und Zahlentastatur sind auf "Kontrollkästen ankreuzen, Voreinstellung #, dann @ und . dann *" gesetzt. 
Die Umgebung ist auf "Kontrollkästen nicht ankreuzen (aus)" gesetzt. 
Der geplante automatische Neustart ist auf "Kontrollkästen ankreuzen, Wöchentlich, Samstag, 12:00 AM" gesetzt. 
Die Allgemeine Einstellung "Fernbedienung" ist auf "Keine" gesetzt. 
Das LAN-Netzwerk hat die IP-Adressen "2: DHCP (188.340.8.0/24) : Statisch (188.455.19.8.0/24)" und kein IPv6. 
Die LAN-Optionen haben den Hostnamen "[Standort]-[RAUM]" mit Domänenname "vk.segment.domain.de" und alle Checkboxen aktiv, außer auf Broad/Multicast-Echoanforderungen, EAP, 802.1p/Q. 
Die Netzwerkqualität ist auf "6144 Bandbreite" gesetzt. 
Das WLAN ist auf "kein WLAN" gesetzt. 
Der DNS-Server ist auf "188.340.8.2" gesetzt. 
Die Anrufeinstellungen sind auf "8 Stunden, Alle Checkboxen aktiv, Anzeigen des Systemnamens statt SIP-Adresse, Zahlentastatur, AES-Verschlüsselung: wenn verfügbar" gesetzt. 
Die Anwahloptionen sind auf "Alle Checkboxen aktiv, Videoanrufreihenfolge: 1. SIP, 2. H323" gesetzt. 
Die bevorzugten Anrufgeschwindigkeiten sind auf "abgehende: 3840, eingehende: 6144" gesetzt. 
Die letzten Anrufe sind auf "Alle Checkboxen aktiv, maximal 100" gesetzt. 
Die H.323-Einstellungen haben den Namen "<ID>@vc.domain.de" und die Nebenstelle "<ID>" mit Gatekeeper (manuell) und IP "188.340.8.22". 
Die SIP-Einstellungen haben den Server auf "Manuell", das Transportprotokoll auf "TCP", BFCP auf "UDP", die Anmeldeadresse auf "<ID>@vc.domain.de", den Benutzernamen auf "<ID>@vc.domain.de", den Registrar-Server auf "188.340.8.22", den Proxy-Server auf "188.340.8.22" und den Registrar-Typ auf "Standard-PIP" mit Kontrollkästen nicht ankreuzen (aus) gesetzt, wobei das Transportprotokoll auf TLS umgestellt werden soll, sobald der CMS-Bund klappt. 
Die Monitore sind auf "Automatisch, Vollbild, Ein Monitor" gesetzt. 
Die Audioeinstellungen sind auf "Pro Raum anpassen" gesetzt, wobei bei G7500 möglicherweise andere Optionen gelten. 
Die Video-Eingänge sind auf "Pro Raum anpassen" gesetzt. 
Der Zugriff ist auf "Netzwerk-IDS-System aktivieren: (deaktiviert), Web-Zugriff aktivieren: (aktiviert), Telnet-Zugriff aktivieren: (deaktiviert), Lgacy-API über SSH aktivieren: (deaktiviert), SNMP-Zugriff aktivieren: (aktiviert), Port nach fehlerhaften Anmeldeversuchen sperren: 10, Dauer der Portsperre: 1 Minute, Portsperrungszäher zurücksetzen nach: Aus, Zulassungsliste aktivieren: (deaktiviert), Zeitüberschreitung für inaktive Sitzungen in Minuten: 10, Zulässige Höchstzahl aktiver Sitzungen: 50, Max. Zeitüberschreitung: Aus, Alle USB-Anschlüsse deaktivieren: (deaktiviert), Mindestens erforderliche TLS-Version: TLS 1.2" gesetzt. 
Die Zertifikate sind auf "Standard-Einstellungen" gesetzt, mit der Bemerkung, dass aktuell keine eigenen Zertifikate vorhanden sind und somit selbstsigniert ist. 
Die Lokalen Konten sind auf "Standard-Einstellungen" gesetzt, mit der Empfehlung, das Kennwort nach der Einrichtung zu ändern. 
Die Globale Sicherheit ist auf "erweitert" gesetzt. 
Die Kennwortanforderungen sind auf "Standard-Einstellungen" gesetzt. 
Der Sicherheitscode ist aktiviert. 
Das Sicherheitsbanner ist deaktiviert. 
Der Content ist auf "Benutzer dürfen Content aus primärem Netzwerk speichern: (Aktiviert), Benutzer dürfen Content aus dem WLAN speichern: (Deaktiviert)" gesetzt. 
Die WLAN- und Bildschirmspiegelungsfunktionen sind auf "WLAN-Funktionen aktivieren (Deaktiviert), Bluetooth aktivieren: (Aktiviert), Bildschirmspiegelung: (deaktiviert), Miracast: (deaktiviert)" gesetzt, mit der Bemerkung, dass geprüft werden sollte, ob Bluetooth abgeschaltet werden kann. 
Der Kalenderdienst ist deaktiviert. 
Der Verzeichnisserver ist auf "Servertyp: Polycom GDS, Serveradresse: 188.340.8.21" gesetzt. 
Der Bereitstellungsserver ist deaktiviert. 
Der SNMP-Server ist aktiviert, mit Benachrichtigungen deaktiviert, Version 1 deaktiviert, Version 2c deaktiviert, Version 3 aktiviert, Community mit Leseberechtigung deaktiviert, Kontaktname "Medientechnik", Standortname "Standard", Gebäude- und Raumname "Standort2 Geb_D D.1.10", Systembeschreibung "Videoconferencing Device", Benutzername "snmpvideo", Authentifizierungsalgorithmus "SHA", Authentifizierungskennwort "siehe PW-Datenbank", Verschlüsselungsalgorithmus "CFB-AES128", Verschlüsselungskennwort "siehe PW-Datenbank", Engine-ID wird automatisch generiert, Listener-Port "161", Transportprotokoll "UDP", Zieladresse 1 aktiviert, Serveradresse "188.340.5.250", Nachrichtenart "TRAP", Protokoll "v3", Port "162", Zieladresse 2 deaktiviert, Zieladresse 3 deaktiviert. 
Der Cloud-Server ist deaktiviert.

## Poly Clariti App Bearbeiten

aktuell nicht in der produktiven Verwendung ( https://188.340.8.22:6228/client/)
