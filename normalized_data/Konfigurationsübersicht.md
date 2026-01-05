# Konfigurationsübersicht

## Konfigurationen

Hier
werden alle wesentlichen Konfigurationen für den laufenden Betrieb in
PROD, TEST und DEMO festgehalten. Änderungen müssen IMMER hier
dokumentiert werden. Dies soll die einzige Referenz darstellen.

Diese Seite ist nicht aktuell und muss überarbeitet werden! Stand: 26.10.2023

## .profile

Setzt Betriebssystemparameter für den Benutzer. Pfad: /home/s0ftw4re/.profile

Diese Tabelle stellt eine Konfigurationsübersicht für Umgebungsvariablen dar, die in der Datei `.profile` verwendet werden. Sie enthält wichtige Einstellungen für Java und Wildfly.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die erste Spalte enthält den Namen des Parameters, der konfiguriert wird.
* Die zweite Spalte enthält den entsprechenden Wert für jeden Parameter.

Die einzelnen Zeilen können wie folgt beschrieben werden:
Die Variable `JAVA_BINDIR` wird auf `/opt/s0ftw4reweb/java/jdk/bin/` gesetzt. 
Die Variable `JAVA_HOME` wird auf `/opt/s0ftw4reweb/java/jdk` gesetzt. 
Die Variable `JAVA_ROOT` wird auf `/opt/s0ftw4reweb/java/jdk` gesetzt. 
Die Variable `JBOSS_HOME` wird auf `/opt/s0ftw4reweb/wildfly` gesetzt. 
Die Variable `PATH` wird auf `$JAVA_HOME/bin:$JBOSS_HOME/bin:$PATH2` gesetzt, wobei `$JAVA_HOME/bin` und `$JBOSS_HOME/bin` vor dem bestehenden Pfad `$PATH2` gesetzt werden.

## standalone.conf

Wildfly Konfiguration für den Java-Prozess.

Pfad: /opt/s0ftw4reweb/wildfly/bin/standalone.conf

Die vorhandenen Java Parameter (JAVA_OPTS) werden um folgende Einträge erweitert.

Diese Tabelle stellt eine Konfigurationsübersicht für die Datei `standalone.conf` dar und enthält verschiedene Parameter mit ihren entsprechenden Werten. Sie bietet einen Überblick über die Einstellungen, die in dieser Konfigurationsdatei vorgenommen wurden.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Die erste Spalte enthält den Parameter, der konfiguriert wird.
* Die zweite Spalte enthält den Wert, der dem jeweiligen Parameter zugewiesen wird.

Die Tabellenzeilen können wie folgt beschrieben werden:
Die Konfiguration enthält den Parameter `-Dde.s0ftw4re.logpath` mit dem Wert `/opt/s0ftw4reweb/logs`. 
Der Parameter `-Dmail.imap.starttls.enable` hat den Wert `True`, was auf die Verwendung von imap oder imaps hinweist.

Bei dem Eintrag -Dhttp.nonProxyHosts sind die \ Zeichen notwendig, um die | zu maskieren. Andernfalls startet der Wildfly nicht.

Der Parameter -Dmail.imap.starttls.enable wird verwendet, damit bei der Funktion "Mit dem E-Mail Server
verbinden" beim Einsatz von IMAP auch eine verschlüsselte Verbindung
aufgebaut wird.

Diese Tabelle stellt eine Konfigurationsübersicht für verschiedene Instanzen dar, insbesondere im Kontext der Datei "standalone.conf". Sie enthält Informationen über die Konfiguration von Java-Parametern für unterschiedliche Umgebungen.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Instanz-Name: Gibt den Namen der Instanz an, für die die Konfiguration gilt.
* Parameter: Enthält den Namen des spezifischen Parameters, der konfiguriert wird.
* Wert: Zeigt den Wert an, der dem entsprechenden Parameter zugewiesen wird.

Die Konfigurationen können wie folgt beschrieben werden:
Die Produktiv-Instanz verwendet den Parameter -Xms mit einem Wert von 64G. 
Für die Produktiv-Instanz ist der Parameter -Xmx auf 64G gesetzt. 
Die Produktiv-Instanz hat außerdem den Parameter ReservedCodeCacheSize mit einem Wert von 1024m konfiguriert. 
Die Test/Demo-Instanz verwendet den Parameter -Xms mit einem Wert von 16G. 
Für die Test/Demo-Instanz ist der Parameter -Xmx auf 16G gesetzt.

