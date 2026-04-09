# Polycom-Videokonferenzsysteme

## Einleitung

Die Liste bezieht sich auf die Konfiguration und Verwaltung von Polycom-Videokonferenzsystemen. Sie umfasst verschiedene Aspekte, die für die Einrichtung und den Betrieb dieser Systeme wichtig sind.

Zusammengefasst handelt es sich um folgende Punkte:

Die Konfiguration von Polycom-Videokonferenzsystemen umfasst mehrere Schritte und Komponenten. Zunächst ist es wichtig, einen Ansprechpartner zu haben, der für die Koordination und den Support verantwortlich ist.

Die Polycom-Infrastruktur basiert auf IP-Netzen und Servern, wie dem S-1870, der für Netzwerkbasisdienste wie DHCP und DNS sowie für die Software-Deployer-Verwaltung zuständig ist. Darüber hinaus gibt es die CMS-Bund-Plattform (BDBOS), die auf dem S-1872-Server läuft.

Für die Endgeräte-Aktualisierung und -Verwaltung gibt es spezielle Poly-Endgeräte, die regelmäßig aktualisiert werden sollten. Es gibt auch verschiedene Clientsysteme, die für die Videokonferenzsysteme verwendet werden können.

Die Standardkonfiguration für Polycom-Systeme umfasst Modelle wie x50, x52 und G7500. Darüber hinaus gibt es die Poly Clariti-App, die für die Videokonferenz-Verwaltung verwendet werden kann.

Schließlich gibt es verschiedene Szenarien, in denen die Polycom-Videokonferenzsysteme eingesetzt werden können. Diese reichen von einfachen Videokonferenzen bis hin zu komplexen Konferenzszenarien mit mehreren Teilnehmern und Standorten.

Insgesamt bietet die Liste eine Übersicht über die verschiedenen Komponenten und Schritte, die für die Einrichtung und den Betrieb von Polycom-Videokonferenzsystemen erforderlich sind.

## Ansprechpartner

## Poly VK-Infrastruktur

## IP-Netze

### Tabelle: IP-Adressbereiche für Polycom-Videokonferenzsysteme
Die Tabelle stellt die verschiedenen IP-Adressbereiche und ihre Beschreibungen für Polycom-Videokonferenzsysteme dar. Sie enthält Informationen über die IP-Adressen, die für bestimmte Netzwerke und Standorte verwendet werden.

### Spaltenbeschreibung
* Die erste Spalte enthält die IP-Adressbereiche.
* Die zweite Spalte enthält die Beschreibungen der IP-Adressbereiche.

### Tabelleninhalte
Die IP-Adresse 123:213:80a:5800::/64 ::444 (vc.domain.de) wird für die DFN über BRAIN verwendet. 
Die IP-Adresse 123.23.231.39/32 (vc.domain.de) wird für die DFN verwendet und soll später an BRAIN annonciert werden. 
Die IP-Adressen 172.[17|19|23].8.0/24 werden durch 188.999.147.160 /28 (DDW) und 188.999.147.128/27 (Standort1) abgelöst und dienen den internen Videonetzen von DDW und Standort1. 
Die IP-Adresse 188.999.147.0/25 wird für die Standortkopplung des Videodienstes in der Hausstraße 49 verwendet. 
Die IP-Adresse 188.999.147.128/27 wird für die Standortkopplung und den Adressbereich für Endgeräte des Videodienstes in der Bundesallee 51 verwendet. 
Die IP-Adresse 188.999.147.160/28 wird für die Standortkopplung und den Adressbereich für Endgeräte des Videodienstes in der Diedersdorfer Weg 1 verwendet. 
Die IP-Adresse 192.168.75.0/29 wird für den Transfer zwischen NdB-SBC und ORGA-SBC verwendet, wobei .2. NdB-SBC, .3 ORGA-SBC und .4 ORGA-SBC (für Redundanz geblockt, nicht vorhanden) genutzt werden.

## Server

