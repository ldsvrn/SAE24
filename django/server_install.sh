#!/bin/bash

apt update
apt install git nginx python3 python3-pip python3-venv python3-dev libmariadb-dev ufw -y

useradd -m toto
su - toto -c "git clone https://github.com/ldsvrn/SAE24 /home/toto/CLONE"
chmod 774 /home/toto/django/user_install.sh

su - toto -c '/home/toto/CLONE/django/user_install.sh'

cat << EOS > /etc/systemd/system/gunicorn.socket
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
EOS

cat << EOF > /etc/systemd/system/gunicorn.service
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=toto
Group=www-data
WorkingDirectory=/home/toto/django/SAE24
ExecStart=/home/toto/django/.venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock SAE23.wsgi:application

[Install]
WantedBy=multi-user.target
EOF

systemctl start gunicorn.socket
systemctl enable gunicorn.socket

cat << EOF > /etc/nginx/sites-available/sae24
server {
    listen 80;
    server_name django-serv.rt13.lab;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/toto/django/SAE24;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
EOF

ln -s /etc/nginx/sites-available/sae24 /etc/nginx/sites-enabled/

systemctl restart nginx

ufw enable
ufw allow 22/tcp
ufw allow 80/tcp