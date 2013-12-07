sudo chmod 755 start.sh
sudo chmod 755 connect.sh
sudo cp -f ./lightpiweb.sh /etc/init.d/
sudo chmod 755 /etc/init.d/lightpiweb.sh
sudo update-rc.d -f lightpiweb.sh defaults