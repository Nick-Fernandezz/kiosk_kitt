FROM python

RUN python3 -m venv /home/$USER/venvs/.env

RUN sourse /home/$USER/venvs/.env/bin/activate

RUN pip install -r requirements.txt

RUN python3 kitt_kiosk/manage.py collectstatic

RUN deactivate

COPY ./kitt_kiosk /var/www/ 

RUN ECHO " \
[Unit] \
Description=gunicorn socket \
[Socket] \
ListenStream=/run/gunicorn.sock \
[Install] \
WantedBy=sockets.target \
" >> /etc/systemd/system/gunicorn.socket

RUN "\
[Unit] \
Description=gunicorn daemon \
Requires=gunicorn.socket \
After=network.target \
\
[Service] \
User=server \
Group=www-data \
WorkingDirectory=/var/www/kitt_kiosk \
ExecStart=/home/$USER/venvs/.env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          myproject.wsgi:application \
\
[Install] \
WantedBy=multi-user.target \
" >> /etc/systemd/system/gunicorn.service

RUN systemctl start gunicorn.socket
RUN systemctl enable gunicorn.socket

RUN ECHO systemctl status gunicorn.socket >> /home/$USER/kitt_logs/status_gunicorn.txt

RUN ECHO "\
server { \
    listen 80; \
    server_name 10.193.245.5; \
\
    location = /favicon.ico { access_log off; log_not_found off; } \
    location /static/ { \
        root /var/www/kitt_kiosk; \
    } \
\
    location /media/ { \
        root /var/www/kitt_kiosk; \
    } \
\
    location / { \
        include proxy_params; \
        proxy_pass http://unix:/run/gunicorn.sock; \
    } \
} \
" >> /etc/nginx/sites-available/kitt_kiosk

RUN ln -s /etc/nginx/sites-available/kitt_kiosk /etc/nginx/sites-enabled
RUN mv /etc/nginx/sites-available/default /home/$USER/
RUN mv /etc/nginx/sites-enabled/default /home/$USER/default1
RUN systemctl restart nginx

COPY source dest
