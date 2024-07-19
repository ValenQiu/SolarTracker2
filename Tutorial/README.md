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

## 2. Connect to PTZ
Run the main function ([here](/main/main.py)), and you will see the following information:

(From the python terminal) It will scan all available COM ports in the device, and print out. It is recommanded to use this function for the first time.
