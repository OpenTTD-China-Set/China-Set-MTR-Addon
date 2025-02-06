# China Set: MTR Addon

## **General Information**

China Set: MTR Addon is a add-on of [China Set: Trains](https://github.com/OpenTTD-China-Set/China-Set-Trains).
This is a add-on GRF of China Set Series. It add the vehicles of MTR uses in HongKong.
China Set: MTR Addon is licensed under GPL v2.

Features:
	- EMUs in East Rail Line and Tuen Ma Line
	- High speed Railway
  - KTT

Features in Future:
	- More EMUs in MTR (25kV AC and 1.5kV DC)
	- Light Rail system
  - Disel Rail Buses in aarly 20th centery

## **Contributors**

Vox:
	- Babel
	- ctx
    - Haiyan
    - Nengyeqing
    More information read [this](docs/voxsourse.csv)

Code:
	- Almost copy from [China Set: Trains](https://github.com/OpenTTD-China-Set/China-Set-Trains)
	- Babel
	- Jonh Franklin

Also thanks to everyone provide support to China Set.

## **Buliding**

Sprites in China Set: MTR Addon are render by Gorender from .vox files.
You can use Magicavoxel to change and create voxes.

The .lng files are generate by [a .csv file](./docs/str.CSV) during the complie process, so please change the csv file to change strings.

If you want to compile the NewGRF, you should(for windows):
	1.Install [nmlc](https://www.tt-wiki.net/wiki/NMLTutorial/Installation) and add it to the system path.
	2.Install [Gorender](https://github.com/mattkimber/gorender) and add it to the system path.
	3.Install Python 3.11+

Then, start mtr-make.py to compile the NewGRF.

## **License**

```text
China Set: Trains

Copyright (C) 2024 China Set Team

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, please check
https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html
```
=======
This is a add-on GRF of China Set Series. It add the vehicles of MTR uses in HongKong. <br>
Will add in Future: <br>
	EMUs in MTR (25kV AC and 1.5kV DC) <br>
	Light Rail system <br>
	KTT and other locomotives and wagons used in Kowloon-Canton Railway <br>
**Other Information** <br>
Made by Babel  <br>
Sprites are made by Gorender and Magicavoxel <br>
All of thsee files, images and GRFs are under GPL-2.0 License <br>


**Obtaining the source**(Copy by README of old China Set: Trains)

The source code can be obtained from GitHub.

1. Install WSL (if you are on Windows)
2. sudo apt install python3;
3. sudo apt install python3-pip;
4. sudo apt install make;
5. pip3 install nml;
6. Unzip China-Set-Trains folder downloaded;
7. Shift-right-click (if you are on Windows) the China-Set-Trains folder;
8. Click "Open Linux Shell";
9. type "make";
10. Compile success.
