# Initial deploy #
Create venv 'python -m venv venv'  
install 'pip install requirements.txt'  
to activate venv type 'source venv/bin/activate'  
deactivate with 'deactivate'  

start programm 'python recv_text.py &'  
logs in log.txt  
listens on port 8089  

# Install Service #
copy `einkdisplay.service` to `/etc/systemd/system/einkdisplay.service` and edit paths to your install location

`sudo systemctl start einkdisplay.service`  
`sudo systemctl status einkdisplay.servic`  
`sudo systemctl stop einkdisplay.service`  

start on system boot  
`sudo systemctl enable einkdisplay.service`  

