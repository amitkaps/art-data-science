# Installation

## Pre-requisites
* Laptop running Linux / OSX / Windows operating system
* Minimum 4GB of RAM
* Laptop charger

## Recommended Installation
We will be using Python 3 version for the workshop. Users should install the Anaconda distribution from Continuum - [https://www.continuum.io/downloads](https://www.continuum.io/downloads). 


We request you to check if your Operating System is 32 bit or 64 bit and download the according installer. To find out what architecture your OS is, here are references for Windows, OSX and Ubuntu:

- Windows and OSX: [http://www.akaipro.com/kb/article/1616#os_32_or_64_bit](http://www.akaipro.com/kb/article/1616#os_32_or_64_bit)
- Ubuntu: [http://askubuntu.com/a/41334](http://askubuntu.com/a/41334)

Please note that installing Anaconda is the **recommended** option for doing the workshop.

## Adding Anaconda to your path
Please add the following to your bash profile
```
PATH=~/anaconda3/bin:$PATH
```

## Post Anaconda Installation
Please run the below commands from your command line interface

```
conda install seaborn
conda install prophet
conda install plotnine
```
