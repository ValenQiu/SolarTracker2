# Tutorial

## 1. Download & Initialization
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

## 2. Connect to PTZ
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
  <img width="60%" src="/media/tutorial_connection_1.png" alt="tutorial_connection_1">
</p>

For Linux, is it shown as:
<p align="center">
  <img width="60%" src="/media/tutorial_connection_2.png" alt="tutorial_connection_2">
</p>

After confirming the port name, you can comment it as you wish.

Consider to the ease of use, there is default value of the port name in the GUI, which is shown below:
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


