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

