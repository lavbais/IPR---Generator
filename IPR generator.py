import numpy as np
import matplotlib.pyplot as g1

#Required Data
Q_IPR=250 #Stabilized Flow Rate
Pwf_IPR=2500 #Recorded Flowing Bottom_hole Pressure
Pr=3000 #Reservoir Pressure
Pb=2130 #Bubble Point Pressure
Qo_max = Q_IPR/(1 - 0.2*(Pwf_IPR/Pr) - 0.8*(Pwf_IPR/Pr)**2)
