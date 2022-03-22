# Leistungsdiagnostik

Werkzeug zur Vereinfachung und Automatisierung von Leistungstests, basierend auf EKG-Daten und Leistungswerten und Patient:innen-Daten
Mit der Software können die vom Ergometer und vom EKG gespeicherten Daten ausgelesen, gespeichert, ausgewertet und visualisiert werden. Bei Unregelmäßigkeiten oder medizinisch alarmierenden Werten soll ein Alarm ausgelöst werden.
Das Programm soll dabei fließend und möglichst ohne Zeitverzögerung die verarbeiteten Daten auf einem Bildschirm anzeigen.

HINWEIS Julian: Sehr gut. Bei der Entwicklung werden wir uns zunächst auf die Auswertung von bestehenden Daten konzentrieren. Also keine Echtzeit-Alarme nötig.

## Installation

Die Software muss auf einem handelsüblichen PC installiert werden, der über Datenleitungen mit dem Ergometer und dem EKG verbunden ist. Der PC muss keine besonderen Anforderungen erfüllen. Die Installation erfolgt dabei über einen Download aus dem Internet, nach Erwerb der Lizenz.
Eine richtige Verwendung des Ergometers und ein korrektes Kleben der EKG-Elektroden wird vorausgesetzt.

t.b.d.

## Usage

Start über Kommandozeile
```python main.py```

Daten müssen wie wie folgt vorliegen?
Die Daten des Ergometers müssen in einer für die Software kompatiblen Form vorliegen. 
Die Benutzung erfolgt ausschließlich über die Kommandozeile. Bei Beginn der Aufzeichnung wird der Name der Versuchsperson, die technische ID und das Geburtsdatum gespeichert. 
Erfolgreiche und abgebrochene Versuche werden in seperaten Ordnern gespeichert. Wenn ein Abbruchkriterium erreicht wird, gilt dieser Durchlauf als ungültig. Diese Kriterien können nachträglich manuell über die Kommandozeile bearbeitet werden.  

## Contributing

Verena Aichinger 2110881001 av1555@mci4me.at  
Sophie-Isabel Altmann 21100881002 as9765@mci4me.at

## License
[MIT](https://choosealicense.com/licenses/mit/)
