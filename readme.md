---------
To install pip: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-linux.html
To install venv: python3 -m venv ./venv
To activate venv: source ./venv/bin/activate
To deactivate venv: deactivate
To install requirments: pip install -r requirments.txt


To Run Flask app:
export FLASK_APP=server.py
flask run --host=0.0.0.0


To run wsgi:
Sometimes you might run into ec2 instances to install wsgi
yum groupinstall "Development Tools"
yum install python-devel
pip install uwsgi
uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app

The above command will run the wsgi but we might want to run this as soon as system boots hence:
sudo vi /etc/systemd/system/portfolio.service
and add this 
```
[Unit]
Description=uWSGI instance to serve portfolio
After=network.target

[Service]
WorkingDirectory=/home/ec2-user/python_projetcs/portfolio
Environment="PATH=/home/ec2-user/python_projetcs/portfolio/venv/bin"
ExecStart=/home/ec2-user/python_projetcs/portfolio/venv/bin/uwsgi --ini portfolio.ini

[Install]
WantedBy=multi-user.target
```
reference : https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04
sudo systemctl start portfolio
sudo systemctl enable portfolio
sudo systemctl status portfolio
sudo systemctl restart portfolio
sudo systemctl stop portfolio




You might need to install nginx manually using sudo yum install nginx after installing nginx.
1. if directories are not present then create
```
mkdir -p /etc/nginx/sites-enabled
mkdir -p /etc/nginx/sites-available
```
2. add following line to nginx config
locating config file path
```
nginx -t
```
```
vi /etc/nginx/nginx.conf
include /etc/nginx/sites-enabled/*.conf;
```

3. add following code to /etc/nginx/nginx.conf
```
server {
    listen 80;
    server_name hotstar;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/ec2-user/python_projetcs/portfolio/portfolio.sock;
    }
}
```

4. Start nginx
```
sudo systemctl restart nginx
sudo systemctl status nginx
sudo systemctl stop nginx
```





[might not be relevant to all]
TO configure AWS for nameserver
https://www.youtube.com/watch?v=hRSj2n-XKGM

Configuring https:
Install certbot 
```
sudo yum install certbot-apache
sudo yum install certbot
sudo amazon-linux-extras install epel
sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
sudo yum install python-certbot-nginx
sudo certbot certonly --nginx
```
Make sure port 443 is open

Reference: https://adamtheautomator.com/nginx-to-redirect-http-to-https/


 add following code to /etc/nginx/nginx.conf
```
server {
    listen 443;
    ssl on;
    server_name hotstar.ai;
    ssl_certificate /etc/letsencrypt/live/hotstar.ai/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/hotstar.ai/privkey.pem;


    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/ec2-user/python_projetcs/portfolio/portfolio.sock;
    }
}         
```


Get ssl certificates for new domains
```
sudo certbot certonly -d domain_name.com
```

