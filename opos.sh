
apt install -y   python3-pip

pip3 install flask 


pip3 install tornado
pip3 install qrcode
pip3 install captcha
pip3 install  qcloudsms_py
apt install -y python-pip
pip install supervisor
echo_supervisord_conf > /etc/supervisord.conf

echo "

[program:run]

command=python3 /root/run.py

autostart=true

autorestart=true

user=root

" >> /etc/supervisord.conf

supervisord -c /etc/supervisord.conf




