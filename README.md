# lazypackage

Welcome to lazypackage!

Lazypackage helps you create organized Python projects that are installed easily and can contain C++ code!

You can use Lazypackage to wrap C++ code for use in Python as well as creating simple Python packages.

Lazypackages do not depend on Lazypackage after creation and only require SWIG to be installed. Lazypackages are easily customizable.

## Installation

To install, simply run setup.sh in the lazypackage installation directory after cloning

*bash*

```bash
git clone http://gitlab-prod/ssi/lazypackage --recursive
cd lazypackage
sudo bash setup.sh
```

## Usage

The first thing you'll probably want to do is create a new lazypackage. 

*bash*

```bash
#Create a directory
mkdir packagename
#Move into folder
cd packagename
#Create package
python -m lazypackage newpackage packagename
```

To view the help message and view the possible commands, you can always add -h to the command.

*bash*

```bash
#View general help
python -m lazypackage -h
#View help about certain command (newpackage)
python -m lazypackage newpackage -h
```

