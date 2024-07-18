# SolarTracker2
The 2nd version of Solar Tracker Project

This is the repository for the project. 

For previous version, please also refer to [SolarTracker](https://github.com/ValenQiu/SolarTracker)

## Contents
This repository includes:
- Controller of the Pan-Tilt-Zoom (PTZ)
- A user friendly GUI with various functions
- A tracker and visualizer based on pvlib that updates the sun angle in real time

## Coordinate Statement
The coordinate in this project is shown in the figure below. Which the Solar Zenith angle (Tile Angle for PTZ) is the angle between the local zenith axis and the line of sight, and the Solar Azimuth (Pan Angle for PTZ) is the angle between the north oriented axis and the plane along the horizon.

<p align="center">
  <img src="/img/coordinate.PNG" alt="Coordinate">
</p>

## PTZ Controller
The PTZ follows the Pelco-D communication protocol, detail information can be found from the [Pelco-D tutorial](https://www.commfront.com/pages/pelco-d-protocol-tutorial), [Pelco-D protocol command list](https://www.epiphan.com/userguides/LUMiO12x/Content/UserGuides/PTZ/3-operation/PELCODcommands.htm), [Pelco Support Community](https://support.pelco.com/s/article/How-to-Troubleshoot-PTZ-Control-Issues-1538586696855?language=en_US).

This project provides a custom PTZ controller class that enables communication with a PTZ device using Python. The class handles the encoding and decoding of commands and responses to/from the PTZ unit. For more detailed information, please refer to [here]().

##





