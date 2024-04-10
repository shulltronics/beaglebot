# Beaglebot -- A robot based on the Beaglebone AI-64
### By Carsten Thue-Bludworth
### 2024

__04/10/2024__
* Start experimenting with `rerun` in Python by creating a virtual environment and then `pip install --upgrade rerun-sdk`.
* On server machine (my laptop) install rerun viewer with `cargo binstall rerun`.

#### General notes on BBAI-64 setup
* Change password for user `debian`.
* Update packages with `sudo apt-get update` and `sudo apt-get upgrade`.
* Install `rustup` via the curl installer. I had to *not* modify the PATH variable due to file path differences. Instead, configure the shell manually by running `source ~/.cargo/env.fish`.
