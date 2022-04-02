# UC 2.0

#%% UC 2.1 Einlesen der Daten

##Erstellen einer leeren Liste in der später die Dateien der zu bearbeitenden Tests gespeichert werden.
list_of_new_tests = []
## Überprüfen ob Dateien vorhanden sind

## Importieren der nötigen Pakete.
import os
import pandas as pd

## Zuerst wird der Ordner der Dateien aufgerufen, dann werden die Dateien in diesem Ordner auf die Endung ".csv" überprüft.
##Die Dateien mit der ".csv"-Endung werden ausgelesen und anschließend zur leeren Liste "list_of_new_tests" hinzugefügt.
folder_current = os.path.dirname(__file__) 
folder_input_data = os.path.join(folder_current, 'input_data')
for file in os.listdir(folder_input_data):
    
    if file.endswith(".csv"):
        file_name = os.path.join(folder_input_data, file)
        print(file_name)
        subject_id = file_name.split(".")[0][-1]
        new_ecg_data= pd.read_csv(file_name)
## Erstellen einer Liste von Tests, die zu verarbeiten sind

        list_of_new_tests.append(new_ecg_data)


new_ecg_data["Subject_3"].plot()

#%% UC 2.2 Vorverarbeiten der Daten

## Anlegen einer Zeitreihe der Herzfrequenz aus den EKG-Daten
## Aus den ausgelesenen Dateien werden die Daten des Subjects 3 herangezogen, um dann die Peaks zu finden.
## Die gesamten Peaks werden aufsummiert, um somit die insgesamte Summe der Herzschläge herauszufinden.
## Die Anzahl der durchschnittlichen Herzschläge pro Minute wird ermittelt.
import neurokit2 as nk

ekg_data=pd.DataFrame()
ekg_data["ECG"] = new_ecg_data["Subject_3"]


def find_average_hr(__file__):
    """Berechnet die durchschnittliche Herzfrequenz:
    die Peaks der EKG-Daten werden gesucht und ihr durchschnittlicher Wert wird berechnet
    die Funktion gibt peaks und average_hr_test zurück """
# Find peaks
    global peaks
    peaks, info = nk.ecg_peaks(__file__, sampling_rate=1000)

    number_of_heartbeats = peaks["ECG_R_Peaks"].sum()

    duration_test_min = __file__.size/1000/60
    
    global average_hr_test
    average_hr_test = number_of_heartbeats / duration_test_min

## Calculate heart rate moving average

    peaks['average_HR_10s'] = peaks.rolling(window=10000).mean()*60*1000
    peaks['average_HR_10s'].plot()
    return peaks['average_HR_10s'], average_hr_test

find_average_hr(ekg_data['ECG'])

#%% UC 2.3 Analysieren der Daten auf Abbruch-Kriterium

## Erstellen der Variablen termination als boolean.
termination = False

## Vergleich der Maximalen Herzfrequenz mit Alter des Patienten

folder_input_data = os.path.join(folder_current, 'input_data')

import json

## Das Alter des Patienten wird aus der JSON Datei ausgelesen
# Opening JSON file

file_name = folder_input_data = os.path.join(folder_input_data, 'subject_3.json')

f = open(file_name)
 
# returns JSON object as
# a dictionary
subject_data = json.load(f)

## Das Abbruchkriterium (Puls > 90% der maximalen Herzfrequenz) wird geprüft. 
## Sollte das Kriterium erfüllt sein, wird termination als true festgelegt. 

maximum_hr = peaks['average_HR_10s'].max()

subject_max_hr = 220 - (2022 - subject_data["birth_year"])

if maximum_hr > subject_max_hr*0.90:
    termination = True

#%% UC 2.4 Erstellen einer Zusammenfassung

## Für die Zusammenfassung werden verarbeiteten Daten aus den vorherigen Use Cases herangezogen.
## Die Ergebnisse werden als string ausgegeben.  

print("Summary for Subject " + str(subject_data["subject_id"]))
print("Year of birth:  " + str(subject_data["birth_year"]))
print("Test level power in W:  " + str(subject_data["test_power_w"]))
print(" \n")
print("Maximum HR was: " + str(maximum_hr))
print("Was test terminated because exceeding HR " + str(termination))

## Ausgabe einer Zusammenfassung

#%% UC 2.5 Visualisierung der Daten

## Zur Visualisierung der Daten werden zunächst die Leistungsdaten aus den txt Datein ausgelesen. 
## Öffnen der Leistungsdaten

# Opening txt file
folder_input_data = os.path.join(folder_current, 'input_data')
file_name =  os.path.join(folder_input_data, 'power_data_3.txt')
power_data_watts = open(file_name).read().split("\n")
power_data_watts.pop(-1)
len(power_data_watts)


# %%
## Erstellung eines Plots

## Der Verlauf der Herzfrequenz und die Leistung des Patienten werden in einem gemeinsamn Plot abgebildet.
## Dazu werden die HR-Daten so manipuliert, dass sie etwa gleich viele Daten wie die power_data Dateien beinhalten.
## Anschließend wird das Diagramm mit der funktion .plot erstellt. 

#peaks['average_HR_10s'].plot()

peaks_downsampled = peaks[peaks.index % 1000 == 0]  

peaks_downsampled = peaks_downsampled.reset_index(drop=True)
peaks_downsampled = peaks_downsampled.drop(["ECG_R_Peaks"],axis=1)
peaks_downsampled


peaks_downsampled["Power (Watt)"] = pd.to_numeric(power_data_watts)
#peaks_downsampled["Power (Watt)"] = peaks_downsampled["Power (Watt)"]
peaks_downsampled.plot()

#peaks_downsampled["Power (Watt)"].plot()

#%% UC 2.6 Manuelle Eingabe eines Abbruchkritierums

## Abfrage an Nutzer:in, ob Abgebrochen werden soll
## Der Diagnostiker*in wird über die Kommandozeile gefragt ob der Test als invalide gezählt werden soll. 
## Sollte etwas eingegeben werden, wird für die Variable termination der Wert True abgespeichert. 

manual_termination = False
manual_termination = input("Is this test invalid? (leave blank if valid): ")

if manual_termination != False:
    termination = True


#%% UC 2.7 Speichern der Daten


# Speichern der Daten
## Festgelegte Informationen (ID, Terminationsgrund, durchschnittlicher Puls, maximaler Puls, Testdauer, Leistung, durschnittliche Leistung) werden in einem json-Dokument im Ordner result_data gespeichert.

data = {"User ID": subject_data["subject_id"], "Reason for test termation": manual_termination, "Average Heart Rate": average_hr_test, "Maximum Heart Rate": subject_max_hr, "Test Length (s)": len(power_data_watts), "Test Power (W)": subject_data["test_power_w"], "Average Power": peaks_downsampled["Power (Watt)"].mean()}

json_data_to_save = json.dumps(data)

folder_current = os.path.dirname(__file__) 
folder_input_data = os.path.join(folder_current, 'result_data')
results_file = os.path.join(folder_input_data, 'data.json')

with open(results_file, 'w', encoding='utf-8') as f:
    json.dump(json_data_to_save, f, ensure_ascii=False, indent=4)

# %%
