
# PTZ Control

The control program of the PTZ follows the Pelco-D protocol, more information can be found here:
[Pelco-D tutorial](https://www.commfront.com/pages/pelco-d-protocol-tutorial), [Pelco-D protocol command list](https://www.epiphan.com/userguides/LUMiO12x/Content/UserGuides/PTZ/3-operation/PELCODcommands.htm), [Pelco Support Community](https://support.pelco.com/s/article/How-to-Troubleshoot-PTZ-Control-Issues-1538586696855?language=en_US).

## 1. Pelco-D Protocol

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

### List of Commands
Here is a list of those commonly used commands:

| Function | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 | Byte 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Up | 0xFF | Address | 0x00 | 0x08 | Pan Speed | Tilt Speed | SUM |
| Down | 0xFF | Address | 0x00 | 0x10 | Pan Speed | Tilt Speed | SUM |
| Left | 0xFF | Address | 0x00 | 0x04 | Pan Speed | Tilt Speed | SUM |
| Right | 0xFF | Address | 0x00 | 0x02 | Pan Speed | Tilt Speed | SUM |
| Upleft | 0xFF | Address | 0x00 | 0x0C | Pan Speed | Tilt Speed | SUM |
| Upright | 0xFF | Address | 0x00 | 0x0A | Pan Speed | Tilt Speed | SUM |
| DownLeft | 0xFF | Address | 0x00 | 0x14 | Pan Speed | Tilt Speed | SUM |
| DownRight | 0xFF | Address | 0x00 | 0x12 | Pan Speed | Tilt Speed | SUM |
| Zoom In | 0xFF | Address | 0x00 | 0x20 | 0x00 | 0x00 | SUM |
| Zoom Out | 0xFF | Address | 0x00 | 0x40 | 0x00 | 0x00 | SUM |
| Focus Far | 0xFF | Address | 0x00 | 0x80 | 0x00 | 0x00 | SUM |
| Focus Near | 0xFF | Address | 0x01 | 0x00 | 0x00 | 0x00 | SUM |
| Set Preset | 0xFF | Address | 0x00 | 0x03 | 0x00 | Preset ID | SUM |
| Clear Preset | 0xFF | Address | 0x00 | 0x05 | 0x00 | Preset ID | SUM |
| Call Preset | 0xFF | Address | 0x00 | 0x07 | 0x00 | Preset ID | SUM |
| Query Pan Position | 0xFF | Address | 0x00 | 0x51 | 0x00 | 0x00 | SUM |
| Query Pan Position Response | 0xFF | Address | 0x00 | 0x59 | Value High Byte | Value Low Byte | SUM |
| Query Tilt Position | 0xFF | Address | 0x00 | 0x53 | 0x00 | 0x00 | SUM |
| Query Tilt Position Response | 0xFF | Address | 0x00 | 0x5B | Value High Byte | Value Low Byte | SUM |
| Query Zoom Position | 0xFF | Address | 0x00 | 0x55 | 0x00 | 0x00 | SUM |
| Query Zoom Position Response | 0xFF | Address | 0x00 | 0x5D | Value High Byte | Value Low Byte | SUM |

## 2. PTZ Controller in Python
The [PTZ.py](/PTZ.py) is the class function developed for controlling the PTZ with integrated class function
of various commands. The Python PTZ controller includes the communication and the encoding & decoding of the hexadecimal
command message. Here is the detail description of the Python code.

### 2.1. Serial Port Detection
Run the main function ([here](/main/main.py)), and you will see the following information:

(From the python terminal) It will scan all available COM ports in the device, and print out. 
The code is located in [here](https://github.com/ValenQiu/SolarTracker2/blob/9f54e47cafa19494f45e1cc4cbf8ad9ea00612f1/PTZ%20Control/PTZ.py#L23).
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

### 2.2. Class Functions
The class functions for controlling the PTZ follows the Pelco-D protocol definition. Please refer to the 
List of Commands in [Part 1](/README.md).

#### Hexadecimal value of commands

In the class function `Frame`, there is a list of the hexadecimal value of commands (the 4th byte of the command message).
```python
    _command2_code = {
        'DOWN': '\x10',
        'UP': '\x08',
        'LEFT': '\x04',
        'RIGHT': '\x02',
        'UP-RIGHT': '\x0A',
        'DOWN-RIGHT': '\x12',
        'UP-LEFT': '\x0C',
        'DOWN-LEFT': '\x14',
        'STOP': '\x00',
        'ZOOM-IN': '\x00',
        'ZOOM-OUT': '\x00',
        'FOCUS-FAR': '\x00',
        'FOCUS-NEAR': '\x00',
        'QUERY-TILT': '\x53',
        'QUERY-PAN': '\x51',
        'SET-PAN': '\x4B',
        'SET-TILT': '\x4D'
    }
```
#### PTZ Moving
The PTZ has total nine motions, which of eight directions ('DOWN', 'UP'.'LEFT','RIGHT', 'UP-LEFT', 'UP-RIGHT', 'DOWN-LEFT', 'DOWN-RIGHT'),
and 'STOP'. The class function `move_to_side(self, side)` defines the general function of giving the direction, 
constructing the command message and send the message to the PTZ.

```python
    def move_to_side(self, side):
        """
        Directions: 'DOWN', 'UP'.'LEFT','RIGHT', 'UP-LEFT', 'UP-RIGHT', 'DOWN-LEFT', 'DOWN-RIGHT', 'STOP'
        The hex value of the directions are as defined in class Frame._command2_code
        """
        cmd = self._command._construct_cmd(command2=side, pan_speed=self._speed['PAN'],
                                           tilt_speed=self._speed['PAN'])
        print("move to side: ", end='')
        for byte in cmd:
            print(f"{byte:02X}", end=' ')
        print()
        self._device.write(cmd)
        time.sleep(0.05)
```

By giving the `side` variable of this function, the PTZ will move towards the desired direction. For example, if I want the PTZ to move to right:
```python
self.move_to_side('RIGHT')
```

#### Set Joint Angle
The PTZ has two joints, which is the tilt joint (zenith angle) and the pan joint (azimuth angle).
We can call the function `set_tilt_position(self, angle)` and `set_pan_position(self, angle)` 
to control each joint moves to the desired position.

Code of setting the pan joint position:
```python
    def set_pan_position(self, angle):
        """
        Set Pan Position    | 0xFF | Address 0x01 | 0x00 | 0x4B | Value High Byte | Value Low Byte | Checksum |
        """
        """
           Converts an angle (in degrees) into high and low byte values.

           Parameters:
           angle (float): The angle in degrees.

           Returns:
           tuple: A tuple containing the high byte and low byte values.
           """
        # Ensure the angle is within the valid range of 0 to 360 degrees
        angle = angle * 100

        # Calculate the high byte and low byte values
        high = int(angle // 256)
        low = int(angle % 256)

        # Convert the MSB and LSB to the correct format
        high_hex = chr(high)
        low_hex = chr(low)

        cmd = self._command._construct_cmd(command2='SET-PAN', pan_speed=high_hex,
                                           tilt_speed=low_hex)
        print("set pan position: ", end='')
        for byte in cmd:
            print(f"{byte:02X}", end=' ')
        print()
        self._device.write(cmd)
```

The similar format with the tilt joint.

#### Query Joint Position
To query the joint position, it needs to first send the query request to the PTZ, and then decode the return message.
According to the protocol, the request message is:

| Description                  | 0xFF | Address | Command 1 | Command 2 | Data 1 | Data 2 | Checksum |
|------------------------------|------|---------|---------|--------|--------|----------|----------
| Query Pan Position           | 0xFF | 0x01 |  0x00 | 0x51 | 0x00 | 0x00 | SUM |
| Query Pan Position Response  | 0xFF | 0x01 |  0x00 | 0x59 | Value High Byte | Value Low Byte | SUM |
| Query Tilt Position           | 0xFF | 0x01 |  0x00 | 0x53 | 0x00 | 0x00 | SUM |
| Query Tilt Position Response  | 0xFF | 0x01 |  0x00 | 0x5B | Value High Byte | Value Low Byte | SUM |

Where the `High Byte` and `Low Byte` are also called "High-Order Byte" and "Low-Order Byte". 

"We generally write numbers from left to right, with the most significant digit first. To understand what is meant by
the "significance" of a digit, think of how much happier you would be if the first digit of your paycheck was increased 
by one compared to the last digit being increased by one.

The bits in a byte of computer memory can be considered digits of a number written in base 2. 
That means the least significant bit represents one, the next bit represents 2´1, or 2, the next bit represents 2´2´1, 
or 4, and so on. If you consider two bytes of memory as representing a single 16-bit number, one byte will hold the 
least significant 8 bits, and the other will hold the most significant 8 bits. Figure shows the bits arranged into two 
bytes. The byte holding the least significant 8 bits is called the least significant byte, or low-order byte. 
The byte containing the most significant 8 bits is the most significant byte, or high- order byte." 
([What is meant by high-order and low-order bytes?](https://www.indiabix.com/technical/c/bits-and-bytes/2))


<p align="center">
  <img width="60%" src="/media/high_low_bytes.png" alt="high_low_bytes">
</p>

The position can be convert back to the original value by using the code:
```python
position = (high_byte << 8) + low_byte
```

## Contact
If you have encounter or interested in contributing, please contat the author [Valen Qiu](https://github.com/ValenQiu) and our labs ([REALab](https://www.li-realab.info/), [Romi-Lab](https://www.romi-lab.org/)), or submit a pull request on GitHub.