### Tabelle: Polycom-Videokonferenzsysteme - Server
Die Tabelle stellt eine Übersicht über verschiedene Server im Kontext von Polycom-Videokonferenzsystemen dar. Sie enthält Informationen über die Namen, Verwendungszwecke, IP-Adressen, Seriennummern, Betriebssysteme und Standorte dieser Server.

### Spaltenbeschreibung
- **Name**: Der Name des Servers.
- **Verwendung**: Der Verwendungszweck oder die Funktion des Servers.
- **IP**: Die IP-Adresse des Servers.
- **SN**: Die Seriennummer des Servers.
- **OS**: Das Betriebssystem des Servers.
- **Standort**: Der physische Standort des Servers.

### Beschreibung der Tabellenzeilen
- Der Server `server70` wird für Netzwerkbasisdienste, Software-Deploy, DNS, DHCP verwendet und hat die IP-Adresse `188.340.8.2`, läuft unter `RHEL 9` und befindet sich im `VK-Cluster Standort2`.
- Der Server `server71` dient als Clariti Manager, hat die IP-Adresse `188.340.8.21`, läuft unter `OL 8` und befindet sich im `VK-Cluster Standort2`.
- Der Server `server72` fungiert als Clariti Core, hat die IP-Adresse `188.340.8.22`, läuft unter `OL 8` und befindet sich im `VK-Cluster Standort2`.
- Der Server `server73` ist ein RealPresence Collaboration Server, hat die IP-Adresse `188.340.8.23`, läuft unter `OL 8` und befindet sich im `VK-Cluster Standort2`.
- Der Server `server74` dient als Clariti Media-Relay, hat die IP-Adresse `188.340.8.24`, läuft unter `OL 8` und befindet sich im `VK-Cluster Standort2`.
- Der Server `server75` ist ein Clariti Edge NdB-ID, hat die IP-Adresse `188.340.8.25`, läuft unter `OL 8` und befindet sich im `VK-Cluster Standort2`.
- Der Server `server76` fungiert als Clariti Edge Internet, hat die IP-Adresse `188.340.8.26`, läuft unter `OL 8` und befindet sich im `VK-Cluster Standort2`.
- Der Server `server77` dient als Clariti Edge Client, hat die IP-Adresse `188.340.8.27`, läuft unter `OL 8` und befindet sich im `VK-Cluster Standort2`.
- Der Server `sbc001` ist ein Secunet SBC Internet und befindet sich im `RZ Standort2`, derzeit ausgebaut.
- Der Server `sbc002` ist ebenfalls ein Secunet SBC Internet und befindet sich im `RZ Standort2`, derzeit ausgebaut.
- Der Server `sbcmgt` ist ein Secunet SBC Manager und befindet sich im `RZ Standort2`, derzeit ausgebaut.

## S-1870: Netzwerkbasisdienste

## DHCP

Genutzt wird der KEA-DHCP-Server (Nachfolger des ISC-DHCP-Servers).

Die Konfigdateien liegen unter /etc/kea/.

Die Liste bezieht sich auf die Konfiguration von Polycom-Videokonferenzsystemen im Zusammenhang mit DHCP (Dynamic Host Configuration Protocol). Sie enthält zwei wichtige Konfigurationsdateien, die für die Einrichtung und Verwaltung von DHCP-Diensten unter Verwendung des Kea-DHCP-Servers erforderlich sind.

Zusammengefasst umfasst die Liste die folgenden Konfigurationsdateien:
- Die Kea-Main-Konfiguration, die in der Datei `keactrl.conf` gespeichert ist. Diese Datei enthält die Hauptkonfiguration für den Kea-Server und steuert die allgemeine Funktionalität des Servers.
- Die Kea-DHCP4-Konfiguration, die in der Datei `kea-dhcp4.conf` gespeichert ist. Diese Datei enthält spezifische Einstellungen für den DHCPv4-Dienst, der für die Zuweisung von IPv4-Adressen an Geräte im Netzwerk verantwortlich ist.

