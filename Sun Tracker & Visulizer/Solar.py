import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime
import time
import pvlib
import pytz
from mpl_toolkits.mplot3d import Axes3D

def get_solar_position(latitude, longitude, altitude, timezone):
    now = datetime.datetime.now(pytz.timezone(timezone))
    solar_position = pvlib.solarposition.get_solarposition(
        time=now,
        latitude=latitude,
        longitude=longitude,
        altitude=altitude
    )
    zenith = solar_position['zenith'].values[0]
    azimuth = solar_position['azimuth'].values[0]
    return zenith, azimuth

latitude = 22.30327  # HK纬度
longitude = 114.17933  # HK经度
altitude = 35 # HK海拔
timezone = 'Asia/Hong_Kong' # 时区

# Animation parameters
num_frames = 5
interval = 100  # Interval between frames in milliseconds

# Initialize the figure and 3D axes
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Show the positive and negative x-y-z axes and hide the grips
ax.set_box_aspect((1, 1, 1))
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(0, 1)
ax.set_xlabel('West-East')
ax.set_ylabel('North-South')
ax.set_zlabel('Zenith')
ax.set_title('Solar Position')
ax.grid(False)

# Add thick, semi-transparent, straight lines for the x, y, and z axes
ax.plot([-1, 1], [0, 0], [0, 0], 'g-', alpha=0.5, linewidth=3, zorder=1)
ax.plot([0, 0], [-1, 1], [0, 0], 'b-', alpha=0.5, linewidth=3, zorder=1)
ax.plot([0, 0], [0, 0], [0, 1], 'r-', alpha=0.5, linewidth=3, zorder=1)

# Initialize the plot elements
sun, = ax.plot([], [], [], 'ro', markersize=10, label='Sun')
azimuth_line, = ax.plot([], [], [], 'b-', linewidth=2, label='Azimuth')
zenith_line, = ax.plot([], [], [], 'g-', linewidth=2, label='Zenith')

# Animation update function
def update(frame):
    zenith, azimuth = get_solar_position(latitude, longitude, altitude, timezone)
    x = np.sin(np.radians(zenith)) * np.cos(np.radians(azimuth))
    y = np.sin(np.radians(zenith)) * np.sin(np.radians(azimuth))
    z = np.cos(np.radians(zenith))
    sun.set_data_3d(x, y, z)
    azimuth_line.set_data_3d([0, x], [0, y], [0, 0])
    zenith_line.set_data_3d([0, x], [0, y], [0, z])
    print(f"Solar Zenith Angle: {zenith:.2f} degrees")
    print(f"Solar Azimuth Angle: {azimuth:.2f} degrees")
    print('-' * 40)
    return sun, azimuth_line, zenith_line

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=interval, blit=True)

# Display the animation
ax.legend()
plt.show()