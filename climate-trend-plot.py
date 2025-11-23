import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data/global-temp.csv')


plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Temperature_Anomaly'], marker='o', color='tomato', linewidth=2)

# Personalizo el grafico
plt.title('Tendencia de la temperatura global (2013–2025)', fontsize=14)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Anomalía de temperatura (°C)', fontsize=12)
plt.grid(True)


plt.savefig('global-temperature-trend.png')

plt.show()
