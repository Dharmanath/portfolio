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





You might need to install nginx manually