To install pip: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-linux.html
To install venv: python3 -m venv ./venv
To activate venv: source ./venv/bin/activate
To deactivate venv: deactivate
To install requirments: pip install -r requirments.txt

export FLASK_APP=server.py
flask run --host=0.0.0.0

