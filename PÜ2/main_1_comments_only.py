# UC 2.0
# importieren der nötigen Pakete (numpy, pandas, matplotlib)

#%% UC 2.1 Einlesen der Daten
# Öffnen der Datei, konvertieren zu numpy-Array und erstellen der Plots innerhalb der For-Schleife.
# Der Dateiname wird durch einen String der unterschiedlichen Dateinummern unterbrochen.

#%% UC 2.2 Vorverarbeiten der Daten 
# Daten die vor Testbeginn oder nach Testende erhoben werden, werden von dem zu bearbeitenden Datensatz entfernt und in einem speraten Ordner gespeichert.
# Störsignale und Rauschen werden behoben.

#%% UC 2.3 Analysieren der Daten auf Abbruchkriterien
# Abbruchkriterien werden festgelegt (Puls 90% der maximalen Herzfrequenz, Herzrythmusstörungen, Nichteinhalten des vorgegebenen Widerstandswertes)
# Daten werden auf diese Kriterien geprüft. 

#%% UC 2.4 Erstellen einer Zusammenfassung
# Die Daten werden durch zuvor festgelegte Kriterien zusammengefasst (durschnittlicher/maximaler Puls, durchschnittliche Leistung, usw.).
# Weiters hat der Diagnostiker durch eine Eingabefunktion die Möglichkeit Anmerkungen hinzuzufügen.

#%% UC 2.5 Visualisierung der Daten
# Die Daten werden in einem Plot entsprechend visualisiert. 
# Durch Diagramme wird der Leistungs- und Pulsverlauf dargestellt.

#%% UC 2.6 Manuelle Eingabe eines Abbruchkriteriums
# Durch die Kommandozeile kann nachträglich ein Abbruchkriterium hinzugefügt werden.
# Dadurch wird der Test auch als abgebrochen gewertet.

#%% UC 2.7 Speichern der Daten
# Es werden zwei seperate Ordner erstellt, in den einen Ordner werden erfolgreiche Testdurchläufe gespeichert.
# NOTE-JHU: Aufpassen beim Programmieren dann. Die Ordner werden nur beim ersten Mal erstellt. 
# In dem anderen werden abgebrochene Durchläufe gespeichert.
# Es werden sowohl die Textdateien, als auch die Plots und Diagramme gespeichert.
