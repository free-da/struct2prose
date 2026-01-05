# Update_6.0

## Einleitung

Die Liste beschreibt die Schritte für das Update auf Version 6.0. Hier ist eine Zusammenfassung der Schritte in einem gut lesbaren Fließtext:

Das Update auf Version 6.0 umfasst mehrere Schritte, die sorgfältig durchgeführt werden müssen. Zunächst müssen einige grundlegende Vorbereitungen getroffen werden, wie das Einrichten des Homeverzeichnisses für den s0ftw4re-user und die Bereitstellung von Ressourcen.

Hier sind die Schritte für das Update:

1. **Vorbereitung**: Stellen Sie sicher, dass das Homeverzeichnis für den s0ftw4re-user eingerichtet ist und die notwendigen Ressourcen bereitgestellt werden.
2. **Update von Java**: Führen Sie ein Update von Java durch, um sicherzustellen, dass die neueste Version verwendet wird.
3. **Update von erp-dbtool**: Führen Sie ein Update von erp-dbtool durch, um sicherzustellen, dass die neueste Version verwendet wird.
4. **Datenbankupdate**: Führen Sie das Datenbankupdate durch, um sicherzustellen, dass die Datenbank auf dem neuesten Stand ist.
5. **ORGA Views und Tabellen**: Spielen Sie die ORGA Views und Tabellen ein, um sicherzustellen, dass die notwendigen Datenbankstrukturen vorhanden sind.
6. **Applicationserver installieren**: Installieren Sie den Applicationserver auf einem Linux-Betriebssystem und bereiten Sie es vor. Dazu gehören auch die Font-Installation für Standard-BI-Berichte und die Verlinkung von JAVA mit dem Benutzerverzeichnis. Installieren Sie Wildfly und richten Sie den Systemdienst ein.
7. **Applicationserver konfigurieren**: Konfigurieren Sie den Applicationserver, indem Sie den Oracle-DB-Treiber installieren, den Applicationserver starten und die Treiberinstallation überprüfen. Richten Sie die Datenbankverbindungen ein und überprüfen Sie die Datenbankverbindung.
8. **Weitere Konfigurationen**: Führen Sie weitere Konfigurationen durch, wie die Konfiguration des Logging, des Timeouts, der SSL-Verschlüsselung und der Datenbank-Validation.
9. **S0FTW4RE-Web-Anwendung installieren**: Installieren Sie die S0FTW4RE-Web-Anwendung.
10. **DAP 3.0 installieren**: Installieren Sie DAP 3.0.
11. **Webservices anschalten**: Schalten Sie die Webservices ein.
12. **Jobrunner + VTindex installieren**: Installieren Sie den Jobrunner und den VTindex.

Indem Sie diese Schritte sorgfältig durchführen, können Sie sicherstellen, dass das Update auf Version 6.0 erfolgreich durchgeführt wird.

Punkt abgearbeitet DEMO Version

Punkt abgearbeitet TEST Version

Punkt abgearbeitet PROD Version

⌛  Punkt in Bearbeitung alle Versionen

🚩 Achtung zweiter Check nötig

## Homeverzeichnis s0ftw4re-user Bearbeiten

Wegen der neuen Installierbarkeit einzelner Komponenten als rpm-package ist es nötig, das Homeverzeichnis des s0ftw4re -user zu ändern von s0ftw4reweb nach s0ftw4re.

```
# als user orga-admin
sudo mkdir /opt/s0ftw4re
sudo usermod -d /opt/s0ftw4re/ s0ftw4re
# git-Repo rüberkopieren und anpassen
cd
/opt/s0ftw4reweb
sudo cp -r /opt/s0ftw4reweb/2012-S0FTW4RE/ /opt/s0ftw4re/
# Konfigdateien rüberkopieren und anpassen
sudo cp /opt/s0ftw4reweb/.bash* /opt/s0ftw4re/
vi /opt/s0ftw4re/.bashrc
# anpassen: :%s/s0ftw4reweb/s0ftw4re/gc
# Berechtigungen anpassen
sudo chown -R s0ftw4re:users /opt/s0ftw4re/
# symlinks neu erstellen
# als user s0ftw4re
su s0ftw4re
cd
ln -s
2012
-S0FTW4RE/ S0FTW4RE_REPO
ln -s S0FTW4RE_REPO/s0ftw4re_resources/resources_6.0 s0ftw4re_resources
```

