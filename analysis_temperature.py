import pandas as pd 
import matplotlib.pyplot as plt 

#reading data
df = pd.read_csv('temperatures.csv', sep=',', header=None, names=["timestamp", "temperature"])
print("\n raw data:")
print(df)

#cleaning invalid values
df['temperature'] = pd.to_numeric(df['temperature'], errors= 'coerce')
df = df.dropna()

#basic statistics
print("\n statistics:")
print("Average", df['temperature'].mean())
print("Maximum:", df['temperature'].max())
print("Minimum:", df['temperature'].min())

#identify alerts (temperature > 85)
alerts = df[df['temperature'] > 85]
print("\n high temperatures:")
print(alerts)

#generate chart
plt.plot(df['timestamp'], df['temperature'], marker='o')
plt.xticks(rotation=45)
plt.axhline(y=85, color='red', linestyle='--', label='safe limit')
plt.title("Temperature over time")
plt.xlabel("Time")
plt.ylabel("Temperature (ºC)")
plt.legend()
plt.tight_layout()
plt.show()