Um diese Konfigurationen zu nutzen, sollten Sie folgende Schritte befolgen:
1. Öffnen Sie die Datei `keactrl.conf`, um die Hauptkonfiguration des Kea-Servers zu überprüfen und gegebenenfalls anzupassen.
2. Öffnen Sie die Datei `kea-dhcp4.conf`, um die spezifischen Einstellungen für den DHCPv4-Dienst zu konfigurieren und anzupassen.

Durch die Bearbeitung und Konfiguration dieser Dateien können Sie den Kea-DHCP-Server für Ihre Polycom-Videokonferenzsysteme einrichten und verwalten.

DHCP6 ist derzeit deaktiviert. Kann in der Kea-Main-Konfig aktiviert und in der kea-dhcp6.conf konfiguriert werden.

Der DHCP ist aktuell nur für die Berliner Endgeräte. Es gibt aktuell kein DHCP-Relay zur BU oder zum DDW.

## DNS

Der
BIND (named) DNS-Server wird für die interne DNS-Zone
vk.segment.domain.de genutzt und sorgt für die DNS-Auflösungen innerhalb
des VK-Clusters.

Die Liste bezieht sich auf die Konfiguration von DNS (Domain Name System) im Rahmen von Polycom-Videokonferenzsystemen. Sie enthält wichtige Informationen über die Dateien, die für die Konfiguration des Namensdienstes verwendet werden.

Zusammengefasst umfasst die Liste die folgenden Punkte:

Die Konfiguration des Namensdienstes wird durch zwei wichtige Dateien gesteuert:
- Die **Named-Konfiguration** befindet sich in der Datei `/etc/named.conf`. Diese Datei enthält die grundlegende Konfiguration des Namensdienstes und legt die allgemeinen Einstellungen für den Betrieb des DNS-Servers fest.
- Die **Named-Zonen** sind in der Datei `/etc/named.rfc1912.zones` definiert. Diese Datei enthält die spezifischen Zoneneinstellungen, die für die Auflösung von Domain-Namen innerhalb des Netzwerks erforderlich sind.

Es handelt sich hier nicht um eine Schrittfolge, sondern um eine Beschreibung der relevanten Konfigurationsdateien für den DNS-Server im Kontext von Polycom-Videokonferenzsystemen. Diese Informationen sind wichtig für die Einrichtung und Verwaltung des DNS-Servers, um sicherzustellen, dass die Namensauflösung innerhalb des Netzwerks korrekt funktioniert.

Ausschnitt

```
zone "vk.segment.domain.de" IN {
type master;
file "/etc/named/vk.segment.forward.zone";
allow-update { none; };
allow-query { any; };
};
```

Der Abschnitt "DNS" im Dokument über Polycom-Videokonferenzsysteme behandelt die Konfiguration der DNS-Einstellungen. Hierbei wird auf die Forward-Zone eingegangen. Die Liste kann wie folgt zusammengefasst werden:

Die Konfiguration der DNS-Einstellungen für Polycom-Videokonferenzsysteme umfasst die Einrichtung der Forward-Zone. Hierbei ist insbesondere die Datei `/etc/named/vk.segment.forward.zone` zu beachten, die für die Domäne `vk.segment.domain.de` zuständig ist.

Es gibt keine spezifischen Schritte, die in einer bestimmten Reihenfolge ausgeführt werden müssen, da die Liste lediglich auf die Existenz und den Zweck dieser Datei hinweist. Wenn jedoch die Konfiguration der Forward-Zone durchgeführt werden soll, könnten die allgemeinen Schritte wie folgt aussehen:

1. Öffnen Sie die Datei `/etc/named/vk.segment.forward.zone` in einem Texteditor.
2. Überprüfen Sie die Einträge in der Datei, um sicherzustellen, dass die Domäne `vk.segment.domain.de` korrekt konfiguriert ist.
3. Führen Sie gegebenenfalls Änderungen an den Einträgen durch, um die gewünschte Konfiguration zu erreichen.
4. Speichern Sie die Änderungen und schließen Sie die Datei.

