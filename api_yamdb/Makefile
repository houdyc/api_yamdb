WORKDIR = .
MANAGE = python $(WORKDIR)/manage.py

lint:
	black -S -l 79 $(WORKDIR)
	isort $(WORKDIR)
	flake8 $(WORKDIR)
	PYTHONPATH=${PYTHONPATH}:${PWD}/$(WORKDIR)
	mypy $(WORKDIR)