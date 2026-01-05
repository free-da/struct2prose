# Logging

## Einleitung

Die Liste aus dem Abschnitt "Einleitung" des Dokuments "Logging" befasst sich mit verschiedenen Aspekten des Loggings. Zusammengefasst kann man sagen, dass diese Liste eine Übersicht über grundlegende Konzepte und Funktionen des Loggings bietet.

Sie umfasst drei wichtige Punkte: 
1. **Logging-Anpassungen zur Laufzeit vornehmen**: Dieser Punkt deutet darauf hin, dass es möglich ist, die Logging-Einstellungen während des Betriebs anzupassen, ohne dass ein Neustart erforderlich ist.
2. **server.log**: Hierbei handelt es sich wahrscheinlich um eine Datei, in der Log-Daten gespeichert werden. Die server.log-Datei ist ein wichtiger Bestandteil des Loggings, da sie alle relevanten Ereignisse und Fehler aufzeichnet.
3. **Logger-Einstellung**: Dieser Punkt bezieht sich auf die Konfiguration der Logger, die für die Erfassung und Speicherung von Log-Daten verantwortlich sind. Die Einstellung der Logger ermöglicht es, die Art und Weise, wie Log-Daten gesammelt und verarbeitet werden, anzupassen.

Insgesamt bietet diese Liste einen Überblick über die grundlegenden Komponenten und Funktionen des Loggings, einschließlich der Anpassung von Logging-Einstellungen, der Verwendung der server.log-Datei und der Konfiguration von Loggern.

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

Diese Tabelle stellt die Konfigurationsoptionen für die Log-Datei "server.log" dar und bietet eine Übersicht über die verschiedenen Parameter, die für die Log-Rotation und -speicherung verwendet werden können. Sie ermöglicht es, die Log-Dateien effizient zu verwalten und zu konfigurieren.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Element-Name: Gibt den Namen des Konfigurationselements an
* Erläuterung des Wertes: Beschreibt den Zweck und die Funktion des jeweiligen Konfigurationselements

Die einzelnen Zeilen der Tabelle können wie folgt beschrieben werden:
Die zu konfigurierende Log-Datei wird durch den Element-Namen "file" identifiziert. 
Die Log-Rotation wird durch die Regel "SizeAndTimeBasedRollingPolicy" festgelegt, die eine Rotation basierend auf verstreichender Zeit und Größe ermöglicht. 
Der Ausgabeort der rotierten Log-Datei wird durch den Element-Namen "fileNamePattern" bestimmt, der ein Benennungsschema wie "server.2024-01-04.0.txt" ermöglicht. 
Die maximale Größe einer Datei, bevor sie rotiert wird, wird durch den Element-Namen "maxFileSize" angegeben. 
Die maximale Anzahl an aufbewahrten Logging-Dateien wird durch den Element-Namen "maxHistory" festgelegt. 
Das Gesamtvolumen an aufbewahrten Logging-Dateien wird durch den Element-Namen "totalSizeCap" bestimmt. 
Das Layout, in dem die Log-Nachrichten in die Logdatei geschrieben werden, wird durch den Element-Namen "pattern" angegeben.

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

Die Liste beschreibt die Schritte, um die Logger-Einstellung in einer logback.xml-Datei zu bearbeiten. Hier sind die Schritte im Detail:

Um die Logger-Einstellung zu bearbeiten, folgen Sie bitte diesen Schritten:
1. Öffnen Sie die Datei `logback.xml` mit dem Editor `vim`.
2. Wechseln Sie in den visuellen Modus, indem Sie die Taste "v" drücken. Dies ermöglicht es Ihnen, die zu bearbeitenden Zeilen auszuwählen.
3. Führen Sie den Befehl `:s/FIND/REPLACE/` aus, um den gewünschten Text zu ersetzen. Ein Beispiel dafür wäre `:s/INFO/ERROR/`, um alle Vorkommen von "INFO" durch "ERROR" zu ersetzen. Bestätigen Sie den Befehl mit der Enter-Taste.
4. Nachdem Sie die Änderungen vorgenommen haben, warten Sie bitte 30 Sekunden, bevor die Änderungen in Kraft treten.

Diese Schritte ermöglichen es Ihnen, die Logger-Einstellung in der logback.xml-Datei zu bearbeiten und die gewünschten Änderungen vorzunehmen.