## Ressourcen bereitstellen Bearbeiten

Folgende Dateien ins S0FTW4RE-Repo einchecken und auf dem Zielserver auschecken:

```
$ ls -la | tr -s
' '
| cut -d
" "
-f9
./
../
ERP-DBTool_6.0.121.x86_64.rpm
S0FTW4REAnwenderprofil_ORGA_6.0.dat
S0FTW4REWeb_6.0.87.x86_64.rpm
S0FTW4RE_Web_6.0.87.zip
erp-dbtool_6.0.87.zip
jobrunnerweb_6.0.87.zip
vtindextool_6.0_240425.zip
wildfly-28.0.1.Final-6.0.2-S0FTW4RE_Erweiterung.zip
wildfly-28.0.1.Final.zip
```

## Update Java Bearbeiten

```
# als user orga-admin
sudo yum install java-17-openjdk.x86_64
# bestätigen mit j
sudo alternatives --config java
Es gibt
2
Programme, welche »java« zur Verfügung stellen.
Auswahl    Befehl
-----------------------------------------------
*+
1
java-11-openjdk.x86_64
(
/usr/lib/jvm/java-11-openjdk-11.0.20.0.8-3.el8.x86_64/bin/java
)
2
java-17-openjdk.x86_64
(
/usr/lib/jvm/java-17-openjdk-17.0.11.0.9-2.el8.x86_64/bin/java
)
Eingabe um die vorgegebene Auswahl
[
+
]
zu behalten, oder geben Sie die Nummer an:2
```

## Update erp-dbtool Bearbeiten

```
# als user orga-admin
cd
/opt/s0ftw4reweb/S0FTW4RE_REPO/s0ftw4re_resources/resources_6.0/
sudo rpm -ivh ERP-DBTool_6.0.121.x86_64.rpm
sudo chown -R s0ftw4re:users erpdbtool/
# als user s0ftw4re
su s0ftw4re
cd
cp S0FTW4RE_REPO/s0ftw4re_configfiles/ojdbc8.jar erpdbtool/jdbc/
# default-Dateien löschen
cd
/opt/s0ftw4re/erpdbtool/
rm dbserver.config
rm erp-dbtool-update.sh
# Serverkonfig für aktuelle Anwenderprofildatei anpassen
cd
/opt/s0ftw4re/S0FTW4RE_REPO/s0ftw4re_configfiles/TEST/
cp dbserver.config_5.0 dbserver.config_6.0
vi dbserver.config_6.0
#### anpassen:
--licensepath
=
/opt/s0ftw4re/S0FTW4RE_REPO/s0ftw4re_resources/resources_6.0/S0FTW4REAnwenderprofil_ORGA_6.0.dat
# symlinks auf konfigurierte Dateien setzen
cd
/opt/s0ftw4re/erpdbtool
ln -s ../S0FTW4RE_REPO/s0ftw4re_configfiles/TEST/dbserver.config_6.0 dbserver.config
ln -s ../S0FTW4RE_REPO/s0ftw4re_configfiles/erp-dbtool-update.sh erp-dbtool-update.sh
ln -s ../S0FTW4RE_REPO/s0ftw4re_configfiles/erp-dbtool-connect.sh erp-dbtool-connect.sh
# Installation überprüfen durch Verbindungs-Check:
cd
/opt/s0ftw4re/erpdbtool
./erp-dbtool-connect.sh
##########
# ...
# 2024-05-14 11:04:14.217  INFO : Starting ErpDbtoolApplication v6.0.121 using Java 17.0.11 with PID 376503 (/opt/s0ftw4re/erpdbtool/erp-dbtool-cli.jar started by s0ftw4re in /opt/s0ftw4re/erpdbtool)
# 2024-05-14 11:04:14.221  INFO : The following 1 profile is active: "oracle"
# 2024-05-14 11:04:18.689  INFO : Started ErpDbtoolApplication in 4.917 seconds (process running for 5.834)
# 2024-05-14 11:04:18.697  INFO : ERP-DBTOOL Software-Version: 6.0.0; Datenmodell-Version: 6.0.33
# 2024-05-14 11:04:18.906  INFO : Datenmodell-Version der DB: 5.0.1
# 2024-05-14 11:04:19.278  INFO : Verbindung erfolgreich hergestellt. S0FTW4RE Datenbank erkannt.
#########
```

