# %% Import der nötigen Pakete
import numpy as np
import matplotlib.pyplot as plt

# %% Öffnen der Datei, konvertieren zu numpy-Array und erstellen der Plots innerhalb der For-Schleife.
# Der Dateiname wird durch einen String der unterschiedlichen Dateinummern unterbrochen.
for i in range(1,4):
    file_name =  'input_data/power_data_' + str(i) + '.txt'
    power_data_watts = open(file_name).read().split("\n")
    x = np.array(power_data_watts)
    plt.title("Leistungsdaten in Watt"+str(i))
    plt.plot(x, color="red")
    plt.show()




# %%

# %%
