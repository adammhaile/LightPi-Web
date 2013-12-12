#! /bin/bash
# /etc/init.d/lightpiweb 

### BEGIN INIT INFO
# Provides:          lightpiweb
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Simple script to start LightPi Web at boot
# Description:       Starts LightPi Web at boot
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting LightPi Web"
    # run application you want to start
    LPW_PATH/start.sh
    ;;
  stop)
    echo "Stopping noip"
    # kill application you want to stop
    # do nothing!
    ;;
  *)
    echo "Usage: /etc/init.d/lightpiweb {start|stop}"
    exit 1
    ;;
esac

exit 0