Es ist jedoch wichtig zu beachten, dass diese Schritte nur eine allgemeine Anleitung darstellen und je nach spezifischer Konfiguration und Umgebung variieren können.

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

Der Abschnitt "DNS" im Dokument "Polycom-Videokonferenzsysteme" befasst sich mit der Konfiguration der DNS-Einstellungen für das Videokonferenzsystem. Eine wichtige Information in diesem Kontext ist die Konfiguration der Reverse-Zone für die Domäne "vk.segment.domain.de". 

Diese Konfiguration wird in der Datei "/etc/named/vk.segment.reverse.zone" durchgeführt. 

Zusammengefasst kann man sagen, dass die Liste lediglich einen Punkt anspricht, nämlich die Konfiguration der Reverse-Zone für die angegebene Domäne. 

Es gibt keine Schrittfolge, da es sich hier um eine einzelne Information handelt. 

Um diese Konfiguration vorzunehmen, müsste man jedoch folgende Schritte ausführen:
1. Öffnen Sie die Datei "/etc/named/vk.segment.reverse.zone" in einem Texteditor.
2. Fügen Sie die erforderlichen Einträge für die Reverse-Zone "vk.segment.domain.de" hinzu.
3. Speichern und schließen Sie die Datei.
4. Überprüfen Sie, ob die Konfiguration erfolgreich war, indem Sie die DNS-Auflösung testen. 

Bitte beachten Sie, dass diese Schritte nur eine allgemeine Anleitung darstellen und je nach spezifischem System und Konfiguration variieren können.

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

Um auf den Software-Deployer zuzugreifen, benötigen Sie die Deploy-Adresse, die unter `http://deploy.vk.sagmente.domain.de/` zu finden ist. Diese Adresse ermöglicht es Ihnen, auf die Plattform zuzugreifen, um Software-Updates oder Konfigurationen durchzuführen.

Der Pfad auf dem Server, der für den Deployer relevant ist, lautet `/var/www/html`. Dieser Pfad ist wichtig, um die Dateien und Konfigurationen des Deployers zu finden und zu bearbeiten.

Es gibt keine spezifischen Schritte, die in einer bestimmten Reihenfolge ausgeführt werden müssen, da die Liste hauptsächlich informativ ist und die notwendigen Informationen für den Zugriff und die Konfiguration des Software-Deployers bereitstellt. Wenn Sie jedoch auf den Deployer zugreifen möchten, können Sie folgende Schritte befolgen:

1. Öffnen Sie einen Webbrowser und geben Sie die Deploy-Adresse `http://deploy.vk.sagmente.domain.de/` ein.
2. Nachdem Sie auf die Plattform zugegriffen haben, können Sie die notwendigen Konfigurationen oder Updates durchführen.
3. Wenn Sie Dateien oder Konfigurationen auf dem Server bearbeiten müssen, navigieren Sie zum Pfad `/var/www/html`, um die entsprechenden Dateien zu finden und zu bearbeiten.

Es ist wichtig, diese Schritte sorgfältig durchzuführen und sicherzustellen, dass Sie die notwendigen Berechtigungen und Kenntnisse haben, um den Software-Deployer korrekt zu konfigurieren und zu verwenden.

Als root im root/ Verzeichnis das Skript "./Poly-Updater.sh" ausführen.

## S-1872: CMS-Bund-Plattform (BDBOS)

In
den DIAL-Plan am Clariti-Core werden alle Rufnummern der
CMS-Bund-Plattform auf die Rufnummer +49 999999999 geändert. Grund sind
Tests für unser Nutzerhaus.

https://188.340.8.22:6228/cce/service-config/dial-plan/dial-plans

DIAL-Rule: Resolve to external SIP Peer NdB println("Original DIAL_STRING: " + DIAL_STRING); println("Modified by us DIAL_STRING: " + DIAL_STRING); return DIAL_STRING;

## Poly Clientsysteme

### Tabelle: Polycom-Videokonferenzsysteme
Die Tabelle trägt keinen expliziten Titel, daher wird sie basierend auf ihrem Inhalt als "Polycom-Videokonferenzsysteme" bezeichnet.