## Datenbankupdate durchführen Bearbeiten

```
cd
/opt/s0ftw4re/erpdbtool
./erp-dbtool-update.sh
#########
# ...
# 2024-05-14 15:24:11.977  INFO : Update von Version 5.0.1 zu 6.0.33 erfolgreich ausgeführt.
#########
```

## ORGA Views und Tabellen einspielen Bearbeiten

s. ORGA Views und Tabellen

## Applicationserver installieren Bearbeiten

Seit
dieser Version bietet S0FTW4RE die Möglichkeit, die Konfiguration des
Webservers und die Installation der Anwendung per RPM-Packet und
Ansible-Skripten zu orchestrieren. Wir wollen diesen Weg gerne
ausprobieren. Zunächst werden wir den gewohnten, "manuellen"
Installationsweg auf den bekannten TEST- und DEMO-Maschinen ausführen.
Parallel dazu haben wir eine weitere TEST-VM beantragt, auf der wir
zunächst die Installation per Wildfly und RPM-Paketen testen wollen,
später dann auch den von A42 bereitgestellten JBoss EAP 8.0. Für die
Ansible-Orchestrierung wird es nach Absprache mit Thorsten absehbar
einen User-Ansible-Agent geben, der für solche Zwecke geeignet ist. All
dies braucht noch etwas Vorlauf. Deswegen wird hier der gewohnte Weg
beschrieben.

## Linux-Betriebssystem vorbereiten Bearbeiten

Die S0FTW4RE-AG empfiehlt, den Applicationserver in einem eigenen Benutzerkontext zu betreiben. Dies ist neu für uns.

```
# als user orga-admin
# user wildfly erstellen und ihm eine Gruppe und Home-Verzeichnis zuweisen
sudo useradd -d /opt/s0ftw4re/s0ftw4reweb -U wildfly
# Passwort entfernen
sudo passwd -d wildfly
# Anzahl zu öffnender Dateien anpassen:
ulimit
-n
# Antwort: mind. 1024, dann:
vi /etc/security/limits.conf
# enter:
wildfly soft nofile
65535
wildfly hard nofile
65535
# Konsolenkonfiguration entspr. TEST vorbereiten und verlinken
# als user wildfly
ln -s ../S0FTW4RE_REPO/s0ftw4re_configfiles/TEST/.vimrc .vimrc
ln -s ../S0FTW4RE_REPO/s0ftw4re_configfiles/TEST/.bashrc .bashrc
```

## Font-Installation für Standard-BI-Berichte Bearbeiten

```
# ORGA-Schriften
sudo cp -r /opt/s0ftw4re/S0FTW4RE_REPO/Schriften/* /usr/share/fonts/
# Deja-vu muss entfernt werden, da sonst ORGA-Schriften nicht greifen
cd
/usr/share/fonts
sudo rm -rf dejavu/
# Font-config-cache aktualisieren
fc-cache -vf
```

## JAVA mit Benutzerverzeichnis verlinken Bearbeiten

```
# als user s0ftw4re
ln -s /usr/lib/jvm/java-17-openjdk-17.0.11.0.9-2.el8.x86_64 /opt/s0ftw4re/java/jdk
# als user wildfly
vi ~.bashrc
# enter:
export
JAVA_HOME
=
/opt/s0ftw4re/java/jdk
export
PATH
=
$JAVA_HOME
/bin:
$PATH
```

## Wildfly installieren Bearbeiten

```
# als user wildfly
cd
/opt/s0ftw4re/S0FTW4RE_REPO/s0ftw4re_resources/resources_6.0
unzip wildfly-28.0.1.Final.zip -d /opt/s0ftw4re/s0ftw4reweb/
unzip wildfly-28.0.1.Final-6.0.2-S0FTW4RE_Erweiterung.zip -d /opt/s0ftw4re/s0ftw4reweb/
cd
ln -s wildfly-28.0.1.Final wildfly
```

Bestätigen Sie das Überschreiben vorhandener Dateien beim Entpacken des Erweiterungspaketes. Beachten Sie die Dateiberechtigungen für das unprivilegierte Benutzerkonto wildfly.

## Systemdienst einrichten Bearbeiten

