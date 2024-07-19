# SolarTracker2
The 2nd version of Solar Tracker Project

For previous version, please also refer to [SolarTracker](https://github.com/ValenQiu/SolarTracker)

## Contents
This repository includes:
- Controller of the Pan-Tilt-Zoom (PTZ)
- A tracker and visualizer based on pvlib that updates the sun angle in real time
- A user friendly GUI with various functions

## How to use
To use this Solar Tracker, please download the codes in [here](/main) and run the `main.py`.

For further details, please refer to: [GUI Guildline](), [How to Connect]()

## Technical Information
### Coordinate Statement
The coordinate in this project is shown in the figure below. Which the Solar Zenith angle (Tile Angle for PTZ) is the angle between the local zenith axis and the line of sight, and the Solar Azimuth (Pan Angle for PTZ) is the angle between the north oriented axis and the plane along the horizon.

<p align="center">
  <img width="60%" src="/media/coordinate.PNG" alt="Coordinate">
</p>

### PTZ Controller
The PTZ follows the Pelco-D communication protocol, detail information can be found from the [Pelco-D tutorial](https://www.commfront.com/pages/pelco-d-protocol-tutorial), [Pelco-D protocol command list](https://www.epiphan.com/userguides/LUMiO12x/Content/UserGuides/PTZ/3-operation/PELCODcommands.htm), [Pelco Support Community](https://support.pelco.com/s/article/How-to-Troubleshoot-PTZ-Control-Issues-1538586696855?language=en_US).

This project provides a custom PTZ controller class that enables communication with a PTZ device using Python. The class handles the encoding and decoding of commands and responses to/from the PTZ unit. For more detailed information, please refer to [here](https://github.com/ValenQiu/SolarTracker2/tree/main/PTZ%20Control).

### Sun Angle Tracker & Visualizer
The Sun Angle Tracker & Visualizer is based on `pvlib`. It can update the sun's zenith and azimuth angle (and some other information as well). Besides, this project also provide a visulizer tool for visulizing the angle, as well as showing the sun path in a period of time. For more information, please refer to [here](https://github.com/ValenQiu/SolarTracker2/tree/main/Sun%20Tracker%20%26%20Visualizer).

<p align="center">
  <img width = "60%" src="/media/visualizer.gif" alt="visualizer">
</p>

### GUI
The custom GUI for this projectis a user friendly interface with various functions. This GUI is developed based on `tkinter`. For more information, please refer to [here](https://github.com/ValenQiu/SolarTracker2/tree/main/GUI).

<p align="center">
  <img width = "60%" src="/media/GUI.PNG" alt="GUI">
</p>

## Contact
If you have encounter or interested in contributing, please contat the author [Valen Qiu](https://github.com/ValenQiu) and our labs ([REALab](https://www.li-realab.info/), [Romi-Lab](https://www.romi-lab.org/)), or submit a pull request on GitHub.







