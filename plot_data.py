import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv('testdata.csv', sep='\t')

# Plot the data
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 8))
fig.suptitle('Sensor Data Over Time')

# Plot Temperature
axes[0, 0].plot(df['time (source1)'], df['temperature'], label='Temperature')
axes[0, 0].set_title('Temperature')
axes[0, 0].set_xlabel('Time')
axes[0, 0].set_ylabel('Temperature')

# Plot Compass
axes[0, 1].plot(df['time (source1)'], df['compass'], label='Compass')
axes[0, 1].set_title('Compass')
axes[0, 1].set_xlabel('Time')
axes[0, 1].set_ylabel('Compass')

# Plot Rotation Pitch
axes[1, 0].plot(df['time (source1)'], df['rotation_pitch'], label='Rotation Pitch')
axes[1, 0].set_title('Rotation Pitch')
axes[1, 0].set_xlabel('Time')
axes[1, 0].set_ylabel('Rotation Pitch')

# Plot Rotation Roll
axes[1, 1].plot(df['time (source1)'], df['rotation_roll'], label='Rotation Roll')
axes[1, 1].set_title('Rotation Roll')
axes[1, 1].set_xlabel('Time')
axes[1, 1].set_ylabel('Rotation Roll')

# Plot Acceleration X, Y, Z
axes[2, 0].plot(df['time (source1)'], df['acceleration_x'], label='Acceleration X')
axes[2, 0].plot(df['time (source1)'], df['acceleration_y'], label='Acceleration Y')
axes[2, 0].plot(df['time (source1)'], df['acceleration_z'], label='Acceleration Z')
axes[2, 0].set_title('Acceleration X, Y, Z')
axes[2, 0].set_xlabel('Time')
axes[2, 0].set_ylabel('Acceleration')

# Plot Acceleration Strength
axes[2, 1].plot(df['time (source1)'], df['acceleration_strength'], label='Acceleration Strength')
axes[2, 1].set_title('Acceleration Strength')
axes[2, 1].set_xlabel('Time')
axes[2, 1].set_ylabel('Acceleration Strength')

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the plot
plt.show()
