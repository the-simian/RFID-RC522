# RFID-RC522 #

## Unfinished/Under Development ##


![RFID-RC522](/documentation/rfid-rd522-banner.jpg)
----
Authors:
- [Jesse Harlin](http://jesseharlin.net/)
- [Jon Yarbor](https://github.com/blazedd)

## About ##

This module is a simple node api that allows a user to read and write to the RFID-RC522 module. It is built on top of a python library authored by `mxgxw` [located here](https://github.com/mxgxw/MFRC522-python);

## Pins ##
Here is the table of which pins you need to plug your RFID-RC522 into on the raspberry pi.

| Name | Pin # | Pin name   |
|------|-------|------------|
| SDA  | 24    | GPIO8      |
| SCK  | 23    | GPIO11     |
| MOSI | 19    | GPIO10     |
| MISO | 21    | GPIO9      |
| IRQ  | None  | None       |
| GND  | Any   | Any Ground |
| RST  | 22    | GPIO25     |
| 3.3V | 1     | 3V3        |
