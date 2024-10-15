import pandas as pd
import matplotlib.pyplot as plt

# Reading the CSV file
file_path = "readings.csv"
data = pd.read_csv(file_path)

# Convert the 'Time' column to datetime format
data['Time'] = pd.to_datetime(data['Time'])

serial_number = '06290bc9-3453-4958-9a2b-3c29562528df' # Device Serial number for Lights
filtered_data = data[data['Serial Number'] == serial_number]

# Plot the time series
plt.figure(figsize=(10, 10))
plt.plot(filtered_data['Time'], filtered_data['Reading'], label='Lights Power Consumption [kW]', color='blue')

# Labeling the plot
plt.title('Time Series of Lights Power Consumption')
plt.xlabel('Date-Time')
plt.ylabel('Lights Power Consumption')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.show()

# Calculate the sum for the total Energy Consumption for the entire business

total_energy = data['Reading'].sum().round(2) # Rounding to 2 significant digits
print(f'Total Energy Consumption: {total_energy} kW')

