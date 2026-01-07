import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("weather_data.csv")


df['date'] = pd.to_datetime(df['date'])


df['month'] = df['date'].dt.month


#   Temperature Trend Over Time

plt.figure()
plt.plot(df['date'], df['temperature_c'])
plt.title("Temperature Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.show()


#   Seasonal Average Temperature

seasonal_temp = df.groupby('month')['temperature_c'].mean()

plt.figure()
seasonal_temp.plot(kind='bar')
plt.title("Seasonal Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.show()

 # Rainfall Distribution

plt.figure()
sns.histplot(df['rainfall_mm'], bins=20)
plt.title("Rainfall Distribution")
plt.xlabel("Rainfall (mm)")
plt.show()


# Extreme Weather Conditions

extreme_temp = df[df['temperature_c'] > 38]
extreme_rain = df[df['rainfall_mm'] > 15]

print("Extreme Temperature Days:", extreme_temp.shape[0])
print("Extreme Rainfall Days:", extreme_rain.shape[0])