```
su wildfly
cd
vi wildfly-28.0.1.Final/bin/systemd/s0ftw4reweb.service
# user und group jboss durch wildfly ersetzen
# JAVA_HOME-Pfad anpassen zu /opt/s0ftw4re/java/jdk"
# als user orga-admin
sudo cp /opt/s0ftw4re/s0ftw4reweb/wildfly-28.0.1.Final/bin/systemd/s0ftw4reweb.service /etc/systemd/system/ ;
sudo systemctl daemon-reload
sudo systemctl
enable
s0ftw4reweb.service
```

## Applicationserver konfigurieren Bearbeiten

## Oracle-DB-Treiber installieren Bearbeiten

```
su wildfly
cd
mkdir -p modules/com/oracle/database/jdbc/main
cp ../S0FTW4RE_REPO/s0ftw4re_configfiles/ojdbc8.jar wildfly-28.0.1.Final/modules/com/oracle/database/jdbc/main
```

Achtung: Damit der Treiber korrekt erkannt wird, muss die standalone-s0ftw4reweb.xml angepasst werden

```
<!-- Folgende Zeilen einkommentieren: -->
<driver
name=
"oracle"
module=
"com.oracle.database.jdbc"
>
<driver-class>
oracle.jdbc.driver.OracleDriver
</driver-class>
</driver>
```

```
<!-- Treiber-Nr. anpassen von 11 auf 8 -->
<resources>
<resource-root
path=
"ojdbc8.jar"
></resource-root>
</resources>
```

```
// in wildfly/bin/standalone.conf hinzufügen:
JAVA_OPTS
=
"$JAVA_OPTS -Xrs -Xms16g -Xmx16g -XX:MaxMetaspaceSize=1g -XX:ReservedCodeCacheSize=750m"
// 64G für's PROD-System
```

## AS + JBoss-cli starten Bearbeiten

```
# wildfly starten als orga-admin
sudo systemctl start s0ftw4reweb
# wildfly konfigurieren über jboss-cli
su wildfly
cd
cd
wildfly-28.0.1.Final/bin/
./jboss-cli.sh
```

```
2024-05-22 14:00:55,891 INFO  [main] [o.j.as.cli.CommandContext] You are disconnected at the moment. Type 'connect' to connect to the server or 'help' for the list of supported commands.
You are disconnected at the moment. Type 'connect' to connect to the server or 'help' for the list of supported commands.
[disconnected /] connect
2024-05-22 14:00:58,947 INFO  [CLI command executor] [org.jboss.remoting] JBoss Remoting version 5.0.27.Final
2024-05-22 14:00:58,954 INFO  [CLI command executor] [org.jboss.threads] JBoss Threads version 2.4.0.Final
```

## Treiberinstallation überprüfen: Bearbeiten

```
[standalone@localhost:9990 /] /schwubsystem=datasources:installed-drivers-list
{
"outcome" => "success",
"result" => [{
"driver-name" => "oracle",
"deployment-name" => undefined,
"driver-module-name" => "com.oracle",
"module-slot" => "main",
"driver-datasource-class-name" => "",
"driver-xa-datasource-class-name" => "",
"datasource-class-info" => undefined,
"driver-class-name" => "oracle.jdbc.driver.OracleDriver",
"driver-major-version" => 19,
"driver-minor-version" => 14,
"jdbc-compliant" => true
}]
}
```

## Datenbankverbindungen einrichten Bearbeiten

Achtung: Passwort anpassen

## TEST

```
data-source add --name=TEST --connection-url=jdbc:oracle:thin:@s-0953.db.domain.de:1522:test --jndi-name=java:/test --user-name=s0ftw4re --password=xxxxx --driver-name=oracle --use-ccm=true --background-validation=true --use-java-context=true
```

## DEMO

```
data-source add --name=DEMO --connection-url=jdbc:oracle:thin:@s-0953.db.domain.de:1521:demo --jndi-name=java:/demo --user-name=s0ftw4re --password=xxxxxxxx --driver-name=oracle --use-ccm=true --background-validation=true --use-java-context=true
```

## Datenbankverbindung überprüfen Bearbeiten

## DEMO

```
/schwubsystem=datasources/data-source=DEMO:test-connection-in-pool
```

## Datenbank Connection-Pool-Größe über jboss.cli konfigurieren Bearbeiten

## TEST

```
/schwubsystem=datasources/data-source=TEST:write-attribute(name=min-pool-size,value=20)
/schwubsystem=datasources/data-source=TEST:write-attribute(name=max-pool-size,value=50)
reload
```

