# Tutorial

## 1. Download
You can clone all the code in this repository by using this code:
```
git clone https://github.com/ValenQiu/SolarTracker2.git
```
The project relies on the following Python libraries and their versions (tested):
```
- numpy==1.21.6
- pandas==1.3.5
- matplotlib==3.5.3
- pvlib==0.10.4
- pynput==1.7.7
- tk==0.1.0
- pyserial>=3.5
```
As well as all supports from the `pvlib`.

## 2. Initialization & Connect to PTZ
Run the main function ([here](/main/main.py)), and you will see the following information:

(From the python terminal) It will scan all available COM ports in the device, and print out. 
The code is located in [here](https://github.com/ValenQiu/SolarTracker2/blob/d46249ba567d52d24c70583080022112b846cabb/main/PTZ.py#L23).
```python
import sys
import serial

...

ports_list = list(serial.tools.list_ports.comports())  # 获取所有串口设备实例
if len(ports_list) <= 0:
    print("无可用的串口设备！")
else:
    print("可用的串口设备如下：")
    for port in ports_list:  # 依次输出每个设备对应的串口号和描述信息
        print(list(port)[0], list(port)[1])
```
It is recommended to use this function for the first time.
It is shown as below:

<p align="center">
  <img width="80%" src="/media/tutorial_connection_1.png" alt="tutorial_connection_1">
</p>

For Linux, is it shown as:
<p align="center">
  <img width="60%" src="/media/tutorial_connection_2.png" alt="tutorial_connection_2">
</p>

After confirming the port name, you can comment it as you wish.

Consider to the ease of use, there is default value of the port name and baud rate (which is 2400 for this PTZ) in the GUI, which is shown below:
<p align="center">
  <img width="60%" src="/media/tutorial_connection_3.png" alt="tutorial_connection_3">
</p>

It is recommended to change the default port name to the actual port name of the PTZ (could be different for different devices).
To do that, please go to [here](https://github.com/ValenQiu/SolarTracker2/blob/f29d7647d813f0f2adcce7b27a252718cbb46446/main/GUI.py#L19)
to edit the `default_port_name` string into your actual port name.

Windows:
```python
default_port_name = 'COM3'
```
Linux:
```python
default_port_name = '/dev/ttyUSB0'
```

Besides, at this moment, the GUI has not yet connected to the PTZ, thus all functions are disabled. 
By clicking the `Connect` button, if the port name and baud rate are correct (normal just need to confirm the port name), 
your device will connect to the PTZ, and enable all functions (as shwon below).

<p align="center">
  <img width="60%" src="/media/tutorial_connection_success.png" alt="tutorial_connection_success">
</p>

Otherwise, a message box will pop up and show the error message:

<p align="center">
  <img width="60%" src="/media/tutorial_connection_fail.png" alt="tutorial_connection_fail">
</p>

## 3. Control the PTZ

The control program of the PTZ follows the Pelco-D protocol, more information can be found here:
[Pelco-D tutorial](https://www.commfront.com/pages/pelco-d-protocol-tutorial), [Pelco-D protocol command list](https://www.epiphan.com/userguides/LUMiO12x/Content/UserGuides/PTZ/3-operation/PELCODcommands.htm), [Pelco Support Community](https://support.pelco.com/s/article/How-to-Troubleshoot-PTZ-Control-Issues-1538586696855?language=en_US).

### Quick guideline of the Pelco-D Protocol
The Pelco-D protocol is a communication standard for PTZ. There are 7 Bytes of hexadecimal bytes, 
the format of the Pelco-D is defined as:

| Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 | Byte 7 |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Sync  | Camera Address  | Command 1  | Command 2  | Data 1 | Data 2 | Check Sum |

- Byte 1 (Sync) - the synchronization byte, fixed to FF
- Byte 2 (Camera Address) - logical address of the camera being controlled (Address 1 is 01)
- Byte 3 & 4 (Command 1 and 2) are shown below
- Byte 5 (Data 1) - pan speed, range from 00 (stop) to 3F (high speed) and FF for "turbo" speed (the maximum pan speed that the device can go)
- Byte 6 (Data 2) - tilt speed, range from 00 (stop) to 3F (maximum speed)
- Byte 7 (Checksum) - sum of bytes (excluding the synchronization byte), then modulo 100 (Decimal code: 256)

For detailed information of how to use this protocol to control the PTZ, as well as the PTZ library for this project, 
please refer to [here](https://github.com/ValenQiu/SolarTracker2/tree/main/PTZ%20Control).
