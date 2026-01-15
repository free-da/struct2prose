# Logging

## Einleitung

Im Abschnitt "Einleitung" des Dokuments "Logging" werden verschiedene Aspekte des Loggings behandelt. Zusammengefasst geht es dabei um die Anpassung und Konfiguration von Logging-Funktionen. Die Liste kann wie folgt zusammengefasst werden:

Das Logging umfasst mehrere wichtige Aspekte, die für eine effiziente Überwachung und Analyse von Systemvorgängen sorgen. Dazu gehören die Möglichkeit, **Logging-Anpassungen zur Laufzeit vorzunehmen**, was bedeutet, dass Änderungen an den Logging-Einstellungen ohne Neustart des Systems vorgenommen werden können. Ein weiterer wichtiger Punkt ist die **server.log**, die als zentrale Datei für die Aufzeichnung von Systemereignissen dient. Darüber hinaus spielen **Logger-Einstellungen** eine entscheidende Rolle, da sie es ermöglichen, die Art und Weise, wie Logs erstellt und verarbeitet werden, genau zu konfigurieren.

Es handelt sich hier nicht um eine Schrittfolge, sondern um eine Sammlung von Konzepten und Funktionen, die im Zusammenhang mit Logging relevant sind. Diese Punkte bieten einen Überblick über die Flexibilität und Anpassungsmöglichkeiten des Logging-Systems, um es an die spezifischen Bedürfnisse eines Systems oder einer Anwendung anzupassen.

Auf allen S0FTW4RE-Instanzen wird das Logging durch die Datei wildfly/standalone/configuration/logback.xml konfiguriert.
Die Logging-Konfigurationen sind auf allen Instanzen gleich, außer dass
in TEST und DEMO ein Loglevel von "INFO" und auf PROD "ERROR"
eingestellt ist. Um eine Versionierung dieser Datei zu gewährleisten,
wird diese Datei durch einen Symlink auf das S0FTW4RE-REPO bereitgestellt:

```
ln -s /opt/s0ftw4reweb/S0FTW4RE_REPO/s0ftw4re_configfiles/
[
PROD|DEMO|TEST
]
/logback.xml /opt/s0ftw4reweb/wildfly/standalone/logback.xml
```

Jede
Konfigurationsdatei soll AUSSCHLIEßLICH aus dem Repo verlinkt werden
und auch nur dort bearbeitet und nach Bearbeitung wieder eingecheckt
werden. Es sollen KEINE Dateien aus dem Repo kopiert werden!

Die logback.xml wird von S0FTW4RE ausgeliefert und folgende ORGA-spezifische Anpassungen werden vorgenommen:

## Logging-Anpassungen zur Laufzeit vornehmen

```
<!-- Zeile 2: regelmäßiges Scannen nach Veränderungen in der Datei -->
<configuration
scan=
"true"
scanPeriod=
"30 seconds"
>
```

Indem
das Logging-Framework alle 30 Sekunden nach Veränderungen in der
Logging-Konfiguration sucht, können Anpassungen im laufenden Betrieb
ohne Neustart vorgenommen werden.

## server.log Bearbeiten

Das eigentliche Logging wird in der Datei /opt/s0ftw4reweb/wildfly/standalone/log/server.log vorgenommen. Diese Datei soll täglich rotiert werden. Die Logs werden
30 Tage aufbewahrt, und bis zu einem Gesamtvolumen von 30 GB.

```
<!-- ab Z. 55 -->
<!-- Definition des Appender für das Schreiben der Logdateien "server.log" -->
<appender
name=
"RequestLogAppender"
class=
"ch.qos.logback.core.rolling.RollingFileAppender"
>
<file>
${JBOSS_HOME}/standalone/log/server.log
</file>
<rollingPolicy
class=
"ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy"
>
<!-- rollover daily -->
<fileNamePattern>
/opt/s0ftw4reweb/wildfly/standalone/log/server.%d{yyyy-MM-dd}.%i.txt
</fileNamePattern>
<!-- each file should be at most 100MB, keep 30 days worth of history, but at most 3GB -->
<maxFileSize>
100MB
</maxFileSize>
<maxHistory>
30
</maxHistory>
<totalSizeCap>
3GB
</totalSizeCap>
</rollingPolicy>
<encoder>
<pattern>
%date - %logger:\n [%level]: %message%n%xException
</pattern>
</encoder>
</appender>
```

Zu
Beachten, falls Konfigurationen kopiert werden: Der Name des Appenders
"RequestLogAppender" muss zwingend erhalten werden, sonst weiß die
Anwendung nicht, wo die zu loggenden Daten hingeschickt werden müssen.

Hier eine Erklärung der Einstellungen:

### Logging-Konfiguration
Die Tabelle hat keinen expliziten Titel, daher kann sie als "Logging-Konfiguration" bezeichnet werden. Diese Tabelle stellt die verschiedenen Parameter und Einstellungen für die Logging-Konfiguration auf einem Server dar. Sie enthält Informationen über die Log-Datei, die Rotation und die Speicherung von Log-Daten.