## DEMO

```
/schwubsystem=datasources/data-source=DEMO:write-attribute(name=min-pool-size,value=20)
/schwubsystem=datasources/data-source=DEMO:write-attribute(name=max-pool-size,value=50)
reload
```

## PROD

```
tba.
```

Die Änderungen treten nach Neustart des WildFly in Kraft.

## Logging konfigurieren Bearbeiten

Die vorkonfigurierte logback.xml aus S0FTW4RE_REPO in den wildfly verlinken:

```
# als user wildfly aus wildfly-Homeverzeichnis
ln -s /opt/s0ftw4re/S0FTW4RE_REPO/s0ftw4re_configfiles/TEST/logback.xml /opt/s0ftw4re/s0ftw4reweb/wildfly/standalone/configuration/logback.xml
```

## Timeout konfigurieren Bearbeiten

in
der standalone-s0ftw4reweb.xml an entsprechender Stelle im http- UND im
https-listener die Parameter "read-timeout" und "write-timeout" auf 0
setzen

```
<http-listener
name=
"default"
socket-binding=
"http"
max-post-size=
"209715200"
max-parameters=
"10000"
url-charset=
"utf-8"
redirect-socket=
"https"
enable-http2=
"false"
read-timeout=
"0"
write-timeout=
"0"
></http-listener>
<https-listener
name=
"https"
socket-binding=
"https"
max-post-size=
"209715200"
max-parameters=
"10000"
url-charset=
"utf-8"
ssl-context=
"applicationSSC"
enable-http2=
"false"
read-timeout=
"0"
write-timeout=
"0"
></https-listener>
```

## SSL-Verschlüsselung Bearbeiten

Der Ort der Angabe des keystore hat sich von wildfly-23 zu wildfly-28 geändert.

```
# als user wildfly in jboss-cli
/schwubsystem
=
elytron/key-store
=
applicationKS:add
(
path
=
/opt/s0ftw4re/S0FTW4RE_REPO/keystore/cacerts,credential-reference
={
clear-text
=
keystore-password
}
,type
=
JKS
)
/schwubsystem
=
elytron/key-manager
=
applicationKM:add
(
key-store
=
applicationKS,credential-reference
={
clear-text
=
key-password
}
,alias-filter
=
s-0220.srv.domain.de
)
/schwubsystem
=
elytron/server-ssl-context
=
applicationSSC:add
(
key-manager
=
httpsKM,protocols
=[
"TLSv1.2"
])
# https-Listener konfigurieren
batch
/schwubsystem
=
undertow/server
=
default-server/https-listener
=
https:undefine-attribute
(
name
=
security-realm
)
/schwubsystem
=
undertow/server
=
default-server/https-listener
=
https:write-attribute
(
name
=
ssl-context,value
=
applicationSSC
)
run-batch
# Server Neustart
reload
```

## Datenbank-Validation hinzufügen Bearbeiten

Nach einem Verlust der DB-Verbindung wird diese automatisch wieder hergestellt. Ein Serverneustart ist dann nicht notwendig.

Folgenden Codeblock innerhalb des <datasource> -Elements hinzufügen:

```
<validation>
<check-valid-connection-sql>
select 1 from dual
</check-valid-connection-sql>
<validate-on-match>
false
</validate-on-match>
<background-validation>
true
</background-validation>
<background-validation-millis>
120000
</background-validation-millis>
</validation>
```

Danach den Server neustarten.

## S0FTW4REWeb-Anwendung installieren Bearbeiten

mit Skript, installS0ftw4reWeb();

## DAP 3.0 installieren Bearbeiten

s. DAP 3.0 installieren

## Webservices anschalten Bearbeiten

```
# als user wildfly
cd
/opt/s0ftw4re/s0ftw4reweb/wildfly/modules/de/s0ftw4re/configuration/webservices/main
mv wsdeploy.properties wsdeploy.properties.default
ln -s /opt/s0ftw4re/S0FTW4RE_REPO/s0ftw4re_configfiles/wsdeploy.properties wsdeploy.properties
```

## Jobrunner + VTindex installieren Bearbeiten

per Skript install_s0ftw4re.sh

evtl. Symlink unter ~/cronjobs/cron-s0ftw4re/jobrunner kontrollieren

Jobrunner starten nach JobRunner