## standalone.xml

Pfad: /opt/s0ftw4reweb/wildfly/standalone/configuration/standalone.xml

## datasource

Bereich datasource gemäß den folgenden Angaben anpassen:

Diese Tabelle stellt eine Übersicht über verschiedene Datenquellen-Konfigurationen dar, die für unterschiedliche Instanzen wie Produktion, Demo und Test verwendet werden. Sie enthält Informationen über die Verbindungseinstellungen zu Datenbanken.

Die Bedeutung jeder Spalte kann wie folgt beschrieben werden:
* Instanz-Name: Gibt den Namen der Instanz an, für die die Konfiguration gilt.
* Parameter: Definiert den spezifischen Parameter, der konfiguriert wird.
* Wert: Enthält den Wert des jeweiligen Parameters.

Die einzelnen Zeilen können wie folgt beschrieben werden:
Die Produktion verwendet den jndi-name java:/database1. 
Für die Produktion ist der pool-name S0FTW4RE. 
Die Produktion verwendet die connection-url jdbc:oracle:thin:@schwubs097.old.domain.de:1521/s0ftw4re. 
Die Produktion verwendet den driver Oracle. 
Die Produktion verwendet den user-name S0ftw4re. 
Die Produktion verwendet das password Xxxx. 
Die Demo verwendet den jndi-name java:/demo. 
Für die Demo ist der pool-name Demo. 
Die Demo verwendet die connection-url jdbc:oracle:thin:@schwubs098.old.domain.de:1521:demo. 
Die Demo verwendet den driver Oracle. 
Die Demo verwendet den user-name s0ftw4re. 
Die Demo verwendet das password Xxxx. 
Die Test verwendet den jndi-name java:/test. 
Für die Test ist der pool-name TEST. 
Die Test verwendet die connection-url jdbc:oracle:thin:@srvlnx97.old.domain.de:1521/test. 
Die Test verwendet den driver Oracle. 
Die Test verwendet den user-name S0FTW4RE. 
Die Test verwendet das password Xxxx.

Im Bereich datasource wird der folgende Block validation verwendet.

```
<validation>
<valid-connection-checker
class-name=
"org.jboss.jca.adapters.jdbc.extensions.oracle.OracleValidConnectionChecker"
></valid-connection-checker>
<check-valid-connection-sql>
select 1 from dual
</check-valid-connection-sql>
<background-validation>
true
</background-validation>
<stale-connection-checker
class-name=
"org.jboss.jca.adapters.jdbc.extensions.oracle.OracleStaleConnectionChecker"
></stale-connection-checker>
<exception-sorter
class-name=
"org.jboss.jca.adapters.jdbc.extensions.oracle.OracleExceptionSorter"
></exception-sorter>
</validation>
```

## HTTP-Listener

Im Bereich <schwubsystem xmlns="urn:jboss:domain:undertow:10.0"> wird für den Parameter http-listener der Wert max-post-size von 50 MB auf 200 MB erhöht.

```
<http-listener name="default" socket-binding="http" max-post-size="209715200" max-parameters="10000" url-charset="utf-8" enable-http2="false"></http-listener>
#aktuelle standalone Demo
<http-listener name="default" socket-binding="http" redirect-socket="https" enable-http2="false" max-parameters="10000" url-charset="utf-8" max-post-size="209715200"></http-listener>
```

Folgenden https-listener hinzufügen (wenn bereits einer vorhanden ist ggf. deaktivieren):

```
<
https-listener
name
=
"httpsServer"
socket-binding
=
"https"
securityrealm
=
"ApplicationRealm"
max-parameters
=
"10000"
url-charset
=
"utf-8"
max-post-size
=
"209715200"
></
https-listener
>
#aktuelle standalone Demo
<
https-listener
name
=
"httpsServer"
socket-binding
=
"https"
security-realm
=
"ApplicationRealm"
enable-http2
=
"false"
max-parameters
=
"10000"
url-charset
=
"utf-8"
max-post-size
=
"209715200"
></
https-listener
>
```

## Logdateien

Bereich: <schwubsystem xmlns="urn:jboss:domain:logging:8.0"> Hier muss ebenfalls der Loglevel abgeändert werden, damit der logger.level=INFO und andere auf ERROR gesetzt werden kann.:

