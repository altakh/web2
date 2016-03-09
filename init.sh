sudo ln -sf /home/kotya/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/kotya/web/etc/hello.py /etc/gunicorn.d/hello.py


