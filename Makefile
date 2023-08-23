.PHONY: clean python-packages install test dev prod all

clean:

python-packages:
	pip install -r requirements.txt

install: python-packages

test:
	export FLASK_DEBUG=0 && flask --app 'app/main:create_app("test")' run

dev:
	export FLASK_DEBUG=1 && flask --app 'app/main:create_app("dev")' run

prod:
	export FLASK_DEBUG=0 && flask --app 'app/main:create_app("prod")' run

all: clean install test prod