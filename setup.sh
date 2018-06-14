#Setup bash script. Made with lazypackage
#At this point, install dependencies

sudo apt-get install -y swig python-cheetah

#This line builds and installs your package
sudo python -m pip uninstall -y lazypackage
sudo python -m pip install .
