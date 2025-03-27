import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read the CSV file
df = pd.read_csv('history.csv')

# Clean up column names by removing extra quotes and spaces
df.columns = [col.strip().replace('"', '') for col in df.columns]

"Time_Iter","Outer_Iter","Inner_Iter",    "rms[Rho]"    ,    "rms[RhoU]"   ,    "rms[RhoV]"   ,    "rms[RhoE]"   ,     "rms[k]"     ,     "rms[w]" 
# Extract relevant data
rms_r = df['rms[Rho]']
rms_ru = df['rms[RhoU]']
rms_rv = df['rms[RhoV]']
rms_re = df['rms[RhoE]']
#rms_k = df['rms[k]']
#rms_w = df['rms[w]']

# Create figure for RMS residuals
plt.figure(figsize=(12, 8))
plt.plot(rms_r, label=r'$\rho$')
plt.plot(rms_ru, label=r'$\rho_U$')
plt.plot(rms_rv, label=r'$\rho_V$')
plt.plot(rms_re, label=r'$\rho_E$')
#plt.plot(rms_k, label='TKE (k)')
#plt.plot(rms_w, label=r'Specific Dissipation ($\omega$)')
plt.xlabel('Iteration', fontsize=12)
plt.ylabel('Residual (RMS)', fontsize=12)
plt.title('Convergence History - RMS Residuals', fontsize=14)
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('rms_residuals.png', dpi=300)
plt.show()
