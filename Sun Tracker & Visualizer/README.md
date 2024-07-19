
# Sun Tracker & Visualizer

This is a useful Python package for tracking and visualizing the sun angle (zenith and azimuth, and other data as well) based on the `pvlib`.

## Package Introduction
In this package, there are two codes in this folder, which is the [Solar.py](Solar.py) and the [Solar_days.py](Solar_days.py).

The `Solar.py` will update the current sun angles in an interval, and visualize the zenith and azimuth in to a 3D plot.

The `Solar_days.py` can extract the sun data in a period of time, and play the animation of the sun's path in the 3D plot. Detail sun information can be found in the [solar_positions.csv](solar_positions.csv).

## How to use
### Real-Time Solar Angle Updating & Visualizing

The code [Solar.py](Solar.py) is a Real-Time Solar Angle Updating & Visualizing is as shown in the figure below.

<p align="center">
  <img width = "30%" src="/media/Solar_realtime.png" alt="Solar_realtime">
</p>

To use this function, please first check the geographical location information, including latitude, longitude, altitude and timezone of your area, which in the code
we provide, as we are locating in Hong Kong, it is defined as:
```Python
latitude = 22.30327  # HK纬度
longitude = 114.17933  # HK经度
altitude = 35 # HK海拔
timezone = 'Asia/Hong_Kong' # 时区
```

After editing these parameters, you can run and use the visualizer. In default, this the visualizer will update the information in every 100ms.
You can also edit the updating rate as desired.

```python
interval = 100  # Interval between frames in milliseconds
```

### Solar Path Visualizer
The code [Solar_days.py](Solar_days.py) provides a visualizer for displaying the sun's path in a period of time in an animation.
The path is as the animation shown below.

<p align="center">
  <img width = "60%" src="/media/visualizer.gif" alt="visualizer">
</p>

To use this, please also follow the previous step to set the geographical location information. The speed of the animation can also be costumed by editing the interval between frames.

The start day and the number of days (the period of sun path you want to visualize) can be defined as:
```python
start_date = '2024-06-01'
timedelta = datetime.timedelta(days=10)
```

