## Overview

LightPi-Web provides a web interface to control addressable LED strips from the Raspberry Pi,
specifically the LPD8806, but it could be easily adapted to support others.

## Requirements

First and foremost, the LPD8806 driver and animation library must be installed.
Follow the instructions the project's [GitHub page](https://github.com/adammhaile/RPi-LPD8806) for installation steps.

Next, LightPi-Web is dependent upon screen (if run as a deamon) and the python web server module "bottle".
Neither come pre-installed on Raspbian so install them using the following commands.

    sudo apt-get install python-bottle 
    sudo apt-get install screen

## Installation

To grab the latest version of LightPi-Web, pull it from GitHub with the following command:

    git clone https://github.com/adammhaile/LightPi-Web.git

Before proceeding, ensure that everything is setup correctly by running these commands:

    cd LightPi-Web
    sudo python LightPi_Web.py

Note, that it must be run with sudo in order for the web server component to function properly.
You will notice the message 'Writing default config file'. It has written out the file lpw.config which stores a few basic config items.
Shutdown the server process by hitting Ctrl+C.
Edit the file by running:

    sudo nano lpw.config

You should see something similar to this:

    [LEDStrip]
    numleds = 36

    [Network]
    http_ip = 0.0.0.0
    http_port = 80

The only item you should need to change is 'numleds'. Change this to the total number of LEDs in your particular strip.
Save the file and exit with Ctrl+O, Ctrl+X.

From now on you can either just run LightPi-Web using the command given above or you can run it as a deamon so it will run on boot.
To do so, run the following commands:

    chmod 755 ./install_service.sh
    ./install_service.sh

You likely see some message about incorrect LSB, this can be ignored. From now on, the server will automatically run when the Raspberry Pi boots, but to start it up now, just run:

    ./start.sh
    ./connect.sh

start.sh fires up the server, but in a screen session named "LPW". connect.sh will connect you to this screen session so that the server can be monitored. 
Type the IP address of your Raspberry Pi into the browser of another computer and you should the server log the file requests in the mentioned screen session.
When done monitoring the server, just hit Ctrl+A,D to detach from the screen session, but leave the server running. You can reconnect at any time with the connect.sh script.

If, at any time, you would like to remove the daemon, simply run:

    chmod 755 remove_service.sh
	./remove_service.sh