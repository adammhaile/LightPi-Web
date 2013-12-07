#!/bin/bash
dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
cd $dir
sudo screen -d -m -S LPW sh -c "python LightPi_Web.py"
