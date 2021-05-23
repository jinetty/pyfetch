<img src="https://raw.githubusercontent.com/kreat0/pyfetch/master/preview/pyfetch.png" alt="Screenshot" />


# pyfetch
Stylish and simple fetch for your terminal that is customizable, and fast.

# Dependencies
* fontawesome on your system


# Installation

## Installation from PyPi
Run `pip install pyfetchh` in order to install it.

## Installation through the binary
* Get the latest release through [here](https://github.com/kreat0/pyfetch/releases)
* Copy the binary to /usr/bin 
* Make it a executable through running `chmod +x /usr/bin/pyfetch`



## Installation from source
### Dependencies
* distro package on PyPi (only for linux systems)
* psutil package on PyPi
* colorama package on PyPi

### Installation
* Clone the repo
* Type `pip install distro colorama psutil` to install the dependencies (for windows its only `pip install colorama distro` but for gentoo its `pip install distro colorama psutil --user`)
* Type `make install` as root
* Enjoy!

## Installation through the AUR package
**Warning, the AUR package is not official!**
```
git clone https://aur.archlinux.org/packages/pyfetch-git.git
cd pyfetch-git
makepkg -si
```
Or use a aur helper like `yay`:
`yay -S pyfetch-git`

# Credits
* Yellowsink
