#!/bin/sh

virtualenv ve
./ve/bin/python setup.py develop
./ve/bin/pip install -r post/tests/requirements.txt
./ve/bin/python setup.py test
