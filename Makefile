# Author: Erik Anderson 
# Date Created: 03/06/2020

default: test

# Lints toolbox-vlsi-tools directory recursively
lint:
	pylint toolbox-vlsi-tools tests

# Formats toolbox-vlsi-tools directory recursively
format:
	yapf -i -r toolbox-vlsi-tools tests

# Type checks toolbox-vlsi-tools directory recursively
type:
	mypy toolbox-vlsi-tools tests

# Runs all tests in tests directory 
test:
	pytest -v tests
