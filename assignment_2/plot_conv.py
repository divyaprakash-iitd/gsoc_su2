import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read the CSV file
df = pd.read_csv('history.csv')

# Clean up column names by removing extra quotes and spaces
df.columns = [col.strip().replace('"', '') for col in df.columns]

# Extract relevant data
rms_p = df['rms[P]']
rms_u = df['rms[U]']
rms_v = df['rms[V]']
rms_k = df['rms[k]']
rms_w = df['rms[w]']
lin_sol_res = df['LinSolRes']
lin_sol_res_turb = df['LinSolResTurb']
avg_total_press = df['Avg_TotalPress']

# Create figure for RMS residuals
plt.figure(figsize=(12, 8))
plt.plot(rms_p, label='Pressure')
plt.plot(rms_u, label='Velocity-X')
plt.plot(rms_v, label='Velocity-Y')
plt.plot(rms_k, label='TKE (k)')
plt.plot(rms_w, label=r'Specific Dissipation ($\omega$)')
plt.xlabel('Iteration', fontsize=12)
plt.ylabel('Residual (RMS)', fontsize=12)
plt.title('Convergence History - RMS Residuals', fontsize=14)
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('rms_residuals.png', dpi=300)
plt.show()