```
<console-handler
name=
"CONSOLE"
>
<level
name=
"ERROR"
></level>
<formatter>
<named-formatter
name=
"COLOR-PATTERN"
></named-formatter>
</formatter>
</console-handler>
```

Sowie

```
<root-logger>
<level
name=
"ERROR"
></level>
<handlers>
<handler
name=
"CONSOLE"
></handler>
<handler
name=
"FILE"
></handler>
</handlers>
</root-logger>
```

Außerdem
müssen der DAP- und S0ftw4re-Logger angeschaltet werden (alle anderen
können auskommentiert werden. Welche davon für uns auch sinnvoll sein
könnten, kann weiter untersucht werden). Das Loglevel wird so restriktiv
gehandhabt wie oben definiert. Wenn ein höheres Loglevel benötigt wird,
oben anpassen.

```
<logger
category=
"de.s0ftw4re.dapservice"
>
<level
name=
"DEBUG"
></level>
</logger>
<logger
category=
"de.s0ftw4re.system.log"
>
<level
name=
"DEBUG"
></level>
</logger>
```

Für die Log-Rotation den <file-handler> austauschen gegen:

```
<periodic-rotating-file-handler
name=
"FILE"
autoflush=
"true"
>
<formatter>
<named-formatter
name=
"PATTERN"
></named-formatter>
</formatter>
<file
relative-to=
"jboss.server.log.dir"
path=
"server.log"
></file>
<suffix
value=
".yyyy-MM-dd"
></suffix>
<append
value=
"true"
></append>
</periodic-rotating-file-handler>
```

## logback.xml

Diese Datei hat sich zwischen v. 1.90 und 3.0 NICHT verändert und kann beibehalten werden!

unter <!-- Definition des Appender für das Schreiben der Logdateien "server.log" --> den Block ersetzen durch:

```
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
"ch.qos.logback.core.rolling.TimeBasedRollingPolicy"
>
<!-- daily rollover -->
<fileNamePattern>
${JBOSS_HOME}/standalone/log/server.%d{yyyy-MM-dd}.log.zip
</fileNamePattern>
<!-- keep 30 days' worth of history capped at 3GB total size -->
<maxHistory>
30
</maxHistory>
<totalSizeCap>
3GB
</totalSizeCap>
</rollingPolicy>
<triggeringPolicy
class=
"ch.qos.logback.core.rolling.SizeBasedTriggeringPolicy"
>
<maxFileSize>
100MB
</maxFileSize>
</triggeringPolicy>
<encoder>
<pattern>
%d %-5p [%thread] [%c] %m%n
</pattern>
</encoder>
</appender>
```

folgende Logger werden für TEST und für DEMO eingestellt:

```
<logger
name=
"de.s0ftw4re.system.ui.component.demo"
level=
"DEBUG"
></logger>
<!--logger name="org.apache.cxf.services" level="DEBUG"/-->
<logger
name=
"de.s0ftw4re.system.ui"
level=
"DEBUG"
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
<!-- <logger name="org.hibernate.SQL" level="DEBUG" ></logger> -->
<!-- <logger name="org.jboss.as.ee" level="DEBUG"></logger> -->
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

Für PROD werden alle Logger auf ERROR gestellt!

## module.xml (Oracle)

Konfigurationsdatei für den Oracle-Treiber im Wildfly.

Pfad: /opt/s0ftw4reweb/wildfly/modules/com/oracle/main

```
<?xml version="1.0" encoding="UTF-8"?>
<module
xmlns=
"urn:jboss:module:1.9"
name=
"com.oracle"
>
<resources>
<resource-root
path=
"ojdbc8.jar"
></resource-root>
</resources>
<dependencies>
<module
name=
"javax.api"
></module>
<module
name=
"javax.transaction.api"
></module>
</dependencies>
</module>
```

## limits.conf

Steuert die Limits (z.B. Anzahl gleichzeitig geöffneter Dateien) im System.

Pfad: /etc/security/limits.conf

Für den Betriebssystemnutzer s0ftw4re muss die Anzahl der offenen Dateien von 1024 (Standard) auf 8192 erhöht werden.

```
s0ftw4re         soft      nofile           8192
s0ftw4re         hard      nofile           8192
```