### Überblick
Diese Tabelle stellt eine Übersicht über verschiedene Polycom-Videokonferenzsysteme an verschiedenen Standorten dar. Die Tabelle enthält Informationen über die Standorte, die Namen der Systeme, IP-Adressen, MAC-Adressen, SIP-Nummern, Modelle und weitere technische Details.

### Spaltenbeschreibung
- **Standort/Raum**: Der Standort oder Raum, in dem das Videokonferenzsystem installiert ist.
- **Name**: Der Name des Videokonferenzsystems.
- **VKA-IP**: Die IP-Adresse des Videokonferenzsystems.
- **VKA-MAC**: Die MAC-Adresse des Videokonferenzsystems.
- **SIP**: Die SIP-Nummer des Videokonferenzsystems.
- **Modell**: Das Modell des Videokonferenzsystems.
- **TC-IP**: Die IP-Adresse des TC-Systems (wahrscheinlich Teil des Videokonferenzsystems).
- **TC-MAC**: Die MAC-Adresse des TC-Systems.
- **TC-SN**: Die Seriennummer des TC-Systems.
- **VMR-ID**: Die VMR-ID des Videokonferenzsystems.

### Beschreibung der Tabellenzeilen
- Im Garten gibt es keine Videokonferenzsysteme.
- Im Raum Standort1 A103 befindet sich ein Videokonferenzsystem namens Standort1-A103 mit der IP-Adresse 188.455.8.50 und der MAC-Adresse 188.34.:5e:c5:79.
- Im Raum Standort1 A107 befindet sich ein Videokonferenzsystem namens Standort1-A107 mit der IP-Adresse 188.455.8.52 und der MAC-Adresse 188.34.:5e:be:98.
- Im Raum Standort1 B001 befindet sich ein Videokonferenzsystem namens Standort1-B001 mit der IP-Adresse 188.455.8.54 und der MAC-Adresse 188.34.:40:95:fc.
- Im Raum Standort1 B003 befindet sich ein Videokonferenzsystem namens Standort1-B003 mit der IP-Adresse 188.455.8.56 und der MAC-Adresse 188.34.:91:71:55.
- Im Raum Standort1 B003 Mobil befindet sich ein Videokonferenzsystem namens Standort1-B003-Mobil mit der IP-Adresse 188.455.8.58 und der MAC-Adresse 188.34.:56:5d:6e.
- Im Raum Standort1 B008 Mobil 2 befindet sich ein Videokonferenzsystem namens Standort1-B008-Mobil mit der IP-Adresse 188.455.8.60 und der MAC-Adresse 188.34.:91:6c:45.
- Im Raum Standort1 B206 befindet sich ein Videokonferenzsystem namens Standort1-B206 mit der IP-Adresse 188.455.8.62 und der MAC-Adresse 188.34.:91:73:fe.
- Im Raum Standort1 C125 befindet sich ein Videokonferenzsystem namens Standort1-C125 mit der IP-Adresse 188.455.8.64 und der MAC-Adresse 188.34.:91:6e:67.
- Im Raum Standort1 C202 Mobil 1 befindet sich ein Videokonferenzsystem namens Standort1-C202-Mobil mit der IP-Adresse 188.455.8.66 und der MAC-Adresse 188.34.:91:72:FF.
- Im Hof gibt es keine Videokonferenzsysteme.
- Im Raum Standort3 0.19 befindet sich ein Videokonferenzsystem namens Standort3-0.19 mit der IP-Adresse 188.888.8.13 und der MAC-Adresse 188.34.:60:95:69.
- In der Hausstraße gibt es keine Videokonferenzsysteme.
- Im Raum Standort2 A.1.1 befindet sich ein Videokonferenzsystem namens Standort2-A.1.1 mit der IP-Adresse 188.340.8.92 und der MAC-Adresse 188.34.:74:b7:b4.
- Im Raum Standort2 B.0.2.2 befindet sich ein Videokonferenzsystem namens Standort2-B.0.2.2 mit der IP-Adresse 188.340.8.83 und der MAC-Adresse 188.34.:6a:b9:5e.
- Im Raum Standort2 B.0.2.3 befindet sich ein Videokonferenzsystem namens Standort2-B.0.2.3 mit der IP-Adresse 188.340.8.84 und der MAC-Adresse 188.34.:6a:bf:c1.
- Im Raum Standort2 B.1.1 befindet sich ein Videokonferenzsystem namens Standort2-B.1.1 mit der IP-Adresse 188.340.8.70 und der MAC-Adresse 188.34.:74:b1:58.
- Im Raum Standort2 B.2.22 befindet sich ein Videokonferenzsystem namens Standort2-B.2.22 mit der IP-Adresse 188.340.8.94 und der MAC-Adresse 188.34.:69:1d:52.
- Im Raum Standort2 B.4.10 befindet sich ein Videokonferenzsystem namens Standort2-B.4.10 mit der IP-Adresse 188.340.8.96 und der MAC-Adresse 188.34.:53:c4:14.
- Im Raum Standort2 B.5.1 befindet sich ein Videokonferenzsystem namens Standort2-B.5.1 mit der IP-Adresse 188.340.8.79 und der MAC-Adresse 188.34.:6a:b4:99.
- Im Raum Standort2 B.5.20 befindet sich ein Videokonferenzsystem namens Standort2-B.5.20 mit der IP-Adresse 188.340.8.80 und der MAC-Adresse 188.34.:6a:b6:7f.
- Im Raum Standort2 B.6.17 befindet sich ein Videokonferenzsystem namens Standort2-B.6.17 mit der IP-Adresse 188.340.8.63 und der MAC-Adresse 188.34.:74:b1:14.
- Im Raum Standort2 D.1.2 befindet sich ein Videokonferenzsystem namens Standort2-D.1.2 mit der IP-Adresse 188.340.8.71 und der MAC-Adresse 188.34.:6a:cf:0c.
- Im Raum Standort2 D.1.10 befindet sich ein Videokonferenzsystem namens Standort2-D.1.10 mit der IP-Adresse 188.340.8.86 und der MAC-Adresse 188.34.:6a:cd:f8.
- Im Raum Standort2 D.2.2 befindet sich ein Videokonferenzsystem namens Standort2-D.2.2 mit der IP-Adresse 188.340.8.57 und der MAC-Adresse 188.34.:6a:ba:99.
- Im Raum Standort2 D.2.11 befindet sich ein Videokonferenzsystem namens Standort2-D.2.11 mit der IP-Adresse 188.340.8.90 und der MAC-Adresse 188.34.:60:d0:64.
- Im Raum Standort2 D.3.3 befindet sich ein Videokonferenzsystem namens Standort2-D.3.3 mit der IP-Adresse 188.340.8.64 und der MAC-Adresse 188.34.:6a:c2:d0.
- Im Raum Standort2 D.4.3 befindet sich ein Videokonferenzsystem namens Standort2-D.4.3 mit der IP-Adresse 188.340.8.62 und der MAC-Adresse 188.34.:6a:bd:33.
- Im Raum Standort2 D.5.2 befindet sich ein Videokonferenzsystem namens Standort2-D.5.2 mit der IP-Adresse 188.340.8.55 und der MAC-Adresse 188.34.:6a:b6:55.
- Im Raum Standort2 E.6.15 befindet sich ein Videokonferenzsystem namens Standort2-E.6.15 mit der IP-Adresse 188.340.8.81 und der MAC-Adresse 188.34.:6a:b4:2a.

## Poly Standardkonfig (x50/x52/G7500)

[LLM-Fehler bei table-Kontextualisierung: Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kaxq4681ezq9f53vp3xgqdn8` service tier `on_demand` on tokens per minute (TPM): Limit 12000, Used 8934, Requested 4159. Please try again in 5.465s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}]

## Poly Clariti App

aktuell nicht in der produktiven Verwendung ( https://188.340.8.22:6228/client/)
