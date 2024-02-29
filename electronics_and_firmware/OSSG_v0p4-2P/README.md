# Open Source Smartglasses PCB V0.4
---

This version was an attempt to use a 2P battery pack.  


### PCB 0.4 Features:

First batch sent off for production: 2022-09-22 for Australian delivery, assembling and testing
- fix missing missing ESP32_VDD3P3 connection
- solder connector pads for i2S microphones (non PDM)
- onboard PDM (over i2S)  microphone
- 2P battery configuration
- 2P battery charger
- MAX17048 Li battery fuel gauge
- power on/off switch
- USB 1A resetable fuse
- auto switch off when battery pack goes below 2.7V
- SY7088 3V to 5V at 1A DC-DC Boost converter
- provision for WS2812B-2020 RGB LED as visual feed back to wearer with connector for more external LEDs
- side mounted user tactile switch
- adjusted ESP32-Pico footprint
- adjusted mounting holes to M1.6 for screws and a M1.5 non-screw hole for alignment
- touch sensor connector pads
- Heads Up Display connector (experimental)


### PCB:

- 4 layer
- 9mm x 85mm long
- 0.8mm thick (Australian board is 1.0mm thick)

