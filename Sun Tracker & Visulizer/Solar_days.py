import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime
import time
import pvlib
import pytz
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D


def get_solar_positions_for_a_day(latitude, longitude, altitude, timezone, start_date):
    if isinstance(start_date, str):
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()

    end_date = start_date + datetime.timedelta(days=10)
    times = pd.date_range(
        start=datetime.datetime(start_date.year, start_date.month, start_date.day, 6, 0, 0,
                               tzinfo=pytz.timezone(timezone)),
        end=datetime.datetime(end_date.year, end_date.month, end_date.day, 23, 59, 59, tzinfo=pytz.timezone(timezone)),
        freq='10T'
    )
    solar_positions = pvlib.solarposition.get_solarposition(
        time=times,
        latitude=latitude,
        longitude=longitude,
        altitude=altitude
    )

    return solar_positions

latitude = 22.30327  # HK纬度
longitude = 114.17933  # HK经度
altitude = 35  # HK海拔
timezone = 'Asia/Hong_Kong'  # 时区
start_date = '2024-06-01'

# Animation parameters
interval = 1  # Interval between frames in milliseconds (0.1 seconds)

# Initialize the figure and 3D axes
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# Set consistent axis limits and labels
ax_limits = (-1, 1)
ax.set_box_aspect((1, 1, 1))
ax.set_xlim3d(ax_limits)
ax.set_ylim3d(ax_limits)
ax.set_zlim3d(0, 1)
ax.set_xlabel('West-East')
ax.set_ylabel('North-South')
ax.set_zlabel('Zenith')
ax.set_title('Solar Position throughout the Day (3D)')
ax.grid(False)

# Add thick, semi-transparent, straight lines for the x, y, and z axes
ax.plot([-1, 1], [0, 0], [0, 0], 'g-', alpha=0.5, linewidth=3, zorder=1)
ax.plot([0, 0], [-1, 1], [0, 0], 'b-', alpha=0.5, linewidth=3, zorder=1)
ax.plot([0, 0], [0, 0], [0, 1], 'r-', alpha=0.5, linewidth=3, zorder=1)

# Initialize the plot elements
sun, = ax.plot([], [], [], 'ro', markersize=10, label='Sun')
azimuth_line, = ax.plot([], [], [], 'b-', linewidth=2, label='Azimuth')
zenith_line, = ax.plot([], [], [], 'g-', linewidth=2, label='Zenith')

# Subplot 2
ax2.set_box_aspect((1, 1, 1))
ax2.set_xlim3d(ax_limits)
ax2.set_ylim3d(ax_limits)
ax2.set_zlim3d(0, 1)
ax2.set_xlabel('West-East')
ax2.set_ylabel('North-South')
ax2.set_zlabel('Zenith')
ax2.set_title('Solar Position throughout the Day (3D)')
ax2.grid(False)

# Add thick, semi-transparent, straight lines for the x, y, and z axes
ax2.plot([-1, 1], [0, 0], [0, 0], 'g-', alpha=0.5, linewidth=3, zorder=1)
ax2.plot([0, 0], [-1, 1], [0, 0], 'b-', alpha=0.5, linewidth=3, zorder=1)
ax2.plot([0, 0], [0, 0], [0, 1], 'r-', alpha=0.5, linewidth=3, zorder=1)

sun_path, = ax2.plot([], [], [], 'g-', linewidth=2, label='Sun Path')
sun_position, = ax2.plot([], [], [], 'ro', markersize=10, label='Sun')


# Animation update function
def update(frame):
    solar_positions = get_solar_positions_for_a_day(latitude, longitude, altitude, timezone, start_date)
    time = solar_positions.index[frame]
    zenith = solar_positions['zenith'].iloc[frame]
    azimuth = solar_positions['azimuth'].iloc[frame]
    x = np.sin(np.radians(zenith)) * np.cos(np.radians(azimuth))
    y = np.sin(np.radians(zenith)) * np.sin(np.radians(azimuth))
    z = np.cos(np.radians(zenith))


    # Update the 3D plot elements
    sun.set_data_3d(x, y, z)
    azimuth_line.set_data_3d([0, x], [0, y], [0, 0])
    zenith_line.set_data_3d([0, x], [0, y], [0, z])

    # Update the 3D plot element
    sun_position.set_data_3d(x, y, z)

    if frame == 0:
        # For the first frame, set the initial data for the sun_path
        sun_path.set_data_3d([x], [y], [z])
        x, y, z = sun_path.get_data_3d()
        print("get Z data: ", z)
    else:
        x_data, y_data, z_data = sun_path.get_data_3d()
        x_data = np.append(x_data, x)
        # print(x_data)
        y_data = np.append(y_data, y)
        # print(y_data)
        z_data = np.append(z_data, z)
        # print(z_data)
        sun_path.set_data_3d(x_data, y_data, z_data)
        # print(sun_path.get_xdata)

    print(f"Time: {time.strftime('%H:%M:%S')}, Solar Zenith Angle: {zenith:.2f} degrees, Solar Azimuth Angle: {azimuth:.2f} degrees")
    print('-' * 40)
    return sun, azimuth_line, zenith_line, sun_path, sun_position

# Create the animation
num_frames = len(get_solar_positions_for_a_day(latitude, longitude, altitude, timezone, start_date))
ani = FuncAnimation(fig, update, frames=num_frames, interval=interval, blit=True)

# Save the solar position data to a CSV file
# solar_positions = get_solar_positions_for_a_day(latitude, longitude, altitude, timezone, start_date)
# solar_positions.to_csv('solar_positions.csv')

# Display the animation
ax.legend()
ax2.legend()
plt.show()