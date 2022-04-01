## Project background

### Purpose of project

Es soll eine Software zur Leistungsdiagnostik erstellt werden, welche auf den Daten eines Ergometers und eines EKGs basiert. Die Daten werden eingelesen, verarbeitet und visualisiert. Dabei wird laufend auf Abbruchkriterien geprüft. Nach Beendigung eines Durchlaufs werden die verarbeiteten Daten gespeichert. Der Speicherort ist abhängig vom Erfolg des Tests.

### Scope of project

Diese Software wird vorerst als Proof-Of-Concept geschrieben, welche die Daten ausliest, auswertet und visualisiert.

### Other background information

Abbruchkriterien werden wie folgt definiert:
* Puls 90% der maximalen Herzfrequenz
* Herzrythmusstörungen
* Nichteinhalten des vorgegeben Widerstandswertes
Weiters können die Abbruchkriterien nachträglich manuell bearbeitet werden. 

## Perspectives
### Who will use the system?

Diagnostiker:innen, die Leistungstests an Sportler:innen durchführen. 

### Who can provide input about the system?

Der Input wird von einem Probanden:in erzeugt und von einem EKG und einem Ergometer aufgezeichnet.

NOTE-JHU: Hier geht es eher darum, bei wem man zusätzlich Information über das System abholen kann ;) Bei mir zum Beispiel.


## Project Objectives
### Known business rules

Das EKG sowie der Ergometer müssen funktionstüchtig sein und davor entsprechend überprüft werden. Die Elektroden des EKGs müssen fachgerecht angebracht sein. 
Der Widerstand muss entsprechend eingestellt werden.
Der Proband:in muss vor der Durchführung über Risiken aufgeklärt werden und darf keine Konterindikationen erfüllen. 
Vor Beginn des Tests müssen die personenbezogenen Daten (Name, technische ID, Geburtsdatum) in die Kommandozeile eingegeben werden. Diese werden unter Einhaltung der DSGVO abgespeichert.

### System information and/or diagrams

Beispiel von aufgezeichneten EKG Daten
![](ekg_example.png)

Aus diesem muss die Herzrate bestimmt werden.

### Assumptions and dependencies
* Die Dateien ecg_data_subject enthalten die vom EKG aufgezeichneten Daten, sowie einen Index und sind als CSV-Dateien abgespeichert. 
* Die Dateien power_data enthalten die während des Leistungstests erzeugten Watt und sind in einer Textdatei abgespeichert.
* Die Dateien subject enthalten Informationen zu den Testpersonen. Darin ist die Subject-ID, die erzeugten Watt während des Tests, das Geburtsjahr sowie die Testdauer gespeichert. Die Informationen sind als json-Datei gespeichert. 

NOTE-JHU: Datenbeschreibung für Aufgabe 2.1 könnte noch genauer sein (Auflösung, Inhalt) - bin ich hier in der falschen Datei? 


### Design and implementation constraints

Die Benutzeroberfläche besteht vorerst nur aus einer Kommandozeile und einem Plot zur Visualisierung der Daten. Entsprechende Änderungen können in zukünftigen Versionen noch vorgenommen werden. 

## Risks

Für medizinische Notfälle während des Leistungstests wird keine Haftung übernommen. Die Software soll die frühzeitige Erkennung solcher Notfälle lediglich unterstützen. Die medizinische Verantwortung trägt eine anwesende Fachkraft.

Wird ein Abbruchkritterium erfüllt und von der Testleitung ignoriert, können folgende Risiken eintreten: 
* cardiale und pulmonale Notfälle bis hin zum Atem-Kreislaufstillstand, infolge von Herzfrequenzen die über 90% des maximalen Puls reichen
* Herzrythmusstörungen aufgrund von Überschreitung der Belastungsgrenze.
* Übelkeit und Erbrechen nach Überanstrengung
* Dehydrierung 

NOTE-JHU: Hier geht es vorallem auch um die Risiken bei der technischen Entwicklung. Z.B. wenn die Daten nicht zuverlässig erzeugt werdne würden o.ä.

## Known future enhancements

In Zukunft soll die Benutzeroberfläche angepasst werden, um die Usability zu verbessern. Weiters kann ein neues Tool eingebaut werden, welches das Vergleichen von verschiedenen Probanden:innen ermöglicht. In Zukunft soll die Applikation dahingehend verbessert, dass die Software auch auf mobilen Endgeräten verwendbar ist (z.B: Smartphone-App).

## References

- [Link zur Aufgabenstellung](tbd)

## Open, unresolved or TBD issues

siehe known future enhancements
t.b.d.
