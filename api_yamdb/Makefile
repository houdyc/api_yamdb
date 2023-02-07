WORKDIR = .
MANAGE = python $(WORKDIR)/manage.py

<<<<<<< HEAD
lint:
=======
lint: 
>>>>>>> 3543b90acf979d28dd806b8beaee95eefd99211d
	black -S -l 79 $(WORKDIR)
	isort $(WORKDIR)
	flake8 $(WORKDIR)
	PYTHONPATH=${PYTHONPATH}:${PWD}/$(WORKDIR)
<<<<<<< HEAD
	mypy $(WORKDIR)
=======
	mypy $(WORKDIR)
>>>>>>> 3543b90acf979d28dd806b8beaee95eefd99211d