### Spaltenbeschreibung
Die Tabelle hat zwei Spalten:
* Element-Name: Diese Spalte enthält die Namen der verschiedenen Konfigurationselemente.
* Erläuterung des Wert: Diese Spalte enthält eine kurze Beschreibung des jeweiligen Konfigurationselements.

### Tabelleninhalte
Die Tabelle enthält folgende Einträge:
Die zu konfigurierende Log-Datei wird durch den Element-Namen "file" identifiziert. 
Die Log-Rotation wird durch die Regel "rollingPolicy" festgelegt, die auf eine Rotation basierend auf verstreichender Zeit und Größe setzt. 
Der Ausgabeort der rotierten Log-Datei wird durch den "fileNamePattern" bestimmt, der ein Benennungsschema wie "server.2024-01-04.0.txt" erstellt. 
Die maximale Größe einer Datei, bevor sie rotiert wird, wird durch "maxFileSize" angegeben. 
Die maximale Anzahl an aufbewahrten Logging-Dateien wird durch "maxHistory" festgelegt. 
Das Gesamtvolumen an aufbewahrten Logging-Dateien wird durch "totalSizeCap" begrenzt. 
Das Layout, in dem die Log-Nachrichten in die Logdatei geschrieben werden, wird durch den "pattern" bestimmt.

## Logger-Einstellung Bearbeiten

Im letzten Teil der logback.xml werden die verwendeten Logger eingebunden und deren Loglevel festgelegt:

```
<!-- Z. 82 -->
<logger
name=
"de.s0ftw4re.system.ui.component.demo"
level=
"INFO"
></logger>
<logger
name=
"org.apache.cxf.services"
level=
"INFO"
></logger>
<logger
name=
"de.s0ftw4re.system.ui"
level=
"INFO"
></logger>
<logger
name=
"de.s0ftw4re.system.jpql"
level=
"INFO"
></logger>
<logger
name=
"org.hibernate"
level=
"INFO"
></logger>
<!-- <logger name="org.hibernate.SQL" level="INFO" ></logger> -->
<!-- <logger name="org.jboss.as.ee" level="INFO"></logger> -->
<!-- <logger name="org.hibernate" level="INFO"></logger> -->
<!-- <logger name="org.jboss.jca" level="INFO"></logger> -->
<!-- <logger name="com.arjuna" level="INFO"></logger> -->
<!-- <logger name="de.s0ftw4re.system.jpql" level="INFO"></logger> -->
<logger
name=
"de.s0ftw4re.system.attach"
level=
"INFO"
></logger>
<logger
name=
"de.s0ftw4re.system.service"
level=
"INFO"
></logger>
<logger
name=
"org.springframework.orm"
level=
"INFO"
></logger>
<!-- <logger name="org.apache.activemq" level="INFO"></logger> -->
<logger
name=
"de.s0ftw4re.system.log"
level=
"INFO"
></logger>
<logger
name=
"de.s0ftw4re.dapservice"
level=
"INFO"
></logger>
<logger
name=
"org.jboss"
level=
"INFO"
></logger>
<logger
name=
"org.springframework"
level=
"INFO"
></logger>
<root
level=
"WARN"
>
<appender-ref
ref=
"RequestLogAppender"
></appender-ref>
<appender-ref
ref=
"S0ftw4re-Ondemand-Appender"
></appender-ref>
<appender-ref
ref=
"Stdout"
></appender-ref>
</root>
```

Für TEST und DEMO wird standardmäßig das Loglevel auf INFO, für PROD auf ERROR gestellt.

Zu Beachten: die Einbindung der Zeile <logger name="de.s0ftw4re.dapservice" level="INFO"/> , die standardmäßig NICHT vorhanden ist, uns aber wichtige Informationen über die DAP-Komponente gibt.

Um
den Loglevel zu ändern, muss, sofern in Z.2 (s.o.) der Scanner
eingeschaltet ist, die Anwendung nicht neugestartet werden. Es reicht,
folgende Schritte auszuführen:

Die Liste beschreibt die Schritte, um die Logger-Einstellung in der Datei `logback.xml` zu bearbeiten. Hier sind die Schritte im Detail:

Um die Logger-Einstellung zu bearbeiten, folgen Sie bitte diesen Schritten:
1. Öffnen Sie die Datei `logback.xml` mit dem Editor `vim`.
2. Wechseln Sie in den visuellen Modus, indem Sie die Taste "v" drücken. Dies ermöglicht es Ihnen, die zu bearbeitenden Zeilen auszuwählen.
3. Führen Sie den Befehl `:s/FIND/REPLACE/` aus, um den gewünschten Text zu ersetzen. Ein Beispiel dafür wäre `:s/INFO/ERROR/`, um alle Vorkommen von "INFO" durch "ERROR" zu ersetzen. Bestätigen Sie den Befehl mit der Enter-Taste.
4. Nachdem Sie die Änderungen vorgenommen haben, warten Sie bitte 30 Sekunden, bevor die Änderung in Kraft tritt.

Diese Schritte ermöglichen es Ihnen, die Logger-Einstellung in der Datei `logback.xml` zu bearbeiten und die gewünschten Änderungen vorzunehmen.
