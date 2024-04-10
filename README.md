# Beaglebot -- A robot based on the Beaglebone AI-64
### By Carsten Thue-Bludworth
### 2024

#### Overview

#### Structure
* `cad` directory contains mechanical and electrical design files.
* `bot` directory contains code that runs on the robot itself.
* `server` directory contains code that runs on a remote server.

__04/10/2024__
* Start experimenting with `rerun` in Python by creating a virtual environment and then `pip install --upgrade rerun-sdk`.
* On server machine (my laptop) install rerun viewer with `cargo binstall rerun`.
* Get realsense camera (D435i model) working.
  * had to install the SDK via [this](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md) document. 
  * Actually, not so straightforward :( The `dpkg` install is only available for Ubuntu and specific versions of the kernel. I was able to build from source following a combination of [this](https://github.com/IntelRealSense/librealsense/blob/master/doc/installation.md) guide and [this](https://github.com/IntelRealSense/librealsense/blob/master/doc/installation_raspbian.md) guide, which worked fine, and `realsense-viewer` successfully shows the camera and depth feeds; however, this didn't install the kernel patch, instead compiling for the RSUSB backend (I think). I after building the python bindings and running `make install` I couldn't access them from a normal (non venv) python repl.
  * TODO: get the kernel patch building and installing (preferred solution, perhaps can contribute back to the BBAI64 community).
  * TODO: figure out best solution for `pyrealsense2` python package (i.e. system wide after source build, or via pip in a venv)?

#### General notes on BBAI-64 setup
* Change password for user `debian`.
* Update packages with `sudo apt-get update`, `sudo apt-get upgrade`, and `sudo apt-get dist-update`.
* Install `rustup` via the curl installer. I had to *not* modify the PATH variable due to file path differences. Instead, configure the shell manually by running `source ~/.cargo/env.fish`.
* Monitor temps via `sudo cat /sys/devices/virtual/thermal/thermal_zone0/temp`
* USB-C connector seems to not work with my dongle (using PD too). TODO: try powering over the barrel connector and then see if the dongle works.
* `realsense-viewer` said my camera was operating on a USB 2.1 port, but the bbai64 specs say its a 3.1 port? Maybe this way because of the cable I was using (says 2.1 on the sheating)?
* `htop` seems to only indicate the 2GB of RAM are present.. but the specs indicate 4 should be there?

